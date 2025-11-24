import pyautogui
import time
import state

from vision import localizar
from actions import clicar_imagem

pyautogui.FAILSAFE = False
pyautogui.useImageNotFoundException(False)


# ============================================================
# CLICAR SEGURO (wrapper interno)
# ============================================================
def clicar(img, log_fn, desc="", conf=0.75):
    if state.hard_stop:
        return False

    return clicar_imagem(img, log_fn, desc, confianca=conf)


# ============================================================
# DETECÇÃO E TRATAMENTO — MECHA 300
# ============================================================
def checar_e_tratar_mecha_300(log_fn):
    """
    ✔ Detectou 300_mecha_local.png → NÃO ATACAR ESSE MECHA!
    ✔ clicar apenas ataque_5x_nao.png
    ✔ ativar state.modo_3x_permanente
    """

    if state.hard_stop:
        return False

    # --------------------------------------------------------
    # DETECÇÃO (já usa IMAGE_PATH internamente)
    # --------------------------------------------------------
    box = localizar("images/300_mecha_local.png", confianca=0.70)

    if not box:
        return False

    # --------------------------------------------------------
    # MECHA 300 FOI DETECTADO
    # --------------------------------------------------------
    log_fn("[ALERTA] MECHA 300 DETECTADO!")

    if state.hard_stop:
        return False

    # --------------------------------------------------------
    # CLICAR SOMENTE NO BOTÃO "5X NÃO"
    # --------------------------------------------------------
    clicar("images/ataque_5x_nao.png", log_fn, "ATAQUE 5X NÃO", conf=0.75)
    time.sleep(0.4)

    if state.hard_stop:
        return False

    # --------------------------------------------------------
    # ATIVAR 3X PERMANENTE
    # --------------------------------------------------------
    state.modo_3x_permanente = True
    log_fn("[OK] Modo 3X permanente ativado!")

    return True
