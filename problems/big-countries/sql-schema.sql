-- Table should have been named `Countries`...
CREATE TABLE IF NOT EXISTS World (name VARCHAR(255), continent VARCHAR(255), area INT, population INT, gdp BIGINT);
TRUNCATE TABLE World;
INSERT INTO World (name, continent, area, population, gdp) VALUES
  ROW('Afghanistan', 'Asia', 652230, 25500100, 20343000000),
  ROW('Albania', 'Europe', 28748, 2831741, 12960000000),
  ROW('Algeria', 'Africa', 2381741, 37100000, 188681000000),
  ROW('Andorra', 'Europe', 468, 78115, 3712000000),
  ROW('Angola', 'Africa', 1246700, 20609294, 100990000000);
