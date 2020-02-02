clients = 'pablo,ricardo,'

def create_client(client_name):
    global clients

    if client_name not in clients:
        clients += client_name
        add_comma()
    else:
        print('Client already is in the client\'s list')


def list_clients():
    global clients

    print(clients)


def update_client(client_name,updated_client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + ',',updated_client_name + ',')
    else:
        _not_client_name()


def delete_client(client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name+',','')
    else:
        _not_client_name()
    pass

def add_comma():
    global clients

    clients += ','


def _print_welcome():
    print('Welcome to PlatziVentas')
    print('*'*50)
    print('What whoul you like to do today?')
    print('[C]reate client ')
    print('[U]pdate Client')
    print('[D]elete client')

def _get_client_name():
    return input('What is the client name? ')

def _not_client_name():
    print('Client is not in client list')
if __name__=='__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
        pass
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the updated client name? ')
        update_client(client_name,updated_client_name)
        list_clients()
        pass
    else:
        print('invalid command')

    
