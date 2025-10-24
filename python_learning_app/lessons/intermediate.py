class IntermediateLessons:
    def __init__(self, game_engine):
        self.game_engine = game_engine
        self.stage = 'intermediate'

    def lesson_1_functions(self):
        """Functions and Parameters"""
        print("\n" + "="*60)
        print("LESSON 1: Functions")
        print("="*60)

        print("\nFunctions are reusable blocks of code that perform a specific task.")
        print("\nDefining a function:")
        print("  def greet(name):")
        print("      return f'Hello, {name}!'")
        print("\nCalling a function:")
        print("  message = greet('Alice')")
        print("  print(message)  # Output: Hello, Alice!")

        print("\nFunction with multiple parameters:")
        print("  def add(a, b):")
        print("      return a + b")
        print("\nDefault parameters:")
        print("  def greet(name='Guest'):")
        print("      return f'Hello, {name}!'")

        input("\nPress Enter to continue...")

        # Quiz
        print("\n" + "-"*60)
        print("QUIZ TIME!")
        print("-"*60)

        score = 0

        print("\nQ1: What keyword is used to exit a function and return a value?")
        print("  1. exit")
        print("  2. return")
        print("  3. break")
        print("  4. yield")

        answer = input("\nYour answer (1-4): ")
        if answer == "2":
            print("Correct! 'return' exits a function and returns a value.")
            score += 15
        else:
            print("Incorrect. The correct answer is 2 (return).")
            score += 7

        print("\nQ2: What is the output of this code?")
        print("  def multiply(x, y=2):")
        print("      return x * y")
        print("  print(multiply(5))")
        print("\n  1. Error")
        print("  2. 5")
        print("  3. 10")
        print("  4. None")

        answer = input("\nYour answer (1-4): ")
        if answer == "3":
            print("Correct! y defaults to 2, so 5 * 2 = 10.")
            score += 15
        else:
            print("Incorrect. The correct answer is 3 (10).")
            print("Default parameter y=2 is used when not provided.")
            score += 7

        print(f"\nLesson Complete! You earned {score} points!")
        self.game_engine.add_points(score, self.stage)
        self.game_engine.mark_lesson_complete('intermediate_lesson_1', self.stage)

    def lesson_2_dictionaries(self):
        """Dictionaries and Key-Value Pairs"""
        print("\n" + "="*60)
        print("LESSON 2: Dictionaries")
        print("="*60)

        print("\nDictionaries store data in key-value pairs.")
        print("\nCreating a dictionary:")
        print("  person = {")
        print("      'name': 'John',")
        print("      'age': 30,")
        print("      'city': 'New York'")
        print("  }")

        print("\nAccessing values:")
        print("  print(person['name'])  # Output: John")
        print("  print(person.get('age'))  # Output: 30")

        print("\nModifying dictionaries:")
        print("  person['age'] = 31  # Update value")
        print("  person['job'] = 'Developer'  # Add new key-value")
        print("  del person['city']  # Remove key-value")

        print("\nUseful methods:")
        print("  person.keys()    # Get all keys")
        print("  person.values()  # Get all values")
        print("  person.items()   # Get all key-value pairs")

        input("\nPress Enter to continue...")

        # Quiz
        print("\n" + "-"*60)
        print("QUIZ TIME!")
        print("-"*60)

        score = 0

        print("\nQ1: How do you add a new key-value pair to a dictionary?")
        print("  dict_name = {'a': 1}")
        print("\n  1. dict_name.add('b', 2)")
        print("  2. dict_name['b'] = 2")
        print("  3. dict_name.append('b': 2)")
        print("  4. dict_name.insert('b', 2)")

        answer = input("\nYour answer (1-4): ")
        if answer == "2":
            print("Correct! Use bracket notation to add/update entries.")
            score += 15
        else:
            print("Incorrect. The correct answer is 2.")
            score += 7

        print("\nQ2: What does this return?")
        print("  data = {'x': 10, 'y': 20}")
        print("  data.get('z', 0)")
        print("\n  1. Error")
        print("  2. None")
        print("  3. 0")
        print("  4. 'z'")

        answer = input("\nYour answer (1-4): ")
        if answer == "3":
            print("Correct! get() returns the default value (0) if key not found.")
            score += 15
        else:
            print("Incorrect. The correct answer is 3 (0).")
            print("get(key, default) returns default if key doesn't exist.")
            score += 7

        print(f"\nLesson Complete! You earned {score} points!")
        self.game_engine.add_points(score, self.stage)
        self.game_engine.mark_lesson_complete('intermediate_lesson_2', self.stage)

    def lesson_3_list_comprehension(self):
        """List Comprehensions"""
        print("\n" + "="*60)
        print("LESSON 3: List Comprehensions")
        print("="*60)

        print("\nList comprehensions provide a concise way to create lists.")
        print("\nTraditional way:")
        print("  squares = []")
        print("  for x in range(5):")
        print("      squares.append(x**2)")
        print("  # Result: [0, 1, 4, 9, 16]")

        print("\nList comprehension way:")
        print("  squares = [x**2 for x in range(5)]")
        print("  # Result: [0, 1, 4, 9, 16]")

        print("\nWith condition:")
        print("  evens = [x for x in range(10) if x % 2 == 0]")
        print("  # Result: [0, 2, 4, 6, 8]")

        print("\nWith transformation:")
        print("  names = ['alice', 'bob', 'charlie']")
        print("  upper_names = [name.upper() for name in names]")
        print("  # Result: ['ALICE', 'BOB', 'CHARLIE']")

        input("\nPress Enter to continue...")

        # Quiz
        print("\n" + "-"*60)
        print("QUIZ TIME!")
        print("-"*60)

        score = 0

        print("\nQ1: What does this list comprehension create?")
        print("  [x*2 for x in range(4)]")
        print("\n  1. [0, 2, 4, 6]")
        print("  2. [0, 1, 2, 3]")
        print("  3. [2, 4, 6, 8]")
        print("  4. [1, 2, 3, 4]")

        answer = input("\nYour answer (1-4): ")
        if answer == "1":
            print("Correct! Each number from 0-3 is multiplied by 2.")
            score += 15
        else:
            print("Incorrect. The correct answer is 1.")
            score += 7

        print("\nQ2: Which creates a list of odd numbers from 1 to 9?")
        print("  1. [x for x in range(10) if x % 2 == 0]")
        print("  2. [x for x in range(1, 10) if x % 2 == 1]")
        print("  3. [x for x in range(10) if x % 2]")
        print("  4. Both 2 and 3")

        answer = input("\nYour answer (1-4): ")
        if answer == "4":
            print("Correct! Both check for odd numbers (remainder of 1 when divided by 2).")
            score += 15
        else:
            print("Incorrect. The correct answer is 4.")
            score += 7

        print(f"\nLesson Complete! You earned {score} points!")
        self.game_engine.add_points(score, self.stage)
        self.game_engine.mark_lesson_complete('intermediate_lesson_3', self.stage)

    def lesson_4_error_handling(self):
        """Try-Except Error Handling"""
        print("\n" + "="*60)
        print("LESSON 4: Error Handling")
        print("="*60)

        print("\nError handling prevents your program from crashing.")
        print("\nBasic try-except:")
        print("  try:")
        print("      result = 10 / 0")
        print("  except ZeroDivisionError:")
        print("      print('Cannot divide by zero!')")

        print("\nMultiple exceptions:")
        print("  try:")
        print("      value = int(input('Enter a number: '))")
        print("  except ValueError:")
        print("      print('Invalid number!')")
        print("  except Exception as e:")
        print("      print(f'Error: {e}')")

        print("\nFinally block (always executes):")
        print("  try:")
        print("      file = open('data.txt')")
        print("  except FileNotFoundError:")
        print("      print('File not found')")
        print("  finally:")
        print("      print('Cleanup complete')")

        input("\nPress Enter to continue...")

        # Quiz
        print("\n" + "-"*60)
        print("QUIZ TIME!")
        print("-"*60)

        score = 0

        print("\nQ1: What happens in this code?")
        print("  try:")
        print("      print(10 / 0)")
        print("  except ValueError:")
        print("      print('Error!')")
        print("\n  1. Prints 'Error!'")
        print("  2. Prints nothing")
        print("  3. Program crashes")
        print("  4. Prints 0")

        answer = input("\nYour answer (1-4): ")
        if answer == "3":
            print("Correct! ZeroDivisionError isn't caught by ValueError handler.")
            score += 20
        else:
            print("Incorrect. The correct answer is 3.")
            print("The exception handler catches ValueError, not ZeroDivisionError.")
            score += 10

        print("\nQ2: When does the 'finally' block execute?")
        print("  1. Only if no exception occurs")
        print("  2. Only if an exception occurs")
        print("  3. Always, regardless of exceptions")
        print("  4. Never")

        answer = input("\nYour answer (1-4): ")
        if answer == "3":
            print("Correct! The 'finally' block always executes.")
            score += 20
        else:
            print("Incorrect. The correct answer is 3.")
            score += 10

        print(f"\nLesson Complete! You earned {score} points!")
        self.game_engine.add_points(score, self.stage)
        self.game_engine.mark_lesson_complete('intermediate_lesson_4', self.stage)

    def lesson_5_file_operations(self):
        """Reading and Writing Files"""
        print("\n" + "="*60)
        print("LESSON 5: File Operations")
        print("="*60)

        print("\nPython can read and write files easily.")
        print("\nReading a file:")
        print("  with open('file.txt', 'r') as file:")
        print("      content = file.read()")
        print("      print(content)")

        print("\nWriting to a file:")
        print("  with open('file.txt', 'w') as file:")
        print("      file.write('Hello, World!')")

        print("\nAppending to a file:")
        print("  with open('file.txt', 'a') as file:")
        print("      file.write('New line\\n')")

        print("\nReading line by line:")
        print("  with open('file.txt', 'r') as file:")
        print("      for line in file:")
        print("          print(line.strip())")

        print("\nFile modes:")
        print("  'r' - Read (default)")
        print("  'w' - Write (overwrites)")
        print("  'a' - Append")
        print("  'r+' - Read and write")

        input("\nPress Enter to continue...")

        # Quiz
        print("\n" + "-"*60)
        print("QUIZ TIME!")
        print("-"*60)

        score = 0

        print("\nQ1: What does 'with' do when opening files?")
        print("  1. Makes the file read-only")
        print("  2. Automatically closes the file")
        print("  3. Creates the file if it doesn't exist")
        print("  4. Locks the file")

        answer = input("\nYour answer (1-4): ")
        if answer == "2":
            print("Correct! 'with' ensures the file is properly closed.")
            score += 20
        else:
            print("Incorrect. The correct answer is 2.")
            score += 10

        print("\nQ2: Which mode would you use to add content to an existing file?")
        print("  1. 'r'")
        print("  2. 'w'")
        print("  3. 'a'")
        print("  4. 'x'")

        answer = input("\nYour answer (1-4): ")
        if answer == "3":
            print("Correct! 'a' appends without overwriting existing content.")
            score += 20
        else:
            print("Incorrect. The correct answer is 3 ('a' for append).")
            score += 10

        print(f"\nLesson Complete! You earned {score} points!")
        self.game_engine.add_points(score, self.stage)
        self.game_engine.mark_lesson_complete('intermediate_lesson_5', self.stage)

        # Check for achievement
        completed = len([l for l in self.game_engine.progress['completed_lessons']
                       if l.startswith('intermediate_')])
        if completed >= 5:
            if self.game_engine.unlock_achievement("Intermediate Scholar"):
                print("\nACHIEVEMENT UNLOCKED: Intermediate Scholar")

    def show_menu(self):
        """Display intermediate lessons menu"""
        while True:
            print("\n" + "="*60)
            print("INTERMEDIATE LESSONS")
            print("="*60)
            print("1. Lesson 1: Functions")
            print("2. Lesson 2: Dictionaries")
            print("3. Lesson 3: List Comprehensions")
            print("4. Lesson 4: Error Handling")
            print("5. Lesson 5: File Operations")
            print("0. Back to Main Menu")
            print("="*60)

            choice = input("\nSelect a lesson (0-5): ")

            if choice == "1":
                self.lesson_1_functions()
            elif choice == "2":
                self.lesson_2_dictionaries()
            elif choice == "3":
                self.lesson_3_list_comprehension()
            elif choice == "4":
                self.lesson_4_error_handling()
            elif choice == "5":
                self.lesson_5_file_operations()
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")
