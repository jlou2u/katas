import org.junit.Test
import org.junit.Assert._

class P04Test {
  @Test def t1(): Unit = {
    val ls = List(1, 1, 2, 3, 5, 8)
    assertEquals(6, P04.length(ls))
  }
  @Test def t2(): Unit = {
    val ls = List.empty[String]
    assertEquals(0, P04.length(ls))
  }
  @Test def t3(): Unit = {
    val ls = List('a, 'b, 'c)
    assertEquals(3, P04.length(ls))
  }
}
