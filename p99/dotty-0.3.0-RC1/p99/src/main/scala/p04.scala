
// find the number of elements in a list

object P04 {

  def length[T](ls: List[T]):Int = ls.foldLeft(0)((a, _) => a + 1)

}
