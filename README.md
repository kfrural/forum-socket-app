# 💬 ForumTCP - Fórum de Mensagens Concorrente (Cenário 2)

## 📊 Sobre o Projeto

**ForumTCP** é um sistema de comunicação distribuída focado na implementação de um **Fórum de Mensagens Concorrente** utilizando o paradigma **Cliente/Servidor** baseado em **Sockets TCP/IP**. O projeto simula um ambiente de chat em grupo onde mensagens enviadas por qualquer cliente são retransmitidas (broadcast) em tempo real para todos os demais participantes.

O sistema foi desenvolvido sob a premissa de **confiabilidade e histórico**, garantindo que:

1.  A entrega das mensagens seja garantida (via TCP).
2.  Novos participantes recebam o histórico completo de todas as mensagens anteriores à sua conexão.
3.  O servidor utilize **concorrência (threading)** para gerenciar múltiplos clientes simultaneamente sem bloqueio.


-----

## 🚀 Principais Funcionalidades

  * **Comunicação TCP/IP:** Utilização de sockets TCP para garantir a entrega ordenada e confiável das mensagens.
  * **Conexão Multiusuário:** Suporte a múltiplos clientes conectados simultaneamente ao servidor.
  * **Mecanismo de Broadcast:** Servidor implementa uma rotina de *broadcast* para retransmitir mensagens recebidas a todos os clientes ativos, exceto o remetente.
  * **Gerenciamento de Histórico:** Servidor armazena todas as mensagens. Ao se conectar, o cliente recebe o *buffer* completo do histórico.
  * **Concorrência (Threading):** Servidor utiliza **threads** para isolar a manipulação de cada conexão, otimizando o desempenho e a responsividade.
  * **Estrutura Modular:** Código dividido claramente entre o lado do Cliente (`client_forum.py`) e do Servidor (`server_forum.py`).

-----

## 🛠️ Tecnologias Utilizadas

| Componente | Tecnologia | Propósito |
| :--- | :--- | :--- |
| **Linguagem Principal** | **Python 3.x** | Linguagem de desenvolvimento. |
| **Rede** | **`socket` (Biblioteca Padrão)** | Implementação do protocolo TCP/IP para comunicação cliente/servidor. |
| **Concorrência** | **`threading` (Biblioteca Padrão)** | Gerenciamento de conexões simultâneas no servidor. |
| **Sincronização** | **`threading.Lock`** | Proteção de recursos compartilhados (lista de clientes e histórico) contra condições de corrida. |

-----

## ⚙️ Como Rodar

O projeto foi configurado para ser executado em um ambiente virtual (`venv`) para garantir a portabilidade.

### Pré-requisitos

  * Python 3.x instalado.

### 1\. Estrutura e Preparação

Clone o repositório e navegue até a pasta raiz:

```bash
git clone https://github.com/kfrural/forum-socket-app.git

```

### 2\. Configuração do Ambiente Virtual (`venv`)

Crie e ative o ambiente virtual para isolar o projeto:

```bash
# Cria o ambiente virtual
python3 -m venv .venv 

# Ativação (Linux/macOS)
source .venv/bin/activate

# Ativação (Windows PowerShell)
.venv\Scripts\Activate.ps1
```

### 3\. Execução

Mantenha o ambiente virtual ativo (`(.venv)`) em todos os terminais.

#### Passo A: Iniciar o Servidor (Terminal 1)

O servidor deve ser o primeiro a ser executado.

```bash
python src/server/server_forum.py
```

**Saída:** O servidor começará a ouvir na porta `65432`.

#### Passo B: Iniciar os Clientes (Terminal 2, Terminal 3, ...)

Abra novos terminais (com o `venv` ativo) para cada cliente. O cliente recebe o IP do servidor como argumento. Use `127.0.0.1` para testar localmente.

```bash
# Conecta o cliente ao servidor local
python src/client/client_forum.py 127.0.0.1
```

Após a conexão, digite suas mensagens no prompt `>` e pressione **Enter** para enviá-las.

**Para sair:** Digite `sair` ou use `Ctrl+C`.

-----

## 📞 Contato

Para dúvidas, sugestões ou contribuições, por favor, entre em contato via GitHub.

Agradecemos por utilizar o **ForumTCP**\!