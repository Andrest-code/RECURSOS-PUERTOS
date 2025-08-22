import sys
import socket
from datetime import datetime
def grab_banner(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            s.connect((ip, port))
            banner = s.recv(1024).decode(errors="ignore").strip()
            return banner if banner else "Servicio desconocido"
    except (socket.timeout, ConnectionRefusedError):
        return "No se pudo obtener el banner"
    except Exception as e:
        return f"Error: {e}"
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Argumentos no válida.")
    print("Sintaxis: python3 port_scanner.py <ip>")
    sys.exit(1)
print("-" * 50)
print(f"Escaneando objetivo: {target}")
print(f"Tiempo de inicio: {datetime.now()}")
print("-" * 50)
start_time = datetime.now()
open_ports = 0
try:
    socket.setdefaulttimeout(1)
    for port in range(1, 1024):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            result = s.connect_ex((target, port))
            if result == 0:
                banner = grab_banner(target, port)
                print(f"[+] Puerto {port}: ABIERTO - {banner}")
                open_ports += 1
except KeyboardInterrupt:
    print("\n[!] Saliendo del programa.")
    sys.exit()
except socket.gaierror:
    print("\n[!] No se puede resolver el Hostname.")
    sys.exit()
except socket.error:
    print("\n[!] No se puede conectar al servidor.")
    sys.exit()
end_time = datetime.now()
total_time = end_time - start_time
print("\n" + "-" * 50)
print(f"Escaneo completado en: {total_time}")
print(f"Puertos abiertos encontrados: {open_ports}")
print("-" * 50)
