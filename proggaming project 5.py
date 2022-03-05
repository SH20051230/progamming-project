Total_fine = 0
number = int(input("press 0 to stop recording, press anything else to start: "))
name = (input("what's the speeder's name: "))
while number != 0:
    Total_fine + 1
    over_limit = int(input("What's the speeder's over limit value: "))
    for over_limit in range(0, 11):
        Fine_1 = 30
        print(f"{Fine_1}")
    for over_limit in range(10, 15):
        Fine_2 = 80
        print(f"{Fine_2}")
    for over_limit in range(15, 20):
        Fine_3 = 120
        print(f"{Fine_3}")
    for over_limit in range(20, 25):
        Fine_4 = 170
        print(f"{Fine_4}")
    for over_limit in range(25, 30):
        Fine_5 = 230
        print(f"{Fine_5}")
    for over_limit in range(30, 35):
        Fine_6 = 300
        print(f"{Fine_6}")
    for over_limit in range(35, 40):
        Fine_7 = 400
        print(f"{Fine_7}")
    for over_limit in range(40, 45):
        Fine_8 = 510
        print(f"{Fine_8}")
    else:
        Fine = 630
        print(f"{Fine}")



print(f"Total Fines for today is {Total_fine}")
print(f"The amount of Fines for today is {Fine_cost}")



