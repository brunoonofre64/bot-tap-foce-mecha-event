# TapForceBot — FULL MECHA MODE (.EXE)

> **Versão para usuário final**  
> Você vai receber uma pasta com um arquivo `.exe` do bot (por exemplo `TapForceBot.exe`) e alguns outros arquivos.  
> **Você NÃO precisa instalar Python, nem nada técnico.**  
> É só seguir os passos abaixo.

---

## 🚀 Como usar o bot (versão .EXE)

1. **Extraia a pasta do bot**
   - Descompacte o `.zip` que você recebeu em uma pasta simples, por exemplo:  
     `C:\TapForceBot\`

2. **Abra o jogo TapForce**
   - Deixe o jogo aberto no PC ou emulador.
   - Mantenha sempre a **mesma resolução** e o jogo **no mesmo lugar da tela**, para o bot reconhecer os botões.

3. **Execute o bot**
   - Dentro da pasta do bot, dê **dois cliques** no arquivo:
     - `TapForceBot.exe` (ou `main.exe`, dependendo de como foi gerado).
   - Vai abrir uma janelinha preta com interface escrita em vermelho, com o título:
     > `BOT TAP FORCE — FULL MECHA MODE`

4. **Escolha o modo de funcionamento**
   Na tela do bot, você verá:
   - Um texto: `Fluxo Mecha Chefe: OFF` (em vermelho)  
   - Um botão: `ATIVAR / DESATIVAR MODO MECHA CHEFE ∞`

   Funciona assim:

   - `Fluxo Mecha Chefe: OFF`  
     → **F5 usa o MODO NORMAL** (Mecha Local + eventos).
   - `Fluxo Mecha Chefe: ON`  
     → **F5 usa o MODO MECHA CHEFE INFINITO** (só chefe, sem limite de tempo).

   Para alternar:
   - Clique no botão **“ATIVAR / DESATIVAR MODO MECHA CHEFE ∞”**:
     - OFF → ON (verde) = chefe infinito  
     - ON → OFF (vermelho) = modo normal

5. **Iniciar e parar o bot**

   - **F5** → Inicia o bot  
     - Ele começa a jogar automaticamente conforme o modo atual.
   - **F6** → Para o bot  
     - Ele finaliza o ciclo atual (quando possível) e para.

6. **Acompanhar o que o bot está fazendo**

   Na parte de baixo da janela tem um campo de **log** (texto rolando).  
   Ali você vê:
   - quando ele clica em `LUTAR`, `LUTAR 3X`, `SKIP`, `CONTINUAR`, etc.
   - quando entra no Mecha Chefe
   - quando detecta eventos (Mecha 300, Máximo Mecha, +3 telefones, recompensas, etc.)
   - quando o fluxo é reiniciado

---

## 🧠 Modos de operação

### 1. Modo Normal (Mecha Local + eventos)

Esse é o modo padrão quando o texto está:

> `Fluxo Mecha Chefe: OFF`

Nesse modo o bot faz:

- Fica na tela de **Mecha Local**.
- Clica em:
  - `LUTAR 3X` (quando disponível), senão
  - `LUTAR` normal.
- Espera aparecer:
  - `LUTAR 2` → segue para o combate, ou
  - o evento de **+3 telefones prata** → trata o evento e volta ao ciclo.

Durante o fluxo normal, ele também trata:

- **Mecha 300**
  - Detecta o ícone de `300_mecha_local`.
  - Clica apenas em **“ATAQUE 5X NÃO”** (não ataca o Mecha 300).
  - Ativa o **modo 3X permanente**, ajustando a forma como luta depois.
- **Máximo Mecha**
  - Quando aparece a tela de **“Máximo Mecha”**, ele:
    - Clica **Cancelar**,
    - Abre o **Mecha Chefe**,
    - Dá **refresh**,
    - Coleta recompensas se existirem,
    - Dá outro refresh,
    - Coleta novamente,
    - Volta para o **Mecha Local**.
- **Cancelamento de Mecha Chefe (ciclo de 12 minutos)**
  - Quando encontra a tela com **“Cancelar”** relacionada ao Mecha Chefe:
    - Entra em um ciclo de ~12 minutos:
      - Abre o Mecha Chefe,
      - Dá refresh,
      - Escaneia todos os mechas na tela,
      - Vai testando cada um até achar um válido,
      - Faz o combate completo,
      - Repete até o tempo acabar.
    - No fim, volta para o **Mecha Local** e continua o fluxo normal.

Durante o combate ele faz:

- Clica em **`LUTAR 2`**;
- Espera um tempo de animação;
- Usa **SKIP reforçado** (clicando várias vezes até o `5x` sumir);
- Clica em **`CONTINUAR`** (e `CONTINUAR 2`, se existir);
- Se houver recompensa:
  - Clica em `COLETAR RECOMPENSA` e `COLETAR 2`;
- Se não houver recompensa:
  - Clica em `VOLTAR` e reinicia o ciclo.

---

### 2. Modo Mecha Chefe Infinito (só chefe, sem limite)

Esse modo é ativado quando o texto está:

> `Fluxo Mecha Chefe: ON` (em verde)

Nesse modo:

- Ao apertar **F5**, o bot:
  - **IGNORA completamente**:
    - Mecha Local,
    - Mecha 300,
    - Máximo Mecha,
    - fluxo de 12 minutos do Cancelar,
  - e foca **100% no Mecha Chefe**, em loop infinito, até você apertar **F6**.

Fluxo resumido do modo chefe infinito:

1. Abre o ícone do **Mecha Chefe**.
2. Clica em **`Refresh`**.
3. Escaneia todos os mechas na tela (Grou, Louva-Deus, Grifo, Kodiak, etc.).
4. Para cada mecha encontrado:
   - Clica nele e analisa o que aparece:
     - **Recompensa direta** → coleta e volta ao início.
     - **Ataque grátis (`ATAQUE GRÁTIS`)**:
       - Usa ataque grátis,
       - Clica em `LUTAR 2`,
       - Executa o combate normal (SKIP → CONTINUAR → recompensa/voltar).
     - **Combate normal**:
       - Verifica se existe **`LUTAR 3X DOURADO`**:
         - Se sim, faz o mini-ciclo 3X:
           - `LUTAR 3X DOURADO` → confirmar sumiço → `LUTAR 2` → combate normal.
         - Se não, clica direto em `LUTAR 2`.
       - Depois segue o **combate normal universal**:
         - SKIP,
         - CONTINUAR,
         - coleta recompensa ou VOLTAR,
         - se surgir `LUTAR 3X DOURADO` pós-continuar, executa o mini-ciclo de novo.

Se nenhum mecha for válido naquele refresh, ele loga algo como:

> `[WARN] Nenhum mecha válido → tentar de novo.`

E repete o ciclo: abre chefe → refresh → scan → teste dos mechas.

---

## 🔍 Principais componentes (visão técnica resumida)

> Esta parte é mais para quem é curioso ou quer entender a lógica interna.  
> Usuário final pode ignorar.

- **`interface.py`**
  - Cria a janela principal do bot (Tkinter).
  - Define:
    - Label de status (`STATUS: PARADO` / `STATUS: EXECUTANDO`).
    - Label do modo de Mecha Chefe (ON/OFF).
    - Botão de ativar/desativar o modo Mecha Chefe Infinito.
    - Caixa de log (texto rolando).
  - Registra as hotkeys globais:
    - F5 → `iniciar_bot`
    - F6 → `parar_bot`

- **`state.py`**
  - Guarda o estado global:
    - `bot_ativo`
    - `modo_3x_permanente`
    - `hard_stop`
    - `modo_mecha_chefe_infinito`

- **`bot_core.py`**
  - Decide qual modo será executado quando o usuário aperta F5:
    - Se `modo_mecha_chefe_infinito == True` → chama fluxo só do chefe.
    - Caso contrário → fluxo normal (Mecha Local + eventos).
  - Garante que as flags de estado existam e estejam consistentes.

- **`controller.py`**
  - **Cérebro do loop principal**:
    - Se Mecha Chefe Infinito estiver ON:
      - Chama `fluxo_mecha_chefe_infinito(log_fn)` e ignora todo o resto.
    - Se estiver OFF:
      - Roda:
        - `tratar_mecha_300`
        - `tratar_maximo_mecha`
        - `tratar_cancelar_mecha_chefe`
        - `rotina_lutar_mecha_local`
        - `rotina_lutar_2_skip_continuar`
        - clique de segurança em `Mecha Local` quando modo 3X está ativo.

- **`mecha_local_service.py` / `mecha_local_combat_service.py`**
  - Responsáveis por:
    - Clicar em `LUTAR 3X` ou `LUTAR` no Mecha Local.
    - Detectar `LUTAR 2` ou evento de `+3 telefones`.
    - Chamar o fluxo de combate (`LUTAR 2` → SKIP → CONTINUAR → etc).

- **`mecha_chefe_service.py` / `mecha_chefe_infinito_service.py` / `ataque_mecha_chefe.py`**
  - Implementam todo o fluxo do Mecha Chefe:
    - Scan de mechas,
    - Caminhos de ataque grátis,
    - Combate normal universal,
    - Mini-ciclo `LUTAR 3X DOURADO`,
    - Coleta de recompensa ou voltar,
    - Ciclo finito (cancelar) e infinito (modo chefe ∞).

- **`mecha_300_service.py`**
  - Detecta o Mecha 300.
  - Evita atacar esse mecha (clica em **“5X NÃO”**).
  - Ativa o modo 3X permanente.

- **`maximo_mecha_service.py`**
  - Trata o evento de **“Máximo Mecha”**:
    - Cancela,
    - Entra no Mecha Chefe,
    - Dá dois refresh,
    - Coleta recompensas,
    - Volta ao Mecha Local.

- **`extra_events_service.py`**
  - Trata o evento de **+3 telefones prata**.

- **`reward_service.py`**
  - Varre a tela coletando qualquer tipo de recompensa:
    - `COLETAR`
    - `COLETAR RECOMPENSA`
    - `COLETAR 2`

- **`actions.py` / `vision.py` / `vision_300_detector.py` / `screen_utils.py`**
  - Funções auxiliares:
    - Clique em imagem com confiança (PyAutoGUI).
    - Localização de imagens com OpenCV.
    - SKIP reforçado.
    - Clique seguro no botão Mecha Local (evitando topo da tela).
    - Detecção do Mecha 300.

---

## ⚙️ Para desenvolvedores — reconstruir o .EXE com cx_Freeze

Se você estiver com o **código-fonte** e quiser gerar o `.exe` novamente:

1. **Pré-requisitos**
   - Python 3.10 instalado.
   - Pip atualizado.
   - Windows.

2. **Criar ambiente virtual (opcional, mas recomendado)**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
