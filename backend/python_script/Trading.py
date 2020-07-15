
import sys
import pymysql
import Contract
from loguru import logger
import random, string
import time
import Info
import DB
import Encrypt
from datetime import datetime
def generate_hash():
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    return x

buyer = Info.buyer
uploader = Info.uploader

buyerKey = Info.buyerKey
uploaderKey = Info.uploaderKey

            
if __name__ == "__main__":

    db = DB.DB()
    trading = Contract.Contract(buyer,uploader,buyerKey,uploaderKey)
    curBlock = int(trading.getBlock()["number"])  

    try :
        select = sys.argv[1]

        if select == "getToken":
            user = sys.argv[2]
            token = int(sys.argv[3])
            trading.getToken(token)

            logger.debug({'event':"getToken", 'token': token})

        elif select == "uploadFile":
            category = sys.argv[2]
            filename = sys.argv[3]
            price = int(sys.argv[4])
            datahash = generate_hash()
            
            
            # data encryption with Encrypt.py
            # actually.. it should be in buyFile method..
            time_out = 20 
            while time_out >0 :
                res = db.get_dbhash()             
                if len(res) != 0:
                    db.update_dbhash(datahash)
                    break 
                time.sleep(5)
                time_out -= 5
                db.db_commit()
                print("checking db newdata ... time out : {}, res : {}".format(time_out))
            
            proxy = Encrypt.Encrypt(db)
            proxy.encrypt(uploader,buyer,datahash)
            
            # Smart Contract call
            trading.uploadFile(category,filename,datahash,price)

            
            print({'event': "uploadFile", 'category':category, 'filename' : filename, 'datahash':datahash,'price':price})
        
        elif select == "buyFile":
            datahash = sys.argv[2]

            # buy file : state = 1
            trading.buyFile(datahash)
            print({'event':"buyFile", 'datahash':datahash, 'buyer':buyer})
            
            # decrypt test
            proxy = Encrypt.Encrypt(db)
            if proxy.decrypt(uploader, buyer, datahash):
                # sales confirm : state = 2
                trading.salesConfirm(datahash) 
                print({'event':"salesConfirm", 'datahash':datahash})
            else : 
                print("decryption fail!! revert salesconfirm")

        elif select == "checkEvent":
            blocknum = curBlock - 100 
            logs = trading.checkEvent(blocknum)
            
            for i in range(len(logs)):
                if logs[i] is not None:
                    for j in range(len(logs[i])):
                        # datainfo update
                        log_args = logs[i][j]["args"]
                        if logs[i][j]["event"] == "GetData":
                            logs_time = datetime.fromtimestamp(int(log_args["timestamp"])).strftime('%Y-%m-%d %H:%M:%S')
                            db.insert_datainfo(
                                    log_args["price"],logs_time,log_args["datah"],
                                    log_args["category"],log_args["name"],log_args["buyer"],log_args["owner"],log_args["state"]
                                )
                            logger.debug(logs[i][j])
                        elif logs[i][j]["event"] == "Balance":
                            db.insert_balanceinfo(
                                    log_args["user"],log_args["balance"]
                                )
                            logger.debug(logs[i][j]) 
        
        print("{} finished normally".format(select))

    except Exception as e:
        logger.exception("what?")
        print("error! ",e)
    
    db.db_commit()
    db.db_close()

