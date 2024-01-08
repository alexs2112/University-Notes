import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestCodeForTesting {
    @Test
    public void testFibFive() {
        assertEquals(5, CodeForTesting.fibonacci(5));
    }

    @Test
    public void testFibonacci() {
        assertEquals(1, CodeForTesting.fibonacci(1));
        assertEquals(1, CodeForTesting.fibonacci(2));

        assertEquals(0, CodeForTesting.fibonacci(450));
    }
}