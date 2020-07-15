from umbral.curve import SECP256K1
from umbral import config
config.set_default_curve(SECP256K1)
import random
from umbral import pre,keys, signing,cfrags
import umbral
import pymysql

class Encrypt:
    def __init__(self,db):
        self.db = db
    def generate_key(self,user):
        private_key = keys.UmbralPrivateKey.gen_key()
        public_key = private_key.get_pubkey()
        signing_key = keys.UmbralPrivateKey.gen_key()
        verifying_key = signing_key.get_pubkey()
        
        # covert bytes to hex 
        key = [private_key.to_bytes().hex(), public_key.to_bytes().hex(),
                signing_key.to_bytes().hex(), verifying_key.to_bytes().hex()]

        self.db.insert_keys(user,key)

    def get_key(self,user, keys=[]):
        req_keys = ""
        for key in keys:
            if key == keys[-1]:
                req_keys += key
            else :
                req_keys += key +","
        return self.db.get_key(user,req_keys)
    
    def encrypt(self,delegator,receiver,datahash):
        delegator_keys = [bytes.fromhex(item) for item in self.get_key(delegator,["privatekey","publickey","signkey","verifykey"])[0] ]
        receiver_keys = [bytes.fromhex(item) for item in self.get_key(receiver, ["privatekey","publickey"])[0] ] 

        alices_private_key = keys.UmbralPrivateKey.from_bytes(delegator_keys[0])
        alices_public_key = keys.UmbralPublicKey.from_bytes(delegator_keys[1])
        alices_signing_key = keys.UmbralPrivateKey.from_bytes(delegator_keys[2])
        alices_verifying_key= keys.UmbralPublicKey.from_bytes(delegator_keys[3])
        
        alices_signer = signing.Signer(private_key=alices_signing_key)
        
        bobs_private_key = keys.UmbralPrivateKey.from_bytes(receiver_keys[0])
        bobs_public_key = keys.UmbralPublicKey.from_bytes(receiver_keys[1])

        plaintext = self.db.get_decrypt(datahash)[0][0].encode()
        pre.encrypt(alices_public_key,plaintext)
        
        ciphertext, capsule = pre.encrypt(alices_public_key, plaintext)
        
        kfrags = pre.generate_kfrags(delegating_privkey=alices_private_key,
                             signer=alices_signer,
                             receiving_pubkey=bobs_public_key,
                             threshold=1,
                             N=20)

        capsule.set_correctness_keys(delegating=alices_public_key,
                             receiving=bobs_public_key,
                             verifying=alices_verifying_key)

        
        cfrags = list()           # Bob's cfrag collection

        for kfrag in kfrags[:1]:
            cfrag = pre.reencrypt(kfrag=kfrag, capsule=capsule)
            cfrags.append(cfrag)    # Bob collects a cfrag
       
        # insert encrypt/capsule to db
        self.db.update_encrypt(ciphertext.hex(), capsule.to_bytes().hex(), cfrags[0].to_bytes().hex(), datahash)
        print("encrypt finished well!")
        
        # receiver_keys = keys.UmbralPrivateKey.from_bytes(bytes.fromhex(self.get_key(receiver, ["privatekey"])[0][0]))
        # query = self.db.get_encrypt(datahash)
        # query_ciphertext, query_capsule,query_cfrag = query[0]
        # query_ciphertext = bytes.fromhex(query_ciphertext)
        # query_capsule = pre.Capsule.from_bytes((bytes.fromhex(query_capsule)),receiver_keys.params)

        # query_capsule.set_correctness_keys(delegating=alices_public_key,
        #                      receiving=bobs_public_key,
        #                      verifying=alices_verifying_key)
        # query_cfrag = umbral.cfrags.CapsuleFrag.from_bytes(bytes.fromhex(query_cfrag)) 
        # query_capsule.attach_cfrag(query_cfrag)           
        
        # bobs_cleartext = pre.decrypt(ciphertext=query_ciphertext,
        #                     capsule=query_capsule,
        #                     decrypting_key=receiver_keys)

        return

    def decrypt(self,delegator, receiver,datahash):

        delegator_keys = [bytes.fromhex(item) for item in self.get_key(delegator,["publickey","verifykey"])[0] ]
        receiver_keys = [bytes.fromhex(item) for item in self.get_key(receiver, ["privatekey","publickey"])[0] ] 

        delegator_public_key =  keys.UmbralPublicKey.from_bytes(delegator_keys[0])
        delegator_verifying_key =  keys.UmbralPublicKey.from_bytes(delegator_keys[1])

        receiver_private_key = keys.UmbralPrivateKey.from_bytes(receiver_keys[0])
        receiver_public_key = keys.UmbralPublicKey.from_bytes(receiver_keys[1])
        
        query = self.db.get_encrypt(datahash)
        ciphertext, capsule, cfrag, decrypt = query[0]
        ciphertext = bytes.fromhex(ciphertext)
        capsule = pre.Capsule.from_bytes((bytes.fromhex(capsule)),receiver_public_key.params)
        
        capsule.set_correctness_keys(delegating=delegator_public_key,
                             receiving=receiver_public_key,
                             verifying=delegator_verifying_key)

        # Bob activates and opens the capsule
        cfrag = umbral.cfrags.CapsuleFrag.from_bytes(bytes.fromhex(cfrag)) 
        capsule.attach_cfrag(cfrag) 

        cleartext = pre.decrypt(ciphertext=ciphertext,
                            capsule=capsule,
                            decrypting_key=receiver_private_key)
        
        

        if cleartext.decode("utf-8") == decrypt :
            print("success decryption!")
            return True
        else :
            print("decrypt text : ", cleartext.decode("utf-8"))
            print("original text : ", decrypt)
            return False
