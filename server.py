from socket import *

HOST = "localhost"
PORT = 50000

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((HOST, PORT))
sockobj.listen(1)

while True:
    connection, endereco = sockobj.accept()
    print('Connected to client')

    balance = 0
    while True:
        login = connection.recv(1024).decode()
        password = connection.recv(1024).decode()

        if login == 'MATEUS' and password == '12345':
            response = 'SUCCESS'
            connection.send(response.encode())

            while True:
                option = connection.recv(1024).decode()

                if option == '1':
                    connection.send(str(balance).encode())

                if option == '2':
                    deposit_value = float(connection.recv(1024))
                    balance = balance + deposit_value
                    connection.send(str(balance).encode())

                if option == '3':
                    withdrawal_value = float(connection.recv(1024))
                    if balance >= withdrawal_value:
                        message = 'SUCCESS'
                        connection.send(message.encode())
                        balance = balance - withdrawal_value
                        connection.send(str(balance).encode())
                    else:
                        message = 'Insufficient balance'
                        connection.send(message.encode())

                if option == '4':
                    break
        else:
            response = 'FAILURE'
            connection.send(response.encode())
    
print('Desconnected', endereco)
connection.close()
