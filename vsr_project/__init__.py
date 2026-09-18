# VSR Digital Hub uses PyMySQL (a pure-Python MySQL driver) instead of the
# compiled mysqlclient package, so `pip install -r requirements.txt` works
# on any machine without needing MySQL C headers / a compiler.
import pymysql

pymysql.install_as_MySQLdb()
