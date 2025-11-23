# vision.py
import cv2
import numpy as np
import pyautogui

def localizar(img_path, confianca=0.85):
    try:
        tela = pyautogui.screenshot()
        tela_np = cv2.cvtColor(np.array(tela), cv2.COLOR_RGB2BGR)

        template = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
        if template is None:
            return None

        res = cv2.matchTemplate(tela_np, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= confianca)

        for pt in zip(*loc[::-1]):
            h, w = template.shape[:2]
            centro = (pt[0] + w//2, pt[1] + h//2)
            return centro

        return None

    except:
        return None


def clicar_imagem(img, log_fn, msg="", confianca=0.85, repetir_ate_sumir=False):
    local = localizar(img, confianca)

    if not local:
        return False

    if msg:
        log_fn(f"[OK] {msg}")

    pyautogui.click(local)

    if repetir_ate_sumir:
        # clica até sumir da tela — turbo
        for i in range(10):
            local2 = localizar(img, confianca)
            if not local2:
                return True
            pyautogui.click(local)

    return True
