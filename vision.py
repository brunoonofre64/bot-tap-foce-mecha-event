import cv2
import numpy as np
import pyautogui


# ============================================================
# LOCALIZAR IMAGEM NA TELA (OpenCV + PyAutoGUI)
# ============================================================
def localizar(img, confianca=0.85):
    try:
        full_path = img

        # Screenshot da tela
        tela = pyautogui.screenshot()
        tela_np = cv2.cvtColor(np.array(tela), cv2.COLOR_RGB2BGR)

        # Carrega o template
        template = cv2.imread(full_path, cv2.IMREAD_UNCHANGED)
        if template is None:
            return None

        # Match da imagem
        res = cv2.matchTemplate(tela_np, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= confianca)

        # Encontra o primeiro ponto válido
        for pt in zip(*loc[::-1]):
            h, w = template.shape[:2]
            centro = (pt[0] + w // 2, pt[1] + h // 2)
            return centro

        return None

    except:
        return None


# ============================================================
# CLICAR EM IMAGEM COM MODO OPCIONAL DE REPETIR ATÉ SUMIR
# ============================================================
def clicar_imagem(img, log_fn, msg="", confianca=0.85, repetir_ate_sumir=False):
    local = localizar(img, confianca)

    if not local:
        return False

    if msg:
        log_fn(f"[OK] {msg}")

    pyautogui.click(local)

    # Modo turbo: clicar até o elemento desaparecer
    if repetir_ate_sumir:
        for _ in range(10):
            local2 = localizar(img, confianca)
            if not local2:
                return True
            pyautogui.click(local)

    return True
