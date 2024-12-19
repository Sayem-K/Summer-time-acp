weather = int(input("What is the weather today in Celsius? "))
if weather <= 0:
    print("Wear a lot of layers, it's too cold of a tempurature!!!")
elif weather >= 1 and weather <= 15:
    print("It is normal tempurature. Wear 1-2 layers.")
elif weather >= 16 and weather <= 25:
    print("It is a bit hot, but wear one layer.")
elif weather >= 26: 
    print("It's very hot!!!! Wear a single, thin layer.")