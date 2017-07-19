import org.scalatest.FunSuite


class TagTest extends FunSuite {

  test("just tag") {
    assert(Tag("strong", "text").toString === "<strong>text</strong>")
    assert(Tag("small", "text2").toString === "<small>text2</small>")
  }

  test("tag with attributes") {
    assert(Tag("a", "text", Map("href"->"http://facebook.com")).toString === "<a href=\"http://facebook.com\">text</a>")
    val tagWithTwoAttributes = Tag("a", "text", Map("a"->"b", "c"->"d")).toString
    assert(tagWithTwoAttributes.contains("a=\"b\"") && tagWithTwoAttributes.contains("c=\"d\""))
  }
}


class ConceptTest extends FunSuite {

  test("Entity") {
    assert(Entity("aaa").toString == "<strong>aaa</strong>")
  }

  test("Link") {
    assert(Link("aaa").toString == """<a href="aaa">aaa</a>""")
  }

  test("TwitterUserLink") {
    assert(TwitterUserLink("@aaa").toString == """@<a href="http://twitter.com/aaa">aaa</a>""")
  }
}