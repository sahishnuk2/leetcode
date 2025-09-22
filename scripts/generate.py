#!/usr/bin/env python3
import argparse
import os
import re
from pathlib import Path

def slugify(text):
    """Convert 'Two Sum' to 'two-sum'"""
    return re.sub(r'[^a-zA-Z0-9\s]', '', text).lower().replace(' ', '-')

def create_java_project(problem_num, problem_name, method_signature):
    """Create Java project structure with Gradle"""
    slug = slugify(problem_name)
    dir_name = f"{problem_num:04d}-{slug}"
    project_path = Path("java") / dir_name

    # Create directories
    (project_path / "src" / "main" / "java").mkdir(parents=True, exist_ok=True)
    (project_path / "src" / "test" / "java").mkdir(parents=True, exist_ok=True)

    # Create build.gradle
    build_gradle = f"""plugins {{
    id 'java'
}}

repositories {{
    mavenCentral()
}}

dependencies {{
    testImplementation 'org.junit.jupiter:junit-jupiter-api:5.9.2'
    testImplementation 'org.junit.jupiter:junit-jupiter-params:5.9.2'
    testRuntimeOnly 'org.junit.jupiter:junit-jupiter-engine:5.9.2'
}}

test {{
    useJUnitPlatform()
}}

java {{
    sourceCompatibility = JavaVersion.VERSION_11
    targetCompatibility = JavaVersion.VERSION_11
}}
"""

    # Create Solution.java
    solution_java = f"""class Solution {{
    {method_signature} {{
        // TODO: Implement solution
        return null;
    }}
}}
"""

    # Create SolutionTest.java
    test_java = f"""import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;
import static org.junit.jupiter.api.Assertions.*;
import java.util.stream.Stream;

class SolutionTest {{
    private Solution solution = new Solution();

    static Stream<Arguments> testCases() {{
        return Stream.of(
            // Add your test cases here
            // Arguments.of("Test name", input1, input2, expected)
        );
    }}

    @ParameterizedTest(name = "{{0}}")
    @MethodSource("testCases")
    void testSolution(String name, Object input1, Object input2, Object expected) {{
        // TODO: Implement test
    }}
}}
"""

    # Write files
    with open(project_path / "build.gradle", "w") as f:
        f.write(build_gradle)
    with open(project_path / "src" / "main" / "java" / "Solution.java", "w") as f:
        f.write(solution_java)
    with open(project_path / "src" / "test" / "java" / "SolutionTest.java", "w") as f:
        f.write(test_java)

    print(f"✅ Created Java project: {project_path}")

def create_python_project(problem_num, problem_name, method_signature):
    """Create Python project structure"""
    slug = slugify(problem_name)
    dir_name = f"{problem_num:04d}-{slug}"
    project_path = Path("python") / "problems" / dir_name

    # Create directory
    project_path.mkdir(parents=True, exist_ok=True)

    # Create solution.py
    solution_py = f"""class Solution:
    {method_signature}
        # TODO: Implement solution
        pass
"""

    # Create test_solution.py
    test_py = f"""import pytest
from solution import Solution

class TestSolution:
    def setup_method(self):
        self.solution = Solution()

    @pytest.mark.parametrize("name,input1,input2,expected", [
        # Add your test cases here
        # ("Test name", input1, input2, expected),
    ])
    def test_solution(self, name, input1, input2, expected):
        # TODO: Implement test
        pass
"""

    # Write files
    with open(project_path / "solution.py", "w") as f:
        f.write(solution_py)
    with open(project_path / "test_solution.py", "w") as f:
        f.write(test_py)

    print(f"✅ Created Python project: {project_path}")

def main():
    parser = argparse.ArgumentParser(description="Generate LeetCode problem structure")
    parser.add_argument("-l", "--language", required=True, choices=["java", "python"],
                       help="Programming language")
    parser.add_argument("-n", "--number", required=True, type=int,
                       help="Problem number")
    parser.add_argument("-t", "--title", required=True,
                       help="Problem title")
    parser.add_argument("-s", "--signature", required=True,
                       help="Method signature")

    args = parser.parse_args()

    # Change to script directory to ensure relative paths work
    os.chdir(Path(__file__).parent.parent)

    if args.language == "java":
        create_java_project(args.number, args.title, args.signature)
    elif args.language == "python":
        create_python_project(args.number, args.title, args.signature)

if __name__ == "__main__":
    main()