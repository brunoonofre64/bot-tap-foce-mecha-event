# interface.py
import tkinter as tk
import keyboard
import state
from bot_core import iniciar_bot, parar_bot

# ============================================================
# CRIAR INTERFACE TKINTER
# ============================================================
def criar_interface():
    root = tk.Tk()
    root.title("Bot TapForce — FULL MECHA + SKIP 5X")
    root.geometry("520x580")
    root.configure(bg="black")

    # --------------------------------------------------------
    # TÍTULO PRINCIPAL
    # --------------------------------------------------------
    tk.Label(
        root,
        text="BOT TAP FORCE — FULL MECHA MODE",
        fg="red",
        bg="black",
        font=("Consolas", 18),
    ).pack(pady=10)

    # --------------------------------------------------------
    # INSTRUÇÕES
    # --------------------------------------------------------
    tk.Label(
        root,
        text=(
            "F5 → Iniciar\n"
            "F6 → Parar\n"
            "Use o botão abaixo para ligar/desligar\n"
            "o modo Mecha Chefe Infinito."
        ),
        fg="white",
        bg="black",
        font=("Consolas", 12),
    ).pack(pady=5)

    # --------------------------------------------------------
    # STATUS GLOBAL
    # --------------------------------------------------------
    lbl_status = tk.Label(
        root,
        text="STATUS: PARADO",
        fg="red",
        bg="black",
        font=("Consolas", 12),
    )
    lbl_status.pack(pady=8)

    # --------------------------------------------------------
    # LABEL DO MODO MECHA CHEFE INFINITO
    # --------------------------------------------------------
    lbl_toggle_mecha_chefe = tk.Label(
        root,
        text="Fluxo Mecha Chefe: OFF",
        fg="red",
        bg="black",
        font=("Consolas", 12),
    )
    lbl_toggle_mecha_chefe.pack(pady=5)

    # --------------------------------------------------------
    # FUNÇÃO LOG (precisa existir antes de usar no botão)
    # --------------------------------------------------------
    txt_log = tk.Text(
        root,
        height=22,
        width=70,
        bg="black",
        fg="red",
        font=("Consolas", 10),
    )
    # vamos empacotar o log DEPOIS do botão, pra ele ficar mais abaixo

    def log_fn(msg: str):
        txt_log.insert(tk.END, msg + "\n")
        txt_log.see(tk.END)

    # --------------------------------------------------------
    # FUNÇÃO STATUS
    # --------------------------------------------------------
    def status_fn(msg: str, color: str):
        lbl_status.config(text=msg, fg=color)

    # --------------------------------------------------------
    # BOTÃO ON/OFF — Fluxo Mecha Chefe INFINITO
    # (logo abaixo do texto "Fluxo Mecha Chefe")
    # --------------------------------------------------------
    def toggle_mecha_chefe():
        state.modo_mecha_chefe_infinito = not state.modo_mecha_chefe_infinito

        if state.modo_mecha_chefe_infinito:
            lbl_toggle_mecha_chefe.config(
                text="Fluxo Mecha Chefe: ON",
                fg="green",
            )
            log_fn("[MODO CHEFE] Fluxo Mecha Chefe INFINITO → ATIVADO")
        else:
            lbl_toggle_mecha_chefe.config(
                text="Fluxo Mecha Chefe: OFF",
                fg="red",
            )
            log_fn("[MODO CHEFE] Fluxo Mecha Chefe INFINITO → DESATIVADO")

    btn_toggle = tk.Button(
        root,
        text="ATIVAR / DESATIVAR",
        command=toggle_mecha_chefe,
        bg="gray20",
        fg="white",
        font=("Consolas", 11),
        width=34,
    )
    # AGORA o botão fica logo abaixo da label
    btn_toggle.pack(pady=5)

    # --------------------------------------------------------
    # LOG (AGORA VEM DEPOIS DO BOTÃO)
    # --------------------------------------------------------
    txt_log.pack()

    # --------------------------------------------------------
    # HOTKEYS GLOBAIS
    # --------------------------------------------------------
    keyboard.add_hotkey("F5", lambda: iniciar_bot(log_fn, status_fn))
    keyboard.add_hotkey("F6", lambda: parar_bot(log_fn, status_fn))

    return root
