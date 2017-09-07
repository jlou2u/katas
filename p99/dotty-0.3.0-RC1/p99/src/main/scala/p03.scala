
// find the Kth element of a list

object P03 {

  def nth[T](n:Int, ls: List[T]): Option[T] = {
    if (n >= 0) {
      (n, ls) match {
        case (0, h :: t) => Some(h)
        case (n, _ :: tail) => nth(n - 1, tail)
        case _ => None
      }
    } else { // support pythonic negative indexing
      nth(-1*n-1, ls.reverse)
    }
  }

}
