#!/usr/bin/env python3
"""
Script to automatically update the docs/index.md file with current progress.
Scans Java and Python directories for completed problems and updates statistics.
Only includes problems where all tests pass.
"""

import os
import re
import subprocess
from pathlib import Path
from datetime import datetime
from collections import defaultdict


def run_java_tests(problem_dir):
    """Run Java tests for a problem and return if they pass."""
    try:
        # Change to problem directory and run gradle test
        result = subprocess.run(
            ['gradle', 'test'],
            cwd=problem_dir,
            capture_output=True,
            text=True,
            timeout=60
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError):
        return False


def run_python_tests(problem_dir):
    """Run Python tests for a problem and return if they pass."""
    try:
        # Look for test file
        test_file = problem_dir / 'test_solution.py'
        if not test_file.exists():
            return False

        # Run pytest on the test file
        result = subprocess.run(
            ['python3', '-m', 'pytest', str(test_file), '-v'],
            cwd=problem_dir,
            capture_output=True,
            text=True,
            timeout=60
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError):
        return False


def get_problem_info(problem_dir):
    """Extract problem information from directory name and solution files."""
    dir_name = problem_dir.name

    # Extract problem number and title from directory name (e.g., "0001-two-sum")
    match = re.match(r'(\d+)-(.+)', dir_name)
    if not match:
        return None

    number = int(match.group(1))
    title = match.group(2).replace('-', ' ').title()

    # Check for solution files and run tests
    has_java = False
    has_python = False

    if problem_dir.parent.name == 'java' or 'java' in str(problem_dir):
        java_solution = problem_dir / 'src' / 'main' / 'java' / 'Solution.java'
        if java_solution.exists():
            print(f"  🧪 Testing Java solution for {number:04d}...")
            has_java = run_java_tests(problem_dir)
            if has_java:
                print(f"  ✅ Java tests passed for {number:04d}")
            else:
                print(f"  ❌ Java tests failed for {number:04d}")

    if 'python' in str(problem_dir):
        python_solution = problem_dir / 'solution.py'
        if python_solution.exists():
            print(f"  🧪 Testing Python solution for {number:04d}...")
            has_python = run_python_tests(problem_dir)
            if has_python:
                print(f"  ✅ Python tests passed for {number:04d}")
            else:
                print(f"  ❌ Python tests failed for {number:04d}")

    # Only include if at least one language passes tests
    if not has_java and not has_python:
        return None

    return {
        'number': number,
        'title': title,
        'has_java': has_java,
        'has_python': has_python
    }




def scan_problems():
    """Scan both Java and Python directories for solved problems."""
    problems = {}
    root_dir = Path('.')

    # Scan Java problems
    java_dir = root_dir / 'java'
    if java_dir.exists():
        for problem_dir in java_dir.iterdir():
            if problem_dir.is_dir() and not problem_dir.name.startswith('.'):
                info = get_problem_info(problem_dir)
                if info:
                    if info['number'] not in problems:
                        problems[info['number']] = info
                    else:
                        problems[info['number']]['has_java'] = info['has_java']

    # Scan Python problems
    python_problems_dir = root_dir / 'python' / 'problems'
    if python_problems_dir.exists():
        for problem_dir in python_problems_dir.iterdir():
            if problem_dir.is_dir() and not problem_dir.name.startswith('.'):
                info = get_problem_info(problem_dir)
                if info:
                    if info['number'] not in problems:
                        problems[info['number']] = info
                    else:
                        problems[info['number']]['has_python'] = info['has_python']

    return list(problems.values())


def generate_index_content(problems):
    """Generate the updated index.md content."""
    # Calculate statistics
    total_problems = len(problems)
    language_counts = {'Java': 0, 'Python': 0}

    for problem in problems:
        if problem['has_java']:
            language_counts['Java'] += 1
        if problem['has_python']:
            language_counts['Python'] += 1

    # Sort problems by number (most recent first for display)
    problems_sorted = sorted(problems, key=lambda x: x['number'], reverse=True)

    # Generate content
    content = f"""# LeetCode Solutions

## 📊 Progress Overview

- **Total Problems Solved**: {total_problems}
- **Last Updated**: {datetime.now().strftime('%Y-%m-%d')}

## 📈 Statistics

### By Language
- **Java**: {language_counts['Java']} problems
- **Python**: {language_counts['Python']} problems

## 📝 Recent Solutions

| # | Problem | Java | Python |
|---|---------|------|--------|"""

    if not problems:
        content += "\n| - | No problems solved yet | - | - |"
    else:
        for problem in problems_sorted[:10]:  # Show latest 10 problems
            java_status = "✅" if problem['has_java'] else "❌"
            python_status = "✅" if problem['has_python'] else "❌"
            content += f"\n| {problem['number']:04d} | {problem['title']} | {java_status} | {python_status} |"

        if len(problems_sorted) > 10:
            content += f"\n| ... | {len(problems_sorted) - 10} more problems | ... | ... |"

    content += """

## 🎯 Goals

- [ ] Solve 100 problems
- [ ] Master all array problems
- [ ] Master all tree problems
- [ ] Master all dynamic programming problems
- [ ] Master all graph problems

---

*This page is automatically updated when new problems are added.*"""

    return content


def main():
    """Main function to update the index file."""
    print("🔍 Scanning for solved problems...")

    problems = scan_problems()
    print(f"📊 Found {len(problems)} solved problems")

    if problems:
        for problem in sorted(problems, key=lambda x: x['number']):
            languages = []
            if problem['has_java']:
                languages.append('Java')
            if problem['has_python']:
                languages.append('Python')
            print(f"  - {problem['number']:04d}: {problem['title']} ({', '.join(languages)})")

    print("📝 Generating updated index...")
    content = generate_index_content(problems)

    # Write to index file
    index_file = Path('docs') / 'index.md'
    index_file.parent.mkdir(exist_ok=True)

    with open(index_file, 'w') as f:
        f.write(content)

    print(f"✅ Updated {index_file}")


if __name__ == '__main__':
    main()