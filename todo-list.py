import random
import os
import json
from datetime import datetime

# --- CONFIGURATION AND FILE PATHS ---
# Define the file where data will be saved (Data Persistence)
DATA_FILE = 'productivity_suite_data.json'

def load_data():
    """Loads application data (budget, notes) from the JSON file."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
                print(f"✅ Data loaded successfully from {DATA_FILE}")
                return data
        except json.JSONDecodeError as e:
            # Error Handling Mastery: Handle corrupted JSON files
            print(f"❌ Error decoding JSON data: {e}. Starting with fresh data.")
            return {"income": {}, "expenses": {}, "notes": []}
        except Exception as e:
            print(f"❌ An unexpected error occurred while loading data: {e}. Starting with fresh data.")
            return {"income": {}, "expenses": {}, "notes": []}
    else:
        print("💾 Data file not found. Starting new session.")
        return {"income": {}, "expenses": {}, "notes": []}

def save_data(data):
    """Saves application data (budget, notes) to the JSON file."""
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
        print("✅ Data saved successfully.")
    except IOError as e:
        # Error Handling Mastery: Handle file writing issues
        print(f"❌ Could not save data due to file error: {e}")

# --- 1. NUMBER GUESSING GAME (Adapted for class structure and error handling) ---

class GuessingGame:
    """Implements the Number Guessing Game concept."""
    def __init__(self):
        self.number = random.randint(1, 100)
        self.life = 7
        self.max_life = 7 # Store the maximum for the display

    def run(self):
        """Runs the game loop."""
        # print(f"[DEBUG] The secret number is {self.number}") # Remove in production
        print("\n\n--- 🔢 Number Guessing Game ---")
        print("I'm thinking of a number between 1 and 100. You have 7 lives.")
        
        while self.life > 0:
            try:
                # Advanced Python Syntax: f-string for clear display
                guess = int(input(f"Attempt {self.max_life - self.life + 1} (Lives left: {self.life}) - Enter your number: "))
                
                if not (1 <= guess <= 100):
                    print("Input out of range! Please enter a number between 1 and 100❌")
                    continue
                    
                self.life -= 1

                if guess == self.number:
                    print(f"\n🏆🏆🏆 CONGRATULATIONS! You guessed the number {self.number} in {self.max_life - self.life} attempts!")
                    break 
                elif guess > self.number:
                    print("Too high📈")
                elif guess < self.number:
                    print("Too low📉")    

            except ValueError:
                # Error Handling Mastery: Catching non-integer input
                print("❌ Invalid input! Please enter a valid integer.")
                
        if self.life == 0 and guess != self.number:
            print(f"\n☹️ You lose! The number was {self.number}")
            
# --- 2. BUDGET TRACKER (Your Class, enhanced for persistence) ---

class BudgetTracker:
    """Manages income and expenses with data persistence."""
    def __init__(self, data):
        # Data Structures: Using dictionaries for key-value mapping (source/category to amount)
        self.income = data.get("income", {})
        self.expenses = data.get("expenses", {})

    def add_income(self, source, amount):
        """Adds income to the tracker."""
        source = source.strip().capitalize()
        self.income[source] = self.income.get(source, 0) + amount
        print(f"💵 Added Income: {source}: ${amount:,.2f}")

    def add_expense(self, category, amount):
        """Adds expense to the tracker."""
        category = category.strip().capitalize()
        self.expenses[category] = self.expenses.get(category, 0) + amount
        print(f"📶 Added Expense: {category}: ${amount:,.2f}")
    
    def calculate_summary(self):
        """Calculates total income, expenses, and net savings."""
        total_income = sum(self.income.values())
        total_expenses = sum(self.expenses.values())
        net_savings = total_income - total_expenses
        return total_income, total_expenses, net_savings

    def view_summary(self):
        """Displays a detailed summary of the budget."""
        total_income, total_expenses, net_savings = self.calculate_summary()
        
        print("\n\n--- 📊 Budget Summary ---")
        print("\n** INCOME SOURCES **")
        if self.income:
            for source, amount in self.income.items():
                print(f"  - {source}: ${amount:,.2f}")
        else:
            print("  (No income recorded)")

        print("\n** EXPENSE CATEGORIES **")
        if self.expenses:
            for category, amount in self.expenses.items():
                print(f"  - {category}: ${amount:,.2f}")
        else:
            print("  (No expenses recorded)")
        
        print("\n------------------------------")
        print(f"💰 TOTAL INCOME: ${total_income:,.2f}")
        print(f"🔻 TOTAL EXPENSES: ${total_expenses:,.2f}")
        print(f"⭐ NET SAVINGS: ${net_savings:,.2f}")
        if net_savings >= 0:
            print("You are on track! Keep saving.")
        else:
            print("Careful! You are over budget.")
        print("------------------------------")
    
    def get_data(self):
        """Returns the current state for saving."""
        return {"income": self.income, "expenses": self.expenses}

# --- 3. NOTE-TAKING TOOL (File Handling Practice) ---

class NoteTaker:
    """Simple tool for managing and viewing notes."""
    def __init__(self, data):
        # Data Structures: Using a list of dictionaries for multiple notes
        self.notes = data.get("notes", [])

    def add_note(self, content):
        """Adds a new note with a timestamp."""
        # Advanced Python Syntax: Dictionary creation and list append
        new_note = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "content": content
        }
        self.notes.append(new_note)
        print("📝 Note saved successfully!")

    def view_notes(self):
        """Displays all recorded notes."""
        print("\n\n--- 🗒️ Your Notes ---")
        if not self.notes:
            print("(No notes found. Add one from the main menu.)")
            return

        # Advanced Python Syntax: enumerate for index and item access
        for i, note in enumerate(self.notes):
            print(f"[{i+1}] {note['timestamp']}:")
            print(f"    {note['content']}")
            print("-" * 20)
    
    def get_data(self):
        """Returns the current state for saving."""
        return {"notes": self.notes}

# --- 4. MAIN APPLICATION AND MENU SYSTEM (Code Organization) ---

class ProductivitySuite:
    """The main application manager."""
    def __init__(self):
        self.data = load_data()
        self.budget_tracker = BudgetTracker(self.data)
        self.note_taker = NoteTaker(self.data)
        self.running = True

    def display_main_menu(self):
        """Displays the main menu options."""
        print("\n" + "="*50)
        print("🚀 Personal Productivity Suite v1.0")
        print("="*50)
        print("1. 🔢 Play Number Guessing Game")
        print("2. 📊 Budget Tracker Menu")
        print("3. 🗒️ Note Taking Tool")
        print("4. 💾 Save Data & Exit")
        print("-" * 50)

    def run_budget_menu(self):
        """Menu for the Budget Tracker."""
        while True:
            print("\n--- Budget Tracker Menu ---")
            print("A. Add Income")
            print("B. Add Expense")
            print("C. View Summary")
            print("D. Back to Main Menu")
            choice = input("Enter your choice (A/B/C/D): ").upper()
            
            if choice == 'A' or choice == 'B':
                try:
                    source_category = input(f"Enter {'Source' if choice == 'A' else 'Category'}: ")
                    amount = float(input("Enter Amount: $"))
                    if amount <= 0:
                        print("Amount must be positive.")
                        continue
                    
                    if choice == 'A':
                        self.budget_tracker.add_income(source_category, amount)
                    else:
                        self.budget_tracker.add_expense(source_category, amount)
                except ValueError:
                    print("❌ Invalid amount. Please enter a valid number.")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
            elif choice == 'C':
                self.budget_tracker.view_summary()
            elif choice == 'D':
                break
            else:
                print("Invalid option. Please try again.")

    def run_note_menu(self):
        """Menu for the Note Taker."""
        while True:
            print("\n--- Note Taking Tool Menu ---")
            print("A. Add New Note")
            print("B. View All Notes")
            print("C. Back to Main Menu")
            choice = input("Enter your choice (A/B/C): ").upper()

            if choice == 'A':
                content = input("Enter your note content: ")
                if content.strip():
                    self.note_taker.add_note(content)
                else:
                    print("Note cannot be empty.")
            elif choice == 'B':
                self.note_taker.view_notes()
            elif choice == 'C':
                break
            else:
                print("Invalid option. Please try again.")

    def run(self):
        """The main application loop."""
        while self.running:
            self.display_main_menu()
            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                # Re-initialize the game to get a new random number
                game = GuessingGame() 
                game.run()
            elif choice == '2':
                self.run_budget_menu()
            elif choice == '3':
                self.run_note_menu()
            elif choice == '4':
                # Combine data from all modules before saving
                all_data = {
                    **self.budget_tracker.get_data(),
                    **self.note_taker.get_data()
                }
                save_data(all_data)
                self.running = False
                print("\n👋 Thank you for using the Productivity Suite. Goodbye!")
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

# --- APPLICATION START ---

if __name__ == "__main__":
    # Development Tools and Environment Setup: Standard entry point
    app = ProductivitySuite()
    app.run()