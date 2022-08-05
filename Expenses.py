from operator import truediv
from secrets import choice


expenses_list = []

def show_expenses(month):
    for expense_amount,expense_type,expense_month in expenses_list:
        if expense_month == month:
            print(f"{expense_amount} - {expense_type}")

    

def add_expense(month):
    print()
    expense_amount = int(input("Specify amount:"))
    expense_type = input("Specify type of expense:")

    expense = (expense_amount,expense_type,month)
    expenses_list.append(expense)

def show_stats(month):
    total_amount_month_expesnes = sum(expense_amount for expense_amount,_,expense_month in expenses_list if expense_month == month)
    number_expenses_month_expesnes = sum(1 for _,_,expense_month in expenses_list if expense_month == month)
    total_amount_all = sum(expense_amount for expense_amount,_,_ in expenses_list)
    average_expenses_tihs_month = total_amount_month_expesnes / number_expenses_month_expesnes
    average_expenses_all = total_amount_all / len(expenses_list)

    print()
    print("Statistics")
    print("Total amount in this month:", total_amount_month_expesnes)
    print("All expense:", total_amount_all)
    print("Average expenses this month:", average_expenses_tihs_month)
    print("Average expenses:", average_expenses_all)

while True:
    print()
    month = int(input("Select the month from 1-12:"))

    if month <= 0:
        break


    while True:
        print()
        print("0.Back to select the month")
        print("1.Show all expenses")
        print("2.Add new expenses")
        print("3.Statistics")
        choice= int(input("Select option: "))

        if choice == 0:
            break
        
        if choice == 1:
            show_expenses(month)
            print("All expenses")

        if choice == 2:
            add_expense(month)
            print("Add new expense")
        
        if choice == 3:
            show_stats(month)