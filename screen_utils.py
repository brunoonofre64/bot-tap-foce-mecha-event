# screen_utils.py
import time
import pyautogui

pyautogui.FAILSAFE = False
pyautogui.useImageNotFoundException(False)


def clicar_mecha_local_seguranca(log_fn):
    """
    Clique seguro no botão Mecha Local, evitando cliques acidentais no topo da tela.
    """

    try:
        box = pyautogui.locateOnScreen("images/mecha_local.png", confidence=0.92)
    except:
        box = None

    if box:
        x, y = pyautogui.center(box)

        if y > 200:
            pyautogui.click(x, y)
            log_fn("[OK] MECHA LOCAL clicado antes da ação.")
            time.sleep(1.0)
        else:
            log_fn("[ALERTA] Mecha Local detectado muito no topo — clique ignorado.")
    else:
        log_fn("[ALERTA] Não encontrou MECHA LOCAL antes da ação.")
