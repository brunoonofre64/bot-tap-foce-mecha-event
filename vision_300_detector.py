import pyautogui
import time
import state   # <--- importante para ativar modo 3X permanente

pyautogui.FAILSAFE = False
pyautogui.useImageNotFoundException(False)


def localizar(img, conf=0.70):
    try:
        return pyautogui.locateOnScreen(img, confidence=conf)
    except:
        return None


def clicar(img, log_fn, desc, conf=0.70):
    alvo = localizar(img, conf)
    if alvo:
        x, y = pyautogui.center(alvo)
        pyautogui.click(x, y)
        log_fn(f"[OK] Clicou em: {desc}")
        return True
    else:
        log_fn(f"[ERRO] Não encontrou para clicar: {desc}")
        return False


def checar_e_tratar_mecha_300(log_fn):
    """
    Se encontrar o 300_mecha_local:
      ❌ NÃO CLICA MAIS NO 300
      ✔ Clica no ataque 5x NÃO
      ✔ Ativa Modo 3X PERMANENTE
    """

    box = localizar("300_mecha_local.png", conf=0.70)

    if box:
        log_fn("[ALERTA] MECHA 300 DETECTADO!")

        # Apenas clica no 5X NÃO
        clicar("ataque_5x_nao.png", log_fn, "ATAQUE 5X NÃO", conf=0.70)
        time.sleep(0.5)

        # Ativar modo permanente
        state.modo_3x_permanente = True
        log_fn("[OK] Modo 3X permanente ativado!")

        return True

    return False
