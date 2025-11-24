# mecha_chefe_service.py
import pyautogui
from ataque_mecha_chefe import ciclo_cancelar_mecha_chefe

pyautogui.FAILSAFE = False
pyautogui.useImageNotFoundException(False)


def tratar_cancelar_mecha_chefe(log_fn):
    """
    Detecta a janela CANCELAR do Mecha Chefe e executa o fluxo correspondente.
    Retorna True se o fluxo foi tratado.
    Retorna False se nada foi detectado.
    """

    try:
        cancelar = pyautogui.locateCenterOnScreen(
            "images/cancelar.png",
            confidence=0.72
        )
    except:
        cancelar = None

    if not cancelar:
        return False

    log_fn("[EVENTO] CANCELAR encontrado — iniciando fluxo Mecha Chefe.")

    try:
        ciclo_cancelar_mecha_chefe(log_fn)
        log_fn("[CHEFE] Mecha Chefe finalizado — retorno ao fluxo normal.")
    except Exception as e:
        log_fn(f"[ERRO] Erro no fluxo Mecha Chefe: {e}")

    return True
