### Prerequisites

- [`mysqlsh` — The MySQL Shell](https://dev.mysql.com/doc/mysql-shell/8.0/en/mysqlsh.html), included with MySQL.
- Bash (on Windows, [Git for Windows](https://gitforwindows.org/) provides Git Bash).
- [jq]](https://jqlang.github.io/jq/).

`mysqlsl`, `bash`, and `jq` need to be in the `PATH`.

### How to use

To use the `run.sh` Bash script, just go to the subdirectory of the SQL problem that needs to be tested, and execute:

```sh
bash ../../utils/sql/run.sh {table_1,table_2,...}
```
