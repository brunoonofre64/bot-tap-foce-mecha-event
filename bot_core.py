# bot_core.py
import threading
import state
from controller import bot_loop

# ============================================================
# INICIAR BOT (F5)
# ============================================================
def iniciar_bot(log_fn, status_fn):
    if state.bot_ativo:
        log_fn("⚠ Bot já está ativo.")
        return

    state.bot_ativo = True
    state.hard_stop = False

    # Loga claramente qual modo o F5 vai rodar
    if state.modo_mecha_chefe_infinito:
        log_fn("[START] F5 acionado em MODO MECHA CHEFE INFINITO (sem Mecha Local).")
    else:
        log_fn("[START] F5 acionado em modo NORMAL (Mecha Local + eventos).")

    thread = threading.Thread(
        target=bot_loop,
        args=(log_fn, status_fn),
        daemon=True,
    )
    thread.start()
    log_fn("⏩ Bot iniciado (F5).")

# ============================================================
# PARAR BOT (F6)
# ============================================================
def parar_bot(log_fn, status_fn):
    if not state.bot_ativo:
        log_fn("⚠ Bot já está parado.")
        return

    state.bot_ativo = False
    state.hard_stop = True
    state.modo_3x_permanente = False

    log_fn("⛔ Parando bot (F6)...")
    status_fn("STATUS: PARADO", "red")
