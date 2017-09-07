import org.junit.Test
import org.junit.Assert._

class P05Test {
  @Test def t1(): Unit = {
    val ls = List(1, 1, 2, 3, 5, 8)
    assertEquals(List(8, 5, 3, 2, 1, 1), P05.reverse(ls))
  }
  @Test def t2(): Unit = {
    val ls = List.empty[String]
    assertEquals(List.empty[String], P05.reverse(ls))
  }
  @Test def t3(): Unit = {
    val ls = List('a)
    assertEquals(List('a), P05.reverse(ls))
  }
  @Test def t4(): Unit = {
    val ls = List('a, 'b)
    assertEquals(List('b, 'a), P05.reverse(ls))
  }
}
