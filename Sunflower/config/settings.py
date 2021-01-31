DATABASE = {
    "mysql":{
       "host": "localhost",
        "port": 3306,
        "username":"root",
        "password":"root",
        "db": "chipscoco"
    },

    "redis":{
        "host": "localhost",
        "port": 6379,
        "db":0
    }
}


class DatabaseType:
    MYSQL = 0
    ORACLE = 1
    REDIS = 2
