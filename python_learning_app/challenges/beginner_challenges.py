import sys
from io import StringIO

class BeginnerChallenges:
    def __init__(self, game_engine):
        self.game_engine = game_engine
        self.stage = 'beginner'

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

    def challenge_1_hello_world(self):
        """Challenge: Print Hello World"""
        print("\n" + "="*60)
        print("CHALLENGE 1: Hello, Python!")
        print("="*60)
        print("\nTask: Write code to print 'Hello, Python!' (exactly)")
        print("\nEnter your code (type 'RUN' on a new line when done):")

        lines = []
        while True:
            line = input()
            if line == "RUN":
                break
            lines.append(line)

        code = "\n".join(lines)
        output, _, error = self.run_code(code)

        if error:
            print(f"\nError: {error}")
            print("Try again! You earned 5 points for trying.")
            self.game_engine.add_points(5, self.stage)
            return False
        elif output and output.strip() == "Hello, Python!":
            print("\nCorrect! You earned 20 points!")
            self.game_engine.add_points(20, self.stage)
            self.game_engine.mark_challenge_complete('beginner_challenge_1', self.stage)
            return True
        else:
            print(f"\nNot quite. Your output: {output.strip()}")
            print("Expected: Hello, Python!")
            print("You earned 5 points for trying.")
            self.game_engine.add_points(5, self.stage)
            return False

    def challenge_2_calculator(self):
        """Challenge: Simple Calculator"""
        print("\n" + "="*60)
        print("CHALLENGE 2: Simple Calculator")
        print("="*60)
        print("\nTask: Create variables 'a' and 'b' with values 15 and 7.")
        print("Then create a variable 'result' that stores their sum.")
        print("Print the result.")
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
            print("Try again! You earned 5 points for trying.")
            self.game_engine.add_points(5, self.stage)
            return False

        success = True
        feedback = []

        if 'a' not in exec_globals or exec_globals.get('a') != 15:
            feedback.append("Variable 'a' should be 15")
            success = False
        if 'b' not in exec_globals or exec_globals.get('b') != 7:
            feedback.append("Variable 'b' should be 7")
            success = False
        if 'result' not in exec_globals or exec_globals.get('result') != 22:
            feedback.append("Variable 'result' should be 22 (a + b)")
            success = False
        if not output or '22' not in output:
            feedback.append("You should print the result")
            success = False

        if success:
            print("\nPerfect! You earned 25 points!")
            self.game_engine.add_points(25, self.stage)
            self.game_engine.mark_challenge_complete('beginner_challenge_2', self.stage)
            return True
        else:
            print("\nNot quite right:")
            for msg in feedback:
                print(f"  - {msg}")
            print("You earned 10 points for trying.")
            self.game_engine.add_points(10, self.stage)
            return False

    def challenge_3_even_odd(self):
        """Challenge: Even or Odd"""
        print("\n" + "="*60)
        print("CHALLENGE 3: Even or Odd Checker")
        print("="*60)
        print("\nTask: Create a variable 'number' with value 42.")
        print("Use an if-else statement to check if it's even or odd.")
        print("Print 'Even' if even, 'Odd' if odd.")
        print("\nHint: Use the modulus operator (%) to check divisibility by 2")
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
            print("Try again! You earned 5 points for trying.")
            self.game_engine.add_points(5, self.stage)
            return False

        if output and output.strip() == "Even":
            print("\nCorrect! 42 is even. You earned 30 points!")
            self.game_engine.add_points(30, self.stage)
            self.game_engine.mark_challenge_complete('beginner_challenge_3', self.stage)
            return True
        else:
            print(f"\nNot quite. Your output: {output.strip() if output else 'None'}")
            print("Expected: Even")
            print("You earned 10 points for trying.")
            self.game_engine.add_points(10, self.stage)
            return False

    def challenge_4_loop_sum(self):
        """Challenge: Sum numbers using a loop"""
        print("\n" + "="*60)
        print("CHALLENGE 4: Sum with Loops")
        print("="*60)
        print("\nTask: Use a for loop to calculate the sum of numbers 1 to 10.")
        print("Store the result in a variable 'total' and print it.")
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
            print("Try again! You earned 5 points for trying.")
            self.game_engine.add_points(5, self.stage)
            return False

        if 'total' in exec_globals and exec_globals['total'] == 55:
            if output and '55' in output:
                print("\nPerfect! The sum of 1 to 10 is 55. You earned 35 points!")
                self.game_engine.add_points(35, self.stage)
                self.game_engine.mark_challenge_complete('beginner_challenge_4', self.stage)

                # Check for achievement
                completed = len([c for c in self.game_engine.progress['completed_challenges']
                               if c.startswith('beginner_')])
                if completed >= 4:
                    if self.game_engine.unlock_achievement("Beginner Challenge Master"):
                        print("\nACHIEVEMENT UNLOCKED: Beginner Challenge Master")
                return True
            else:
                print("\nYou calculated it correctly, but forgot to print the result!")
                print("You earned 20 points!")
                self.game_engine.add_points(20, self.stage)
                return False
        else:
            print(f"\nNot quite. The sum of 1 to 10 is 55.")
            if 'total' in exec_globals:
                print(f"Your total: {exec_globals['total']}")
            print("You earned 10 points for trying.")
            self.game_engine.add_points(10, self.stage)
            return False

    def challenge_5_list_operations(self):
        """Challenge: List manipulation"""
        print("\n" + "="*60)
        print("CHALLENGE 5: List Master")
        print("="*60)
        print("\nTask: Create a list called 'numbers' with values [1, 2, 3, 4, 5]")
        print("1. Add the number 6 to the end")
        print("2. Remove the number 3")
        print("3. Print the final list")
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
            print("Try again! You earned 5 points for trying.")
            self.game_engine.add_points(5, self.stage)
            return False

        expected = [1, 2, 4, 5, 6]
        if 'numbers' in exec_globals and exec_globals['numbers'] == expected:
            print("\nPerfect! You earned 40 points!")
            self.game_engine.add_points(40, self.stage)
            self.game_engine.mark_challenge_complete('beginner_challenge_5', self.stage)
            return True
        else:
            print(f"\nNot quite. Expected: {expected}")
            if 'numbers' in exec_globals:
                print(f"Your list: {exec_globals['numbers']}")
            print("You earned 15 points for trying.")
            self.game_engine.add_points(15, self.stage)
            return False

    def show_menu(self):
        """Display beginner challenges menu"""
        while True:
            print("\n" + "="*60)
            print("BEGINNER CHALLENGES")
            print("="*60)
            print("1. Challenge 1: Hello, Python!")
            print("2. Challenge 2: Simple Calculator")
            print("3. Challenge 3: Even or Odd Checker")
            print("4. Challenge 4: Sum with Loops")
            print("5. Challenge 5: List Master")
            print("0. Back to Main Menu")
            print("="*60)

            choice = input("\nSelect a challenge (0-5): ")

            if choice == "1":
                self.challenge_1_hello_world()
            elif choice == "2":
                self.challenge_2_calculator()
            elif choice == "3":
                self.challenge_3_even_odd()
            elif choice == "4":
                self.challenge_4_loop_sum()
            elif choice == "5":
                self.challenge_5_list_operations()
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")

            input("\nPress Enter to continue...")
