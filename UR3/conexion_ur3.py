import socket
from rtde_control import RTDEControlInterface

ip_ur3 = '192.168.250.112' 
puerto = 30002
robot = RTDEControlInterface(ip_ur3)
print("RTDE conectado al UR3")
conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conexion.connect((ip_ur3, puerto))

print("Conexión establecida con el UR3 en la IP:", ip_ur3, "y puerto:", puerto)

conexion.close()
