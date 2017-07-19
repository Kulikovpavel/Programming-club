abstract class TextNewsReader extends NewsReader {

  def getRawData: (String, List[String])

  def matchConcept(conceptName: String, value: String): Concept = {
    conceptName match {
      case "Entity" => Entity(value)
      case "Link" => Link(value)
      case "TwitterUserLink" => TwitterUserLink(value)
      case unknown => throw new IllegalArgumentException("tag is unknown: " + unknown)
    }
  }

  override def getData: (String, List[ConceptWithPosition]) = {
    val (text, raw_concepts) = getRawData

    val splitted_concepts = raw_concepts.map(_.split(" "))

    val parsed_concepts = for(elem <- splitted_concepts) yield {
      val start = elem(0).toInt
      val end = elem(1).toInt

      val conceptName = elem(2)
      val value = text.substring(start, end)

      val concept = matchConcept(conceptName, value)
      ConceptWithPosition(start, end, concept)
    }
    (text, parsed_concepts)
  }

}