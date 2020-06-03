from web3 import Web3
import time
from web3.logs import DISCARD
import sys
from pprint import pprint
import json
#import attributedict

class Contract:

    # set buyer, uploader 
    def __init__(self,buyer, uploader,buyerKey,uploaderKey):
        #infura_url = "https://ropsten.infura.io/v3/5f5c1d6d2baf41509d5499dac0041758" 
        infura_url = "wss://ropsten.infura.io/ws/v3/5f5c1d6d2baf41509d5499dac0041758" 

        self.contract_add = "0xc5bfff9413E0C87a3E31B4AD829E9E205C29f5b2"

        self.buyer = buyer
        self.uploader = uploader

        self.buyerPk = buyerKey
        self.uploaderPk = uploaderKey
        self.PK = {buyer : buyerKey, uploader: uploaderKey}

        contract_abi = '[ { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "_from", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "_balance", "type": "uint256" } ], "name": "Balance", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "address", "name": "_from", "type": "address" }, { "indexed": false, "internalType": "address", "name": "_to", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "_datah", "type": "uint256" } ], "name": "Buy", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "uint256", "name": "timestamp", "type": "uint256" }, { "indexed": false, "internalType": "string", "name": "category", "type": "string" }, { "indexed": false, "internalType": "string", "name": "name", "type": "string" }, { "indexed": false, "internalType": "uint256", "name": "datah", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "price", "type": "uint256" }, { "indexed": false, "internalType": "enum TradingPlatform.STATE", "name": "state", "type": "uint8" }, { "indexed": false, "internalType": "address", "name": "owner", "type": "address" }, { "indexed": false, "internalType": "address", "name": "buyer", "type": "address" } ], "name": "GetData", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": false, "internalType": "string", "name": "_category", "type": "string" }, { "indexed": false, "internalType": "string", "name": "_name", "type": "string" }, { "indexed": false, "internalType": "uint256", "name": "_datah", "type": "uint256" }, { "indexed": false, "internalType": "uint256", "name": "_price", "type": "uint256" } ], "name": "Upload", "type": "event" }, { "inputs": [ { "internalType": "address", "name": "", "type": "address" } ], "name": "balanceOf", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_datah", "type": "uint256" } ], "name": "buy", "outputs": [], "stateMutability": "payable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_datah", "type": "uint256" } ], "name": "getData", "outputs": [ { "internalType": "uint256", "name": "timestamp", "type": "uint256" }, { "internalType": "string", "name": "category", "type": "string" }, { "internalType": "string", "name": "name", "type": "string" }, { "internalType": "uint256", "name": "datah", "type": "uint256" }, { "internalType": "uint256", "name": "price", "type": "uint256" }, { "internalType": "enum TradingPlatform.STATE", "name": "state", "type": "uint8" }, { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "address", "name": "buyer", "type": "address" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_token", "type": "uint256" } ], "name": "giveToken", "outputs": [ { "internalType": "uint256", "name": "balnce", "type": "uint256" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "_datah", "type": "uint256" } ], "name": "salesConfirm", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "_category", "type": "string" }, { "internalType": "string", "name": "_name", "type": "string" }, { "internalType": "uint256", "name": "_datah", "type": "uint256" }, { "internalType": "uint256", "name": "_price", "type": "uint256" } ], "name": "upload", "outputs": [], "stateMutability": "nonpayable", "type": "function" } ]'
        self.w3 = Web3(Web3.WebsocketProvider(infura_url))
        self.contract = self.w3.eth.contract(address=self.contract_add,abi=contract_abi)

    def getBlock(self):
        return self.w3.eth.getBlock('latest')

    # upload file
    def uploadFile(self, category, fileName, dataHash, price):
        tx = self.contract.functions.upload(category, fileName, dataHash, price).buildTransaction({'nonce': self.w3.eth.getTransactionCount(self.uploader), 'gas': 999999}) 
        self.signTx(tx, self.uploaderPk)
        return

    # get balance
    def getBalance(self, user):
        return

    # get coin from Contract
    def getToken(self, user, token):
        tx = self.contract.functions.giveToken(token).buildTransaction({'nonce': self.w3.eth.getTransactionCount(user), 'gas': 999999}) 
        self.signTx(tx, self.PK[user])
        return 

    # buy file with dataHash
    def buyFile(self, dataHash):
        tx = self.contract.functions.buy(dataHash).buildTransaction({'nonce': self.w3.eth.getTransactionCount(self.buyer), 'gas': 999999})
        self.signTx(tx, self.buyerPk)
        return

    # confirm sales
    def salesConfirm(self, dataHash):
        tx = self.contract.functions.salesConfirm(dataHash).buildTransaction({'nonce': self.w3.eth.getTransactionCount(self.uploader), 'gas': 999999})
        self.signTx(tx, self.uploaderPk)

        return
    
    # get File Information
    def getFileInformation(self,dataHash):
        tx = self.contract.functions.getData(dataHash).buildTransaction({'nonce': self.w3.eth.getTransactionCount(self.buyer), 'gas': 999999})
        self.signTx(tx, self.buyerPk)

        return

    # sign on Tx
    def signTx(self, tx, privateKey):
        
        signed_tx = self.w3.eth.account.signTransaction(tx, private_key=privateKey)
        send_tx = self.w3.toHex(self.w3.eth.sendRawTransaction(signed_tx.rawTransaction))
        
        return send_tx

    def checkEvent(self, fromBlock, toBlock = 'latest'):
        event_filter = self.w3.eth.filter(({"fromBlock": fromBlock , "toBlock" : toBlock, "address" : self.contract_add}))
        events = self.w3.eth.getFilterLogs(event_filter.filter_id)
        for event in events :
            tx_hash = event['transactionHash']
            tx_receipt = self.w3.eth.getTransactionReceipt(tx_hash.hex())
            for eventName in ["Upload","GetData","Buy","Balance"]:
                self.logCall(eventName,tx_receipt)
            

    def logCall(self, eventName, tx_receipt):
        rich_logs = ()
        if eventName == "Upload":
            rich_logs = self.contract.events.Upload().processReceipt(tx_receipt,DISCARD)
        elif eventName == "GetData":
            rich_logs = self.contract.events.GetData().processReceipt(tx_receipt,DISCARD)
        elif eventName == "Buy":
            rich_logs = self.contract.events.Buy().processReceipt(tx_receipt,DISCARD)
        elif eventName == "Balance":
            rich_logs = self.contract.events.Balance().processReceipt(tx_receipt,DISCARD)
        
        if rich_logs != ():
            for i in range(len(rich_logs)):
                print(Web3.toJSON(rich_logs[i]))
                

if __name__ == "__main__":

    
    
    buyer = "0x78658C9AaD8523BB283029C43135CF87339ADC21"
    uploader = "0x7161a4eCE5dD841756ee38cBEa7da055F29302c9"

    buyerKey = "2918AC344DCA518C78A9B03403DCD63BADE19C06CEFA4948FE9281495F98A6A9"
    uploaderKey = "14F5CEE6EE9209B4D491F18C8F11F6D1C3579218C849959D50897EF517D9D7BB"

    trading = Contract(buyer,uploader,buyerKey,uploaderKey)

    curBlock = trading.getBlock()["number"]
    

    select = sys.argv[1]

    if select == "getToken":
        user = sys.argv[2]
        token = int(sys.argv[3])
        trading.getToken(user,token)
        print(Web3.toJSON({'user' : user, 'token': token}))

    elif select == "uploadFile":
        category = sys.argv[2]
        filename = sys.argv[3]
        datahash = int(sys.argv[4])
        price = int(sys.argv[5])
        trading.uploadFile(category,filename,datahash,price)
        print(Web3.toJSON({'category':category, 'filename' : filename, 'datahash':datahash,'price':price}))

    elif select == "getFileInformation":
        datahash = int(sys.argv[2])
        trading.getFileInformation(datahash)
        print(Web3.toJSON({'datahash':datahash}))

    elif select == "buyFile":
        datahash = int(sys.argv[2])
        trading.buyFile(datahash)
        print(Web3.toJSON({'datahash':datahash}))

    elif select == "checkEvent":
        blocknum = int(sys.argv[2])
        trading.checkEvent(blocknum)




