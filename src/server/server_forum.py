import socket
import threading
import sys

HOST = '0.0.0.0'
PORT = 65432
BUFFER_SIZE = 1024

clients = []
message_history = []

lock = threading.Lock()

def broadcast(message, sender_socket=None):
    """Envia uma mensagem para todos os clientes, exceto o remetente (opcional)."""
    with lock:
        for client_socket, _ in list(clients): 
            if client_socket != sender_socket:
                try:
                    client_socket.sendall(message.encode('utf-8'))
                except:
                    remove_client((client_socket, None))

def handle_client(conn, addr):
    """Lida com a comunicação de um cliente específico."""
    print(f"[NOVA CONEXÃO] {addr} conectado.")

    with lock:
        if message_history:
            history_msg = "\n".join(message_history) + "\n"
            try:
                conn.sendall(history_msg.encode('utf-8'))
            except:
                print(f"[ERRO] Falha ao enviar histórico para {addr}. Fechando conexão.")
                remove_client((conn, addr))
                return

    while True:
        try:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                break

            message = data.decode('utf-8').strip()
            
            formatted_message = f"[{addr[0]}] {message}"
            print(f"Mensagem recebida: {formatted_message}")

            with lock:
                message_history.append(formatted_message)

            broadcast(formatted_message + "\n", conn) 

        except ConnectionResetError:
            break
        except Exception as e:
            print(f"[ERRO] Erro na comunicação com {addr}: {e}")
            break

    print(f"[DESCONEXÃO] {addr} desconectado.")
    remove_client((conn, addr))

def remove_client(client_tuple):
    """Remove um cliente da lista e fecha o socket."""
    client_socket, addr = client_tuple
    with lock:
        if any(c[0] == client_socket for c in clients): 
            try:
                client_to_remove = next(c for c in clients if c[0] == client_socket)
                clients.remove(client_to_remove)
            except StopIteration:
                 pass
            
            try:
                client_socket.close()
            except:
                pass 

def start_server():
    """Inicia o socket do servidor e o loop de aceitação."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    
    try:
        server.bind((HOST, PORT))
        server.listen()
        print(f"*** Servidor do Fórum iniciado em {HOST}:{PORT} ***")

        while True:
            conn, addr = server.accept() 
            
            with lock:
                clients.append((conn, addr))
            
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.daemon = True
            thread.start()
            print(f"[ATIVO] Total de clientes conectados: {threading.active_count() - 1}")
    
    except KeyboardInterrupt:
        print("\n[ENCERRAMENTO] Servidor desligado pelo usuário.")
    except Exception as e:
        print(f"[ERRO CRÍTICO] Falha ao executar o servidor: {e}")
    finally:
        server.close()
        sys.exit(0)

if __name__ == "__main__":
    start_server()