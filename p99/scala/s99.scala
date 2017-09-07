
import $ivy.`com.lihaoyi::utest:0.4.8`
import utest._
import utest.TestSuite
import utest.framework.Result
import scala.concurrent.ExecutionContext.Implicits.global
import scala.util.{Success,Failure}

object s99 extends TestSuite {
  def last(l: List[_]) = l.lastOption
  val tests = this{
    'p01_test1{
      last(List(1, 1, 2, 3, 5, 8)) == Some(8)
    }
    'p01_test2{
      last(List(1, 1, 2, 3, 5, 5)) == Some(5)
    }
    'p01_test3{
      last(List.empty[Int]) == None
    }
    'p01_test4{
      last(List(20)) == Some(20)
    }
    'p01_test5{
      last(List(-5, 20)) == Some(20)
    }
    'p01_test6{
      last(List(20, -5)) == Some(-5)
    }
    'p02_test1{
      penultimate(List(1, 1, 2, 3, 5, 8)) == 5
    }
  }
}
val printPassing = false
s99.tests.run().map{
  case Result(name, Success(value:Boolean), _) => if (!value || printPassing) println((if (value) "Pass: " else  "Fail: ") + name)
  case Result(name, Success(value), _) if name.startsWith("ammonite.file.s99") => //ignore
  case Result(name, Success(value), _) => println("name is " + name + " value is " + value)
  case Result(name, Failure(value), _) => println("Fail: " + name + " " + value)
}
println("done")
