import pytest
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
