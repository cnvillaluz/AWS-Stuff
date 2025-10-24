import time

class BeginnerLessons:
    def __init__(self, game_engine):
        self.game_engine = game_engine
        self.stage = 'beginner'

    def lesson_1_variables(self):
        """Introduction to Variables"""
        print("\n" + "="*60)
        print("LESSON 1: Variables and Data Types")
        print("="*60)

        print("\nVariables are containers for storing data values.")
        print("Python has no command for declaring a variable.")
        print("A variable is created the moment you first assign a value to it.\n")

        print("Examples:")
        print("  x = 5          # Integer")
        print("  name = 'John'  # String")
        print("  pi = 3.14      # Float")
        print("  is_valid = True # Boolean")

        input("\nPress Enter to continue...")

        # Quiz
        print("\n" + "-"*60)
        print("QUIZ TIME!")
        print("-"*60)

        score = 0

        print("\nQ1: Which of these is a valid variable name in Python?")
        print("  1. 2cool")
        print("  2. my_variable")
        print("  3. my-variable")
        print("  4. my variable")

        answer = input("\nYour answer (1-4): ")
        if answer == "2":
            print("Correct! Variable names can contain letters, numbers, and underscores.")
            print("They cannot start with a number or contain spaces/hyphens.")
            score += 10
        else:
            print("Incorrect. The correct answer is 2.")
            print("Variable names must start with a letter or underscore, not a number.")
            score += 5

        print("\nQ2: What is the data type of: x = 'Hello'?")
        print("  1. Integer")
        print("  2. String")
        print("  3. Float")
        print("  4. Boolean")

        answer = input("\nYour answer (1-4): ")
        if answer == "2":
            print("Correct! Text in quotes is a string.")
            score += 10
        else:
            print("Incorrect. The correct answer is 2 (String).")
            print("Any text enclosed in quotes is a string.")
            score += 5

        print(f"\nLesson Complete! You earned {score} points!")
        self.game_engine.add_points(score, self.stage)
        self.game_engine.mark_lesson_complete('beginner_lesson_1', self.stage)

        if score >= 20:
            if self.game_engine.unlock_achievement("Perfect Score - Lesson 1"):
                print("\nACHIEVEMENT UNLOCKED: Perfect Score - Lesson 1")

    def lesson_2_operators(self):
        """Arithmetic and Comparison Operators"""
        print("\n" + "="*60)
        print("LESSON 2: Operators")
        print("="*60)

        print("\nPython supports various operators:")
        print("\nArithmetic Operators:")
        print("  + (addition)    : 5 + 3 = 8")
        print("  - (subtraction) : 5 - 3 = 2")
        print("  * (multiplication): 5 * 3 = 15")
        print("  / (division)    : 5 / 2 = 2.5")
        print("  // (floor division): 5 // 2 = 2")
        print("  % (modulus)     : 5 % 2 = 1")
        print("  ** (exponent)   : 5 ** 2 = 25")

        print("\nComparison Operators:")
        print("  == (equal)      : 5 == 5 is True")
        print("  != (not equal)  : 5 != 3 is True")
        print("  > (greater)     : 5 > 3 is True")
        print("  < (less)        : 5 < 3 is False")

        input("\nPress Enter to continue...")

        # Quiz
        print("\n" + "-"*60)
        print("QUIZ TIME!")
        print("-"*60)

        score = 0

        print("\nQ1: What is the result of: 10 // 3?")
        print("  1. 3.33")
        print("  2. 3")
        print("  3. 1")
        print("  4. 4")

        answer = input("\nYour answer (1-4): ")
        if answer == "2":
            print("Correct! // performs floor division, returning the integer part.")
            score += 10
        else:
            print("Incorrect. The correct answer is 2.")
            print("The // operator divides and rounds down to the nearest integer.")
            score += 5

        print("\nQ2: What is the result of: 17 % 5?")
        print("  1. 2")
        print("  2. 3")
        print("  3. 5")
        print("  4. 3.4")

        answer = input("\nYour answer (1-4): ")
        if answer == "1":
            print("Correct! The % operator returns the remainder of division.")
            score += 10
        else:
            print("Incorrect. The correct answer is 1.")
            print("17 divided by 5 is 3 with a remainder of 2.")
            score += 5

        print("\nQ3: What is the result of: 5 == 5?")
        print("  1. 5")
        print("  2. True")
        print("  3. False")
        print("  4. Error")

        answer = input("\nYour answer (1-4): ")
        if answer == "2":
            print("Correct! The == operator checks equality and returns a boolean.")
            score += 10
        else:
            print("Incorrect. The correct answer is 2 (True).")
            print("The == operator compares values and returns True or False.")
            score += 5

        print(f"\nLesson Complete! You earned {score} points!")
        self.game_engine.add_points(score, self.stage)
        self.game_engine.mark_lesson_complete('beginner_lesson_2', self.stage)

        if score >= 30:
            if self.game_engine.unlock_achievement("Math Wizard - Lesson 2"):
                print("\nACHIEVEMENT UNLOCKED: Math Wizard - Lesson 2")

    def lesson_3_conditionals(self):
        """If, Elif, Else Statements"""
        print("\n" + "="*60)
        print("LESSON 3: Conditional Statements")
        print("="*60)

        print("\nConditional statements allow you to execute different code")
        print("based on certain conditions.\n")

        print("Syntax:")
        print("  if condition:")
        print("      # code to execute if condition is True")
        print("  elif another_condition:")
        print("      # code to execute if this condition is True")
        print("  else:")
        print("      # code to execute if all conditions are False")

        print("\nExample:")
        print("  age = 18")
        print("  if age >= 18:")
        print("      print('You are an adult')")
        print("  else:")
        print("      print('You are a minor')")

        input("\nPress Enter to continue...")

        # Quiz
        print("\n" + "-"*60)
        print("QUIZ TIME!")
        print("-"*60)

        score = 0

        print("\nQ1: What will this code print?")
        print("  x = 10")
        print("  if x > 5:")
        print("      print('A')")
        print("  else:")
        print("      print('B')")
        print("\n  1. A")
        print("  2. B")
        print("  3. Both A and B")
        print("  4. Nothing")

        answer = input("\nYour answer (1-4): ")
        if answer == "1":
            print("Correct! x (10) is greater than 5, so 'A' is printed.")
            score += 15
        else:
            print("Incorrect. The correct answer is 1 (A).")
            print("Since 10 > 5 is True, the if block executes.")
            score += 7

        print("\nQ2: How do you check if x equals 10?")
        print("  1. if x = 10:")
        print("  2. if x == 10:")
        print("  3. if x := 10:")
        print("  4. if x is 10:")

        answer = input("\nYour answer (1-4): ")
        if answer == "2":
            print("Correct! Use == for comparison, not =")
            score += 15
        else:
            print("Incorrect. The correct answer is 2.")
            print("== is for comparison, = is for assignment.")
            score += 7

        print(f"\nLesson Complete! You earned {score} points!")
        self.game_engine.add_points(score, self.stage)
        self.game_engine.mark_lesson_complete('beginner_lesson_3', self.stage)

        if score >= 30:
            if self.game_engine.unlock_achievement("Logic Master - Lesson 3"):
                print("\nACHIEVEMENT UNLOCKED: Logic Master - Lesson 3")

    def lesson_4_loops(self):
        """For and While Loops"""
        print("\n" + "="*60)
        print("LESSON 4: Loops")
        print("="*60)

        print("\nLoops allow you to execute code repeatedly.\n")

        print("FOR Loop - iterate over a sequence:")
        print("  for i in range(5):")
        print("      print(i)  # Prints 0, 1, 2, 3, 4")

        print("\nWHILE Loop - repeat while condition is True:")
        print("  count = 0")
        print("  while count < 5:")
        print("      print(count)")
        print("      count += 1")

        input("\nPress Enter to continue...")

        # Quiz
        print("\n" + "-"*60)
        print("QUIZ TIME!")
        print("-"*60)

        score = 0

        print("\nQ1: How many times will this loop run?")
        print("  for i in range(3):")
        print("      print(i)")
        print("\n  1. 2")
        print("  2. 3")
        print("  3. 4")
        print("  4. Infinite")

        answer = input("\nYour answer (1-4): ")
        if answer == "2":
            print("Correct! range(3) produces 0, 1, 2 (3 values).")
            score += 15
        else:
            print("Incorrect. The correct answer is 2.")
            print("range(n) generates numbers from 0 to n-1.")
            score += 7

        print("\nQ2: What does 'break' do in a loop?")
        print("  1. Skips the current iteration")
        print("  2. Exits the loop completely")
        print("  3. Restarts the loop")
        print("  4. Pauses the loop")

        answer = input("\nYour answer (1-4): ")
        if answer == "2":
            print("Correct! 'break' exits the loop immediately.")
            score += 15
        else:
            print("Incorrect. The correct answer is 2.")
            print("'break' terminates the loop, 'continue' skips an iteration.")
            score += 7

        print(f"\nLesson Complete! You earned {score} points!")
        self.game_engine.add_points(score, self.stage)
        self.game_engine.mark_lesson_complete('beginner_lesson_4', self.stage)

        if score >= 30:
            if self.game_engine.unlock_achievement("Loop Master - Lesson 4"):
                print("\nACHIEVEMENT UNLOCKED: Loop Master - Lesson 4")

    def lesson_5_lists(self):
        """Lists and Basic Operations"""
        print("\n" + "="*60)
        print("LESSON 5: Lists")
        print("="*60)

        print("\nLists are ordered, mutable collections of items.\n")

        print("Creating a list:")
        print("  fruits = ['apple', 'banana', 'cherry']")
        print("  numbers = [1, 2, 3, 4, 5]")

        print("\nCommon list operations:")
        print("  fruits[0]          # Access first item: 'apple'")
        print("  fruits.append('orange')  # Add item to end")
        print("  fruits.remove('banana')  # Remove specific item")
        print("  len(fruits)        # Get list length")
        print("  fruits[1:3]        # Slice: items from index 1 to 2")

        input("\nPress Enter to continue...")

        # Quiz
        print("\n" + "-"*60)
        print("QUIZ TIME!")
        print("-"*60)

        score = 0

        print("\nQ1: What is the index of the first item in a list?")
        print("  1. -1")
        print("  2. 0")
        print("  3. 1")
        print("  4. It depends")

        answer = input("\nYour answer (1-4): ")
        if answer == "2":
            print("Correct! Python uses 0-based indexing.")
            score += 10
        else:
            print("Incorrect. The correct answer is 2.")
            print("Python lists start at index 0.")
            score += 5

        print("\nQ2: What does this return? [1, 2, 3, 4, 5][1:3]")
        print("  1. [1, 2]")
        print("  2. [2, 3]")
        print("  3. [2, 3, 4]")
        print("  4. [1, 2, 3]")

        answer = input("\nYour answer (1-4): ")
        if answer == "2":
            print("Correct! Slicing includes start index but excludes end index.")
            score += 10
        else:
            print("Incorrect. The correct answer is 2.")
            print("[1:3] means from index 1 up to (but not including) index 3.")
            score += 5

        print("\nQ3: How do you add an item to the end of a list?")
        print("  1. list.add(item)")
        print("  2. list.append(item)")
        print("  3. list.insert(item)")
        print("  4. list.push(item)")

        answer = input("\nYour answer (1-4): ")
        if answer == "2":
            print("Correct! append() adds an item to the end of a list.")
            score += 10
        else:
            print("Incorrect. The correct answer is 2.")
            print("Use append() to add items to the end of a list.")
            score += 5

        print(f"\nLesson Complete! You earned {score} points!")
        self.game_engine.add_points(score, self.stage)
        self.game_engine.mark_lesson_complete('beginner_lesson_5', self.stage)

        if score >= 30:
            if self.game_engine.unlock_achievement("List Expert - Lesson 5"):
                print("\nACHIEVEMENT UNLOCKED: List Expert - Lesson 5")

    def show_menu(self):
        """Display beginner lessons menu"""
        while True:
            print("\n" + "="*60)
            print("BEGINNER LESSONS")
            print("="*60)
            print("1. Lesson 1: Variables and Data Types")
            print("2. Lesson 2: Operators")
            print("3. Lesson 3: Conditional Statements")
            print("4. Lesson 4: Loops")
            print("5. Lesson 5: Lists")
            print("0. Back to Main Menu")
            print("="*60)

            choice = input("\nSelect a lesson (0-5): ")

            if choice == "1":
                self.lesson_1_variables()
            elif choice == "2":
                self.lesson_2_operators()
            elif choice == "3":
                self.lesson_3_conditionals()
            elif choice == "4":
                self.lesson_4_loops()
            elif choice == "5":
                self.lesson_5_lists()
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")
