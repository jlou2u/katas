
// reverse a list

object P05 {

  def reverse[T](ls: List[T]): List[T] = ls match {
    case h :: Nil => List(h)
    case h :: tail => reverse(tail) ++ List(h)
    case Nil => List.empty[T]
  }

}
