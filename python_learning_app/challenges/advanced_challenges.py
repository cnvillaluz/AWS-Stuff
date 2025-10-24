import sys
from io import StringIO

class AdvancedChallenges:
    def __init__(self, game_engine):
        self.game_engine = game_engine
        self.stage = 'advanced'

    def run_code(self, code):
        """Safely execute user code and capture output"""
        old_stdout = sys.stdout
        redirected_output = StringIO()
        sys.stdout = redirected_output

        try:
            exec_globals = {}
            exec(code, exec_globals)
            sys.stdout = old_stdout
            return redirected_output.getvalue(), exec_globals, None
        except Exception as e:
            sys.stdout = old_stdout
            return None, None, str(e)

    def challenge_1_bank_account(self):
        """Challenge: Create a BankAccount class"""
        print("\n" + "="*60)
        print("CHALLENGE 1: Bank Account Class")
        print("="*60)
        print("\nTask: Create a class 'BankAccount' with:")
        print("  - __init__(self, owner, balance=0)")
        print("  - deposit(self, amount) - adds to balance")
        print("  - withdraw(self, amount) - subtracts from balance")
        print("    (only if sufficient funds, otherwise print error)")
        print("  - get_balance(self) - returns current balance")
        print("\nTest it:")
        print("  acc = BankAccount('Alice', 100)")
        print("  acc.deposit(50)")
        print("  acc.withdraw(30)")
        print("  Print the balance (should be 120)")
        print("\nEnter your code (type 'RUN' on a new line when done):")

        lines = []
        while True:
            line = input()
            if line == "RUN":
                break
            lines.append(line)

        code = "\n".join(lines)
        output, exec_globals, error = self.run_code(code)

        if error:
            print(f"\nError: {error}")
            print("You earned 15 points for trying.")
            self.game_engine.add_points(15, self.stage)
            return False

        if 'BankAccount' not in exec_globals:
            print("\nClass 'BankAccount' not found.")
            print("You earned 15 points for trying.")
            self.game_engine.add_points(15, self.stage)
            return False

        try:
            BankAccount = exec_globals['BankAccount']
            acc = BankAccount('TestUser', 100)

            # Test deposit
            acc.deposit(50)
            # Test withdraw
            acc.withdraw(30)
            balance = acc.get_balance()

            if balance == 120:
                print("\nPerfect! Your BankAccount class works correctly!")
                print("You earned 70 points!")
                self.game_engine.add_points(70, self.stage)
                self.game_engine.mark_challenge_complete('advanced_challenge_1', self.stage)
                return True
            else:
                print(f"\nBalance is {balance}, expected 120.")
                print("You earned 30 points for trying.")
                self.game_engine.add_points(30, self.stage)
                return False
        except Exception as e:
            print(f"\nError testing your class: {e}")
            print("You earned 20 points for trying.")
            self.game_engine.add_points(20, self.stage)
            return False

    def challenge_2_inheritance_shapes(self):
        """Challenge: Inheritance with shapes"""
        print("\n" + "="*60)
        print("CHALLENGE 2: Shape Inheritance")
        print("="*60)
        print("\nTask: Create a class hierarchy:")
        print("\n1. Base class 'Shape' with method 'area(self)' that returns 0")
        print("\n2. Class 'Rectangle(Shape)' with:")
        print("     __init__(self, width, height)")
        print("     area(self) - returns width * height")
        print("\n3. Class 'Circle(Shape)' with:")
        print("     __init__(self, radius)")
        print("     area(self) - returns 3.14159 * radius * radius")
        print("\nTest: Create Rectangle(5, 3) and Circle(4)")
        print("Print both areas.")
        print("\nEnter your code (type 'RUN' on a new line when done):")

        lines = []
        while True:
            line = input()
            if line == "RUN":
                break
            lines.append(line)

        code = "\n".join(lines)
        output, exec_globals, error = self.run_code(code)

        if error:
            print(f"\nError: {error}")
            print("You earned 15 points for trying.")
            self.game_engine.add_points(15, self.stage)
            return False

        try:
            Shape = exec_globals.get('Shape')
            Rectangle = exec_globals.get('Rectangle')
            Circle = exec_globals.get('Circle')

            if not all([Shape, Rectangle, Circle]):
                print("\nMissing one or more classes.")
                print("You earned 20 points for trying.")
                self.game_engine.add_points(20, self.stage)
                return False

            rect = Rectangle(5, 3)
            circ = Circle(4)

            rect_area = rect.area()
            circ_area = circ.area()

            if abs(rect_area - 15) < 0.01 and abs(circ_area - 50.26544) < 0.01:
                print("\nExcellent! Your inheritance hierarchy works perfectly!")
                print("You earned 75 points!")
                self.game_engine.add_points(75, self.stage)
                self.game_engine.mark_challenge_complete('advanced_challenge_2', self.stage)
                return True
            else:
                print(f"\nAreas don't match expected values.")
                print(f"Rectangle area: {rect_area} (expected ~15)")
                print(f"Circle area: {circ_area} (expected ~50.27)")
                print("You earned 35 points for trying.")
                self.game_engine.add_points(35, self.stage)
                return False
        except Exception as e:
            print(f"\nError testing your classes: {e}")
            print("You earned 25 points for trying.")
            self.game_engine.add_points(25, self.stage)
            return False

    def challenge_3_decorator(self):
        """Challenge: Create a timing decorator"""
        print("\n" + "="*60)
        print("CHALLENGE 3: Timing Decorator")
        print("="*60)
        print("\nTask: Create a decorator 'timer' that:")
        print("  - Measures how long a function takes to execute")
        print("  - Prints 'Function executed'")
        print("\nNote: For this challenge, just make the decorator print")
        print("'Function executed' before and after calling the function.")
        print("\nApply it to a function 'slow_function()' that prints 'Working...'")
        print("\nEnter your code (type 'RUN' on a new line when done):")

        lines = []
        while True:
            line = input()
            if line == "RUN":
                break
            lines.append(line)

        code = "\n".join(lines)
        output, exec_globals, error = self.run_code(code)

        if error:
            print(f"\nError: {error}")
            print("You earned 15 points for trying.")
            self.game_engine.add_points(15, self.stage)
            return False

        # Check if output contains expected strings
        if output and 'Function executed' in output and 'Working' in output:
            print("\nGreat! Your decorator works!")
            print("You earned 80 points!")
            self.game_engine.add_points(80, self.stage)
            self.game_engine.mark_challenge_complete('advanced_challenge_3', self.stage)
            return True
        else:
            print("\nOutput doesn't match expected pattern.")
            print("You earned 30 points for trying.")
            self.game_engine.add_points(30, self.stage)
            return False

    def challenge_4_generator(self):
        """Challenge: Fibonacci generator"""
        print("\n" + "="*60)
        print("CHALLENGE 4: Fibonacci Generator")
        print("="*60)
        print("\nTask: Create a generator function 'fibonacci(n)' that:")
        print("  - Yields the first n Fibonacci numbers")
        print("  - Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13...")
        print("    (each number is the sum of the previous two)")
        print("\nGenerate and print the first 7 Fibonacci numbers.")
        print("Expected output: 0 1 1 2 3 5 8")
        print("\nEnter your code (type 'RUN' on a new line when done):")

        lines = []
        while True:
            line = input()
            if line == "RUN":
                break
            lines.append(line)

        code = "\n".join(lines)
        output, exec_globals, error = self.run_code(code)

        if error:
            print(f"\nError: {error}")
            print("You earned 15 points for trying.")
            self.game_engine.add_points(15, self.stage)
            return False

        if 'fibonacci' not in exec_globals:
            print("\nFunction 'fibonacci' not found.")
            print("You earned 15 points for trying.")
            self.game_engine.add_points(15, self.stage)
            return False

        try:
            fib = exec_globals['fibonacci']
            result = list(fib(7))
            expected = [0, 1, 1, 2, 3, 5, 8]

            if result == expected:
                print("\nPerfect! Your Fibonacci generator is correct!")
                print("You earned 85 points!")
                self.game_engine.add_points(85, self.stage)
                self.game_engine.mark_challenge_complete('advanced_challenge_4', self.stage)
                return True
            else:
                print(f"\nExpected: {expected}")
                print(f"Got: {result}")
                print("You earned 35 points for trying.")
                self.game_engine.add_points(35, self.stage)
                return False
        except Exception as e:
            print(f"\nError: {e}")
            print("You earned 25 points for trying.")
            self.game_engine.add_points(25, self.stage)
            return False

    def challenge_5_functional_programming(self):
        """Challenge: Map, Filter, Reduce"""
        print("\n" + "="*60)
        print("CHALLENGE 5: Functional Programming Master")
        print("="*60)
        print("\nTask: Given numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
        print("\nUsing lambda, map, filter, and reduce:")
        print("  1. Filter to keep only even numbers")
        print("  2. Map to square each number")
        print("  3. Use reduce to find the sum")
        print("\nStore the final result in 'result' and print it.")
        print("Expected result: 220 (2^2 + 4^2 + 6^2 + 8^2 + 10^2)")
        print("\nHint: from functools import reduce")
        print("\nEnter your code (type 'RUN' on a new line when done):")

        lines = []
        while True:
            line = input()
            if line == "RUN":
                break
            lines.append(line)

        code = "\n".join(lines)
        output, exec_globals, error = self.run_code(code)

        if error:
            print(f"\nError: {error}")
            print("You earned 20 points for trying.")
            self.game_engine.add_points(20, self.stage)
            return False

        if 'result' in exec_globals and exec_globals['result'] == 220:
            print("\nOutstanding! You've mastered functional programming!")
            print("You earned 100 points!")
            self.game_engine.add_points(100, self.stage)
            self.game_engine.mark_challenge_complete('advanced_challenge_5', self.stage)

            # Check for achievement
            completed = len([c for c in self.game_engine.progress['completed_challenges']
                           if c.startswith('advanced_')])
            if completed >= 5:
                if self.game_engine.unlock_achievement("Python Master - All Advanced Challenges"):
                    print("\nACHIEVEMENT UNLOCKED: Python Master - All Advanced Challenges")

            # Check if completed all challenges
            total_completed = len(self.game_engine.progress['completed_challenges'])
            if total_completed >= 15:
                if self.game_engine.unlock_achievement("Ultimate Python Champion"):
                    print("\nACHIEVEMENT UNLOCKED: Ultimate Python Champion")
                    print("Congratulations! You've completed ALL challenges!")

            return True
        else:
            result = exec_globals.get('result', 'Not found')
            print(f"\nExpected: 220")
            print(f"Got: {result}")
            print("You earned 40 points for trying.")
            self.game_engine.add_points(40, self.stage)
            return False

    def show_menu(self):
        """Display advanced challenges menu"""
        while True:
            print("\n" + "="*60)
            print("ADVANCED CHALLENGES")
            print("="*60)
            print("1. Challenge 1: Bank Account Class")
            print("2. Challenge 2: Shape Inheritance")
            print("3. Challenge 3: Timing Decorator")
            print("4. Challenge 4: Fibonacci Generator")
            print("5. Challenge 5: Functional Programming Master")
            print("0. Back to Main Menu")
            print("="*60)

            choice = input("\nSelect a challenge (0-5): ")

            if choice == "1":
                self.challenge_1_bank_account()
            elif choice == "2":
                self.challenge_2_inheritance_shapes()
            elif choice == "3":
                self.challenge_3_decorator()
            elif choice == "4":
                self.challenge_4_generator()
            elif choice == "5":
                self.challenge_5_functional_programming()
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")

            input("\nPress Enter to continue...")
