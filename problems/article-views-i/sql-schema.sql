CREATE TABLE IF NOT EXISTS Views (article_id INT, author_id INT, viewer_id INT, view_date DATE);
TRUNCATE TABLE Views;
INSERT INTO Views (article_id, author_id, viewer_id, view_date) VALUES
  ROW(1, 3, 5, '2019-08-01'),
  ROW(1, 3, 6, '2019-08-02'),
  ROW(2, 7, 7, '2019-08-01'),
  ROW(2, 7, 6, '2019-08-02'),
  ROW(4, 7, 1, '2019-07-22'),
  ROW(3, 4, 4, '2019-07-21'),
  ROW(3, 4, 4, '2019-07-21');
