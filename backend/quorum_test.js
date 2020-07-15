const Web3 = require("web3")
const quorumjs = require("quorum-js")
const web3 = new Web3("http://localhost:22000")
var contract = require("../private-contracts")

quorumjs.extend(web3)

var code = contract.bytecode

// web3.eth.sendTransaction({
//     data: code,
//     privateFor: ["02a5dd45f93ecc23ce6bef19e80863c48598569dfa7e538111daf94c52e7a31848=",
//             "03f34e627e0aca0ff87cbf5e7f1bb6e1da17d4c817cc38e643dc343c6b224356da="]
//   },
//   function(err, address) {
//     if (!err) {
//       console.log(address); // "0x7f9fade1c0d57a7af66ab4ead7c2eb7b11a91385"
//     }
//   }
// );

var Tx = require('ethereumjs-tx').Transaction
var privateKey = new Buffer('bbe9cedcc6d7cb2e205e01e0e17be2359d0531216c970e7c574aaff7d06d5bd5', 'hex')
var rawTx = {
  nonce: '0x00',
  gasPrice: '0x00', 
  gasLimit: '0x2710',
  to: '0x7161a4eCE5dD841756ee38cBEa7da055F29302c9', 
  from : '0x78658C9AaD8523BB283029C43135CF87339ADC21',
  value: 0, 
  // This data should be the hex value of the hash returned by Quorum's privacy transaction manager after invoking storeraw api
  data: '0x00'
}

var tx =new Tx(rawTx);
tx.sign(privateKey);
var serializedTx = tx.serialize();

web3.eth.sendRawPrivateTransaction('0x' + serializedTx.toString('hex'), {privateFor: ["03f34e627e0aca0ff87cbf5e7f1bb6e1da17d4c817cc38e643dc343c6b224356da="]}, function(err, hash) {
  if (!err)
    console.log(hash); // "0x7f9fade1c0d57a7af66ab4ead79fade1c0d57a7af66ab4ead7c2c2eb7b11a91385"
});

//console.log(contract.bytecode)