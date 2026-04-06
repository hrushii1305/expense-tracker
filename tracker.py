class ExpenseTracker:
    
    def __init__(self):
        self.expenses=[]
        self.total=0
        self.category_map={}
        
    def add_expense(self):
        amount=float(input("Enter the amount: "))
        category=input("Enter the category: ")
        self.expenses.append({"amount": amount, "category": category})
        self.total += amount
        if category in self.category_map:
            self.category_map[category] += amount
        else:
            self.category_map[category] = amount
        
        with open("expenses.txt", "a") as file:
            file.write(f"{amount},{category}\n")
        print("Expense added successfully.")
        
    def show_total(self):
        print("Total expenses: ", self.total)
        
    def show_category(self):
        print("Category-wise expenses: ")
        for cat in self.category_map:
            print(cat, ": ", self.category_map[cat])
            
    def show_all(self):
        print("All expenses: ")
        for expense in self.expenses:
            print(expense["amount"], " - ", expense["category"])
            