import ipaddress
import socket
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

COMMON_PORTS = [22, 80, 135, 139, 443, 445, 3389, 8080]
TIMEOUT = 0.5
results = []
host_count = 0


def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(TIMEOUT)
            result = sock.connect_ex((ip, port))
            return result == 0
    except:
        return False


def scan_host(ip):
    global host_count
    open_ports = []

    for port in COMMON_PORTS:
        if scan_port(ip, port):
            open_ports.append(port)

    if open_ports:
        host_count += 1
        print(f"\nHost ativo: {ip}")
        results.append(f"Host ativo: {ip}")

        for port in open_ports:
            print(f"  Porta {port}: ABERTA")
            results.append(f"  Porta {port}: ABERTA")


def save_results():
    if not results:
        return

    filename = f"scan_result_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("=== RESULTADO DO ESCANEAMENTO ===\n\n")
        for line in results:
            file.write(line + "\n")

    print(f"\nResultado salvo em: {filename}")


def main():
    print("""
==============================
      Python Network Scanner
==============================
""")

    network_input = input("Digite a rede (ex: 192.168.0.0/24): ")

    try:
        network = ipaddress.ip_network(network_input, strict=False)
    except ValueError:
        print("Rede inválida.")
        return

    print("\nEscaneando rede...")

    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(lambda ip: scan_host(str(ip)), network.hosts())

    print("\nEscaneamento finalizado.")
    print(f"\nHosts encontrados: {host_count}")
    save_results()


if __name__ == "__main__":
    main()
