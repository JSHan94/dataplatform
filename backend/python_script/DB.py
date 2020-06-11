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
        except Exception:
            logger.exception("what?")

    def db_close(self):
        self.db.close()
        return
    
    def db_commit(self):
        self.db.commit()
        return

    # Encrypt.py
    def get_encrypt(self,datahash):
        sql =(
            """
            select encrypt,capsule,cfrag,decrypt from db
            where datahash = "%s"
            """%(
                datahash
            )
        )
        try :
            res = self.send_sql(sql)
            return res
        except Exception:
            logger.exception("get_encrypt")

    def update_encrypt(self,encrypt,capsule,cfrag,datahash):
        sql = (
            """
            UPDATE db 
            SET encrypt = "%s", capsule ="%s", cfrag = "%s" 
            WHERE datahash = "%s"
            """
            %(
                encrypt,
                capsule,
                cfrag,
                datahash
            )
        )
        try :
            res = self.send_sql(sql)
            return res
        except Exception:
            logger.exception("insert_encrypt")

    def insert_keys(self, user, keys):
        sql = (
            """
            INSERT INTO keyinfo (user,privatekey,publickey,signkey,verifykey) 
            VALUES ("%s","%s","%s","%s","%s") 
            """
            %(
                user,
                keys[0],
                keys[1],
                keys[2],
                keys[3]
            )
        )

        try :
            res = self.send_sql(sql)
            return res
        except Exception:
            logger.exception("insert_keys")

    def get_key(self, user, req_keys):
        sql = (
            """
            select %s from keyinfo where user = "%s"
            """%(
                req_keys,
                user
            )
        )
        try :
            res = self.send_sql(sql)
            return res
        except Exception:
            logger.exception("get_key")

    def get_decrypt(self,datahash):
        sql  =(
            """
            select decrypt from db where datahash = "%s"
            """%(
                datahash
            )
        )
        try :
            res = self.send_sql(sql)
            return res
        except Exception:
            logger.exception("get_decrypt")


    # Trading.py
    def get_dbhash(self):
        sql = (
            """
            select * from db
            """
            # select * from db where datahash is Null limit 1
        )
        try :
            print("get_dbhash called!")
            res = self.send_sql(sql)
            return res
        except Exception as e :
            logger.exception("get_dbhash")
    
    def update_dbhash(self,datahash):
        sql = (
            """
            update db set datahash = "%s"
            where datahash is Null limit 1
            """%(
                datahash
            )
        )
        try :
            res = self.send_sql(sql)
            return res
        except Exception as e :
            logger.exception("update_dbhash")
    
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
            VALUES(%s, "%s", "%s", "%s", "%s", "%s", "%s", %s)
            ON DUPLICATE KEY UPDATE    
            price = %s, timestamp ="%s", category = "%s",name = "%s", buyer = "%s", owner = "%s", state = %s
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