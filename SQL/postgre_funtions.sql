CREATE TABLE Conference(
  id SERIAL PRIMARY KEY, name TEXT UNIQUE);
  
CREATE TABLE ConferenceEvent(
  id SERIAL PRIMARY KEY,
  conference_id INT REFERENCES Conference,
  year INT,
  UNIQUE(conference_id, year));

CREATE TABLE Paper(
  id SERIAL PRIMARY KEY,
  event_id INT REFERENCES ConferenceEvent,
  title TEXT,
  accepted BOOLEAN
);

CREATE TABLE Reviewer(
  id SERIAL PRIMARY KEY,
  email TEXT UNIQUE,
  name TEXT
);

CREATE TABLE PaperReviewing(
  paper_id INT REFERENCES Paper,
  reviewer_id INT REFERENCES Reviewer,
  score INT,
  UNIQUE(paper_id, reviewer_id)
);




CREATE OR REPLACE FUNCTION SubmitReview(_paper_id INT, _reviewer_id INT, _score INT)
RETURNS VOID AS $$
DECLARE
score_val numeric;
count_val int;
accepted_val boolean;
update_result int;
BEGIN
IF _score > 7 OR _score < 1 THEN RAISE EXCEPTION 'Message text'; END IF;
UPDATE PaperReviewing SET score=$1 WHERE paper_id=$1 AND reviewer_id=$2 RETURNING 1 into update_result;
IF update_result = 0 THEN RAISE EXCEPTION 'Message text'; END IF;
SELECT AVG(score) into score_val FROM PaperReviewing WHERE paper_id=$1;
SELECT COUNT(*) into count_val FROM PaperReviewing WHERE paper_id=$1;
accepted_val = (count_val >= 3 AND score_val > 4);
UPDATE Paper SET accepted=accepted_val WHERE id=$1;
END;
$$ LANGUAGE plpgsql;
