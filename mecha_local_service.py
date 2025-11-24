# mecha_local_service.py
import time
import pyautogui

from actions import clicar_imagem
from screen_utils import clicar_mecha_local_seguranca
from extra_events_service import tratar_extra_telefones

pyautogui.FAILSAFE = False
pyautogui.useImageNotFoundException(False)


def rotina_lutar_mecha_local(log_fn):
    """
    Novo fluxo REAL e CORRETO:
    1) Clica LUTAR 3X ou LUTAR
    2) AGUARDA uma das DUAS coisas aparecer:
         - LUTAR 2  (fluxo normal)
         - +3 TELEFONES  (fluxo extra)
    3) Se +3 TELEFONES → trata e reinicia ciclo
    4) Se LUTAR 2 → retorno True para seguir ao passo SKIP
    """

    clicar_mecha_local_seguranca(log_fn)
    log_fn("────────────────────────────────────────────")
    log_fn("[FLOW] INÍCIO DO PASSO 1 → Buscar botão LUTAR")
    log_fn("────────────────────────────────────────────")

    # 1) Tenta LUTAR 3X
    log_fn("[CHECK] Tentando LUTAR 3X...")
    if clicar_imagem("images/lutar_3x.png", log_fn, "LUTAR 3X"):
        log_fn("[STATE] LUTAR 3X foi clicado com sucesso.")
    else:
        # 2) Tenta LUTAR normal
        log_fn("[CHECK] Tentando LUTAR normal...")
        if not clicar_imagem("images/lutar.png", log_fn, "LUTAR (1x)"):
            log_fn("[FALHA] Nenhum botão LUTAR encontrado — aguardando próximo ciclo.")
            return False
        log_fn("[STATE] LUTAR normal foi clicado com sucesso.")

    # 3) Esperar pelo LUTAR 2 OU pelo +3 TELEFONES
    log_fn("[CHECK] Aguardando LUTAR 2 OU +3 TELEFONES...")

    for tentativa in range(15):
        log_fn(f"[CHECK] Tentativa {tentativa+1}/15...")

        # A) Checar evento extra
        if pyautogui.locateOnScreen("images/mais3_telefone_prata.png", confidence=0.72):
            log_fn("[EVENTO] +3 TELEFONES DETECTADO!")
            tratar_extra_telefones(log_fn)
            log_fn("[RESULT] Evento extra finalizado → reiniciando ciclo.")
            return "EXTRA"

        # B) Checar se apareceu LUTAR 2
        if pyautogui.locateOnScreen("images/lutar_2.png", confidence=0.72):
            log_fn("[OK] LUTAR 2 detectado → seguir fluxo normal.")
            return "LUTAR"

        time.sleep(0.35)

    # Se nenhum dos dois aparecer
    log_fn("[ERRO] Nem LUTAR 2 nem +3 telefones apareceram — reiniciando ciclo.")
    return False
