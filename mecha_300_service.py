# mecha_300_service.py
import time
import pyautogui
from vision_300_detector import checar_e_tratar_mecha_300

pyautogui.FAILSAFE = False
pyautogui.useImageNotFoundException(False)


def tratar_mecha_300(log_fn):
    """
    Wrapper simples para manter compatibilidade com o comportamento original:
    - chama checar_e_tratar_mecha_300(log_fn)
    - retorna True se houve ação
    - retorna False caso contrário
    """

    try:
        mudou = checar_e_tratar_mecha_300(log_fn)
    except Exception as e:
        log_fn(f"[ERRO] Mecha 300: {e}")
        return False

    return bool(mudou)
