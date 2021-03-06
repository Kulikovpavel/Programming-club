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

DROP TABLE IF EXISTS PaperReviewing;
DROP TABLE IF EXISTS Reviewer;
DROP TABLE IF EXISTS Paper;
DROP TABLE IF EXISTS ConferenceEvent;
DROP TABLE IF EXISTS Conference;

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

INSERT INTO Conference(name) VALUES ('SIGMOD'), ('VLDB');
INSERT INTO ConferenceEvent(conference_id, year) VALUES (1, 2015), (1, 2016), (2, 2016);
INSERT INTO Reviewer(email, name) VALUES
    ('jennifer@stanford.edu', 'Jennifer Widom'),
    ('donald@ethz.ch', 'Donald Kossmann'),
    ('jeffrey@stanford.edu', 'Jeffrey Ullman'),
    ('jeff@google.com', 'Jeffrey Dean'),
    ('michael@mit.edu', 'Michael Stonebraker');

INSERT INTO Paper(event_id, title) VALUES
    (1, 'Paper1'),
    (2, 'Paper2'),
    (2, 'Paper3'),
    (3, 'Paper4');

INSERT INTO PaperReviewing(paper_id, reviewer_id) VALUES
    (1, 1), (1, 4), (1, 5),
    (2, 1), (2, 2), (2, 4),
    (3, 3), (3, 4), (3, 5),
    (4, 2), (4, 3), (4, 4);
    
    
CREATE OR REPLACE FUNCTION SubmitReview(_paper_id INT, _reviewer_id INT, _score INT)
RETURNS VOID AS $$
DECLARE
score_val numeric;
count_val int;
accepted_val boolean;
BEGIN

IF _score > 7 OR _score < 1 THEN RAISE EXCEPTION 'Message text'; END IF;

UPDATE PaperReviewing SET score=$3 WHERE paper_id=$1 AND reviewer_id=$2;
IF NOT FOUND THEN RAISE EXCEPTION 'Message text'; END IF;

SELECT AVG(score) into score_val FROM PaperReviewing WHERE paper_id=$1;
SELECT COUNT(*) into count_val FROM PaperReviewing WHERE paper_id=$1 AND score IS NOT NULL;

IF count_val >= 3 THEN
  accepted_val = (score_val > 4);
  UPDATE Paper SET accepted=accepted_val WHERE id=$1;
END IF;

END;
$$ LANGUAGE plpgsql;
