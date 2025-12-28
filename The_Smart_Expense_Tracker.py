'''
Task: Allow the user to input an expense category (Food, Fees, Fun) and the amount.
Store these in a dictionary.
At the end, calculate the total and show which category you spent the most on.
'''
print("\t\tWelcome\t\t")
print("Here you can calculate your daily expenses\t\t")
expenses = {}

while True :
    print("1. Add Expenses")
    print("2. View Summary")
    print("3. Exit")

    choice = input("Select an option (1-3): ") 
    if choice == '1':
        category = input("Enter categroy : ").capitalize()
        amount_input = input(f"ENter the amount of {category} : ")

        if amount_input.isdigit():
            amount = float(amount_input)

            if category in expenses : 
                expenses[category] = expenses[category] + amount 
            else :
                expenses[category] = amount
            print("Done ! Added to your list.")
        else :
            print("Error : Please enter numbers only for the amount.")

    elif choice == '2':
        print("\t\tYour Expenses\t\t")
        if not expenses:
            print("List is empty")
        else :
            total = 0 
            for i in expenses :
                print(f"{i} : {expenses[i]}")
                total  = total  + expenses[i]
            print(f"Total spent : {total}")
    
    elif choice == '3':
        print("Exiting ....focus on your studies ")
        break
    else : print("Invalid option , try again")

