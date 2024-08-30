# Delete all tables from the database used for LeetCode:
mysqlsh --user=jpl --database=leetcode --sql --table --file=../../utils/sql/drop-all-tables.sql

# Create the SQL schema for the problem, and display the data (table names separated by comma as only parameter of this script):
mysqlsh --user=jpl --database=leetcode --sql --table --file=sql-schema.sql
mysqlsh --user=jpl --database=leetcode --sql --table --execute="SELECT * FROM "$1";"

# Create the example for the problem, and display the data (these are the data to retrieve):
mysqlsh --user=jpl --database=leetcode --sql --table --file=sql-example1.sql
mysqlsh --user=jpl --database=leetcode --sql --table --execute="SELECT * FROM Example1;"

# Execute the solution, and display the data:
mysqlsh --user=jpl --database=leetcode --sql --table --file=sql-solution.sql
mysqlsh --user=jpl --database=leetcode --sql --table --execute="SELECT * FROM Solution;"

# Compare the solution to the example:
echo The next line will display true if the solution matches the example:
mysqlsh --user=jpl --database=leetcode --sql --json --execute="CHECKSUM TABLE Example1, Solution;"\
 | jq --slurp "last.rows
    | map(select((.Table == \"leetcode.example1\" or .Table ==\"leetcode.solution\")).Checksum)
    | .[0] as \$firstVal | all(.[]; . == \$firstVal)"
