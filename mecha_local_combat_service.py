# mecha_local_combat_service.py
import time
import pyautogui

from actions import clicar_imagem, skip_com_reforco
from screen_utils import clicar_mecha_local_seguranca

pyautogui.FAILSAFE = False
pyautogui.useImageNotFoundException(False)


def rotina_lutar_2_skip_continuar(log_fn):
    """
    Fluxo real e correto:
    1) Aguardar LUTAR 2 aparecer (até 15 tentativas)
    2) Clicar LUTAR 2
    3) Aguardar combate começar (animação inicial)
    4) Aplicar SKIP reforçado
    5) Clicar CONTINUAR
    6) Clicar CONTINUAR 2 (se existir)
    """

    log_fn("────────────────────────────────────────────")
    log_fn("[FLOW] INÍCIO DO PASSO 2 → Fluxo LUTAR 2 / SKIP / CONTINUAR")
    log_fn("────────────────────────────────────────────")

    # -----------------------------
    # 1 — AGUARDAR LUTAR 2 APARECER
    # -----------------------------
    log_fn("[CHECK] Procurando LUTAR 2 (até 15 tentativas)...")

    tentou = 0
    achou_lutar2 = False

    for _ in range(15):
        tentou += 1
        log_fn(f"[CHECK] Tentativa {tentou}/15 para encontrar LUTAR 2...")

        if clicar_imagem("images/lutar_2.png", log_fn, "LUTAR 2"):
            log_fn("[STATE] LUTAR 2 encontrado e clicado!")
            achou_lutar2 = True
            break

        time.sleep(0.35)

    if not achou_lutar2:
        log_fn("[ERRO] LUTAR 2 NÃO apareceu — abortando combate e voltando para o ciclo principal.")
        return False

    # -----------------------------
    # 2 — Aguarda animação inicial
    # -----------------------------
    log_fn("[WAIT] Aguardando animação inicial da luta...")
    time.sleep(2.8)

    # -----------------------------
    # 3 — SKIP
    # -----------------------------
    log_fn("[CHECK] Aplicando SKIP reforçado...")
    skip_com_reforco(log_fn)
    time.sleep(0.8)

    # -----------------------------
    # 4 — CONTINUAR
    # -----------------------------
    log_fn("[CHECK] Procurando botão CONTINUAR...")

    clicar_mecha_local_seguranca(log_fn)

    if clicar_imagem("images/continuar.png", log_fn, "CONTINUAR"):
        log_fn("[STATE] CONTINUAR 1 clicado com sucesso.")
    else:
        log_fn("[WARN] CONTINUAR 1 não encontrado — tentando fluxo normal mesmo assim.")

    time.sleep(1.2)

    # -----------------------------
    # 5 — CONTINUAR 2 (OPCIONAL)
    # -----------------------------
    log_fn("[CHECK] Verificando se existe CONTINUAR 2...")

    if clicar_imagem("images/continuar_2.png", log_fn, "CONTINUAR 2"):
        log_fn("[STATE] CONTINUAR 2 clicado com sucesso.")
    else:
        log_fn("[OK] CONTINUAR 2 não existe — seguindo fluxo normalmente.")

    time.sleep(1.0)

    log_fn("────────────────────────────────────────────")
    log_fn("[RESULT] PASSO 2 concluído → pronto para reiniciar ciclo")
    log_fn("────────────────────────────────────────────")

    return True
