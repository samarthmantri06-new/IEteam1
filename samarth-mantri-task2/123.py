import random
import time

# DHCP Server
class DHCPServer:
    def __init__(self, ip_pool_start="192.168.1.2", ip_pool_end="192.168.1.254"):
        # Create IP pool (192.168.1.2 192.168.1.254)
        self.ip_pool = [f"192.168.1.{i}" for i in range(int(ip_pool_start.split('.')[-1]),
                                                        int(ip_pool_end.split('.')[-1]) + 1)]
        self.leases = {}  # MAC IP assigned

    def handle_dhcp_discover(self, mac):
        print(f"[DHCP] DISCOVER from {mac}")
        # Choose next available IP
        offer_ip = self.ip_pool[0]
        print(f"[DHCP] OFFER {offer_ip}")
        return offer_ip

    def handle_dhcp_request(self, mac, requested_ip):
        print(f"[DHCP] REQUEST from {mac} for {requested_ip}")
        # Confirm and assign IP
        if requested_ip in self.ip_pool:
            self.ip_pool.remove(requested_ip)
        self.leases[mac] = requested_ip
        print(f"[DHCP] ACK Assigned {requested_ip} to {mac}")
        return requested_ip


# DNS Server
class DNSServer:
    def __init__(self):
        self.records = {}  # hostname   IP

    def add_record(self, hostname, ip):
        self.records[hostname] = ip
        print(f"[DNS] Added record {hostname:<20} {ip}")

    def resolve(self, hostname):
        ip = self.records.get(hostname)
        if ip:
            print(f"[DNS] RESOLVE {hostname:<20} {ip}")
            return ip
        else:
            print(f"[DNS] Hostname {hostname} not found")
            return None

# Client
class Client:
    def __init__(self, name, dhcp_server, dns_server):
        self.name = name
        self.dhcp_server = dhcp_server
        self.dns_server = dns_server
        self.mac = self.generate_mac()
        self.ip = None

    def generate_mac(self):
        # Generate a random MAC address
        return "02:00:00:%02x:%02x:%02x" % (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

    def boot(self):
        # DHCP DISCOVER
        offered_ip = self.dhcp_server.handle_dhcp_discover(self.mac)
        # DHCP REQUEST
        self.ip = self.dhcp_server.handle_dhcp_request(self.mac, offered_ip)
        print(f"[BOOT] {self.name} received IP {self.ip}")

    def resolve_hostname(self, hostname):
        print(f"[QUERY] {self.name} requesting DNS for {hostname}...")
        return self.dns_server.resolve(hostname)

    def ping(self, target_ip):
        print(f"[PING] {self.name}   {target_ip} ...")
        time.sleep(0.5)
        print(f"[PING] {target_ip} replied to {self.name}\n")


# Simulation Start

# Initialize servers
dhcp_server = DHCPServer()
dns_server = DNSServer()

# Initialize clients
clientA = Client("ClientA", dhcp_server, dns_server)
clientB = Client("ClientB", dhcp_server, dns_server)

# Boot clients (DHCP negotiation)
clientA.boot()
print()
clientB.boot()
print()

# Add DNS records
dns_server.add_record("clientA.local", clientA.ip)
dns_server.add_record("clientB.local", clientB.ip)

# Client A resolves and pings Client B
target_ip = clientA.resolve_hostname("clientB.local")
if target_ip:
    clientA.ping(target_ip)

# Client B resolves and pings Client A
target_ip_b = clientB.resolve_hostname("clientA.local")
if target_ip_b:
    clientB.ping(target_ip_b)
