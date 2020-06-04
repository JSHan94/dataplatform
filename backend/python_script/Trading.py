
import sys
import pymysql
import Contract
from loguru import logger
import random, string
import time
import Info
import DB

def generate_hash():
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    return x

buyer = Info.buyer
uploader = Info.buyer

buyerKey = Info.buyerKey
uploaderKey = Info.uploaderKey

            
if __name__ == "__main__":

    db = DB.DB()
    trading = Contract.Contract(buyer,uploader,buyerKey,uploaderKey)

    curBlock = int(trading.getBlock()["number"])    
    try :     
        select = sys.argv[1]

        if select == "getToken":
            token = int(sys.argv[2])
            trading.getToken(token)

            logger.debug({'event':"getToken", 'token': token})

        elif select == "uploadFile":
            category = sys.argv[2]
            filename = sys.argv[3]
            price = int(sys.argv[4])
            datahash = generate_hash()
            
            trading.uploadFile(category,filename,datahash,price)
            db.insert_datahash(datahash,0)
            logger.debug({'event': "uploadFile", 'category':category, 'filename' : filename, 'datahash':datahash,'price':price})

    
        elif select == "getFileInformation":
            datahash_list = db.get_hashinfo()
            for datahash in datahash_list:
                while True:
                    try : 
                        trading.getFileInformation(datahash[0])
                        break
                    except Exception :
                        #logger.exception("what")
                        print("pending transaction waiting.. {}".format(datahash[0]))
                        time.sleep(30)
                
                db.update_hash(datahash[0],1)
                logger.debug("datahash : {} getFileInformation called!".format(datahash[0]))
            logger.debug({'event':"getFileInformation"})
            
        elif select == "salesConfirm":
            datahash = sys.argv[2]
            trading.salesConfirm(datahash) 
            
            db.update_hash(datahash,0)
            logger.debug({'event':"salesConfirm", 'category':category, 'filename' : filename, 'datahash':datahash,'price':price})

        elif select == "buyFile":
            datahash = sys.argv[2]
            trading.buyFile(datahash)
   
            db.update_hash(datahash,0)
            logger.debug({'event':"buyFile", 'datahash':datahash, 'buyer':buyer})

        elif select == "checkEvent":
            blocknum = curBlock - 100 #int(sys.argv[2])
            logs = trading.checkEvent(blocknum)
            
            for i in range(len(logs)):
                if logs[i] is not None:
                    for j in range(len(logs[i])):
                        # datainfo update
                        log_args = logs[i][j]["args"]
                        if logs[i][j]["event"] == "GetData":
                            db.insert_datainfo(
                                    log_args["price"],log_args["timestamp"],log_args["datah"],
                                    log_args["category"],log_args["name"],log_args["buyer"],log_args["owner"],log_args["state"]
                                )
                            print(logs[i][j])
                        elif logs[i][j]["event"] == "Balance":
                            db.insert_balanceinfo(
                                    log_args["user"],log_args["balance"]
                                )
                            print(logs[i][j]) 

    except Exception:
        logger.exception("main problem") 
    
    db.db_commit()
    db.db_close()


