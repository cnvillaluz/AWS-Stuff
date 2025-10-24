import sys
from io import StringIO

class IntermediateChallenges:
    def __init__(self, game_engine):
        self.game_engine = game_engine
        self.stage = 'intermediate'

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

    def challenge_1_function_power(self):
        """Challenge: Create a power function"""
        print("\n" + "="*60)
        print("CHALLENGE 1: Power Function")
        print("="*60)
        print("\nTask: Create a function called 'power' that takes two parameters:")
        print("  - base: the base number")
        print("  - exponent: the power to raise it to (default value should be 2)")
        print("\nThe function should return base raised to the exponent.")
        print("Then call: power(3, 3) and power(5) and print both results.")
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
            print("You earned 10 points for trying.")
            self.game_engine.add_points(10, self.stage)
            return False

        success = True
        feedback = []

        # Check if function exists
        if 'power' not in exec_globals:
            feedback.append("Function 'power' not found")
            success = False
        else:
            func = exec_globals['power']
            # Test the function
            try:
                result1 = func(3, 3)
                result2 = func(5)
                if result1 != 27:
                    feedback.append(f"power(3, 3) should return 27, not {result1}")
                    success = False
                if result2 != 25:
                    feedback.append(f"power(5) should return 25, not {result2}")
                    success = False
            except Exception as e:
                feedback.append(f"Function error: {e}")
                success = False

        if success and output and '27' in output and '25' in output:
            print("\nPerfect! You earned 40 points!")
            self.game_engine.add_points(40, self.stage)
            self.game_engine.mark_challenge_complete('intermediate_challenge_1', self.stage)
            return True
        else:
            if feedback:
                print("\nIssues found:")
                for msg in feedback:
                    print(f"  - {msg}")
            else:
                print("\nFunction works but output is missing or incorrect.")
            print("You earned 15 points for trying.")
            self.game_engine.add_points(15, self.stage)
            return False

    def challenge_2_dict_manipulation(self):
        """Challenge: Dictionary operations"""
        print("\n" + "="*60)
        print("CHALLENGE 2: Student Grade Manager")
        print("="*60)
        print("\nTask: Create a dictionary 'grades' with the following:")
        print("  - 'Alice': 85")
        print("  - 'Bob': 92")
        print("  - 'Charlie': 78")
        print("\nThen:")
        print("  1. Add 'Diana' with grade 95")
        print("  2. Update Bob's grade to 88")
        print("  3. Calculate and print the average of all grades")
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
            print("You earned 10 points for trying.")
            self.game_engine.add_points(10, self.stage)
            return False

        success = True
        feedback = []

        if 'grades' not in exec_globals:
            feedback.append("Dictionary 'grades' not found")
            success = False
        else:
            grades = exec_globals['grades']
            expected = {'Alice': 85, 'Bob': 88, 'Charlie': 78, 'Diana': 95}

            if grades != expected:
                feedback.append(f"Expected grades: {expected}")
                feedback.append(f"Your grades: {grades}")
                success = False

            # Check average calculation
            average = sum(expected.values()) / len(expected)
            if output and f"{average}" not in output and f"{average:.1f}" not in output:
                feedback.append(f"Average ({average}) should be printed")
                success = False

        if success:
            print("\nExcellent! You earned 45 points!")
            self.game_engine.add_points(45, self.stage)
            self.game_engine.mark_challenge_complete('intermediate_challenge_2', self.stage)
            return True
        else:
            print("\nNot quite right:")
            for msg in feedback:
                print(f"  - {msg}")
            print("You earned 15 points for trying.")
            self.game_engine.add_points(15, self.stage)
            return False

    def challenge_3_list_comp(self):
        """Challenge: List comprehension mastery"""
        print("\n" + "="*60)
        print("CHALLENGE 3: List Comprehension Challenge")
        print("="*60)
        print("\nTask: Using list comprehension, create:")
        print("  1. 'squares': List of squares of numbers 1-10")
        print("  2. 'evens': List of even numbers from 1-20")
        print("  3. 'upper_words': Convert ['hello', 'world'] to uppercase")
        print("\nPrint all three lists.")
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
            print("You earned 10 points for trying.")
            self.game_engine.add_points(10, self.stage)
            return False

        success = True
        feedback = []

        expected_squares = [x**2 for x in range(1, 11)]
        expected_evens = [x for x in range(1, 21) if x % 2 == 0]
        expected_upper = ['HELLO', 'WORLD']

        if 'squares' not in exec_globals or exec_globals['squares'] != expected_squares:
            feedback.append(f"squares should be {expected_squares}")
            success = False

        if 'evens' not in exec_globals or exec_globals['evens'] != expected_evens:
            feedback.append(f"evens should be {expected_evens}")
            success = False

        if 'upper_words' not in exec_globals or exec_globals['upper_words'] != expected_upper:
            feedback.append(f"upper_words should be {expected_upper}")
            success = False

        if success:
            print("\nFantastic! You're a list comprehension master! You earned 50 points!")
            self.game_engine.add_points(50, self.stage)
            self.game_engine.mark_challenge_complete('intermediate_challenge_3', self.stage)
            return True
        else:
            print("\nNot quite right:")
            for msg in feedback:
                print(f"  - {msg}")
            print("You earned 20 points for trying.")
            self.game_engine.add_points(20, self.stage)
            return False

    def challenge_4_error_handler(self):
        """Challenge: Error handling"""
        print("\n" + "="*60)
        print("CHALLENGE 4: Safe Division")
        print("="*60)
        print("\nTask: Create a function 'safe_divide(a, b)' that:")
        print("  - Returns a / b if successful")
        print("  - Returns 'Cannot divide by zero' if b is 0")
        print("  - Returns 'Invalid input' for any other error")
        print("\nTest it with: safe_divide(10, 2), safe_divide(10, 0)")
        print("Print both results.")
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
            print("You earned 10 points for trying.")
            self.game_engine.add_points(10, self.stage)
            return False

        if 'safe_divide' not in exec_globals:
            print("\nFunction 'safe_divide' not found.")
            print("You earned 10 points for trying.")
            self.game_engine.add_points(10, self.stage)
            return False

        func = exec_globals['safe_divide']
        try:
            result1 = func(10, 2)
            result2 = func(10, 0)

            if result1 == 5.0 and result2 == 'Cannot divide by zero':
                print("\nPerfect error handling! You earned 50 points!")
                self.game_engine.add_points(50, self.stage)
                self.game_engine.mark_challenge_complete('intermediate_challenge_4', self.stage)
                return True
            else:
                print(f"\nNot quite. Got: {result1}, {result2}")
                print("Expected: 5.0, 'Cannot divide by zero'")
                print("You earned 20 points for trying.")
                self.game_engine.add_points(20, self.stage)
                return False
        except Exception as e:
            print(f"\nFunction error: {e}")
            print("You earned 15 points for trying.")
            self.game_engine.add_points(15, self.stage)
            return False

    def challenge_5_word_counter(self):
        """Challenge: Build a word frequency counter"""
        print("\n" + "="*60)
        print("CHALLENGE 5: Word Frequency Counter")
        print("="*60)
        print("\nTask: Create a function 'count_words(text)' that:")
        print("  - Takes a string as input")
        print("  - Returns a dictionary with word frequencies")
        print("  - Should be case-insensitive")
        print("\nExample: count_words('Hello hello world')")
        print("Should return: {'hello': 2, 'world': 1}")
        print("\nTest with: 'Python is fun Python is powerful'")
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
            print("You earned 10 points for trying.")
            self.game_engine.add_points(10, self.stage)
            return False

        if 'count_words' not in exec_globals:
            print("\nFunction 'count_words' not found.")
            print("You earned 10 points for trying.")
            self.game_engine.add_points(10, self.stage)
            return False

        func = exec_globals['count_words']
        try:
            result = func('Python is fun Python is powerful')
            expected = {'python': 2, 'is': 2, 'fun': 1, 'powerful': 1}

            if result == expected:
                print("\nExcellent work! You earned 60 points!")
                self.game_engine.add_points(60, self.stage)
                self.game_engine.mark_challenge_complete('intermediate_challenge_5', self.stage)

                # Check for achievement
                completed = len([c for c in self.game_engine.progress['completed_challenges']
                               if c.startswith('intermediate_')])
                if completed >= 5:
                    if self.game_engine.unlock_achievement("Intermediate Code Master"):
                        print("\nACHIEVEMENT UNLOCKED: Intermediate Code Master")
                return True
            else:
                print(f"\nNot quite. Expected: {expected}")
                print(f"Got: {result}")
                print("You earned 25 points for trying.")
                self.game_engine.add_points(25, self.stage)
                return False
        except Exception as e:
            print(f"\nFunction error: {e}")
            print("You earned 15 points for trying.")
            self.game_engine.add_points(15, self.stage)
            return False

    def show_menu(self):
        """Display intermediate challenges menu"""
        while True:
            print("\n" + "="*60)
            print("INTERMEDIATE CHALLENGES")
            print("="*60)
            print("1. Challenge 1: Power Function")
            print("2. Challenge 2: Student Grade Manager")
            print("3. Challenge 3: List Comprehension Challenge")
            print("4. Challenge 4: Safe Division")
            print("5. Challenge 5: Word Frequency Counter")
            print("0. Back to Main Menu")
            print("="*60)

            choice = input("\nSelect a challenge (0-5): ")

            if choice == "1":
                self.challenge_1_function_power()
            elif choice == "2":
                self.challenge_2_dict_manipulation()
            elif choice == "3":
                self.challenge_3_list_comp()
            elif choice == "4":
                self.challenge_4_error_handler()
            elif choice == "5":
                self.challenge_5_word_counter()
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")

            input("\nPress Enter to continue...")
