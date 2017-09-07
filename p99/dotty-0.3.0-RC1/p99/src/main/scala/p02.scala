
// find the last but one element of a list

object P02 {

  def penultimate[T](ls: List[T]): Option[T] = ls match {
    case head :: tail :: Nil  => Some(head)
    case head :: tail         => penultimate(tail)
    case _                    => None
  }

}
