import org.junit.Test
import org.junit.Assert._

class P06Test {
  @Test def t1(): Unit = {
    val ls = List(1, 1, 2, 3, 5, 8)
    assertFalse(P06.isPalindrome(ls))
  }
  @Test def t2(): Unit = {
    val ls = List(1, 1, 2, 1, 1)
    assertTrue(P06.isPalindrome(ls))
  }
  @Test def t3(): Unit = {
    assertTrue(P06.isPalindrome(List(1)))
    assertTrue(P06.isPalindrome(List(1, 1)))
    assertTrue(P06.isPalindrome(List(1, 1, 1)))
    assertTrue(P06.isPalindrome(List.empty[Int]))
    assertFalse(P06.isPalindrome(List(1, 2)))
  }
}
