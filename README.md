# LeetCode Solutions

My personal repository for LeetCode problem solutions in Java and Python.

## 🚀 Quick Start

### Generate a New Problem

```bash
# Java
python scripts/generate.py -l java -n 1 -t "Two Sum" -s "public int[] twoSum(int[] nums, int target)"

# Python
python scripts/generate.py -l python -n 1 -t "Two Sum" -s "def twoSum(self, nums: List[int], target: int) -> List[int]:"
```

### Test Your Solutions

```bash
# Test specific Java problem
cd java/0001-two-sum
gradle test
gradle --continuous test  # Watch mode

# Test specific Python problem
cd python/problems/0001-two-sum
pytest test_solution.py
find . -name "*.py" | entr -c pytest test_solution.py  # Watch mode

# Test all problems
cd java && find . -name "build.gradle" -execdir gradle test \;
cd python && pytest
```

## 📁 Project Structure

```
leetcode/
├── README.md
├── java/
│   └── 0001-two-sum/           # Problem directory
│       ├── build.gradle        # Isolated Gradle build
│       └── src/
│           ├── main/java/
│           │   └── Solution.java
│           └── test/java/
│               └── SolutionTest.java
├── python/
│   └── problems/
│       └── 0001-two-sum/       # Problem directory
│           ├── solution.py
│           └── test_solution.py
├── docs/                       # GitHub Pages website
│   ├── _config.yml
│   └── index.md               # Progress tracking
└── scripts/
    └── generate.py            # Problem generator
```

## 🧪 Testing Framework

### Java (JUnit 5 + Gradle)
```java
@ParameterizedTest(name = "{0}")
@MethodSource("testCases")
void testSolution(String name, int[] nums, int target, int[] expected) {
    assertArrayEquals(expected, solution.twoSum(nums, target));
}
```

### Python (pytest)
```python
@pytest.mark.parametrize("name,nums,target,expected", [
    ("Example 1", [2, 7, 11, 15], 9, [0, 1]),
])
def test_two_sum(self, name, nums, target, expected):
    assert self.solution.twoSum(nums, target) == expected
```

## 📊 Progress Tracking

Visit the [GitHub Pages site](docs/index.md) to see:
- Total problems solved
- Progress by difficulty and language
- Recent solutions

## 🛠️ Requirements

- **Java**: JDK 11+, Gradle
- **Python**: Python 3.7+, pytest
- **Watch Mode**: entr (install via `brew install entr`)

## 📝 Adding Test Cases

1. Generate the problem structure
2. Edit the test files to add your test cases using the table-driven pattern
3. Implement your solution
4. Run tests to verify

Each problem is isolated with its own dependencies and test environment.