import json
import os
from datetime import datetime

class GameEngine:
    def __init__(self):
        self.progress_file = os.path.join(os.path.dirname(__file__), 'data', 'progress.json')
        self.progress = self.load_progress()

    def load_progress(self):
        """Load user progress from file"""
        if os.path.exists(self.progress_file):
            with open(self.progress_file, 'r') as f:
                return json.load(f)
        return {
            'username': '',
            'total_points': 0,
            'level': 1,
            'current_stage': 'beginner',
            'completed_lessons': [],
            'completed_challenges': [],
            'achievements': [],
            'streak_days': 0,
            'last_played': None,
            'stats': {
                'beginner': {'lessons': 0, 'challenges': 0, 'points': 0},
                'intermediate': {'lessons': 0, 'challenges': 0, 'points': 0},
                'advanced': {'lessons': 0, 'challenges': 0, 'points': 0}
            }
        }

    def save_progress(self):
        """Save user progress to file"""
        os.makedirs(os.path.dirname(self.progress_file), exist_ok=True)
        self.progress['last_played'] = datetime.now().isoformat()
        with open(self.progress_file, 'w') as f:
            json.dump(self.progress, f, indent=4)

    def add_points(self, points, stage):
        """Add points to user's total and stage-specific points"""
        self.progress['total_points'] += points
        self.progress['stats'][stage]['points'] += points
        self.check_level_up()
        self.save_progress()

    def check_level_up(self):
        """Check if user has leveled up"""
        old_level = self.progress['level']
        new_level = (self.progress['total_points'] // 100) + 1

        if new_level > old_level:
            self.progress['level'] = new_level
            return True
        return False

    def mark_lesson_complete(self, lesson_id, stage):
        """Mark a lesson as completed"""
        if lesson_id not in self.progress['completed_lessons']:
            self.progress['completed_lessons'].append(lesson_id)
            self.progress['stats'][stage]['lessons'] += 1
            self.save_progress()

    def mark_challenge_complete(self, challenge_id, stage):
        """Mark a challenge as completed"""
        if challenge_id not in self.progress['completed_challenges']:
            self.progress['completed_challenges'].append(challenge_id)
            self.progress['stats'][stage]['challenges'] += 1
            self.save_progress()

    def unlock_achievement(self, achievement):
        """Unlock an achievement"""
        if achievement not in self.progress['achievements']:
            self.progress['achievements'].append(achievement)
            self.save_progress()
            return True
        return False

    def get_rank(self):
        """Get user's rank based on total points"""
        points = self.progress['total_points']
        if points < 100:
            return "Newbie"
        elif points < 300:
            return "Apprentice"
        elif points < 600:
            return "Intermediate"
        elif points < 1000:
            return "Advanced"
        elif points < 1500:
            return "Expert"
        else:
            return "Python Master"

    def display_stats(self):
        """Display user statistics"""
        print("\n" + "="*60)
        print(f"{'PLAYER STATISTICS':^60}")
        print("="*60)
        print(f"Username: {self.progress['username']}")
        print(f"Level: {self.progress['level']}")
        print(f"Rank: {self.get_rank()}")
        print(f"Total Points: {self.progress['total_points']}")
        print(f"Current Stage: {self.progress['current_stage'].capitalize()}")
        print(f"\nAchievements: {len(self.progress['achievements'])}")
        if self.progress['achievements']:
            for achievement in self.progress['achievements']:
                print(f"  - {achievement}")

        print(f"\n{'Stage Progress':^60}")
        print("-"*60)
        for stage, stats in self.progress['stats'].items():
            print(f"{stage.capitalize()}: Lessons: {stats['lessons']}, "
                  f"Challenges: {stats['challenges']}, Points: {stats['points']}")
        print("="*60 + "\n")
