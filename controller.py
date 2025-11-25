# controller.py
import time
import state
import pyautogui

from mecha_chefe_infinito_service import fluxo_mecha_chefe_infinito
from mecha_chefe_service import tratar_cancelar_mecha_chefe
from mecha_300_service import tratar_mecha_300
from maximo_mecha_service import tratar_maximo_mecha
from mecha_local_service import rotina_lutar_mecha_local
from mecha_local_combat_service import rotina_lutar_2_skip_continuar
from screen_utils import clicar_mecha_local_seguranca

pyautogui.FAILSAFE = False
pyautogui.useImageNotFoundException(False)

# ============================================================
# LOOP PRINCIPAL DO BOT
# ============================================================
def bot_loop(log_fn, status_fn):
    status_fn("STATUS: EXECUTANDO", "green")

    # ========================================================
    # 1 — MODO MECHA CHEFE INFINITO (ignora TODO o resto)
    #     Se o toggle estiver ON na hora do F5, ele:
    #       - NÃO entra no Mecha Local
    #       - NÃO roda Mecha 300
    #       - NÃO roda Máximo Mecha
    #       - NÃO roda o ciclo de 12 minutos (cancelar)
    #     Fica só no fluxo do Mecha Chefe pra sempre.
    # ========================================================
    if state.modo_mecha_chefe_infinito:
        log_fn("Bot iniciado — MODO MECHA CHEFE INFINITO ativo.")
        log_fn("────────────────────────────────────────────")
        log_fn("[MODO CHEFE ∞] Entrando no fluxo infinito do Mecha Chefe…")
        log_fn("────────────────────────────────────────────")

        fluxo_mecha_chefe_infinito(log_fn)

        status_fn("STATUS: PARADO", "red")
        log_fn("[MODO CHEFE ∞] Fluxo infinito encerrado.")
        return

    # ========================================================
    # 2 — FLUXO NORMAL (MECHA LOCAL + eventos)
    # ========================================================
    log_fn("Bot iniciado — modo NORMAL (Mecha Local + eventos).")

    while state.bot_ativo:
        # 2.1 — Mecha 300
        if tratar_mecha_300(log_fn):
            continue

        # 2.2 — Máximo Mecha
        if tratar_maximo_mecha(log_fn):
            continue

        # 2.3 — Mecha Chefe (CANCELAR → ciclo de 12 min)
        if tratar_cancelar_mecha_chefe(log_fn):
            continue

        # 2.4 — LUTAR (3X / 1X) em Mecha Local
        resultado = rotina_lutar_mecha_local(log_fn)
        if resultado == "EXTRA":  # +3 telefones tratado
            time.sleep(1)
            continue

        if resultado is False:  # não achou LUTAR
            continue

        # 2.5 — LUTAR 2 / SKIP / CONTINUAR
        rotina_lutar_2_skip_continuar(log_fn)

        # 2.6 — Modo 3X permanente (quando encontra Mecha 300)
        if state.modo_3x_permanente:
            clicar_mecha_local_seguranca(log_fn)

        # 2.7 — Ciclo final
        log_fn("[CICLO] Reiniciando...\n")
        time.sleep(1)

    # ========================================================
    # 3 — BOT DESLIGANDO
    # ========================================================
    status_fn("STATUS: PARADO", "red")
    log_fn("Bot desligado.")
