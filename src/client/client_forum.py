import socket
import threading
import sys

HOST = '127.0.0.1'
PORT = 65432
BUFFER_SIZE = 1024

def receive_messages(client_socket):
    """Thread dedicada a receber e imprimir mensagens do servidor."""
    while True:
        try:
            data = client_socket.recv(BUFFER_SIZE)
            if data:
                print(f"\n{data.decode('utf-8').strip()}", flush=True)
            else:
                print("\n[DESCONEXÃO] Servidor fechou a conexão.")
                client_socket.close()
                sys.exit()
        except OSError:
            break
        except Exception as e:
            break

def start_client():
    """Inicia a conexão e o loop de envio de mensagens."""
    
    if len(sys.argv) > 1:
        server_host = sys.argv[1]
    else:
        server_host = HOST
        
    print(f"Tentando conectar ao Servidor: {server_host}:{PORT}")
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((server_host, PORT))
        print(f"*** Conectado ao Fórum. Digite 'sair' ou pressione Ctrl+C para encerrar. ***")

        receive_thread = threading.Thread(target=receive_messages, args=(client,))
        receive_thread.daemon = True
        receive_thread.start()

        while True:
            message = input("> ") 
            
            if message.lower() == 'sair':
                break
            
            client.sendall(message.encode('utf-8'))

    except ConnectionRefusedError:
        print(f"[ERRO] Conexão recusada. Verifique se o servidor está rodando.")
    except KeyboardInterrupt:
        print("\n[ENCERRANDO] Cliente desligado pelo usuário.")
    except Exception as e:
        print(f"[ERRO] Ocorreu um erro: {e}")
    finally:
        print("[ENCERRANDO] Fechando conexão.")
        client.close()
        sys.exit(0)

if __name__ == "__main__":
    start_client()