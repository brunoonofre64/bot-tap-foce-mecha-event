import threading
from controller import bot_loop
import state


def iniciar_bot(log_fn, status_fn):
    if not state.bot_ativo:
        state.bot_ativo = True

        threading.Thread(
            target=bot_loop,
            args=(log_fn, status_fn),
            daemon=True
        ).start()

        log_fn("⏩ Bot iniciado (F5).")


def parar_bot(log_fn, status_fn):
    if state.bot_ativo:
        state.bot_ativo = False
        log_fn("⛔ Parando bot (F6)...")
