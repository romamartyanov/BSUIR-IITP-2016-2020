import random
import time

from pydes import des
from ast import literal_eval as make_tuple

current_milli_time = lambda: int(round(time.time() * 1000))
hours_to_milli = lambda hour: hour * 3600 * 10000


class DesEncrpter:
    # Encrypts or decrypts any tuple of data with DES encryption
    # Uses pydes library by Robin David (https://github.com/RobinDavid/pydes)

    def encrypt(self, data, key):
        print()
        print('BEFORE encrypt:', data)
        encrypted = des().encrypt(str(key), str(data), padding=True)
        print('AFTER encrypt:', encrypted)
        print()
        return encrypted

    def decrypt(self, data, key):
        print()
        print('BEFORE decrypt:', data)
        decrypted = des().decrypt(str(key), data, padding=True)
        decrypted = make_tuple(decrypted)
        print('AFTER decrypt:', decrypted)
        print()
        return decrypted


class KeyCreator:
    @staticmethod
    def create_key():
        return random.randint(100000000, 999999999)


class KDC:
    available_clients = ['client1', 'client2']
    clients_keys = [KeyCreator.create_key(), KeyCreator.create_key()]
    available_servers = ['server1', 'server2']
    servers_keys = [KeyCreator.create_key(), KeyCreator.create_key()]

    def __init__(self):
        self.des = DesEncrpter()
        self.tgs_id = 1
        self.key_tgs = KeyCreator.create_key()

    def get_permission_ticket(self, client_id):
        print('New permission ticket call')
        if client_id in self.available_clients:
            t = current_milli_time()
            p = hours_to_milli(48)
            key_tgs_c = KeyCreator.create_key()
            ticket = self.build_permission_ticket(client_id, self.tgs_id, t, p, key_tgs_c)
            print('New permission ticket:', ticket)

            encrypted_ticket = self.des.encrypt(ticket, self.key_tgs)
            bundle = (encrypted_ticket, key_tgs_c)

            index = self.available_clients.index(client_id)
            client_key = self.clients_keys[index]
            encrypted_bundle = self.des.encrypt(bundle, client_key)

            return encrypted_bundle

        print('Unknown client id')

    def get_server_ticket(self, permission_ticket, authority, server_id):
        print('New server ticket call')
        permission_ticket = self.des.decrypt(permission_ticket, self.key_tgs)
        client_id = permission_ticket[0]
        t = permission_ticket[2]
        p = permission_ticket[3]
        key_tgs_c = permission_ticket[4]

        print(
            'Permission ticket data. Client id: {}, timestamp: {}, period: {}, key TGS-Client: {}'.format(client_id, t,
                                                                                                          p, key_tgs_c))

        authority = self.des.decrypt(authority, key_tgs_c)
        auth_client_id = authority[0]
        auth_t = authority[1]

        print('Authority data. Client id: {}, timestamp: {}'.format(auth_client_id, auth_t))

        if client_id != auth_client_id:
            print('Invalid client')
            return None
        if auth_t < t or auth_t > t + p:
            print('Ticket is expired')
            return None

        t = current_milli_time()
        p = hours_to_milli(48)
        key_ss_c = KeyCreator.create_key()
        server_ticket = self.build_server_ticket(client_id, server_id, t, p, key_ss_c)
        print('New server ticket:', server_ticket)

        index = self.available_servers.index(server_id)
        server_key = self.servers_keys[index]
        encrypted_server_ticket = self.des.encrypt(server_ticket, server_key)
        bundle = (encrypted_server_ticket, key_ss_c)
        encrypted_bundle = self.des.encrypt(bundle, key_tgs_c)
        return encrypted_bundle

    @staticmethod
    def build_permission_ticket(client_id, tgs, t, p, key_tgs_c):
        return client_id, tgs, t, p, key_tgs_c

    @staticmethod
    def build_server_ticket(client_id, server_id, t, p, key_ss_c):
        return client_id, server_id, t, p, key_ss_c


class Client:
    def __init__(self, client_id, client_key, kdc, servers):
        self.client_id = client_id
        self.client_key = client_key
        self.kdc = kdc
        self.servers = servers
        self.des = DesEncrpter()
        self.permission_ticket = None
        self.key_tgs_c = None

    def make_server_call(self, server_number):
        print()
        print()
        print('Call server', server_number)
        server = self.servers[server_number]

        if self.permission_ticket is None or self.key_tgs_c is None:
            print('Trying to take permission ticket')
            permission_ticket_bundle = self.kdc.get_permission_ticket(self.client_id)
            if permission_ticket_bundle is None:
                return

            permission_ticket_bundle = self.des.decrypt(permission_ticket_bundle, self.client_key)

            permission_ticket = permission_ticket_bundle[0]
            key_tgs_c = permission_ticket_bundle[1]
            print('Key TGS-Client:', key_tgs_c)

            self.permission_ticket = permission_ticket
            self.key_tgs_c = key_tgs_c
        else:
            print('Permission ticket and key TGS-Client already defined')
            permission_ticket = self.permission_ticket
            key_tgs_c = self.key_tgs_c

        print()
        print('Trying to get server ticket')
        bundle = self.__call_tgs(permission_ticket, key_tgs_c, server.server_id)
        if bundle is None:
            return
        bundle = self.des.decrypt(bundle, key_tgs_c)

        server_ticket = bundle[0]
        key_ss_c = bundle[1]
        print('Key Server-Client:', key_ss_c)

        print()
        print('Trying to connect server')
        t = current_milli_time()
        authority = (self.client_id, t)
        authority_enctypted = self.des.encrypt(authority, key_ss_c)
        confirm_t = server.connect(server_ticket, authority_enctypted)
        if confirm_t is None:
            return
        confirm_t = self.des.decrypt(confirm_t, key_ss_c)
        if confirm_t != t + 1:
            print('Server returns wrong confirmation timestamp')
            return

        print()
        print('Server call is successful')

    def __call_tgs(self, permission_ticket, key_tgs_c, server_id):
        t = current_milli_time()
        print('Call TGS. Server id: {}, timestamp: {}'.format(server_id, t))
        authority = (self.client_id, t)
        authority_enctypted = self.des.encrypt(authority, key_tgs_c)
        bundle = self.kdc.get_server_ticket(permission_ticket, authority_enctypted, server_id)
        return bundle


class Server:
    def __init__(self, server_id, server_key):
        self.server_id = server_id
        self.server_key = server_key
        self.des = DesEncrpter()

    def connect(self, server_ticket, authority):
        print('New server connection')
        server_ticket = self.des.decrypt(server_ticket, self.server_key)
        client_id = server_ticket[0]
        server_id = server_ticket[1]
        t = server_ticket[2]
        p = server_ticket[3]
        key_ss_c = server_ticket[4]

        print('Server ticket data. Client id: {}, timestamp: {}, period: {}, key Server-Client: {}'.format(client_id, t,
                                                                                                           p, key_ss_c))

        if server_id != self.server_id:
            print('Wrong server')
            return None

        authority = self.des.decrypt(authority, key_ss_c)
        auth_client_id = authority[0]
        auth_t = authority[1]

        print('Authority data. Client id: {}, timestamp: {}'.format(auth_client_id, auth_t))

        if client_id != auth_client_id:
            print('Invalid client')
            return None
        if auth_t < t or auth_t > t + p:
            print('Ticket is expired')
            return None

        confirm_t = auth_t + 1
        print('Confirmation timestamp is', confirm_t)
        encrypted_confirm_t = self.des.encrypt(confirm_t, key_ss_c)
        return encrypted_confirm_t


def init():
    kdc = KDC()
    server1 = Server(kdc.available_servers[0], kdc.servers_keys[0])
    server2 = Server(kdc.available_servers[1], kdc.servers_keys[1])
    client = Client(kdc.available_clients[0], kdc.clients_keys[0], kdc, [server1, server2])

    print('server0 id: {}, server0 key: {}'.format(server1.server_id, server1.server_key))
    print('server1 id: {}, server1" key: {}'.format(server2.server_id, server2.server_key))
    print('Client id: {}, Client key: {}'.format(client.client_id, client.client_key))

    return client


client = init()
client.make_server_call(0)
client.make_server_call(1)

