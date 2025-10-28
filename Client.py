import socket
import threading
import sys


class AdvancedChatClient:
    def __init__(self, host='26.182.186.124', port=8000):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.running = True
        self.username = ""

    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print("Подключение к серверу установлено!")

            # Получаем приветственное сообщение
            welcome = self.client_socket.recv(1024).decode()
            print(welcome)

            # Ввод имени пользователя
            self.username = input().strip()
            self.client_socket.send(self.username.encode())

            # Запускаем поток для приема сообщений
            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.daemon = True
            receive_thread.start()

            print("-" * 50)

            # Основной цикл для отправки сообщений
            self.send_messages()

        except Exception as e:
            print(f"Ошибка подключения: {e}")
        finally:
            self.client_socket.close()

    def receive_messages(self):
        # Поток для приема сообщений от сервера
        while self.running:
            try:
                message = self.client_socket.recv(1024).decode()
                if message:
                    print(f"\r{message}\n> ", end='')
                else:
                    print("\nСервер отключен")
                    self.running = False
                    break
            except:
                print("\nОшибка соединения с сервером")
                self.running = False
                break

    def send_messages(self):
        # Цикл для отправки сообщений
        while self.running:
            try:
                message = input("> ")
                if message.lower() == '/quit':
                    self.client_socket.send('/quit'.encode())
                    self.running = False
                    break
                self.client_socket.send(message.encode())
            except KeyboardInterrupt:
                print("\nВыход из чата...")
                self.client_socket.send('/quit'.encode())
                self.running = False
                break
            except:
                print("Ошибка отправки сообщения")
                break

        self.client_socket.close()
        sys.exit()


if __name__ == "__main__":
    client = AdvancedChatClient()
    client.connect()