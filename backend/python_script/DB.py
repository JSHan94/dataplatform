import pymysql
from loguru import logger

class DB:
    def __init__(self):
        self.db = pymysql.connect(
                host="141.223.82.142",
                port=3306,
                user="root",
                passwd="pass",
                db="keeper",
                charset="utf8",
            )

    def send_sql(self, sql):
        try:
            cursor = self.db.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except pymysql.err.IntegrityError:
            print("IntegrityError")

    
    def db_close(self):
        self.db.close()
        return
    
    def db_commit(self):
        self.db.commit()
        return

    def get_datainfo(self):
        sql = (
            """
            select *
            from datainfo
            """
        )
        try :
            res = self.send_sql(sql)
            return res
        except Exception as e :
            logger.exception("get_datainfo")

    def update_hash(self,datahash,updated):
        sql = (
            """
            update hashinfo
            set updated = %s
            where datahash = "%s"
            """%(
                str(updated),
                datahash
            )
        )
        try :
            res = self.send_sql(sql)
            return res
        except Exception as e :
            logger.exception("update_hash")

    def get_hashinfo(self):
        sql = (
            """
            select *
            from hashinfo
            where updated = 0
            """
        )
        try :
            res = self.send_sql(sql)
            return res
        except Exception as e :
            logger.exception("get_hashinfo")

    def insert_balanceinfo(self, _user, _balance):
        sql =(
            """
            INSERT INTO balanceinfo (user,balance)
            VALUES ("%s",%s)
            ON DUPLICATE KEY UPDATE
            balance = %s 
            """%(
                _user,_balance,
                _balance
            )
        )
        try :
            res = self.send_sql(sql)
        except Exception:
            logger.exception("insert_balanceinfo")

    def insert_datainfo(self, _price, _timestamp, _datahash, _category, _name, _buyer, _owner, _state):
        sql = (
            """
            INSERT INTO datainfo (price, timestamp, datahash, category,name,buyer,owner,state) 
            VALUES(%s, %s, "%s", "%s", "%s", "%s", "%s", %s)
            ON DUPLICATE KEY UPDATE    
            price = %s, timestamp =%s, category = "%s",name = "%s", buyer = "%s", owner = "%s", state = %s
            """
            %(
                _price, _timestamp, _datahash, _category, _name, _buyer, _owner, _state,
                _price, _timestamp, _category, _name, _buyer, _owner, _state
            )
        )
        
        try :
            res = self.send_sql(sql)
        except Exception:
            logger.exception("insert_datainfo")


    def insert_datahash(self,datahash,updated):
        sql = (
            """
            INSERT IGNORE INTO hashinfo(datahash,updated) VALUES("%s",%s)
            """%(
                datahash,updated
            )
        )

        try :
            res = self.send_sql(sql)
        except Exception :
            logger.exception("what")