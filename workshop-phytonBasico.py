import random
# JUEGO DE PIEDRA, PAPEL O TIJERA 

comenzandoJuego = ["piedra", "papel", "tijera"]

while True: 
    humano = input ("Escoge: piedra, papel o tijera -----> : ")
    if humano not in comenzandoJuego:
        print("Opcion no valida , escoge piedra, papel o tijera !!")
        continue
    opcionMaquina = random.choice(comenzandoJuego)
    print(f"\n La Maquina ha escogido -----> {opcionMaquina}  ")

    if humano == opcionMaquina:
        print(f"Juego Empatado , ambos escogieron {humano}!!")
    elif humano == "piedra" and opcionMaquina =="tijera":
        print(f"Ganaste !!! , {humano} ganas en contra de {opcionMaquina} ")
    elif humano == "tijera" and opcionMaquina =="papel":
        print(f"Ganaste !!! , {humano} ganas en contra de {opcionMaquina} ")
    elif humano == "papel" and opcionMaquina =="piedra":
        print(f"Ganaste !!! , {humano} ganas en contra de {opcionMaquina} ")
    else:
        print(f"Perdiste !!! , {humano} pierde contra {opcionMaquina} ")
    print(f" Fin del Juego !!! ")