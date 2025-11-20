# import random
# number = random.randint(1,100)
#   # For testing purposes, remove or comment this line in production
# life = 7
# max_life = 0
# print("🔢🔢enter your number between 1 to 100 🔢🔢")
# while life > 0:
#     try:
#         guees = int(input(f"Attempt {life+1} enter the number:"))
#         life -= 1

#         if guees == number:
#             print("🏆You win!!!")   
#             break 
#         elif guees > number:
#             print("Too high📈")
#         elif guees < number:
#             print("Too low📉")    

#     except ValueError:
#         print("Invalid input! Please enter a valid integer❌")

# if life ==  0 and guees != number:
#     print(f"☹️\tYou lose!!! The number was {number}")           

print("Budget Tracker")
class BudgetTracker:
    def __init__(self):
        self.income = {}
        self.expenses = {}

    def add_income(self, source,amount):    
        if source in self.income:
            self.income[source] += amount
        else:
            self.income[source] = amount

        print(f"💵💵 added: {self.income} source:{source} amount:{amount}")

    def add_expense(self,category,eamount):
        if category in self.expenses:
            self.expenses[category] += eamount
        else:
            self.expenses[category] = eamount

        print(f"📶📶expenses added: {self.expenses} category:{category} amount:{eamount}")
        

       



tracker = BudgetTracker()
tracker.add_income("Salary",5000)
tracker.add_expense("Rent",1500)
# Access by source/category name (keys are the source/category strings)
print("Income Salary:", tracker.income.get("Salary"))
print("Expense Rent:", tracker.expenses.get("Rent"))
# total_savings = tracker.total_income["amount"] - tracker.total_expenses["amount"]
# print("Total savings:",total_savings)
# # tracker.view_summary()
