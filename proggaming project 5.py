def main():
    key = "X"
    name = (input("what's the speeder's name: ")).title()
    total_fine = 0
    speeder_list = []
    if name == "X":
        end_input() == (total_fine, speeder_list)
    else:
        warrants(name)
        amount_over = int(input("Enter the amount over limit: "))
        fine = int(fine_calc(amount_over))
        total_fine += fine
        if fine > 0:
           speeder_list.append([name, amount_over])

        print(f"{name} is be fined with {fine}")

def end_input(total_fines, speeder_list):
    print(f"total fines is {len(speeder_list)}")
    for fine in speeder_list:
        print(f"{speeder_list.index(fine) + 1}")
        f"{fine[0]}\tamount over limite: {fine[1]}"
    print(f"total fine value is {total_fines}")



def fine_calc(amount_over):
    if  amount_over < 10:
        fine = 30
    elif amount_over < 15:
        fine = 80
    elif amount_over < 20:
        fine = 120
    elif amount_over < 25:
        fine = 170
    elif amount_over < 30:
        fine = 230
    elif amount_over < 35:
        fine = 300
    elif amount_over < 40:
        fine = 400
    elif amount_over < 45:
        fine = 510
    else:
        fine = 630
    return fine

def warrants(name):
    warrant_list = ["James_Wilson", "Helga_Norman", "Zachary Conroy"]
    if name in warrant_list:
        print(f"{name} warrant to arrest".upper())


print("Speeding tracer, Ebter X to exit input mode and produce a summary")
main()



