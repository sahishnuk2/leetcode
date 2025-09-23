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
            Arguments.of("Test1", "1.2", "1.10", -1),
            Arguments.of("Test2", "1.01", "1.001", 0),
            Arguments.of("Test3", "1.0", "1.0.0.0", 0)
        );
    }

    @ParameterizedTest(name = "{0}")
    @MethodSource("testCases")
    void testSolution(String name, String input1, String input2, int expected) {
        assertEquals(expected, solution.compareVersion(input1, input2));
    }
}
