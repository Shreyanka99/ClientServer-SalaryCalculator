import socket


def calc_net_salary(basic_sal, da, it):
    # Calculation
    net_sal = basic_sal + da - it
    return net_sal


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = '127.0.0.1'  # Server IP (localhost)
    server_port = 12345       # Server port number

    server_socket.bind((server_host, server_port))
    server_socket.listen(1)
    print("Server is listening (Activated)")

    while True:
        client_socket, client_address = server_socket.accept()
        print("Connection is established with:", client_address)

        try:
            # Receive data from the client (basic salary, DA, IT)
            data = client_socket.recv(1024).decode()
            basic_salary, da, it = map(float, data.split(','))

            # Calculate net salary
            net_salary = calc_net_salary(basic_salary, da, it)

            # Send net salary back to the client
            client_socket.send(str(net_salary).encode())

        except ValueError:
            print("Invalid data received from client.")
        except Exception as e:
            print("An error occurred:", e)

        client_socket.close()
        print("Connection closed with:", client_address)


if __name__ == "__main__":
    start_server()
