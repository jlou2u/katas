
// find out whether a list is a palindrome

object P06 {

  def isPalindrome[T](ls: List[T]) = ls == P05.reverse(ls)

}
