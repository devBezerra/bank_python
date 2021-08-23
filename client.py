from socket import *
import os

clear = lambda: os.system('cls')

HOST = "localhost"
PORT = 50000

connection = socket(AF_INET, SOCK_STREAM) #IPV4 e TCP
connection.connect((HOST, PORT))

while True:
    login = input('Login: ').upper()
    password = input('Password: ')

    if login.isalnum() and password.isalnum():
        connection.send(login.encode())
        connection.send(password.encode())
    else:
        print('Login or Password Invalid! \n')
        continue

    response = connection.recv(1024).decode()
    print(response)
    
    if response == 'SUCCESS':
        clear()
        print('================== WELCOME ==================')
        logged = True
        while logged:
            print('')
            print('Enter the option you want to perform:')
            print('1 - View Balance')
            print('2 - Deposit')
            print('3 - Draw')
            print('4 - Exit  \n')

            option = input('')
            print('')
            
            if option == '1':
                connection.send(option.encode())
                balance = connection.recv(1024)
                print(f'Your balance: $ {balance.decode()}')
            
            elif option == '2':
                deposit_value = input('Enter deposit amount: ')
                if deposit_value.isnumeric():
                    connection.send(option.encode())
                    connection.send(deposit_value.encode())
                    balance = connection.recv(1024)
                    print('')
                    print(f'Updated Balance: $ {balance.decode()}')
                else: print('Invalid Operation. Please try again.')

            elif option == '3':
                withdrawal_value = input('Enter withdraw amount: ')
                if withdrawal_value.isnumeric():
                    connection.send(option.encode())
                    connection.send(withdrawal_value.encode())
                    message = connection.recv(1024).decode()

                    if message == 'SUCCESS':
                        balance = connection.recv(1024)
                        print('')
                        print(f'Updated Balance: $ {balance.decode()}')
                    else:
                        print('')
                        print(message)
                else: 
                    print('Invalid Operation. Please try again.')
                    withdrawal_value = 0


            elif option == '4':
                connection.send(option.encode())
                print('=============== SEE YOU LATER =============== \n')
                logged = False

            else: print('INVALID OPERATION')
    else:
        print('Login or Password invalid! \n')

connection.close()