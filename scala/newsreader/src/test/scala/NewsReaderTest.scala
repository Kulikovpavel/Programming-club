import org.scalatest.FunSuite


// hack for test output from module 2, dont sure is that bug or feature, "positions 55 through 66 → Twitter username"
// should be 55 through 67
// I can fix it in code of NewsReader, but that dont seems right


class NewsReaderTest extends FunSuite {
  val input_text = "Obama visited Facebook headquarters: http://bit.ly/xyz @elversatile"
  val correct_answer = """<strong>Obama</strong> visited <strong>Facebook</strong> headquarters: <a href="http://bit.ly/xyz">http://bit.ly/xyz</a> @<a href="http://twitter.com/elversatile">elversatile</a>"""

  test("NewsReader") {
    val concepts = List(ConceptWithPosition(14, 22, Entity("Facebook")),
               ConceptWithPosition(0, 5, Entity("Obama")),
               ConceptWithPosition(55, 67, TwitterUserLink("@elversatile")),
               ConceptWithPosition(37, 54, Link("http://bit.ly/xyz")))

    assert(NewsReader(input_text, concepts) == correct_answer)
  }

  test("testConvert") {
    object MockTextNewsReader extends TextNewsReader {
      def getRawData = {
        (input_text,
          List("14 22 Entity", "0 5 Entity", "55 67 TwitterUserLink", "37 54 Link"))
      }
    }

    assert(MockTextNewsReader.convert == correct_answer)
  }

  test("throw tag is unknown") {
    object MockTextNewsReader extends TextNewsReader {
      def getRawData = {
        (input_text,
          List("14 22 SomeWrongTag", "0 5 Entity", "55 67 TwitterUserLink", "37 54 Link"))
      }
    }
    var caught = intercept[IllegalArgumentException] {MockTextNewsReader.convert}

    assert(caught.getMessage.contains("SomeWrongTag"))
  }
}
