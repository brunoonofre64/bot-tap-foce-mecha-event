# interface.py
import tkinter as tk
import keyboard
from bot_core import iniciar_bot, parar_bot


# ============================================================
# CRIAR INTERFACE TKINTER
# ============================================================
def criar_interface():
    root = tk.Tk()
    root.title("Bot TapForce — FULL MECHA + SKIP 5X")
    root.geometry("500x520")
    root.configure(bg="black")

    # Título
    tk.Label(
        root,
        text="BOT TAP FORCE — FULL MECHA MODE",
        fg="red",
        bg="black",
        font=("Consolas", 18)
    ).pack(pady=10)

    # Instruções
    tk.Label(
        root,
        text="F5 → Iniciar\nF6 → Parar\nInclui fluxo completo para Máximo Mecha",
        fg="white",
        bg="black",
        font=("Consolas", 12)
    ).pack(pady=5)

    # Status
    lbl_status = tk.Label(
        root,
        text="STATUS: PARADO",
        fg="red",
        bg="black",
        font=("Consolas", 12)
    )
    lbl_status.pack(pady=10)

    # Log
    txt_log = tk.Text(
        root,
        height=20,
        width=65,
        bg="black",
        fg="red",
        font=("Consolas", 10)
    )
    txt_log.pack()

    # Função para log
    def log_fn(msg):
        txt_log.insert(tk.END, msg + "\n")
        txt_log.see(tk.END)

    # Função para status
    def status_fn(msg, color):
        lbl_status.config(text=msg, fg=color)

    # Hotkeys
    keyboard.add_hotkey("F5", lambda: iniciar_bot(log_fn, status_fn))
    keyboard.add_hotkey("F6", lambda: parar_bot(log_fn, status_fn))

    return root
