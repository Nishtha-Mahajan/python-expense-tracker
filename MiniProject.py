expensesList=[]
print("Welcome to The Expenses Trackers..")

while True:
    print("*======MENU======*")
    print("1. Add Expenses :")
    print("2. Viwe All Expenses :")
    print("3. Viwe Total Expenses :")
    print("4. Exit")

    chooice =int(input("Enter the ypur choices ✍️ :"))

# Add Expenses :

    if(chooice==1):
        date=input("Enter the date of expense: ")
        category=input("Enter the expense category (Food, Travel, Makeup, Books): ")
        description=input("Enter expense description: ")
        amount=float(input("Enter the amount :"))

        expenses={
                 "date" : date,
                 "category" : category,
                 "description" : description,
                 "amount" : amount
                 }
        
        expensesList.append(expenses)
        print("Your Expenses Added Succesfully....✅")
        
# Viwe ALL Expenses..

    elif(chooice==2):
        if(len(expensesList)==0):
           print("No expenses added yet 😑 Please add some expenses first 😌")

        else:
           print("Here are all your expenses 👇")
           count=1

           for eachKharcha in expensesList:
               print(f"Kharcha No {count} ->,Date is :{eachKharcha["date"]},Category is :{eachKharcha["category"]},Description is :{eachKharcha["description"]},amount is :{eachKharcha["amount"]}")   
               count=count+1          
     
# Viwe All Total..

    elif(chooice==3):
        total=0
        for eachKharcha in expensesList:
            total= total+ eachKharcha["amount"]

        print("\n your total amount is 💵 :",total)

# Exit

    elif(chooice==4):
        print("Thank you... 🙏 for using our system... 😊")

    else:
        print("INVALID CHOICE..❌  PLEASE TRY AGAIN..🙂")                     