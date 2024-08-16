#Proyecto Administración
#Administración de redes     	Grupo 3
#Semestre 2018-2
#Profesora: M.C. Cintia Quezada Reyes
#Benitez Herrera Adolfo
#Chávez Molina José Alberto
#Gutiérrez Álvarez Luis Horacio
#Real Badillo Sandra Angélica
#Velazquez Paulin Tania N.

#Exporta las librerias necesarias para la parte gráfica
from tkinter import *
import math
import ipaddress

#Declaro una ventana
#v=Tk()

v=Tk()

v.title("Proyecto")
imagenL=PhotoImage(file="portada.gif")
lblImagen=Label(v,image=imagenL).place(x=100,y=30)

#Crear un objeto de tipo label que es solo el texto que se muestra
#La funcion recibe la ventana donde estara y el texto a mostrar
l1=Label(v,text="Inserta una dirección")
#Posiciono mi ventana
l1.place(x=10,y=490)
#Creo la entrada
#La funcion recibe la ventana donde estara y su tamaño
e1=Entry(v,bd=5)
#Posiciono mi entrada
e1.place(x=200,y=490)

#Crear un objeto de tipo label que es solo el texto que se muestra
#La funcion recibe la ventana donde estara y el texto a mostrar
l2=Label(v,text="Inserta el número de redes")
#Posiciono mi ventana
l2.place(x=10,y=520)
#Creo la entrada
#La funcion recibe la ventana donde estara y su tamaño
e2=Entry(v,bd=5)
#Posiciono mi entrada
e2.place(x=200,y=520)

#Crear un objeto de tipo label que es solo el texto que se muestra
#La funcion recibe la ventana donde estara y el texto a mostrar
l3=Label(v,text="Inserta el número de hosts")
#Posiciono mi ventana
l3.place(x=10,y=550)
#Creo la entrada
#La funcion recibe la ventana donde estara y su tamaño
e3=Entry(v,bd=5)
#Posiciono mi entrada
e3.place(x=200,y=550)

#Crear un objeto de tipo label que es solo el texto que se muestra
#La funcion recibe la ventana donde estara y el texto a mostrar
l4=Label(v,text="Escoje el número de red")
#Posiciono mi ventana
l4.place(x=10,y=580)
#Creo la entrada
#La funcion recibe la ventana donde estara y su tamaño
e4=Entry(v,bd=5)
#Posiciono mi entrada
e4.place(x=200,y=580)

###################################################################
#####################Salidas###########################
###################################################################

try:
	def promCallback():

		#Funcion para obtener la direccion IP
		#Es una clase
		print("###############################################################################################################################################")
		print("Dirección dada")
		print(ipaddress.IPv4Address(e1.get()))
		#print(int(ipaddress.IPv4Address(e1.get())))

		#Calculo el número de redes
		#print(math.log(float(e2.get()),2))
		Numred = math.ceil(math.log(float(e2.get()),2))
		#print(Numred)

		#Calculo los bits para host
		#print(math.log(float(e3.get()),2))
		Numhost =math.ceil(math.log(float(e3.get()),2))
		#print(Numhost)

		#Calculo de bits para host
		print("Numero de bits para los host")
		print(len(bin(int(e3.get()))))

		#Caluclo de la red
		print("Numero de bits para la red")
		print(len(bin(int(e4.get()))))
		Nored = bin(int(e4.get()))

		#wea
		#print(bin(int(ipaddress.IPv4Address(e1.get()))))

##############################################################################################################################################################

		#Secuencia para determinar que tipo de red es
		if ipaddress.IPv4Address(e1.get()) >= ipaddress.IPv4Address('1.0.0.0') and ipaddress.IPv4Address(e1.get()) <= ipaddress.IPv4Address('127.255.255.255'):
			print('clase A')
#Verifica cuantos bits caben en los octeto
			if len(str(bin(((int(e2.get())+int(e3.get())))))) == 24:
				#print("valido")
				#Obtiene la direccion dada
				prueba = str((ipaddress.IPv4Address(e1.get()))).split(".")
				#Declaro variables auxiliares
				#prueba2 = []
				#Saber cuantos bits necesita
				#A 8 bits resto los necesarios para la red
				numBits = 24 - Numred
				#Variable auxiliar para el ultimo octeto
				#prueba3 = str(bin(numBits))

				#Guardo la dir en una variable auxiliar
				#for i in prueba:
					#print(i)
					#prueba2.append(bin(int(i)))

				#Para poder sumar la cadena
				#Así se ve el número de cada red
				for j in range(0,numBits):
					Nored =Nored+"0"
				#print(Nored)

				#######
				##Aqui hago las transformaciones para devolverlo como una dirección
				###

				#El resultado de redes del octeto
				#octeto1 = int(prueba2[3],2)+int(Nored,2)
				#Octeto es el ultimoi el que 
				octetodoble = ipaddress.IPv4Address(e1.get())+int(Nored,2)
				print("Red")
				redaux = int(e4.get())
				#print(redaux)


				##########
				#print(int(prueba2[3],2)+Numhost)

				#Segmento
				print("Segmento")
				print(octetodoble+redaux)
				
				#Broadcast
				if Numhost==0 or Numred == 0:
					printf("Error")
					pass
				elif Numhost ==1:
					broad=="1"
					print("Broadcast")
					print(ipaddress.IPv4Address(e1.get())+int(broad,2)+int(Nored,2))	

					#Rango útil
					print("Rango")
					print(ipaddress.IPv4Address(e1.get())+1+int(Nored,2))
					print(ipaddress.IPv4Address(e1.get())+int(broad,2)-1+int(Nored,2))

				else:
					for k in range(0,Numhost):
							broad=broad+"1"
					#print(int(broad,2))
					print("Broadcast")
					print(ipaddress.IPv4Address(e1.get())+int(broad,2)+int(Nored,2))	

					#Rango útil
					print("Rango")
					print(ipaddress.IPv4Address(e1.get())+1+int(Nored,2))
					print(ipaddress.IPv4Address(e1.get())+int(broad,2)-1+int(Nored,2))


			elif len(str(bin(int(e2.get())+int(e3.get())))) < 24:
				#print("valido")

				#Obtiene la direccion dada
				prueba3 = str((ipaddress.IPv4Address(e1.get()))).split(".")
				#Declaro variables auxiliares
				prueba4 = []
				#Saber cuantos bits necesita
				numBits = 16 - Numred
				#Variable auxiliar para el ultimo octeto
				#prueba3 = str(bin(numBits))
				bitsSobrantes=16-(Numred+Numhost)
				Compartidos=int(bitsSobrantes/2)

				#Guardo la dir en una variable auxiliar
				for i in prueba3:
					#print(i)
					prueba4.append(bin(int(i)))

				#Para poder sumar la cadena del número de red
				#Empuja la cadena
				for j in range(0,numBits-Compartidos):
					Nored =Nored+"0"
				#print(Nored)

				#######
				##Aqui hago las transformaciones para devolverlo como una dirección
				###
				octeto = ipaddress.IPv4Address(e1.get())+int(Nored,2)
				print("Red")
				print(int(e4.get()))


				##########
				#print(int(prueba2[3],2)+Numhost)

				#Segmento
				print("Segmento")
				print(octeto)
				
				#Broadcast
				broad=""
				if Numhost==0:
					printf("Error")
					pass
				elif Numhost ==1:
					broad=="1"
					print("Broadcast")
					print(ipaddress.IPv4Address(e1.get())+int(broad,2)+int(Nored,2))	

					#Rango útil
					print("Rango")
					print(ipaddress.IPv4Address(e1.get())+1+int(Nored,2))
					print(ipaddress.IPv4Address(e1.get())+int(broad,2)-1+int(Nored,2))

				else:
					for k in range(0,Numhost):
						broad=broad+"1"
					#print(int(broad,2))
					print("Broadcast")
					print(ipaddress.IPv4Address(e1.get())+int(broad,2)+int(Nored,2))	

					#Rango útil
					print("Rango")
					print(ipaddress.IPv4Address(e1.get())+1+int(Nored,2))
					print(ipaddress.IPv4Address(e1.get())+int(broad,2)-1+int(Nored,2))


##############################################################################################################################################################

		elif ipaddress.IPv4Address(e1.get()) >= ipaddress.IPv4Address('128.0.0.0') and ipaddress.IPv4Address(e1.get()) <= ipaddress.IPv4Address('191.255.255.255'):
			print('clase B')
			#Verifica cuantos bits caben en los octeto
			if len(str(bin(((int(e2.get())+int(e3.get())))))) == 16:
				#print("valido")
				#Obtiene la direccion dada
				prueba = str((ipaddress.IPv4Address(e1.get()))).split(".")
				#Declaro variables auxiliares
				prueba2 = []
				#Saber cuantos bits necesita
				#A 8 bits resto los necesarios para la red
				numBits = 16 - Numred
				#Variable auxiliar para el ultimo octeto
				#prueba3 = str(bin(numBits))

				#Guardo la dir en una variable auxiliar
				for i in prueba:
					#print(i)
					prueba2.append(bin(int(i)))

				#Para poder sumar la cadena
				#Así se ve el número de cada red
				for j in range(0,numBits):
					Nored =Nored+"0"
				#print(Nored)

				#######
				##Aqui hago las transformaciones para devolverlo como una dirección
				###

				#El resultado de redes del octeto
				#octeto1 = int(prueba2[3],2)+int(Nored,2)
				#Octeto es el ultimoi el que 
				octetodoble = ipaddress.IPv4Address(e1.get())+int(Nored,2)
				print("Red")
				redaux = int(e4.get())
				print(redaux)


				##########
				#print(int(prueba2[3],2)+Numhost)

				#Segmento
				print("Segmento")
				print(octetodoble+redaux)
				
				#Broadcast
				if Numhost==0:
					printf("Error")
					pass
				elif Numhost ==1:
					broad=="1"
					print("Broadcast")
					print(ipaddress.IPv4Address(e1.get())+int(broad,2)+int(Nored,2))	

					#Rango útil
					print("Rango")
					print(ipaddress.IPv4Address(e1.get())+1+int(Nored,2))
					print(ipaddress.IPv4Address(e1.get())+int(broad,2)-1+int(Nored,2))

				else:
					for k in range(0,Numhost):
							broad=broad+"1"
					#print(int(broad,2))
					print("Broadcast")
					print(ipaddress.IPv4Address(e1.get())+int(broad,2)+int(Nored,2))	

					#Rango útil
					print("Rango")
					print(ipaddress.IPv4Address(e1.get())+1+int(Nored,2))
					print(ipaddress.IPv4Address(e1.get())+int(broad,2)-1+int(Nored,2))


			elif len(str(bin(int(e2.get())+int(e3.get())))) < 16:
				#print("valido")

				#Obtiene la direccion dada
				prueba3 = str((ipaddress.IPv4Address(e1.get()))).split(".")
				#Declaro variables auxiliares
				prueba4 = []
				#Saber cuantos bits necesita
				numBits = 16 - Numred
				#Variable auxiliar para el ultimo octeto
				#prueba3 = str(bin(numBits))
				bitsSobrantes=16-(Numred+Numhost)
				Compartidos=int(bitsSobrantes/2)

				#Guardo la dir en una variable auxiliar
				for i in prueba3:
					#print(i)
					prueba4.append(bin(int(i)))

				#Para poder sumar la cadena del número de red
				#Empuja la cadena
				for j in range(0,numBits-Compartidos):
					Nored =Nored+"0"
				#print(Nored)

				#######
				##Aqui hago las transformaciones para devolverlo como una dirección
				###
				octeto = ipaddress.IPv4Address(e1.get())+int(Nored,2)
				print("Red")
				print(int(e4.get()))


				##########
				#print(int(prueba2[3],2)+Numhost)

				#Segmento
				print("Segmento")
				print(octeto)
				
				#Broadcast
				broad=""
				if Numhost==0:
					printf("Error")
					pass
				elif Numhost ==1:
					broad=="1"
					print("Broadcast")
					print(ipaddress.IPv4Address(e1.get())+int(broad,2)+int(Nored,2))	

					#Rango útil
					print("Rango")
					print(ipaddress.IPv4Address(e1.get())+1+int(Nored,2))
					print(ipaddress.IPv4Address(e1.get())+int(broad,2)-1+int(Nored,2))

				else:
					#broad=""
					for k in range(0,Numhost):
						broad=broad+"1"
					#print(int(broad,2))
					print("Broadcast")
					print(ipaddress.IPv4Address(e1.get())+int(broad,2)+int(Nored,2))	

					#Rango útil
					print("Rango")
					print(ipaddress.IPv4Address(e1.get())+1+int(Nored,2))
					print(ipaddress.IPv4Address(e1.get())+int(broad,2)-1+int(Nored,2))

##########################################################################################################################################################
		
		elif ipaddress.IPv4Address(e1.get()) >= ipaddress.IPv4Address('192.0.0.0') and ipaddress.IPv4Address(e1.get()) <= ipaddress.IPv4Address('223.255.255.255'):
			print('clase C')
			#Verifica cuantos bits caben en el octeto
			if len(str(bin(((int(e2.get())+int(e3.get())))))) == 8:
				#print("valido")
				#Obtiene la direccion dada
				prueba = str((ipaddress.IPv4Address(e1.get()))).split(".")
				#Declaro variables auxiliares
				prueba2 = []
				#Saber cuantos bits necesita
				#A 8 bits resto los necesarios para la red
				numBits = 8 - Numred
				#Variable auxiliar para el ultimo octeto
				#prueba3 = str(bin(numBits))

				#Guardo la dir en una variable auxiliar
				for i in prueba:
					#print(i)
					prueba2.append(bin(int(i)))

				#Para poder sumar la cadena
				#Así se ve el número de cada red
				for j in range(0,numBits):
					Nored =Nored+"0"
				#print(Nored)

				#######
				##Aqui hago las transformaciones para devolverlo como una dirección
				###

				#El resultado de redes del octeto
				#octeto1 = int(prueba2[3],2)+int(Nored,2)
				#Octeto es el ultimoi el que 
				octeto = ipaddress.IPv4Address(e1.get())+int(Nored,2)
				print("Red")
				print(int(e4.get()))


				##########
				#print(int(prueba2[3],2)+Numhost)

				#Segmento
				print("Segmento")
				print(octeto)
				
				#Broadcast
				if Numhost==0:
					printf("Error")
					pass
				elif Numhost ==1:
					broad=="1"
					print("Broadcast")
					print(ipaddress.IPv4Address(e1.get())+int(broad,2)+int(Nored,2))	

					#Rango útil
					print("Rango")
					print(ipaddress.IPv4Address(e1.get())+1+int(Nored,2))
					print(ipaddress.IPv4Address(e1.get())+int(broad,2)-1+int(Nored,2))

				else:
					broad=""
					for k in range(0,Numhost):
						broad=broad+"1"
					#print(int(broad,2))
					print("Broadcast")
					print(ipaddress.IPv4Address(e1.get())+int(broad,2)+int(Nored,2))	

					#Rango útil
					print("Rango")
					print(ipaddress.IPv4Address(e1.get())+1+int(Nored,2))
					print(ipaddress.IPv4Address(e1.get())+int(broad,2)-1+int(Nored,2))


			elif len(str(bin(int(e2.get())+int(e3.get())))) < 8:
				#print("valido")

				#Obtiene la direccion dada
				prueba3 = str((ipaddress.IPv4Address(e1.get()))).split(".")
				#Declaro variables auxiliares
				prueba4 = []
				#Saber cuantos bits necesita
				numBits = 8 - Numred
				#Variable auxiliar para el ultimo octeto
				#prueba3 = str(bin(numBits))
				bitsSobrantes=8-(Numred+Numhost)
				Compartidos=int(bitsSobrantes/2)

				#Guardo la dir en una variable auxiliar
				for i in prueba3:
					#print(i)
					prueba4.append(bin(int(i)))

				#Para poder sumar la cadena del número de red
				#Empuja la cadena
				for j in range(0,numBits-Compartidos):
					Nored =Nored+"0"
				#print(Nored)

				#######
				##Aqui hago las transformaciones para devolverlo como una dirección
				###
				octeto = ipaddress.IPv4Address(e1.get())+int(Nored,2)
				print("Red")
				print(int(e4.get()))


				##########
				#print(int(prueba2[3],2)+Numhost)

				#Segmento
				print("Segmento")
				print(octeto)
				
				#Broadcast
				broad=""
				if Numhost==0:
					printf("Error")
					pass
				elif Numhost ==1:
					broad=="1"
					print("Broadcast")
					print(ipaddress.IPv4Address(e1.get())+int(broad,2)+int(Nored,2))	

					#Rango útil
					print("Rango")
					print(ipaddress.IPv4Address(e1.get())+1+int(Nored,2))
					print(ipaddress.IPv4Address(e1.get())+int(broad,2)-1+int(Nored,2))

				else:
					broad=""
					for k in range(0,Numhost):
						broad=broad+"1"
					#print(int(broad,2))
					print("Broadcast")
					print(ipaddress.IPv4Address(e1.get())+int(broad,2)+int(Nored,2))	

					#Rango útil
					print("Rango")
					print(ipaddress.IPv4Address(e1.get())+1+int(Nored,2))
					print(ipaddress.IPv4Address(e1.get())+int(broad,2)-1+int(Nored,2))


			else:
				print("La red usada no puede soportar es cantidad de hosts y redes que se solicitan")

		else:
			print('No se puede trabajar con esa red')

		print("###############################################################################################################################################")

except AddressValueError:
	pass

#Posiciono mi boton
b=Button(v,text="Calcula",command=promCallback)
b.place(x=200, y=610)

label=Label(v)
label.pack()
#Tamaño de la ventana
v.geometry("1200x1000+10+10")
#La ventana principal esta en un loop infinito porque no queremos que se cierre
v.mainloop()