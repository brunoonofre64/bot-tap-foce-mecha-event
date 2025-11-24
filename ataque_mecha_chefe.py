# ataque_mecha_chefe.py
import time
import pyautogui
import state

pyautogui.FAILSAFE = False
pyautogui.useImageNotFoundException(False)


# ============================================================
# CLIQUE PADRÃO (Com IMAGE_PATH)
# ============================================================
def clicar(img, log_fn, desc="", conf=0.70, wait=0.4):
    full_path = img

    try:
        pos = pyautogui.locateCenterOnScreen(full_path, confidence=conf)
    except:
        pos = None

    if pos:
        pyautogui.click(pos)
        log_fn(f"[OK] {desc}")
        time.sleep(wait)
        return True

    return False


# ============================================================
# SKIP REFORÇADO (corrigido)
# ============================================================
def skip_com_reforco_mecha(log_fn):
    for tent in range(10):
        try:
            skip = pyautogui.locateCenterOnScreen(
                "images/skip.png",
                confidence=0.65
            )
        except:
            skip = None

        if skip:
            pyautogui.click(skip)
            log_fn(f"[OK] SKIP clicado ({tent+1}/10)")
            time.sleep(0.6)

            try:
                ainda = pyautogui.locateOnScreen(
                   "images/5x.png",
                    confidence=0.65
                )
            except:
                ainda = None

            if not ainda:
                log_fn("[OK] 5x sumiu → animação encerrada")
                return True

    log_fn("[ERRO] Skip falhou após 10 tentativas.")
    return False


# ============================================================
# COLETA COMPLETA (corrigida com IMAGE_PATH)
# ============================================================
def ciclo_coleta(log_fn):
    encontrou = False

    while True:
        achou = False

        if clicar("images/coletar.png", log_fn, "COLETAR pequeno"): achou = True
        if clicar("images/coletar_recompensa.png", log_fn, "COLETAR RECOMPENSAS"): achou = True
        if clicar("images/coletar_2.png", log_fn, "COLETAR GRANDE"): achou = True

        if clicar("images/continuar.png", log_fn, "CONTINUAR"):
            time.sleep(0.5)
            clicar("images/voltar.png", log_fn, "VOLTAR")
            achou = True

        if not achou:
            break

        encontrou = True
        time.sleep(0.4)

    if encontrou:
        log_fn("[OK] Coleta finalizada.")
        return True

    return False


# ============================================================
# LISTA DOS MECHAS (corrigido)
# ============================================================
IMAGENS_MECHAS = [
    "images/mecha_grou.png",
    "images/mecha_kodiak.png",
    "images/mecha_louva_deus.png",
    "images/mecha_serpente.png",
    "images/mecha_simio.png",
    "images/mecha_grifo.png",
]


# ============================================================
# ENCONTRAR MECHAS DO CHEFE (corrigido)
# ============================================================
def encontrar_mechas_real(log_fn):
    encontrados = []

    for img in IMAGENS_MECHAS:
        full_path = img

        try:
            results = list(pyautogui.locateAllOnScreen(full_path, confidence=0.70))
        except:
            results = []

        for r in results:
            cx = r.left + r.width // 2
            cy = r.top + r.height // 2

            if cy > 900:
                continue

            encontrados.append((img, (cx, cy)))

    encontrados.sort(key=lambda x: x[1][1])
    log_fn(f"[INFO] {len(encontrados)} mechas encontrados.")
    return encontrados


# ============================================================
# TESTAR MECHA INDIVIDUAL (corrigido)
# ============================================================
def testar_mecha(img, pos, log_fn):
    pyautogui.click(pos)
    time.sleep(1.0)
    log_fn(f"[MECHA] Testando → {img}")

    if clicar("images/coletar_recompensa.png", log_fn, "COLETAR instantâneo"):
        clicar("images/coletar_2.png", log_fn, "COLETAR final")
        return True

    if clicar("images/ataque_gratis.png", log_fn, "ATAQUE GRÁTIS"):
        return True

    if clicar("images/lutar_3x_dourado.png", log_fn, "LUTAR 3X DOURADO"):
        return True

    clicar("images/voltar.png", log_fn, "Mecha inválido → VOLTAR")
    return False


# ============================================================
# EXECUTAR COMBATE COMPLETO (corrigido)
# ============================================================
def executar_combate(log_fn):

    if not clicar("images/lutar_2.png", log_fn, "LUTAR 1x"):
        return

    time.sleep(4)

    skip_com_reforco_mecha(log_fn)
    time.sleep(1.2)

    if clicar("images/continuar.png", log_fn, "CONTINUAR"):
        time.sleep(0.4)

        tem_algo = False
        for b in ["images/coletar.png", "images/coletar_recompensa.png", "images/coletar_2.png"]:
            if pyautogui.locateOnScreen(b, confidence=0.70):
                tem_algo = True
                break

        if not tem_algo:
            clicar("images/voltar.png", log_fn, "VOLTAR (sem loot)")

    if not ciclo_coleta(log_fn):
        clicar("images/voltar.png", log_fn, "VOLTAR (fallback coleta)")

    clicar("images/mecha_chefe.png", log_fn, "ABRIR MECHA CHEFE", conf=0.65, wait=1.0)

    clicar("images/refresh.png", log_fn, "REFRESH 1")
    time.sleep(3)
    clicar("images/refresh.png", log_fn, "REFRESH 2")
    time.sleep(2)


# ============================================================
# 10 MINUTOS DE ATAQUE INTENSIVO (corrigido)
# ============================================================
def ciclo_mecha_chefe_10_min(log_fn):

    inicio = time.time()
    limite = 10 * 60

    while True:

        if state.hard_stop:
            return

        if time.time() - inicio >= limite:
            log_fn("[CHEFE] 10 minutos finalizados.")
            return

        mechas = encontrar_mechas_real(log_fn)

        if not mechas:
            log_fn("[ERRO] Nenhum mecha encontrado. Tentando refresh…")
            clicar("images/refresh.png", log_fn, "REFRESH")
            time.sleep(3)
            continue

        for img, pos in mechas:
            ok = testar_mecha(img, pos, log_fn)
            if ok:
                executar_combate(log_fn)
                break

        time.sleep(1.0)


# ============================================================
# FLUXO COMPLETO CANCELAR → CHEFE → 10 MIN → LOCAL
# ============================================================
def ciclo_cancelar_mecha_chefe(log_fn):
    log_fn("[EVENTO] CANCELAR detectado → iniciando fluxo completo do Mecha Chefe.")

    ciclo_mecha_chefe_10_min(log_fn)

    log_fn("[CHEFE] Fluxo concluído — retornando ao Mecha Local.")
    clicar("images/mecha_local.png", log_fn, "Retornando ao Mecha Local", conf=0.70, wait=1.5)
