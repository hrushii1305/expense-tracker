from tracker import ExpenseTracker

obj=ExpenseTracker()

while True:
    print("\n1. add expense")
    print("2. show total")
    print("3. show category-wise")
    print("4. show all expenses")
    print("5. exit")
    choice= input("enter choice: ")
    
    if choice=="1":
        obj.add_expense()
    elif choice=="2":
        obj.show_total()
    elif choice=="3":
        obj.show_category()
    elif choice=="4":
        obj.show_all()
    elif choice=="5":
        print("exiting...")
        break
    else:
        print("invalid choice")