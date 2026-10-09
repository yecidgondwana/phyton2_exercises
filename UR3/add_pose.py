from rtde_receive import RTDEReceiveInterface

# Configuración de la conexión con el UR3
robot_receive = RTDEReceiveInterface("192.168.250.112")

# obtener la posición actual del robot
posicion_actual = robot_receive.getActualTCPPose() # primera posición del robot
print("Posición actual del robot:", posicion_actual)
input("para mover el robot manualmente a p1.")# move the robot manualmente con la teach pendant a la posición p1 y luego presiona Enter para continuar
p1 = robot_receive.getActualTCPPose() # primera posición del robot
print("Posición p1 del robot:", p1)

lado = 20

p2 = [p1[0] + lado, p1[1], p1[2], p1[3], p1[4], p1[5]]# segunda posición del robot
p3 = [p2[0], p2[1] + lado, p2[2], p2[3], p2[4], p2[5]]# tercera posición del robot
p4 = [p3[0] - lado, p3[1], p3[2], p3[3], p3[4], p3[5]]# cuarta posición del robot
p5 = [p2[0] + lado, p2[1], p2[2], p2[3], p2[4], p2[5]]
p6 = [p5[0], p5[1] + lado, p5[2], p5[3], p5[4], p5[5]]
p7 = [p6[0] - lado, p6[1], p6[2], p6[3], p6[4], p6[5]]
p8 = [p7[0], p7[1] - lado, p7[2], p7[3], p7[4], p7[5]]
p9 = [p5[0] + lado, p5[1], p5[2], p5[3], p5[4], p5[5]]
p10 = [p9[0], p9[1] + lado, p9[2], p9[3], p9[4], p9[5]]
     
recorrido = [p1, p2, p3, p4, p1, p2, p5, p6, p3, p2, p5, p9, p10, p6, p5, p9]
print("Recorrido del robot:", recorrido)
