import sys
clients = [
    [{
        "name":'Pablo',
        'company':'Google',
        'email':'jjjj@jjjj.com',
        'position':'data engineer',

    }],
    [{
        'name':'ricardo',
        'company':'facebook',
        'email':'aaaa@aaaa.aaa',
        'position':'data scientist',
    }]

]

def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')


def list_client():
    for idx, client in enumerate(clients):
        print(idx)
        print("{uid} | {name} | {company} | {email} | {position} ".format(
            uid=idx,
            name=clients["name"],
            company=clients["company"],
            email=clients["email"],
            position=clients["position"],
        ))


def update_client(client_name,updated_client_name):
    global clients
    if client_name in clients:
        index = client.index(client_name)
        client[index]=updated_client_name
    else:
        _not_client_name()


def search_client(client_name):
    for client in clients:
        if clients != client_name:
            continue
        else:
            return True


def delete_client(client_name):
    global clients
    if client_name in clients:
        clients.remove(client_name)
    else:
        _not_client_name()


def _print_welcome():
    print('Welcome to PlatziVentas')
    print('*'*50)
    print('What whoul you like to do today?')
    print('[C]reate client ')
    print('[U]pdate Client')
    print('[D]elete client')
    print('[L]ist client')
    print('[S]earch Client')

def _get_client_field(field_name):
    field = None
    while not field:
        field = input('What is the client {}? '.format(field_name))
    return field

def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name? ')
        if client_name == 'exit':
            client_name = None
            break
    if not client_name:
            sys.exit()

    return client_name

def _not_client_name():
    print('Client is not in client list')

if __name__=='__main__':
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'name':_get_client_field('name'),
            'company':_get_client_field('company'),
            'email':_get_client_field('email'),
            'position':_get_client_field('position'),
        }
        create_client(client)
        list_client()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_client()
        pass
    elif command == 'L':
        list_client()
        pass
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the updated client name? ')
        update_client(client_name,updated_client_name)
        list_client()
        pass
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('invalid command')

    
