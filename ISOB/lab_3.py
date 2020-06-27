import time


def print_package(package):
    try:
        time.sleep(1.5)
    except KeyboardInterrupt:
        raise BaseException("Interrupted by user")

    print("Next package. {}".format(package))


class IP:

    def __init__(self, source_ip, destination_ip, payload):
        self.version = 4
        self.ihl = 5
        self.dscp = None
        self.ecn = None
        self.total_length = 576  # let it be 576 to not fragment package
        self.id = None
        self.flags = None
        self.fragment_offset = None
        self.ttl = 15  # let it be max
        self.protocol = 6  # tcp code
        self.checksum = None  # ignore in ip
        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.payload = payload


class TCP:

    def __init__(self, source_port, destination_port, ip):
        self.ip = ip
        self.source_port = source_port
        self.destination_port = destination_port
        self.sequence = 0
        self.acknowledgment = 0
        self.offset = 20  # there is no additional options
        self.ns = None
        self.cwr = None
        self.ece = None
        self.urg = None
        self.ack = False
        self.psh = None
        self.rst = False
        self.syn = False
        self.fin = False
        self.window_size = None
        self.checksum = 0
        self.urgent = None

    def __str__(self):
        return 'Source {}:{}, Destination {}:{}, Seq: {}, Ack: {} Payload: "{}"'.format(
            self.ip.source_ip, self.source_port, self.ip.destination_ip, self.destination_port,
            self.sequence, self.acknowledgment, self.ip.payload)


class Connection:

    def __init__(self, members, middlewares):
        self.members = members
        self.middlewares = middlewares
        self.closed = False
        self.connected = False

    def __find_receiver(self, package):
        for member in self.members:
            if (member.ip_address == package.ip.destination_ip
                    and member.tcp_port == package.destination_port):
                return member

    def connect(self, package):
        self.connected = True
        self.process(package)

    def process(self, package):
        if not self.connected or self.closed:
            return

        print_package(package)

        for middleware in self.middlewares:
            package = middleware.change(package)

        if package.rst:
            print('Tcp was reset by rst flag')
            self.close()
            return

        package.ip.ttl -= 1
        if package.ip.ttl <= 0:
            print('Package ttl is expired')
            self.close()
            return

        receiver = self.__find_receiver(package)
        if receiver is None:
            print('Unknown destination {}:{}'.format(package.ip.destination_ip, package.destination_port))
            self.close()
            return

        package = receiver.receive(package)
        if package is None:
            print('One of members stop sending requests')
            self.close()
        else:
            self.process(package)

    def close(self):
        self.closed = True
        print('Connection is closed')


class Member:

    def __init__(self, ip_address, tcp_port):
        self.ip_address = ip_address
        self.tcp_port = tcp_port
        self.caller = False

    def callAnyOther(self, connection):
        self.caller = True
        other = connection.members[1]
        package = self.__build_package(other, self.__generate_payload())
        connection.connect(package)

    def __build_package(self, receiver, payload):
        ip = IP(self.ip_address, receiver.ip_address, "")
        tcp = TCP(self.tcp_port, receiver.tcp_port, ip)
        tcp.sequence = 0
        tcp.syn = True
        return tcp

    def _build_answer(self, package, payload):
        ip = IP(package.ip.destination_ip, package.ip.source_ip, "")
        tcp = TCP(package.destination_port, package.source_port, ip)

        if package.syn and package.ack:
            tcp.sequence = package.acknowledgment
            tcp.acknowledgment = package.sequence + 1
            tcp.ack = True
            return tcp
        if package.syn:
            tcp.sequence = 0
            tcp.acknowledgment = package.sequence + 1
            tcp.syn = True
            tcp.ack = True
            return tcp
        if package.ack:
            tcp.sequence = package.acknowledgment
            tcp.acknowledgment = len(payload)
            tcp.ip.payload = "Dummy package"
            return tcp

        tcp.ip.payload = payload

        if self.caller:
            tcp.sequence = package.acknowledgment
            tcp.acknowledgment = package.sequence + len(payload)
        else:
            tcp.sequence = package.acknowledgment
            tcp.acknowledgment = package.sequence
        return tcp

    def __generate_payload(self):
        return "A payload for member with address {}:{}".format(self.ip_address, self.tcp_port)

    def receive(self, package):
        answer = self._build_answer(package, self.__generate_payload())
        return answer


class HackerMember(Member):

    def __init__(self, ip_address, tcp_port):
        self.ip_address = ip_address
        self.tcp_port = tcp_port
        self.caller = False

    def receive(self, package):
        answer = self._build_answer(package, "Hacker server payload")
        return answer


class RSTMiddleware:

    def __init__(self):
        self.call_number = 0

    def change(self, package):
        self.call_number += 1
        if self.call_number == 5:
            package.rst = True
        return package


class TcpResetMiddleware:

    def __init__(self):
        self.call_number = 0

    def change(self, package):
        self.call_number += 1
        if self.call_number == 5:
            package.rst = False
        return package


class FakeIpAddressMiddleware:

    def __init__(self, ip_address, tcp_port):
        self.ip_address = ip_address
        self.tcp_port = tcp_port
        self.call_number = 0

    def change(self, package):
        self.call_number += 1
        if self.call_number == 5:
            package.ip.destination_ip = self.ip_address
            package.destination_port = self.tcp_port
        return package


class ConnectionHijack:

    def __init__(self):
        self.call_number = 0

    def change(self, package):
        self.call_number += 1
        if self.call_number >= 5:
            package.ip.payload = "Connection hijacked"
            t = package.sequence
            package.sequence = package.acknowledgment
            package.acknowledgment = t + len(package.ip.payload)
            package.ip.destination_ip = package.ip.source_ip
            package.destination_port = package.source_port
            print_package(package)
        return package


def run_attacks():
    client = Member(123, 1)
    server1 = Member(321, 3)
    server2 = HackerMember(231, 2)

    tcpResetMiddleware = TcpResetMiddleware()
    fakeIpAddressMiddleware = FakeIpAddressMiddleware(231, 2)
    rstMiddleware = RSTMiddleware()
    connectionHijack = ConnectionHijack()
    connection = Connection([client, server1, server2], [rstMiddleware])

    client.callAnyOther(connection)


run_attacks()
