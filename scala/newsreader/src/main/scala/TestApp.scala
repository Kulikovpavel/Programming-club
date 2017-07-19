object StdinNewsReader extends TextNewsReader{

  def getRawData: (String, List[String]) = {
    val text = scala.io.StdIn.readLine()
    val concepts = new scala.collection.mutable.ListBuffer[String]()
    var line = ""
    while ({line = scala.io.StdIn.readLine(); line != null && line != ""}) {
      concepts += line
    }
    (text, concepts.toList)
  }
}


object TestApp{

  def main(args: Array[String]): Unit = {
    val res = StdinNewsReader.convert
    println(res)
  }
}