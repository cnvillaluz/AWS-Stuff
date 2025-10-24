# Python Learning App

An interactive, gamified Python learning application that takes you from beginner to advanced level. Learn Python through engaging lessons and hands-on coding challenges while earning points, leveling up, and unlocking achievements!

## Features

- **Progressive Learning Path**: Structured curriculum from Beginner to Advanced
- **Interactive Lessons**: Learn concepts with quizzes and immediate feedback
- **Hands-on Challenges**: Write real Python code and get instant validation
- **Gamification**: Earn points, level up, and unlock achievements
- **Progress Tracking**: Your progress is automatically saved
- **No Dependencies**: Uses only Python standard library
- **Fun & Engaging**: Makes learning Python enjoyable and motivating

## What You'll Learn

### Beginner Level
- Variables and Data Types
- Operators (Arithmetic, Comparison)
- Conditional Statements (if/elif/else)
- Loops (for, while)
- Lists and Basic Operations

### Intermediate Level
- Functions and Parameters
- Dictionaries
- List Comprehensions
- Error Handling (try/except)
- File Operations

### Advanced Level
- Object-Oriented Programming (OOP)
- Inheritance and Polymorphism
- Decorators
- Generators and Iterators
- Lambda, Map, Filter, and Reduce

## Installation

### Prerequisites

- Python 3.6 or higher
- Terminal/Command Prompt access

### Step-by-Step Installation

#### Option 1: Quick Start (Recommended)

**On Linux/Mac:**
```bash
cd python_learning_app
chmod +x setup.sh
./setup.sh
```

**On Windows:**
```cmd
cd python_learning_app
setup.bat
```

#### Option 2: Manual Installation

1. **Check if Python is installed:**
   ```bash
   python3 --version
   ```
   or on Windows:
   ```cmd
   python --version
   ```

   If Python is not installed, download it from [python.org](https://www.python.org/downloads/)

2. **Navigate to the app directory:**
   ```bash
   cd python_learning_app
   ```

3. **Make the main script executable (Linux/Mac only):**
   ```bash
   chmod +x main.py
   ```

4. **You're ready to go!**

## How to Use

### Starting the Application

**On Linux/Mac:**
```bash
python3 main.py
```
or
```bash
./main.py
```

**On Windows:**
```cmd
python main.py
```

### Using the Application

1. **First Time Setup:**
   - Enter your name when prompted
   - Your progress will be automatically saved

2. **Main Menu:**
   - Choose from Beginner, Intermediate, or Advanced paths
   - View your statistics and achievements
   - Access help information

3. **Lessons:**
   - Read the concept explanations
   - Answer quiz questions
   - Earn points for correct answers

4. **Challenges:**
   - Read the challenge description
   - Write your Python code
   - Type `RUN` on a new line when finished
   - Get immediate feedback on your solution

### Example Challenge Workflow

```
Task: Create a variable 'x' with value 10 and print it.

Enter your code (type 'RUN' on a new line when done):
x = 10
print(x)
RUN

Correct! You earned 20 points!
```

## Application Structure

```
python_learning_app/
├── main.py                          # Main application entry point
├── game_engine.py                   # Progress tracking and scoring
├── requirements.txt                 # Dependencies (none needed!)
├── setup.sh                         # Setup script for Linux/Mac
├── setup.bat                        # Setup script for Windows
├── lessons/
│   ├── beginner.py                 # Beginner lessons
│   ├── intermediate.py             # Intermediate lessons
│   └── advanced.py                 # Advanced lessons
├── challenges/
│   ├── beginner_challenges.py      # Beginner coding challenges
│   ├── intermediate_challenges.py  # Intermediate challenges
│   └── advanced_challenges.py      # Advanced challenges
└── data/
    └── progress.json               # Your saved progress (auto-created)
```

## Scoring System

- **Lessons**: Earn 20-50 points per lesson
- **Challenges**: Earn 20-100 points per challenge
- **Level Up**: Every 100 points
- **Achievements**: Unlock special achievements for milestones

### Rank Progression

| Points | Rank |
|--------|------|
| 0-99 | Newbie |
| 100-299 | Apprentice |
| 300-599 | Intermediate |
| 600-999 | Advanced |
| 1000-1499 | Expert |
| 1500+ | Python Master |

## Tips for Success

1. **Start with Beginner Path**: Even if you have some programming experience, starting from the beginning ensures you don't miss fundamental concepts.

2. **Complete Lessons Before Challenges**: Lessons introduce concepts that you'll need for challenges.

3. **Take Your Time**: Understanding is more important than speed.

4. **Experiment**: Try different solutions to challenges. Learning from mistakes is part of the process.

5. **Practice Regularly**: Consistent practice is key to mastering Python.

6. **Don't Skip Levels**: Each level builds on the previous one.

## Achievements

Unlock special achievements by completing milestones:

- Perfect Score - Lesson 1
- Math Wizard
- Logic Master
- Loop Master
- List Expert
- Beginner Challenge Master
- Intermediate Scholar
- Intermediate Code Master
- Advanced Python Scholar
- Python Master - All Advanced Challenges
- Ultimate Python Champion (Complete ALL challenges!)

## Troubleshooting

### "Command not found: python3"
- **Solution**: Install Python from [python.org](https://www.python.org/downloads/)

### "Permission denied" when running setup.sh
- **Solution**: Run `chmod +x setup.sh` first

### "Module not found" errors
- **Solution**: Make sure you're running the app from the `python_learning_app` directory

### Progress not saving
- **Solution**: Ensure the app has write permissions in the directory. The progress file is stored in `data/progress.json`

## System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python Version**: 3.6 or higher
- **Disk Space**: Less than 1 MB
- **RAM**: Minimal (50 MB or less)
- **Internet**: Not required (works completely offline!)

## Frequently Asked Questions

**Q: Do I need to install any packages?**
A: No! This app uses only Python's standard library. No pip install needed.

**Q: Can I skip lessons and go straight to challenges?**
A: Yes, but we recommend completing lessons first to understand the concepts.

**Q: Will my progress be saved?**
A: Yes! Your progress is automatically saved after each lesson and challenge.

**Q: Can multiple people use this on the same computer?**
A: The app stores one profile at a time. To use different profiles, you can rename or backup the `data/progress.json` file.

**Q: I'm stuck on a challenge. Can I get hints?**
A: Each challenge includes task descriptions and sometimes hints. Review the corresponding lesson for more help.

**Q: What if I make a syntax error in a challenge?**
A: The app will show you the error message and still award some points for trying. Use the error message to debug your code.

## Contributing

This is an educational project. Feel free to:
- Extend it with more lessons
- Add new challenges
- Improve the UI
- Add new features like hints system or code examples

## License

This project is provided as-is for educational purposes. Feel free to use, modify, and distribute it.

## Author

Created to make learning Python fun, interactive, and accessible to everyone!

---

**Happy Learning! May you become a Python Master!** 🐍
