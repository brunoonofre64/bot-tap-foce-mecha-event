# mecha_chefe_infinito_service.py
import time
import pyautogui
import state

from ataque_mecha_chefe import (
    encontrar_mechas_real,
    testar_mecha,
    executar_combate,
)

pyautogui.FAILSAFE = False
pyautogui.useImageNotFoundException(False)


# ============================================================
# Função auxiliar — abre Mecha Chefe e dá refresh
# ============================================================
def abrir_mecha_chefe(log_fn):
    log_fn("────────────────────────────────────────────")
    log_fn("[CHEFE ∞] Abrindo Mecha Chefe + Refresh")
    log_fn("────────────────────────────────────────────")

    try:
        pos = pyautogui.locateCenterOnScreen("images/mecha_chefe.png", confidence=0.70)
    except Exception:
        pos = None

    if not pos:
        log_fn("[ERRO] Ícone Mecha Chefe NÃO encontrado.")
        return False

    try:
        pyautogui.click(pos)
        log_fn("[OK] Mecha Chefe aberto.")
    except Exception:
        log_fn("[ERRO] Falha ao clicar no ícone Mecha Chefe.")
        return False

    time.sleep(1.0)

    # Refresh
    try:
        pos_ref = pyautogui.locateCenterOnScreen("images/refresh.png", confidence=0.70)
    except Exception:
        pos_ref = None

    if not pos_ref:
        log_fn("[ERRO] Refresh não encontrado.")
        return False

    try:
        pyautogui.click(pos_ref)
        log_fn("[OK] Refresh executado.")
    except Exception:
        log_fn("[ERRO] Falha ao clicar no botão de refresh.")
        return False

    time.sleep(1.2)
    return True


# ============================================================
# LOOP INFINITO — ATACA MECHA CHEFE PRA SEMPRE (com rodízio)
# ============================================================
def fluxo_mecha_chefe_infinito(log_fn):
    log_fn("====================================================================")
    log_fn("[MODO CHEFE ∞] Fluxo Infinito do Mecha Chefe → ATIVO")
    log_fn("====================================================================")

    while state.bot_ativo and state.modo_mecha_chefe_infinito:
        if state.hard_stop:
            log_fn("[STOP] Hard-stop detectado → encerrando fluxo infinito.")
            return

        # 1 — abrir chefe + refresh
        if not abrir_mecha_chefe(log_fn):
            time.sleep(1)
            continue

        time.sleep(1.0)

        # 2 — scan mechas atuais
        mechas = encontrar_mechas_real(log_fn)
        if not mechas:
            log_fn("[WARN] Nenhum mecha encontrado → novo refresh.")
            time.sleep(1)
            continue

        total = len(mechas)
        start_index = state.indice_mecha_chefe % total

        log_fn(
            f"[INFO] {total} mechas encontrados. "
            f"Iniciando rodízio a partir da posição lógica {start_index + 1}/{total}."
        )

        mecha_ok = False

        # 3 — testar cada mecha começando do índice atual (rodízio)
        for offset in range(total):
            idx = (start_index + offset) % total
            img, pos = mechas[idx]

            if not state.bot_ativo or not state.modo_mecha_chefe_infinito or state.hard_stop:
                log_fn("[STOP] Estado alterado durante o loop → saindo do fluxo infinito.")
                return

            ok = testar_mecha(img, pos, log_fn)

            if ok:
                log_fn("[CHEFE ∞] Mecha válido encontrado → iniciando combate.")
                executar_combate(log_fn)

                # Próximo ciclo começa pelo próximo mecha na lista
                state.indice_mecha_chefe = (idx + 1) % total
                mecha_ok = True
                break

        if not mecha_ok:
            # Se nenhum mecha foi válido, reseta o índice pro início
            state.indice_mecha_chefe = 0
            log_fn("[WARN] Nenhum mecha válido neste ciclo → tentando de novo.")
            time.sleep(1)
            continue

        # Pequena folga entre um combate e outro
        time.sleep(0.5)

    log_fn("[MODO CHEFE ∞] Desativado — encerrando fluxo infinito.")
