# controller.py
import time
import state
import pyautogui

from screen_utils import clicar_mecha_local_seguranca
from mecha_300_service import tratar_mecha_300
from maximo_mecha_service import tratar_maximo_mecha
from mecha_chefe_service import tratar_cancelar_mecha_chefe
from mecha_local_service import rotina_lutar_mecha_local
from mecha_local_combat_service import rotina_lutar_2_skip_continuar

pyautogui.FAILSAFE = False
pyautogui.useImageNotFoundException(False)


def bot_loop(log_fn, status_fn):

    status_fn("STATUS: EXECUTANDO", "green")
    log_fn("Bot iniciado — fluxo completo ativo.")

    while state.bot_ativo:

        tratar_mecha_300(log_fn)

        if tratar_maximo_mecha(log_fn):
            continue

        if tratar_cancelar_mecha_chefe(log_fn):
            continue

        # ----------- LUTAR --------------
        resultado = rotina_lutar_mecha_local(log_fn)

        if resultado == "EXTRA":
            # evento +3 telefones tratado → volta ao início
            log_fn("[INFO] Ciclo reiniciado após evento extra.\n")
            time.sleep(1)
            continue

        if resultado == False:
            continue

        # ----------- LUTAR 2 / SKIP / CONTINUAR -------------
        rotina_lutar_2_skip_continuar(log_fn)

        if state.modo_3x_permanente:
            clicar_mecha_local_seguranca(log_fn)

        log_fn("[CICLO] Reiniciando...\n")
        time.sleep(1)

    status_fn("STATUS: PARADO", "red")
    log_fn("Bot desligado.")
