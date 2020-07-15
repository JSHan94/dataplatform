from web3 import HTTPProvider
from web3 import Web3
import Info

buyer = "0x78658C9AaD8523BB283029C43135CF87339ADC21"
uploader = "0x7161a4eCE5dD841756ee38cBEa7da055F29302c9"

#w3 = Web3(HTTPProvider('http://localhost:22000'))
w3 = Web3(Web3.HTTPProvider('http://localhost:22000'))


#tx = w3.contract.functions.giveToken(10).buildTransaction({'nonce': w3.eth.getTransactionCount(buyer), 'gas': 999999}) 


print(w3.eth.getBlock("latest"))

