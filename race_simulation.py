import random

car_1 = "Max"
car_2 = "Jack"
car_3 = "Pio"


laps = int(input("Enter number of laps: "))  #vueltas=laps(in)

# Se decide al azar cuándo falla el coche 3. Cada vez que se ejecute fallara en una vuelta aleatoria

fail_lap = random.randint(1, laps)   #fail_lap= vuelta_fallo

total_1 = 0
total_2 = 0
total_3 = 0

print("\n ¡PYTHON GRAND PRIX STARTS NOW! \n")

for i in range(3, 0, -1):
    print(i)
else:
    print("🏁 🚦 ¡The race has started!\n")

for i in range(1, laps + 1):

    distance_1 = i * 3
    distance_2 = i * 4

    if i < fail_lap:
        distance_3 = i * 2
    else:
        distance_3 = 0
        if i == fail_lap:
            print(f"\n {car_3} has an engine failure on lap {i}")       #fallo de motor
 
    total_1 += distance_1
    total_2 += distance_2
    total_3 += distance_3

    print(f"\n Lap {i}")
    print(f"🚗 {car_1} advances {distance_1} m")
    print(f"🚙 {car_2} advances {distance_2} m")
    print(f"🚕 {car_3} advances {distance_3} m")


print("\n🏁 Finished")

print(f"{car_1} total distance: {total_1} m")
print(f"{car_2} total distance: {total_2} m")
print(f"{car_3} total distance: {total_3} m")

if total_3 == 0:
    print(f"\n {car_3}  is disqualified due to an engine failure on lap {fail_lap}")

if total_1 > total_2:
    print(f"\n winner: {car_1}")
elif total_2 > total_1:
    print(f"\n winner: {car_2}")
else:
    print("\n ¡Draw!")    #empate