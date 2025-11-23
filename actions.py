import time
import pyautogui

pyautogui.FAILSAFE = False
pyautogui.useImageNotFoundException(False)


def clicar_imagem(img, log_fn, descricao):
    try:
        item = pyautogui.locateOnScreen(img, confidence=0.65)
    except:
        return False

    if item:
        try:
            x, y = pyautogui.center(item)
            pyautogui.click(x, y)
            log_fn(f"[OK] Clicou em {descricao}")
            return True
        except:
            return False

    return False


def skip_com_reforco(log_fn):
    tentativas = 0
    max_tentativas = 10

    while tentativas < max_tentativas:
        tentativas += 1

        try:
            skip_item = pyautogui.locateOnScreen("skip.png", confidence=0.65)
        except:
            skip_item = None

        if skip_item:
            x, y = pyautogui.center(skip_item)
            pyautogui.click(x, y)
            log_fn(f"[OK] SKIP clicado (tentativa {tentativas})")
            time.sleep(0.6)

            try:
                ainda_tem_5x = pyautogui.locateOnScreen("5x.png", confidence=0.65)
            except:
                ainda_tem_5x = None

            if not ainda_tem_5x:
                log_fn("[OK] 5x sumiu — SKIP confirmado")
                return True

            log_fn("[...] 5x ainda na tela — reforçando SKIP")
            time.sleep(0.4)

    log_fn("[ERRO] SKIP falhou após várias tentativas")
    return False


def tratar_maximo_mecha(log_fn):
    from actions import clicar_imagem  # evitar ciclo circular

    log_fn("[ALERTA] Máximo Mecha detectado — iniciando sequência especial")

    clicar_imagem("cancelar.png", log_fn, "Cancelar Máximo Mecha")
    time.sleep(2)

    clicar_imagem("mecha_chefe.png", log_fn, "Mecha Chefe")
    time.sleep(2)

    clicar_imagem("refresh.png", log_fn, "Refresh (1)")
    time.sleep(2)

    clicar_imagem("refresh.png", log_fn, "Refresh (2)")
    time.sleep(2)

    clicar_imagem("mecha_local.png", log_fn, "Mecha Local")
    time.sleep(2)

    log_fn("[CICLO] Reiniciando após Máximo Mecha")
    time.sleep(1)
