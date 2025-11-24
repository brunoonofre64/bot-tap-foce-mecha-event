# extra_events_service.py
import time
import pyautogui

pyautogui.FAILSAFE = False
pyautogui.useImageNotFoundException(False)


def tratar_extra_telefones(log_fn):
    img_plus3 = "images/mais3_telefone_prata.png"
    box_plus3 = pyautogui.locateOnScreen(img_plus3, confidence=0.72)

    if not box_plus3:
        return False

    log_fn("[EVENTO] Tela extra detectada: +3 telefones!")

    # 2) Clique reforçado
    try:
        px, py = pyautogui.center(box_plus3)
        pyautogui.click(px, py)
        time.sleep(0.25)
        pyautogui.click(px, py)  # clique duplo
        log_fn("[OK] Clique reforçado no +3 executado.")
    except:
        log_fn("[ERRO] Não conseguiu clicar no botão +3 telefones.")
        return False

    # 3) Aguardar transmissores SUMIR
    log_fn("[CHECK] Aguardando 'transmissores' SUMIR...")

    img_transm = "images/transmissores.png"
    for _ in range(20):
        ainda = pyautogui.locateOnScreen(img_transm, confidence=0.72)
        if not ainda:
            log_fn("[OK] Imagem 'transmissores' sumiu — tela mudou corretamente.")
            break
        time.sleep(0.2)
    else:
        log_fn("[ERRO] 'transmissores' NÃO sumiu — clique no +3 pode ter falhado.")
        return False

    time.sleep(0.3)

    # 4) Procurar botão CONFIRMAR 100
    log_fn("[CHECK] Procurando botão CONFIRMAR (100)...")

    img_conf = "images/confirmar_100_telefone_prata.png"

    for _ in range(12):
        box_conf = pyautogui.locateOnScreen(img_conf, confidence=0.72)
        if box_conf:
            cx, cy = pyautogui.center(box_conf)
            pyautogui.click(cx, cy)
            time.sleep(0.2)
            pyautogui.click(cx, cy)
            log_fn("[OK] Compra confirmada (+3 telefones).")
            time.sleep(1.0)
            return True

        time.sleep(0.25)

    log_fn("[ERRO] Botão CONFIRMAR (100) não encontrado após sumir transmissores.")
    return False
