# reward_service.py
import time
import pyautogui
from actions import clicar_imagem

pyautogui.FAILSAFE = False
pyautogui.useImageNotFoundException(False)


def coletar_recompensas(log_fn):
    """
    Verifica e coleta qualquer tipo de recompensa na tela.
    Mantém o comportamento original:
    - Loop até não haver mais nada para coletar
    - Usa clicar_imagem (com IMAGE_PATH)
    - Logs consistentes
    """

    log_fn("[CHECK] Verificando recompensas...")

    while True:
        achou = False

        if clicar_imagem("images/coletar.png", log_fn, "COLETAR"):
            achou = True

        if clicar_imagem("images/coletar_recompensa.png", log_fn, "COLETAR RECOMPENSAS"):
            achou = True

        if clicar_imagem("images/coletar_2.png", log_fn, "COLETAR (botão grande)"):
            achou = True

        # Se nenhuma recompensa foi encontrada, encerra o loop
        if not achou:
            log_fn("[OK] Nada para coletar.")
            return

        time.sleep(0.4)
