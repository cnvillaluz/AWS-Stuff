class AdvancedLessons:
    def __init__(self, game_engine):
        self.game_engine = game_engine
        self.stage = 'advanced'

    def lesson_1_oop(self):
        """Object-Oriented Programming"""
        print("\n" + "="*60)
        print("LESSON 1: Object-Oriented Programming (OOP)")
        print("="*60)

        print("\nClasses are blueprints for creating objects.")
        print("\nDefining a class:")
        print("  class Dog:")
        print("      def __init__(self, name, age):")
        print("          self.name = name")
        print("          self.age = age")
        print("")
        print("      def bark(self):")
        print("          return f'{self.name} says Woof!'")

        print("\nCreating objects (instances):")
        print("  my_dog = Dog('Buddy', 3)")
        print("  print(my_dog.bark())  # Output: Buddy says Woof!")

        print("\nKey OOP concepts:")
        print("  - __init__: Constructor method (initializes object)")
        print("  - self: References the instance itself")
        print("  - Attributes: Data stored in objects (name, age)")
        print("  - Methods: Functions that belong to a class")

        input("\nPress Enter to continue...")

        # Quiz
        print("\n" + "-"*60)
        print("QUIZ TIME!")
        print("-"*60)

        score = 0

        print("\nQ1: What is 'self' in a class method?")
        print("  1. A keyword like 'if'")
        print("  2. A reference to the class instance")
        print("  3. A global variable")
        print("  4. A function parameter")

        answer = input("\nYour answer (1-4): ")
        if answer == "2":
            print("Correct! 'self' refers to the instance of the class.")
            score += 20
        else:
            print("Incorrect. The correct answer is 2.")
            score += 10

        print("\nQ2: What is the purpose of __init__?")
        print("  1. To delete an object")
        print("  2. To initialize object attributes")
        print("  3. To inherit from another class")
        print("  4. To print object information")

        answer = input("\nYour answer (1-4): ")
        if answer == "2":
            print("Correct! __init__ is the constructor that initializes objects.")
            score += 20
        else:
            print("Incorrect. The correct answer is 2.")
            score += 10

        print(f"\nLesson Complete! You earned {score} points!")
        self.game_engine.add_points(score, self.stage)
        self.game_engine.mark_lesson_complete('advanced_lesson_1', self.stage)

    def lesson_2_inheritance(self):
        """Inheritance and Polymorphism"""
        print("\n" + "="*60)
        print("LESSON 2: Inheritance")
        print("="*60)

        print("\nInheritance allows a class to inherit attributes and methods")
        print("from another class.\n")

        print("Parent class:")
        print("  class Animal:")
        print("      def __init__(self, name):")
        print("          self.name = name")
        print("")
        print("      def speak(self):")
        print("          pass")

        print("\nChild classes:")
        print("  class Dog(Animal):")
        print("      def speak(self):")
        print("          return f'{self.name} barks'")
        print("")
        print("  class Cat(Animal):")
        print("      def speak(self):")
        print("          return f'{self.name} meows'")

        print("\nUsage:")
        print("  dog = Dog('Buddy')")
        print("  cat = Cat('Whiskers')")
        print("  print(dog.speak())  # Buddy barks")
        print("  print(cat.speak())  # Whiskers meows")

        input("\nPress Enter to continue...")

        # Quiz
        print("\n" + "-"*60)
        print("QUIZ TIME!")
        print("-"*60)

        score = 0

        print("\nQ1: What is inheritance in OOP?")
        print("  1. Creating multiple objects")
        print("  2. A class acquiring properties from another class")
        print("  3. Deleting a class")
        print("  4. Copying code between files")

        answer = input("\nYour answer (1-4): ")
        if answer == "2":
            print("Correct! Inheritance allows code reuse through parent-child relationships.")
            score += 20
        else:
            print("Incorrect. The correct answer is 2.")
            score += 10

        print("\nQ2: If class B inherits from class A, what is class A called?")
        print("  1. Child class")
        print("  2. Subclass")
        print("  3. Parent/Base class")
        print("  4. Sibling class")

        answer = input("\nYour answer (1-4): ")
        if answer == "3":
            print("Correct! A is the parent/base/superclass.")
            score += 20
        else:
            print("Incorrect. The correct answer is 3.")
            score += 10

        print(f"\nLesson Complete! You earned {score} points!")
        self.game_engine.add_points(score, self.stage)
        self.game_engine.mark_lesson_complete('advanced_lesson_2', self.stage)

    def lesson_3_decorators(self):
        """Decorators"""
        print("\n" + "="*60)
        print("LESSON 3: Decorators")
        print("="*60)

        print("\nDecorators modify the behavior of functions or methods.")
        print("\nSimple decorator:")
        print("  def my_decorator(func):")
        print("      def wrapper():")
        print("          print('Before function')")
        print("          func()")
        print("          print('After function')")
        print("      return wrapper")

        print("\nUsing the decorator:")
        print("  @my_decorator")
        print("  def say_hello():")
        print("      print('Hello!')")
        print("")
        print("  say_hello()")
        print("  # Output:")
        print("  # Before function")
        print("  # Hello!")
        print("  # After function")

        print("\nCommon built-in decorators:")
        print("  @staticmethod - Method doesn't need instance")
        print("  @classmethod - Method takes class as first parameter")
        print("  @property - Makes method accessible like an attribute")

        input("\nPress Enter to continue...")

        # Quiz
        print("\n" + "-"*60)
        print("QUIZ TIME!")
        print("-"*60)

        score = 0

        print("\nQ1: What does a decorator do?")
        print("  1. Deletes a function")
        print("  2. Modifies or extends function behavior")
        print("  3. Creates a new class")
        print("  4. Handles errors")

        answer = input("\nYour answer (1-4): ")
        if answer == "2":
            print("Correct! Decorators wrap functions to add functionality.")
            score += 25
        else:
            print("Incorrect. The correct answer is 2.")
            score += 12

        print("\nQ2: How do you apply a decorator to a function?")
        print("  1. decorator(function)")
        print("  2. function.decorator()")
        print("  3. @decorator above the function definition")
        print("  4. function(@decorator)")

        answer = input("\nYour answer (1-4): ")
        if answer == "3":
            print("Correct! Use @decorator_name above the function.")
            score += 25
        else:
            print("Incorrect. The correct answer is 3.")
            score += 12

        print(f"\nLesson Complete! You earned {score} points!")
        self.game_engine.add_points(score, self.stage)
        self.game_engine.mark_lesson_complete('advanced_lesson_3', self.stage)

    def lesson_4_generators(self):
        """Generators and Iterators"""
        print("\n" + "="*60)
        print("LESSON 4: Generators")
        print("="*60)

        print("\nGenerators are functions that return an iterator using 'yield'.")
        print("They generate values on-the-fly, saving memory.\n")

        print("Regular function (stores all in memory):")
        print("  def get_numbers():")
        print("      return [1, 2, 3, 4, 5]")

        print("\nGenerator function (generates one at a time):")
        print("  def get_numbers():")
        print("      for i in range(1, 6):")
        print("          yield i")

        print("\nUsing a generator:")
        print("  gen = get_numbers()")
        print("  for num in gen:")
        print("      print(num)  # Prints 1, 2, 3, 4, 5")

        print("\nGenerator expression:")
        print("  squares = (x**2 for x in range(5))")
        print("  # Similar to list comprehension but with ()")

        input("\nPress Enter to continue...")

        # Quiz
        print("\n" + "-"*60)
        print("QUIZ TIME!")
        print("-"*60)

        score = 0

        print("\nQ1: What keyword is used to create a generator?")
        print("  1. return")
        print("  2. yield")
        print("  3. generate")
        print("  4. next")

        answer = input("\nYour answer (1-4): ")
        if answer == "2":
            print("Correct! 'yield' produces values one at a time.")
            score += 25
        else:
            print("Incorrect. The correct answer is 2 (yield).")
            score += 12

        print("\nQ2: What's the main advantage of generators?")
        print("  1. Faster execution")
        print("  2. Memory efficiency")
        print("  3. Easier to write")
        print("  4. Better error handling")

        answer = input("\nYour answer (1-4): ")
        if answer == "2":
            print("Correct! Generators don't store all values in memory at once.")
            score += 25
        else:
            print("Incorrect. The correct answer is 2.")
            score += 12

        print(f"\nLesson Complete! You earned {score} points!")
        self.game_engine.add_points(score, self.stage)
        self.game_engine.mark_lesson_complete('advanced_lesson_4', self.stage)

    def lesson_5_lambda_map_filter(self):
        """Lambda, Map, Filter, and Reduce"""
        print("\n" + "="*60)
        print("LESSON 5: Lambda, Map, and Filter")
        print("="*60)

        print("\nLambda: Anonymous functions")
        print("  square = lambda x: x**2")
        print("  print(square(5))  # Output: 25")

        print("\nMap: Apply function to all items")
        print("  numbers = [1, 2, 3, 4]")
        print("  squared = list(map(lambda x: x**2, numbers))")
        print("  # Result: [1, 4, 9, 16]")

        print("\nFilter: Select items that match condition")
        print("  numbers = [1, 2, 3, 4, 5, 6]")
        print("  evens = list(filter(lambda x: x % 2 == 0, numbers))")
        print("  # Result: [2, 4, 6]")

        print("\nReduce: Accumulate values (from functools)")
        print("  from functools import reduce")
        print("  numbers = [1, 2, 3, 4]")
        print("  product = reduce(lambda x, y: x * y, numbers)")
        print("  # Result: 24 (1*2*3*4)")

        input("\nPress Enter to continue...")

        # Quiz
        print("\n" + "-"*60)
        print("QUIZ TIME!")
        print("-"*60)

        score = 0

        print("\nQ1: What does this lambda do?")
        print("  lambda x, y: x + y")
        print("\n  1. Multiplies x and y")
        print("  2. Adds x and y")
        print("  3. Subtracts y from x")
        print("  4. Returns x")

        answer = input("\nYour answer (1-4): ")
        if answer == "2":
            print("Correct! It's an anonymous function that adds two numbers.")
            score += 25
        else:
            print("Incorrect. The correct answer is 2.")
            score += 12

        print("\nQ2: What does map() return?")
        print("  1. A list")
        print("  2. A dictionary")
        print("  3. An iterator/map object")
        print("  4. A tuple")

        answer = input("\nYour answer (1-4): ")
        if answer == "3":
            print("Correct! map() returns an iterator (convert with list()).")
            score += 25
        else:
            print("Incorrect. The correct answer is 3.")
            score += 12

        print(f"\nLesson Complete! You earned {score} points!")
        self.game_engine.add_points(score, self.stage)
        self.game_engine.mark_lesson_complete('advanced_lesson_5', self.stage)

        # Check for achievement
        completed = len([l for l in self.game_engine.progress['completed_lessons']
                       if l.startswith('advanced_')])
        if completed >= 5:
            if self.game_engine.unlock_achievement("Advanced Python Scholar"):
                print("\nACHIEVEMENT UNLOCKED: Advanced Python Scholar")

    def show_menu(self):
        """Display advanced lessons menu"""
        while True:
            print("\n" + "="*60)
            print("ADVANCED LESSONS")
            print("="*60)
            print("1. Lesson 1: Object-Oriented Programming")
            print("2. Lesson 2: Inheritance")
            print("3. Lesson 3: Decorators")
            print("4. Lesson 4: Generators")
            print("5. Lesson 5: Lambda, Map, and Filter")
            print("0. Back to Main Menu")
            print("="*60)

            choice = input("\nSelect a lesson (0-5): ")

            if choice == "1":
                self.lesson_1_oop()
            elif choice == "2":
                self.lesson_2_inheritance()
            elif choice == "3":
                self.lesson_3_decorators()
            elif choice == "4":
                self.lesson_4_generators()
            elif choice == "5":
                self.lesson_5_lambda_map_filter()
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")
