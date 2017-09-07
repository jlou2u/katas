import org.junit.Test
import org.junit.Assert._

class P03Test {
  @Test def t1(): Unit = {
    val ls = List(1, 1, 2, 3, 5, 8)
    assertEquals(Some(2), P03.nth(2, ls))
  }
  @Test def t2(): Unit = {
    val ls = List.empty[Int]
    assertEquals(None, P03.nth(2, ls))
  }
  @Test def t3(): Unit = {
    val ls = List(1)
    assertEquals(Some(1), P03.nth(0, ls))
    assertEquals(None, P03.nth(1, ls))
    assertEquals(None, P03.nth(2, ls))
    assertEquals(Some(1), P03.nth(-1, ls))
    assertEquals(None, P03.nth(-2, ls))
  }
  @Test def t4(): Unit = {
    val ls = List(1, 2)
    assertEquals(Some(1), P03.nth(0, ls))
    assertEquals(Some(2), P03.nth(1, ls))
    assertEquals(None, P03.nth(2, ls))
    assertEquals(Some(2), P03.nth(-1, ls))
    assertEquals(Some(1), P03.nth(-2, ls))
    assertEquals(None, P03.nth(-3, ls))
  }
  @Test def t5(): Unit = {
    val ls = List(1, 2, 3)
    assertEquals(Some(1), P03.nth(0, ls))
    assertEquals(Some(2), P03.nth(1, ls))
    assertEquals(Some(3), P03.nth(2, ls))
    assertEquals(None, P03.nth(3, ls))
    assertEquals(Some(3), P03.nth(-1, ls))
    assertEquals(Some(2), P03.nth(-2, ls))
    assertEquals(Some(1), P03.nth(-3, ls))
  }
}
