print("""=================
Conversor de peso
=================""")
instrucciones = ("""Por favor introduca el peso en
kilogramos y con un solo decimal""")
print(instrucciones)

peso = float(input("""Introduzaca su peso para saber cuanto 
pesa en los planetas del sistema solar: """))
#Peso en la Luna 
print("su peso en la Luna es :",peso / 6.053, "kg")
if peso<=100:
    print("Yo creo que deberiamos irnos a la Luna a vivir")

#Peso en Venus
print("Su peso en Venus es : ", peso / 1.105, "kg")

#Peso en Mercurio
print("Supeso en Mercurio es : ", peso / 2.65,"kg")

#Peso en Marte
print("Su peso en Marte es : ", peso / 2.643, "kg")

#Peso en Jupiter
print("Su peso en Jupiter es : ",peso / 0.395, "kg")
if peso/0.395 > 300 :
    print("Mejor no vamos a Jupiter")
else : 
    print("Mejor nos quedamos en la Tierra")

#Peso en Saturno
print("Su peso en Saturno es : ", peso / 0.939, "kg")

#Peso en Urano
print("Su peso en Urano es : ", peso / 1.105, "kg")

#Peso en Neptuno
print("Su peso en Neptuno es ", peso / 0.87, "kg")
 
