def main():
    incomes = []
    Month_number = int(input("How many months? "))

    for month in range(1, Month_number + 1):
        income = float(input("Enter income for month {}: ".format(month)))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, Month_number + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()


def improved():

    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(
            input("Enter income for month {}: ".format(month)))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes):
        total += income
        print("Month {:2} - Income: ${:10.2f} \
        Total: ${:10.2f}".format(month + 1, income, total))


improved()





