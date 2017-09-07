import org.junit.Test
import org.junit.Assert._

class P01Test {
  @Test def t1(): Unit = {

    val l1 = List(1, 1, 2, 3, 5, 8)
    assertEquals(Some(8), P01.last(l1))
    assertEquals(Some(8), P01.lastRecursive(l1))

    val l2 = List.empty[Int]
    assertEquals(None, P01.last(l2))
    assertEquals(None, P01.lastRecursive(l2))

    val l3 = List(1)
    assertEquals(Some(1), P01.last(l3))
    assertEquals(Some(1), P01.lastRecursive(l3))
  }
}
