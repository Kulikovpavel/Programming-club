abstract class NewsReader {

  def getData: (String, List[ConceptWithPosition])

  def convert: String = {
    val (text, concepts) = getData
    val resultBuilder = new StringBuilder(text)

    for (elem <- concepts.sortBy(_.end).reverse) {
      resultBuilder.replace(elem.start, elem.end, elem.concept.toString)
    }

    resultBuilder.toString
  }
}

object NewsReader {

  def apply(text: String, concepts: List[ConceptWithPosition]): String = {
    object ObjNewsReader extends NewsReader {
      override def getData: (String, List[ConceptWithPosition]) = {
        (text, concepts)
      }
    }

    ObjNewsReader.convert
  }

}

