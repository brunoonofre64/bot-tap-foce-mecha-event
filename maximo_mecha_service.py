# maximo_mecha_service.py
import time
import pyautogui
from actions import clicar_imagem
from reward_service import coletar_recompensas

pyautogui.FAILSAFE = False
pyautogui.useImageNotFoundException(False)


def tratar_maximo_mecha(log_fn):
    """
    Fluxo completo quando o jogo exibe 'Máximo Mecha'.
    Retorna True se o fluxo foi tratado e o controller deve continuar o loop.
    Retorna False caso contrário.
    """

    # Detectar a imagem do Máximo Mecha
    if not clicar_imagem("images/maximo_mecha.png", log_fn, "Máximo Mecha"):
        return False

    log_fn("[ALERTA] Máximo Mecha detectado!")

    # Cancelar
    clicar_imagem("images/cancelar.png", log_fn, "Cancelar Máximo Mecha")
    time.sleep(1.0)

    # Entrar no Mecha Chefe
    clicar_imagem("images/mecha_chefe.png", log_fn, "Mecha Chefe")
    time.sleep(2)

    # Primeiro refresh
    clicar_imagem("images/refresh.png", log_fn, "Refresh (1)")
    time.sleep(2)

    coletar_recompensas(log_fn)

    # Segundo refresh
    clicar_imagem("images/refresh.png", log_fn, "Refresh (2)")
    time.sleep(2)

    coletar_recompensas(log_fn)

    # Voltar para o Mecha Local
    clicar_imagem("images/mecha_local.png", log_fn, "Voltar ao Mecha Local")
    time.sleep(2)

    return True
