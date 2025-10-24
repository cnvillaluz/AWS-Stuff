#!/usr/bin/env python3
"""
Kubernetes Learning Application
A comprehensive learning platform for CKA certification preparation
"""

from flask import Flask, render_template, send_from_directory
import os
import markdown
import yaml
from pathlib import Path

app = Flask(__name__)

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Module directories
MODULES_DIR = BASE_DIR / 'modules'
EXERCISES_DIR = BASE_DIR / 'exercises'
RESOURCES_DIR = BASE_DIR / 'resources'

def get_module_content(level, module_file):
    """Read and convert markdown module to HTML"""
    module_path = MODULES_DIR / level / module_file
    if module_path.exists():
        with open(module_path, 'r', encoding='utf-8') as f:
            content = f.read()
            html_content = markdown.markdown(
                content,
                extensions=['fenced_code', 'codehilite', 'tables', 'toc']
            )
            return html_content
    return None

def list_modules():
    """List all available modules organized by level"""
    modules = {
        'basics': [],
        'intermediate': [],
        'advanced': []
    }

    for level in ['01-basics', '02-intermediate', '03-advanced']:
        level_key = level.split('-')[1]
        level_dir = MODULES_DIR / level
        if level_dir.exists():
            for module_file in sorted(level_dir.glob('*.md')):
                module_name = module_file.stem
                # Extract module number and title
                parts = module_name.split('-', 1)
                if len(parts) == 2:
                    title = parts[1].replace('-', ' ').title()
                else:
                    title = module_name.replace('-', ' ').title()

                modules[level_key].append({
                    'file': module_file.name,
                    'title': title,
                    'level': level
                })

    return modules

@app.route('/')
def index():
    """Home page"""
    modules = list_modules()
    return render_template('index.html', modules=modules)

@app.route('/module/<level>/<module_file>')
def view_module(level, module_file):
    """View specific module"""
    content = get_module_content(level, module_file)
    if content:
        # Extract title from filename
        title = module_file.replace('.md', '').replace('-', ' ').title()
        return render_template('module.html', title=title, content=content, level=level)
    return "Module not found", 404

@app.route('/exercises')
def exercises():
    """List exercises"""
    exercise_files = {
        'basics': [],
        'intermediate': [],
        'advanced': []
    }

    for level in ['basics', 'intermediate', 'advanced']:
        exercise_dir = EXERCISES_DIR / level
        if exercise_dir.exists():
            for ex_file in sorted(exercise_dir.glob('*.yaml')):
                exercise_files[level].append({
                    'file': ex_file.name,
                    'title': ex_file.stem.replace('-', ' ').title(),
                    'level': level
                })

    return render_template('exercises.html', exercises=exercise_files)

@app.route('/exercise/<level>/<exercise_file>')
def view_exercise(level, exercise_file):
    """View specific exercise"""
    exercise_path = EXERCISES_DIR / level / exercise_file
    if exercise_path.exists():
        with open(exercise_path, 'r', encoding='utf-8') as f:
            content = f.read()
            html_content = markdown.markdown(
                content,
                extensions=['fenced_code', 'codehilite']
            )
        title = exercise_file.replace('.yaml', '').replace('-', ' ').title()
        return render_template('exercise.html', title=title, content=html_content, raw_content=content)
    return "Exercise not found", 404

@app.route('/cka-guide')
def cka_guide():
    """CKA Exam Preparation Guide"""
    guide_path = RESOURCES_DIR / 'CKA-EXAM-GUIDE.md'
    if guide_path.exists():
        with open(guide_path, 'r', encoding='utf-8') as f:
            content = f.read()
            html_content = markdown.markdown(
                content,
                extensions=['fenced_code', 'codehilite', 'tables', 'toc']
            )
        return render_template('cka-guide.html', content=html_content)
    return "Guide not found", 404

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.route('/static/<path:path>')
def send_static(path):
    """Serve static files"""
    return send_from_directory('static', path)

if __name__ == '__main__':
    # Create necessary directories
    (BASE_DIR / 'web-app' / 'static' / 'css').mkdir(parents=True, exist_ok=True)
    (BASE_DIR / 'web-app' / 'static' / 'js').mkdir(parents=True, exist_ok=True)
    (BASE_DIR / 'web-app' / 'templates').mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("Kubernetes Learning Application")
    print("=" * 60)
    print("\nStarting application...")
    print("Navigate to: http://localhost:5000")
    print("\nAvailable routes:")
    print("  / - Home page with module listing")
    print("  /exercises - Practice exercises")
    print("  /cka-guide - CKA exam preparation guide")
    print("  /about - About this application")
    print("\nPress Ctrl+C to stop")
    print("=" * 60)

    app.run(debug=True, host='0.0.0.0', port=5000)
