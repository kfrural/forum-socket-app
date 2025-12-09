# 💬 ForumTCP - Concurrent Message Forum (Scenario 2)

## 📊 About the Project

**ForumTCP** is a distributed communication system focused on implementing a **Concurrent Message Forum** using the **Client/Server** paradigm based on **TCP/IP Sockets**. The project simulates a group chat environment where messages sent by any client are retransmitted (**broadcasted**) in real-time to all other connected participants.

The system was developed under the premise of **reliability and history**, ensuring that:

1.  Message delivery is guaranteed (via TCP).
2.  New participants receive the **complete history** of all messages sent prior to their connection.
3.  The server uses **concurrency (threading)** to manage multiple clients simultaneously without blocking.

-----

## 🚀 Main Features

  * **TCP/IP Communication:** Uses TCP sockets to ensure ordered and reliable message delivery.
  * **Multi-User Connection:** Supports multiple clients connected to the server simultaneously.
  * **Broadcast Mechanism:** The server implements a *broadcast* routine to retransmit received messages to all active clients, excluding the original sender.
  * **History Management:** The server stores all messages. Upon connecting, the client receives the complete *buffer* of message history.
  * **Concurrency (Threading):** The server uses **threads** to isolate the handling of each connection, optimizing performance and responsiveness.
  * **Modular Structure:** Code is clearly divided between the Client side (`client_forum.py`) and the Server side (`server_forum.py`).

-----

## 🛠️ Technologies Used

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Main Language** | **Python 3.x** | Development language. |
| **Networking** | **`socket` (Standard Library)** | Implementation of the TCP/IP protocol for client/server communication. |
| **Concurrency** | **`threading` (Standard Library)** | Management of simultaneous connections on the server. |
| **Synchronization** | **`threading.Lock`** | Protection of shared resources (client list and history) against race conditions. |

-----

## ⚙️ How to Run

The project has been configured to be run in a virtual environment (`venv`) to ensure portability.

### Prerequisites

  * Python 3.x installed.

### 1\. Structure and Setup

Clone the repository and navigate to the root folder:

```bash
git clone https://github.com/kfrural/forum-socket-app.git
cd forum-socket-app
```

### 2\. Virtual Environment (`venv`) Configuration

Create and activate the virtual environment to isolate the project:

```bash
# Create the virtual environment
python3 -m venv .venv 

# Activation (Linux/macOS)
source .venv/bin/activate

# Activation (Windows PowerShell)
.venv\Scripts\Activate.ps1
```

### 3\. Execution

Keep the virtual environment active (`(.venv)`) in all terminals.

#### Step A: Start the Server (Terminal 1)

The server must be started first.

```bash
python src/server/server_forum.py
```

**Output:** The server will start listening on port `65432`.

#### Step B: Start the Clients (Terminal 2, Terminal 3, ...)

Open new terminals (with `venv` active) for each client. The client requires the server's IP address as an argument. Use `127.0.0.1` for local testing.

```bash
# Connects the client to the local server
python src/client/client_forum.py 127.0.0.1
```

After connecting, type your messages at the `>` prompt and press **Enter** to send them.

**To exit:** Type `sair` or use `Ctrl+C`.

-----

## 📞 Contact

For questions, suggestions, or contributions, please contact us via GitHub.

Thank you for using **ForumTCP**\!