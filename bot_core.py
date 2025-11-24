# bot_core.py
import threading
import state
from controller import bot_loop


# ============================================================
# INICIAR BOT
# ============================================================
def iniciar_bot(log_fn, status_fn):
    if state.bot_ativo:
        log_fn("⚠ Bot já está ativo.")
        return

    state.bot_ativo = True

    thread = threading.Thread(
        target=bot_loop,
        args=(log_fn, status_fn),
        daemon=True
    )
    thread.start()

    log_fn("⏩ Bot iniciado (F5).")


# ============================================================
# PARAR BOT
# ============================================================
def parar_bot(log_fn, status_fn):
    if not state.bot_ativo:
        log_fn("⚠ Bot já está parado.")
        return

    state.bot_ativo = False
    log_fn("⛔ Parando bot (F6)...")
    status_fn("STATUS: PARADO", "red")
