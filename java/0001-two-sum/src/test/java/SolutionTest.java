import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;
import static org.junit.jupiter.api.Assertions.*;
import java.util.stream.Stream;

class SolutionTest {
    private Solution solution = new Solution();

    static Stream<Arguments> testCases() {
        return Stream.of(
            // Add your test cases here
            Arguments.of("Test 1", new int[] {2, 7, 11, 15}, 9, new int[] {1, 0}),
            Arguments.of("Test 2", new int[]{3,2,4}, 6, new int[]{2,1})
        );
    }

    @ParameterizedTest(name = "{0}")
    @MethodSource("testCases")
    void testSolution(String name, int[] input1, int input2, int[] expected) {
        int[] result = solution.twoSum(input1, input2);
        assertArrayEquals(expected, result);
    }
}
