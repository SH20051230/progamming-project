def drop_Off():
    name = str(input("what's your children's name?: "))
    roll_list.append(name)
    print(f"{name} has been confirm added to roll list")


def pick_up():
    Check_out_name = str(input("what's your children's name?: "))
    if Check_out_name in roll_list:
        roll_list.remove(Check_out_name)
        print(f"{Check_out_name} has been check out!: ")
    else:
        print("please enter a valid name")
        input("what's your children's name")


def calc_cost():
    hours_fee = 12
    Hours = int(input("how many hours have you charged?: "))
    Child_number = int(input("how many children have you checked out?: "))
    Fee = {Hours * Child_number * hours_fee}
    print("your final fee is", Fee)


def print_Roll():
    print(roll_list, "is in the current roll list")


# Main Routine
roll_list = []
choice = 0
while choice != 5:
    print("__________________________________________")
    print("welcome to MGS Child care")
    print("what would you like to do? Please choose one of them below")
    print("__________________________________________")
    print("1 drop off a child")
    print("2 pick up a child")
    print("3 load the cost")
    print("4 print roll")
    print("5 Exit the system")
    choice = int(input("What choice: "))
    if choice == 1:
        drop_Off()
    elif choice == 2:
        pick_up()
    elif choice == 3:
        calc_cost()
    elif choice == 4:
        print_Roll()
    else:
        print("Goodbye")
