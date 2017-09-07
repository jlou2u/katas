
// find the last element of a list

object P01 {

  def last[T](ls: List[T]): Option[T] = {
    if (ls.isEmpty) { None } else { Some(ls.last) }
  }

  def lastRecursive[T](ls: List[T]): Option[T] = ls match {
    case head :: Nil  => Some(head)
    case _ :: tail    => lastRecursive(tail)
    case _            => None
  }

}
