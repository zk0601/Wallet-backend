from tornado.options import define

# Database
define("mysql_host", default="47.91.252.155:3306")
define("mysql_database", default="wallet_info")
define("mysql_user", default="root")
define("mysql_password", default="123456")
define("pool_size", default=5)
