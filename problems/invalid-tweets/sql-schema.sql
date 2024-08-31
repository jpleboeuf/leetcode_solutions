CREATE TABLE IF NOT EXISTS Tweets(tweet_id INT, content VARCHAR(50));
TRUNCATE TABLE Tweets;
INSERT INTO Tweets (tweet_id, content) VALUES
  ROW(1, 'Vote for Biden'),
  ROW(2, 'Let us make America great again!');
