case class Tag(tag: String, content: String,  attributes: Map[String, String]=Map()) {

  override def toString: String = {
    if (attributes.isEmpty) {
      s"<$tag>$content</$tag>"
    } else {
      val attributesString = attributes.map(x => "%s=\"%s\"".format(x._1, x._2)).mkString(" ")  //  (key, value) to key="value"
      s"<$tag $attributesString>$content</$tag>"
    }
  }
}


sealed trait Concept


case class Entity(text: String) extends Concept{

  override def toString: String = {
    Tag("strong", text).toString()
  }
}


case class Link(link: String) extends Concept{

  override def toString: String = {
    Tag("a", link, Map("href"->link)).toString()
  }
}


case class TwitterUserLink(username: String) extends Concept{

  override def toString: String = {
    val fixed_username = username.stripPrefix("@")
    "@" + Tag("a", fixed_username, Map("href"-> {"http://twitter.com/" + fixed_username})).toString()
  }
}


case class ConceptWithPosition(start: Int, end: Int, concept: Concept)
