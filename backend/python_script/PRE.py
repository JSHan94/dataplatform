




from umbral.curve import SECP256K1
from umbral import config
config.set_default_curve(SECP256K1)
import random
from umbral import pre,keys, signing,params, curve
import pymysql


# Generate Umbral keys for Alice.
alices_private_key = keys.UmbralPrivateKey.gen_key()
alices_public_key = alices_private_key.get_pubkey()

alices_signing_key = keys.UmbralPrivateKey.gen_key()
alices_verifying_key = alices_signing_key.get_pubkey()
alices_signer = signing.Signer(private_key=alices_signing_key)

# Generate Umbral keys for Bob.
bobs_private_key = keys.UmbralPrivateKey.gen_key()
bobs_public_key = bobs_private_key.get_pubkey()
bobs_signing_key = keys.UmbralPrivateKey.gen_key()
bobs_verifying_key = bobs_signing_key.get_pubkey()

print(alices_private_key.to_bytes().hex())
print(alices_public_key.to_bytes().hex())
print(alices_signing_key.to_bytes().hex())
print(alices_verifying_key.to_bytes().hex())

print(bobs_private_key.to_bytes().hex())
print(bobs_public_key.to_bytes().hex())
print(bobs_signing_key.to_bytes().hex())
print(bobs_verifying_key.to_bytes().hex())

# # print(alices_private_key.to_bytes().hex())
# # print(type(alices_private_key.to_bytes()))
# # print(str(alices_private_key.to_bytes(),'utf-16'))

# # print(len(alices_private_key.to_bytes()))
# # print(keys.UmbralPrivateKey.from_bytes(alices_private_key.to_bytes()))
# # print(alices_public_key.to_bytes())
# # print(type(alices_public_key.to_bytes()))
# # print(len(alices_public_key.to_bytes()))
# # print(alices_signing_key)
# # print(alices_verifying_key)
# # print(bobs_private_key)
# # print(bobs_public_key)


# # Encrypt data with Alice's public key.
# plaintext = (b'''
#               One of the key policies of Wikipedia is that all article content has to be verifiable. This means that reliable sources must be able to support the material. All quotations, any material whose verifiability has been challenged or is likely to be challenged, and contentious material (whether negative, positive, or neutral) about living persons must include an inline citation to a source that directly supports the material. This also means that Wikipedia is not the place for original work, archival findings that have not been published, or evidence from any source that has not been published.
#               If you are adding new content, it is your responsibility to add sourcing information along with it. Material provided without a source is more likely to be removed from an article. Sometimes such material will be tagged first with a "citation needed" template to give editors time to find and add sources before it is removed, but sometimes editors will simply remove it because they question its veracity.
#               This tutorial will show you how to add inline citations to articles, and also briefly explain what Wikipedia considers to be a reliable source.
#             ''')

# ciphertext, capsule = pre.encrypt(alices_public_key, plaintext)

# # # Decrypt data with Alice's private key.
# # cleartext = pre.decrypt(ciphertext=ciphertext,
# #                         capsule=capsule,
# #                         decrypting_key=alices_private_key)

# # Alice generates "M of N" re-encryption key fragments (or "KFrags") for Bob.
# # In this example, 10 out of 20.
# kfrags = pre.generate_kfrags(delegating_privkey=alices_private_key,
#                              signer=alices_signer,
#                              receiving_pubkey=bobs_public_key,
#                              threshold=10,
#                              N=20)

# # Several Ursulas perform re-encryption, and Bob collects the resulting `cfrags`.
# # He must gather at least `threshold` `cfrags` in order to activate the capsule.
# capsule.set_correctness_keys(delegating=alices_public_key,
#                              receiving=bobs_public_key,
#                              verifying=alices_verifying_key)

# cfrags = list()           # Bob's cfrag collection

# # for kfrag in kfrags[:10]:
# kfrag_sam = random.sample(kfrags,10) 
# for kfrag in kfrag_sam:
#   cfrag = pre.reencrypt(kfrag=kfrag, capsule=capsule)
#   cfrags.append(cfrag)    # Bob collects a cfrag


# # Bob activates and opens the capsule
# for cfrag in cfrags:
#   capsule.attach_cfrag(cfrag)

# # print(bytes.fromhex(capsule.hex()))
# print(pre.Capsule.from_bytes((bytes.fromhex(capsule.to_bytes().hex())),bobs_private_key.params))
# assert pre.Capsule.from_bytes((bytes.fromhex(capsule.to_bytes().hex())),bobs_private_key.params) == capsule
# # print(type(capsule))
# print(type(ciphertext))
# # #print(type(ciphertext))
# # print(ciphertext.hex())
# bob_cleartext = pre.decrypt(ciphertext=ciphertext,
#                             capsule=capsule,
#                             decrypting_key=bobs_private_key)


# #print(bob_cleartext)
# #bob_cleartext = bob_cleartext.decode('ascii')
# assert bob_cleartext == plaintext


