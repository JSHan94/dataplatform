
from web3 import Web3
from web3.logs import DISCARD
import Info


class Contract:

    # set buyer, uploader 
    def __init__(self,buyer, uploader,buyerKey,uploaderKey):
        #infura_url = "https://ropsten.infura.io/v3/5f5c1d6d2baf41509d5499dac0041758" 
        infura_url = "wss://ropsten.infura.io/ws/v3/5f5c1d6d2baf41509d5499dac0041758" 

        self.contract_add = Info.contract
        self.buyer = Info.buyer
        self.uploader = Info.uploader

        self.buyerPk = Info.buyerKey
        self.uploaderPk = Info.uploaderKey
        self.PK = {buyer : buyerKey, uploader: uploaderKey}

        contract_abi = Info.abi 
        self.w3 = Web3(Web3.WebsocketProvider(infura_url))
        self.contract = self.w3.eth.contract(address=self.contract_add,abi=contract_abi)

    def getBlock(self):
        return self.w3.eth.getBlock('latest')

    # upload file
    def uploadFile(self, category, fileName, dataHash, price):
        tx = self.contract.functions.upload(category, fileName, dataHash, price).buildTransaction({'nonce': self.w3.eth.getTransactionCount(self.uploader), 'gas': 999999}) 
        self.signTx(tx, self.uploaderPk)
        return


    # get coin from Contract
    def getToken(self,token):
        tx = self.contract.functions.giveToken(token).buildTransaction({'nonce': self.w3.eth.getTransactionCount(self.buyer), 'gas': 999999}) 
        self.signTx(tx, self.buyerPk)
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
    
    # sign on Tx
    def signTx(self, tx, privateKey):
        
        signed_tx = self.w3.eth.account.signTransaction(tx, private_key=privateKey)
        send_tx = self.w3.toHex(self.w3.eth.sendRawTransaction(signed_tx.rawTransaction))
        
        return send_tx

    def checkEvent(self, fromBlock, toBlock = 'latest'):
        event_filter = self.w3.eth.filter(({"fromBlock": fromBlock , "toBlock" : toBlock, "address" : self.contract_add}))
        events = self.w3.eth.getFilterLogs(event_filter.filter_id)
        res = []
        for event in events :
            tx_hash = event['transactionHash']
            tx_receipt = self.w3.eth.getTransactionReceipt(tx_hash.hex())
            for eventName in ["GetData","Balance"]: #["Upload","GetData","Buy","Balance"]:
                res.append(self.logCall(eventName,tx_receipt))

        return res
            

    def logCall(self, eventName, tx_receipt):
        rich_logs = ()
        if eventName == "GetData":
            rich_logs = self.contract.events.GetData().processReceipt(tx_receipt,DISCARD)
        elif eventName == "Balance":
            rich_logs = self.contract.events.Balance().processReceipt(tx_receipt,DISCARD)
        
        if rich_logs != ():
            return rich_logs