import org.junit.Test
import org.junit.Assert._

class P02Test {
  @Test def t1(): Unit = {
    val ls = List(1, 1, 2, 3, 5, 8)
    assertEquals(Some(5), P02.penultimate(ls))
  }
  @Test def t2(): Unit = {
    val ls = List.empty[Int]
    assertEquals(None, P02.penultimate(ls))
  }
  @Test def t3(): Unit = {
    val ls = List(1)
    assertEquals(None, P02.penultimate(ls))
  }
  @Test def t4(): Unit = {
    val ls = List(1, 2)
    assertEquals(Some(1), P02.penultimate(ls))
  }
  @Test def t5(): Unit = {
    val ls = List(1, 2, 3)
    assertEquals(Some(2), P02.penultimate(ls))
  }
}
