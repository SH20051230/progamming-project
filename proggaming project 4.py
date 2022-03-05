def staff_absent_tracker():
    employee_name = ""
    absense_name = []
    while employee_name != "$":
        employee_name = input("what's your name: ")
        if len(absense_name) > 0:
            if employee_name == "$":

             summary(absense_name)


        absent_days = int(input("how many days have you absent: "))
        absense_name.append([employee_name, absent_days])


def summary(absense_name):
    total_days_absent = 0
    total_numbers_absent = len(absense_name)
    most_absent = [["", 0]]
    no_absent = []
    for employee_name in absense_name:
        if employee_name[1] > most_absent[0][1]:
            most_absent = employee_name
        elif employee_name[1] == most_absent[0][1]:
            most_absent.append(employee_name)
        elif employee_name[1] == 0:
            no_absent.append(employee_name)
        total_days_absent += int(employee_name[1])
        average(total_days_absent, total_numbers_absent, absense_name)
        calc_most_absent(most_absent)
        if len(no_absent) > 0:
            print("The employees who were not absent at all: ")
            sort_no_absent = sorted(no_absent)
            for employee_name in sort_no_absent:
                print(f"\t {employee_name[0]}")
        else:
            print("There are no employee who did not absent at all")


def average(total_days_absent, total_numbers_absent, absense_name):
    average_numbers = round(total_days_absent / total_numbers_absent, 2)
    print(f"The average number of absent days this year was{average_numbers}")
    for employee_name in absense_name:
        if employee_name[1] > average_numbers:
            print(f"{employee_name[0]} has been absent {employee_name[1]} days")

def calc_most_absent(most_absent):
    if len(most_absent) == 1:
        print(f"The person who has most absent days was{most_absent[0][0]} with absent days of {most_absent[0][1]}")
    else:
        for employee_name in most_absent:
            print(f"\t{employee_name[0]} with {employee_name[1]} days")

#Main
staff_absent_tracker()
