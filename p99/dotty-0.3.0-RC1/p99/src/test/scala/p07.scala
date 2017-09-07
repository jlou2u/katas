import org.junit.Test
import org.junit.Assert._

class P07Test {
  @Test def t1(): Unit = {
    val ls = List(List(1, 1), 2, List(3, List(5, 8)))
    assertEquals(List(1, 1, 2, 3, 5, 8), P07.flatten(ls))
  }
}
