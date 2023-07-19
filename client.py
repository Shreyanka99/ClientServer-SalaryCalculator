import socket


def employee_details():
    # Entering User Defined Data for every component
    basic_sal = float(input("Enter Basic Salary: "))
    da = float(input("Enter DA: "))
    it = float(input("Enter Income Tax: "))
    return basic_sal, da, it


def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_host = '127.0.0.1'  # Server IP (localhost)
    server_port = 12345        # Server port number

    try:
        client_socket.connect((server_host, server_port))
        print("Connected to server.")

        basic_sal, da, it = employee_details()

        # Send data to the server (basic salary, DA, IT)
        data = f"{basic_sal},{da},{it}"
        client_socket.send(data.encode())

        # Receive and print the net salary from the server
        net_salary = client_socket.recv(1024).decode()
        print(f"Net Salary: {net_salary}")

    except ConnectionRefusedError:
        print("Connection refused, Make sure the server is running.")
    except Exception as e:
        print("An Error occurred:", e)

    client_socket.close()
    print("Connection closed.")


if __name__ == "__main__":
    connect_to_server()
