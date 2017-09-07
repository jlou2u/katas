
// flatten a nested list structure

object P07 {

  def flatten(ls: List[Any]): List[Any] = ls flatMap {
    case sl: List[_] => flatten(sl)
    case e => List(e)
  }

}
