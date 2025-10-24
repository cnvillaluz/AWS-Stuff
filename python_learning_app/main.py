#!/usr/bin/env python3
"""
Python Learning App - Interactive learning from Beginner to Advanced
"""

import os
import sys

# Add the parent directory to the path to import modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from game_engine import GameEngine
from lessons.beginner import BeginnerLessons
from lessons.intermediate import IntermediateLessons
from lessons.advanced import AdvancedLessons
from challenges.beginner_challenges import BeginnerChallenges
from challenges.intermediate_challenges import IntermediateChallenges
from challenges.advanced_challenges import AdvancedChallenges


class PythonLearningApp:
    def __init__(self):
        self.game_engine = GameEngine()
        self.beginner_lessons = BeginnerLessons(self.game_engine)
        self.intermediate_lessons = IntermediateLessons(self.game_engine)
        self.advanced_lessons = AdvancedLessons(self.game_engine)
        self.beginner_challenges = BeginnerChallenges(self.game_engine)
        self.intermediate_challenges = IntermediateChallenges(self.game_engine)
        self.advanced_challenges = AdvancedChallenges(self.game_engine)

    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('clear' if os.name != 'nt' else 'cls')

    def welcome_screen(self):
        """Display welcome screen and get username"""
        self.clear_screen()
        print("="*60)
        print(r"""
    ____             __    ___
   / __ \ __  __   / /_  / __   ____   ____
  / /_/ // / / /  / __/ / /___ / __ \ / __ \
 / ____// /_/ /  / /_  /  ___// / / // / / /
/_/     \__, /  /\__/ /_/    /_/ /_//_/ /_/
       /____/
        __                                     ___
       / /   ___   ____ _ _____ ____   ___   / _/____
      / /   / _ \ / __ `// ___// __ \ / _ \ / / / __ \
     / /___/  __// /_/ // /   / / / //  __// / / /_/ /
    /_____/\___/ \__,_//_/   /_/ /_/ \___//_/  \____/

        """)
        print("="*60)
        print("Welcome to the Python Learning App!")
        print("Your journey from Beginner to Python Master starts here!")
        print("="*60)

        if not self.game_engine.progress['username']:
            username = input("\nEnter your name to begin: ").strip()
            if username:
                self.game_engine.progress['username'] = username
                self.game_engine.save_progress()
            else:
                self.game_engine.progress['username'] = "Student"

        print(f"\nWelcome back, {self.game_engine.progress['username']}!")
        print(f"Current Level: {self.game_engine.progress['level']}")
        print(f"Total Points: {self.game_engine.progress['total_points']}")
        print(f"Rank: {self.game_engine.get_rank()}")

        input("\nPress Enter to continue...")

    def main_menu(self):
        """Display main menu"""
        while True:
            self.clear_screen()
            print("\n" + "="*60)
            print(f"{'PYTHON LEARNING APP - MAIN MENU':^60}")
            print("="*60)
            print(f"Player: {self.game_engine.progress['username']} | "
                  f"Level: {self.game_engine.progress['level']} | "
                  f"Points: {self.game_engine.progress['total_points']}")
            print(f"Rank: {self.game_engine.get_rank()}")
            print("="*60)
            print("\n1. Beginner Path")
            print("2. Intermediate Path")
            print("3. Advanced Path")
            print("4. View Statistics")
            print("5. How to Use This App")
            print("0. Exit")
            print("="*60)

            choice = input("\nSelect an option (0-5): ")

            if choice == "1":
                self.beginner_menu()
            elif choice == "2":
                self.intermediate_menu()
            elif choice == "3":
                self.advanced_menu()
            elif choice == "4":
                self.game_engine.display_stats()
                input("\nPress Enter to continue...")
            elif choice == "5":
                self.show_help()
            elif choice == "0":
                print("\nThank you for learning Python!")
                print(f"Keep up the great work, {self.game_engine.progress['username']}!")
                print(f"Final Score: {self.game_engine.progress['total_points']} points")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to continue...")

    def beginner_menu(self):
        """Beginner path menu"""
        while True:
            self.clear_screen()
            print("\n" + "="*60)
            print(f"{'BEGINNER PATH':^60}")
            print("="*60)
            print("\n1. Lessons (Learn the Basics)")
            print("2. Challenges (Practice Your Skills)")
            print("0. Back to Main Menu")
            print("="*60)

            choice = input("\nSelect an option (0-2): ")

            if choice == "1":
                self.beginner_lessons.show_menu()
            elif choice == "2":
                self.beginner_challenges.show_menu()
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")

    def intermediate_menu(self):
        """Intermediate path menu"""
        while True:
            self.clear_screen()
            print("\n" + "="*60)
            print(f"{'INTERMEDIATE PATH':^60}")
            print("="*60)
            print("\n1. Lessons (Expand Your Knowledge)")
            print("2. Challenges (Test Your Understanding)")
            print("0. Back to Main Menu")
            print("="*60)

            choice = input("\nSelect an option (0-2): ")

            if choice == "1":
                self.intermediate_lessons.show_menu()
            elif choice == "2":
                self.intermediate_challenges.show_menu()
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")

    def advanced_menu(self):
        """Advanced path menu"""
        while True:
            self.clear_screen()
            print("\n" + "="*60)
            print(f"{'ADVANCED PATH':^60}")
            print("="*60)
            print("\n1. Lessons (Master Advanced Concepts)")
            print("2. Challenges (Prove Your Mastery)")
            print("0. Back to Main Menu")
            print("="*60)

            choice = input("\nSelect an option (0-2): ")

            if choice == "1":
                self.advanced_lessons.show_menu()
            elif choice == "2":
                self.advanced_challenges.show_menu()
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")

    def show_help(self):
        """Show help information"""
        self.clear_screen()
        print("\n" + "="*60)
        print("HOW TO USE THIS APP")
        print("="*60)
        print("\nThis app helps you learn Python progressively:")
        print("\n1. START WITH BEGINNER PATH")
        print("   - Learn fundamental concepts through interactive lessons")
        print("   - Practice with hands-on coding challenges")
        print("   - Earn points and unlock achievements")

        print("\n2. PROGRESS TO INTERMEDIATE PATH")
        print("   - Learn functions, dictionaries, and file operations")
        print("   - Tackle more complex programming challenges")
        print("   - Build real-world programming skills")

        print("\n3. MASTER WITH ADVANCED PATH")
        print("   - Learn OOP, decorators, and functional programming")
        print("   - Solve challenging problems")
        print("   - Become a Python expert")

        print("\n" + "-"*60)
        print("TIPS FOR SUCCESS:")
        print("-"*60)
        print("  - Complete lessons before attempting challenges")
        print("  - Take your time to understand each concept")
        print("  - Practice writing code for challenges")
        print("  - Type 'RUN' after your code to test it")
        print("  - Don't worry about mistakes - you learn from them!")
        print("  - Your progress is automatically saved")

        print("\n" + "-"*60)
        print("SCORING SYSTEM:")
        print("-"*60)
        print("  - Lessons: 20-50 points each")
        print("  - Challenges: 20-100 points each")
        print("  - Level up every 100 points")
        print("  - Unlock achievements for milestones")

        print("\n" + "-"*60)
        print("RANKS:")
        print("-"*60)
        print("  0-99 points: Newbie")
        print("  100-299 points: Apprentice")
        print("  300-599 points: Intermediate")
        print("  600-999 points: Advanced")
        print("  1000-1499 points: Expert")
        print("  1500+ points: Python Master")

        print("\n" + "="*60)
        input("\nPress Enter to return to main menu...")

    def run(self):
        """Main application loop"""
        try:
            self.welcome_screen()
            self.main_menu()
        except KeyboardInterrupt:
            print("\n\nExiting... Your progress has been saved!")
            print(f"See you next time, {self.game_engine.progress['username']}!")
            sys.exit(0)


def main():
    """Entry point"""
    app = PythonLearningApp()
    app.run()


if __name__ == "__main__":
    main()
