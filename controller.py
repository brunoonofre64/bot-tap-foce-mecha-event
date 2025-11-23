import time
import state
from actions import clicar_imagem, skip_com_reforco, tratar_maximo_mecha
from vision_300_detector import checar_e_tratar_mecha_300
import pyautogui


def bot_loop(log_fn, status_fn):
    status_fn("STATUS: EXECUTANDO", "green")
    log_fn("Bot iniciado — FULL MECHA + SKIP 5X + MECHA 300 + LUTAR INTELIGENTE + MODO 3X PERMANENTE")

    while state.bot_ativo:

        # =====================================================
        # 0 — CHECK: MECHA 300 (antes de tudo)
        # =====================================================
        checar_e_tratar_mecha_300(log_fn)

        # =====================================================
        # 1 — Emergência: Máximo Mecha
        # =====================================================
        if clicar_imagem("maximo_mecha.png", log_fn, "Máximo Mecha"):
            tratar_maximo_mecha(log_fn)
            continue

        # =====================================================
        # 2 — LUTAR INTELIGENTE (3X ou normal)
        # =====================================================
        log_fn("[PASSO] Procurando botões LUTAR...")

        achou_3x = clicar_imagem("lutar_3x.png", log_fn, "LUTAR 3X")
        if achou_3x:
            log_fn("[OK] LUTAR 3X detectado e clicado.")
        else:
            achou_normal = clicar_imagem("lutar.png", log_fn, "LUTAR")
            if achou_normal:
                log_fn("[OK] LUTAR normal detectado e clicado.")
            else:
                log_fn("[ERRO] Nenhum botão LUTAR encontrado.")
                time.sleep(2)
                continue

        time.sleep(2)

        # Emergência
        if clicar_imagem("maximo_mecha.png", log_fn, "Máximo Mecha"):
            tratar_maximo_mecha(log_fn)
            continue

        # =====================================================
        # 3 — LUTAR 2
        # =====================================================
        log_fn("[PASSO] Procurando LUTAR 2...")
        clicar_imagem("lutar_2.png", log_fn, "LUTAR 2")
        time.sleep(5)

        if clicar_imagem("maximo_mecha.png", log_fn, "Máximo Mecha"):
            tratar_maximo_mecha(log_fn)
            continue

        # =====================================================
        # 4 — SKIP
        # =====================================================
        log_fn("[PASSO] Procurando SKIP...")
        skip_com_reforco(log_fn)
        time.sleep(2)

        if clicar_imagem("maximo_mecha.png", log_fn, "Máximo Mecha"):
            tratar_maximo_mecha(log_fn)
            continue

        # =====================================================
        # 5 — CONTINUAR
        # =====================================================
        log_fn("[PASSO] Procurando CONTINUAR...")
        clicar_imagem("continuar.png", log_fn, "CONTINUAR")
        time.sleep(2)

        # =====================================================
        # 6 — CONTINUAR 2 opcional
        # =====================================================
        log_fn("[PASSO] Verificando CONTINUAR 2...")
        if clicar_imagem("continuar_2.png", log_fn, "CONTINUAR 2"):
            time.sleep(2)

        # =====================================================
        # 7 — MODO 3X: VOLTAR AO MECHA LOCAL (SEGURO)
        # =====================================================
        if state.modo_3x_permanente:
            log_fn("[INFO] Modo 3X permanente — retornando ao Mecha Local")

            # Delay para a tela carregar e não alucinar
            time.sleep(1.4)

            # localizar com confiança alta, sem clicar ainda
            box = pyautogui.locateOnScreen("mecha_local.png", confidence=0.92)

            if box:
                x, y = pyautogui.center(box)

                # NÃO CLICA SE ESTIVER PERTO DO TOPO (onde fica o chefe)
                if y > 200:
                    pyautogui.click(x, y)
                    log_fn("[OK] Clicou com segurança em MECHA LOCAL.")
                else:
                    log_fn("[ALERTA] Detecção suspeita perto do topo — clique ignorado.")
            else:
                log_fn("[ALERTA] Mecha Local não encontrado — evitando clique perigoso.")

        # =====================================================
        # CICLO FINAL
        # =====================================================
        log_fn("[CICLO] Ciclo concluído — reiniciando...\n")
        time.sleep(1)

    status_fn("STATUS: PARADO", "red")
    log_fn("Bot desligado.")
