Total_time = 0
Total_cost = 0
Total_trip = 0
name = input("what's your name: ")
answer = input("Do you want to start a trip?: ")
while answer != "no":
    Total_trip += 1
    Time = int(input("how many minutes did the trip took: "))
    Total_time += Time
    BASE_COST = 10
    min_fee = 2 * Time
    cost = BASE_COST + min_fee
    Total_cost += cost
    print(f"The Final fee of the trip is: {cost} $ ")
    print(f"The time of the trip is {Time} minutes")
    answer = input("Do you want to start a trip?: ")

Average_time = Total_time / Time
Average_cost = Total_cost / cost
print(f"for driver {name} your total time is {Total_time} minutes")
print(f"your total income is {Total_cost} $ ")
print(f"your average time is {Average_time} minutes and your average income is {Average_cost} $ ")




