
# Programa de un Cajero Automatico
# Autor: Andres Tencio
# Fecha: 17/3/2022
# Hora: 21:00
# ************************************
# Analisis
# Crear un programa que tenga las funciones de un cajero automatico
# Debe solicitarnos un PIN  de acceso
# Se debe poder consultar el saldo disponible
# Se pueden hacer depositos o retiros de ese saldo
# Debe ser posible hacer transferencias a otras cuentas
# Debemos poder pagar servicios publicos como agua, luz, telefono
# Es necesario poder cambiar el PIN de acceso a la cuenta
#
# Diseño
# Damos la bienvenida al usuario
# Al inico suponemos una cuenta en blanco y sin ningun PIN de acceso por lo cual se le solicita al usuario
# Indicamos que para iniciar debe ingresar el PIN  nuevamente
# Se realiza la validacion del PIN  con el mensaje que solo tiene 3 intentos de ingresar
#   el PIN incorrecto
# Indicamos al usuario si desea seguir realizando otra transaccion
# Verificamos la respuesta, en caso de ser SI se le mostrara las opciones disponibles
# En caso de la respuesta ser NO se le mostrara un mensaje de despedida
# Las opciones disponibles son: deposito, retiro, saldo, transferencia, pago de servicios y salir
# En la opcion de deposito solicitamos el monto a depositar y lo sumamos al saldo
# En la opciom de retiro solicitamos el monto y lo restamos al saldo, mostramos los billetes que se dispendaran dependiendo del montoa retirar
# En la opcion de transferencia mostramos las cuentas disponibles para hacer transferencias y solicitamons que digite una y el monto a transferir
#    restamos el monto al saldo y sumamos el saldo a la cuenta indicada
# En la opcion de pago de servicios mostramos los servicios disponibles para pagar y solicitamos que digite una de las opciones
#    restamos el monto o valor del servicio al saldo y actualizamos el valor del servicio a 0
# En la opcion de salir mostramos un mensaje de despedida

import random
import datetime


def num_trans():           # generamos un numero aleatorio junto con la fecha y hora para crear un numero de transacción
    n = 0
    x = datetime.datetime.now()
    r = random.randint(10000, 99999)
    print(r,x.year,x.month,x.day,x.hour,x.minute,x.second)
    
    

i = int
nuevo_pin = int(0)
salu2 = 0
opciones = int
saldo = float(0)

deposito = float()
retiro = float

cliente_trans = str
monto_trans = float
separador = ", "
transferencia = {"CARLOS": 0, "MARIA": 0, "JUAN": 0, "PABLO": 0, "OSCAR": 0} # opciones de nombres a quien se le pueden hacer transferecias
pago_servicios = {"AGUA": 5850, "ELECTRICIDAD": 15300, "TELEFONO": 10000} # opciones de pago de servicios
ser_pagar = str
cant_20 = 10
cant_10 = 10
cant_5 = 10
cant_2 = 100

# verificamos que el ususario ingrese solo numeros en el nuevo_pin
print ("\n      Bienvenido al Banco Nacional\n".upper())
while nuevo_pin == ValueError or nuevo_pin == 0:
    try:
        nuevo_pin = int(input("Digite su nuevo PIN: > "))
    except ValueError:
        print("Ingrese su pin en numeros")

# verificamos que el deposito sea en numeros
while saldo == ValueError or saldo == 0:
    try:
        saldo = int(input("Monto del primer deposito a su cuenta: > "))
    except:
        print("Digite su saldo en numeros")


while True:  # retornamos a la pantalla de inicio
    x = []
    SoN = ""
    pin = 0
    intentos = 3
    salu2 +=1
    if salu2 > 1:
        print("\n      Bienvenido al Banco Nacional\n".upper())
    for i in range(intentos):  # validamos solo 3 intentos de pin fallido
        if pin != nuevo_pin:
                 pin = int(input("Para iniciar digite su PIN: > "))
                 x.append(pin)
                 if x[i]!= nuevo_pin and i < intentos - 1: # no se muestra el " 0 intentos"
                     print("PIN incorrecto, le quedan ",intentos - i - 1," intentos")    
                     #if i == intentos - 1:
                 if i == intentos -1 and pin != nuevo_pin:
                         print("Su tarjeta sera bloqueada")
                 if x[i] == nuevo_pin:
                     
                      
    # cuando ingresamos solicitamos la respuesta de S o N para otra transaccion        
                     while SoN != "n" and SoN != "s":
                        SoN = input("Desea realizar otra transaccion: S/N > ").lower() # con lower() eliminamos el problema de mayuscula o minusculas
                        while SoN == "s":
                           opciones = (input("""\n 1.Deposito
 2.Retiro
 3.Saldo
 4.Transferencia a otra cuenta
 5.Pago de Servicios
 6.Salir
 > """))
                           
    # condicionamos las opciones 
                           if opciones == "1":
                              deposito = float(input("\nDigite el monto a depositar: > "))
                              saldo += deposito
                              print("Su saldo es de: > ",saldo)
                              print("Numero de transaccion: "),num_trans()

                                
                           if opciones == "2":
                              bil_2 = 2000
                              aux_2 = 0
                              bil_5 = 5000
                              aux_5 = 0
                              bil_10 = 10000
                              aux_10 = 0
                              bil_20 = 20000
                              aux_20 = 0  
                              aux_retiro = 0
                              retiro = int(input("\nDigite el monto a retirar: > "))
                              aux_retiro = retiro
                              for a in range(1000, aux_retiro+1, 1000):   # verificamos que se ingrese un monto en valores de 1000
                                  aux_retiro -= 1000
                              if aux_retiro == 0 and retiro != 1000 and retiro != 3000:     # se realiza el retiro solo si esta en valores de 1000, no es 1000 ni 3000
                                  if retiro <= saldo:
                                      bil_retiro = retiro
                            
                                      while bil_retiro >= bil_20 and cant_20 > 0:   #  contamos la cantidad de billetes que se necesitan para alcanzar el monto
                                          bil_retiro -= bil_20                      
                                          aux_20 += 1
                                          cant_20 -= 1                              # restamos los billetes que va entregando el cajero
                                      if bil_retiro > 100000:
                                          print("No se puede dispensar ese  monto el cajero no tiene billetes de ",bil_20)
                                      elif bil_retiro >= bil_10 and cant_10 == 0 and bil_retiro > 25000:   # verificamos tener billetes suficientes dependiendo del monto
                                           print("No se puede dispensar ese  monto el cajero no tiene billetes de ",bil_10)
                                      else:     
                                          while bil_retiro >= bil_10 and cant_10 > 0:     
                                              bil_retiro -= bil_10
                                              aux_10 += 1
                                              cant_10 -= 1
                                          
                                          if bil_retiro >= bil_5 and cant_5 == 0:
                                              print("No se puede dispensar ese  monto el cajero no tiene billetes de ",bil_5)
                                          else:    
                                              while bil_retiro >= bil_5 and bil_retiro != 8000 and cant_5 > 0:
                                                  bil_retiro -= bil_5
                                                  aux_5 += 1
                                                  cant_5 -= 1
                                              
                                            
                                              if bil_retiro >= 2000 and cant_2 < 4 or bil_retiro > 10000:  # verificacion e cantidad e billetes
                                                  print("No se puede dispensar ese monto el cajero no tiene billetes de ",bil_2)
                                              else:    
                                                  while bil_retiro >= bil_2 and cant_2 > 0:
                                                      bil_retiro -= bil_2
                                                      aux_2 += 1
                                                      cant_2 -= 1
                                                      
                                                  print("\nSe le entregaran:")   # si llegamos hasta acá mostramos la cantidad de billetes necesarios para dispensar el monto 
                                                  if aux_20 >= 1: print(aux_20," billetes de ",bil_20)
                                                  if aux_10 >= 1: print(aux_10," billetes de ",bil_10)
                                                  if aux_5 >= 1: print(aux_5," billetes de ",bil_5)
                                                  if aux_2 >= 1: print(aux_2," billetes de ",bil_2)
                                                  saldo -= retiro

                                                  
                                          print("Su saldo es de: > ",saldo)
                                          print("Numero de transaccion: "),num_trans()
                                  else: print("Saldo insuficiente")
                              else: print("Monto no valido")    
                              
                           if opciones == "3":
                              print("\nSu saldo es de: > ",saldo)
                              
                           if opciones == "4":
                              print("\nCuentas favoritas: ")
                              print(" > ",separador.join(transferencia)," < ")
                              cliente_trans = input("A quien desea realizar la transferencia? : > ")
                              if  cliente_trans in transferencia.keys():  # verificamos que el nombre ingresado se encuentre registrado
                                  monto_trans = int(input("Digite la cantidad a transferir: > "))
                                  if saldo >= monto_trans:
                                      #saldo = saldo - monto_trans
                                      saldo -= monto_trans
                                      print("> Transaccion exitosa <")
                                      print("Su saldo es de: > ",saldo)
                                      z = transferencia.get(cliente_trans) + monto_trans  # obtenemos el valor de la clave y le sumamos el monto a transferir
                                      transferencia.update({cliente_trans : z })          # actualizamos el valor de la clave 
                                      print("( Nuevo saldo de ", cliente_trans," es ",z,")")  # mostramos el saldo del otro cliente solo para verificar funcionamiento
                                      print("Numero de transaccion: "),num_trans()
                                  else:  print("Saldo insuficiente para realizar la transferencia")
                              else: print(cliente_trans, " no esta en sus cuentas favoritas")

                           if opciones == "5":
                              print("\nPago de servicios")
                              print("Sus servicios afiliados son:")
                              print(" > ",separador.join(pago_servicios)," < ")
                              serv_pagar = str(input("Cual servicio desea pagar: > "))
                              if serv_pagar in pago_servicios:
                                  s = pago_servicios.get(serv_pagar)      # obtenemos el valor de la clave 
                                  if s > 0:
                                      print("Monto a pagar: ",s)
                                      sino = ""
                                      while sino != "si" and sino != "no":
                                          sino = str(input("Desea realizar el pago SI/NO: > ")).lower()
                                      if sino == "si":
                                          if saldo >= s:
                                              saldo -= s
                                              s = 0
                                              pago_servicios.update({serv_pagar : s })  # actualizamos el valor de la clave
                                              print("> Transaccion exitosa <")
                                              print("Su saldo es de: > ",saldo)
                                              print("Numero de transaccion: "),num_trans()  
                                          else: print("Saldo insuficiente")
                                  else: print("El servicio no tiene pendientes de pago")
                              else: print("Servicio no afiliado")
                           if opciones != "":
                               SoN = input("\nDesea realizar otra transacción: S/N > ").lower()
                              
                        
                     else:
                         print ("\n      Gracias por utilizar los servicios del Banco Nacional \n     =====================================================".upper())
                         
                         
                       

