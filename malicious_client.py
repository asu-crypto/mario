from seal import *
from util import *
import numpy as np

class MaliciousClient:
    clients = []
    def __init__(self, id, context):
        MaliciousClient.clients.append(self)
        self.client_id = id
        self.context = context
    
    @staticmethod
    def broadcast_pk(encryptor):
        MaliciousClient.encryptor = encryptor

    def encrypt_malicious(self, msgs):
        msgs = msgs.reshape(-1,self.context.degree)
        
        res = []
        full = []
        for i in range(msgs.shape[0]):
            poly = Plaintext(to_string(msgs[i,:]))
            ctx, e1, e2, r1, r2 = MaliciousClient.encryptor.encrypt_detail(poly)
            res.append(ctx)
            full.append((ctx,e1,e2,r1,r2))
        # self.full = full
        proof = self.zkproof(full) # zk proof for the encryption   
        return res, proof
    
    def verify_decryption(self, dec, proof):
        # check the decryption
        pass
    
    def zkproof(self, full_enc_info):
        enc_proof = self.enc_proof(full_enc_info)
        validation_proof = self.input_validation(full_enc_info)
        return enc_proof, validation_proof
    
    def enc_proof(self, full_enc_info):
        # check the encryption
        pass

    def input_validation(self, full_enc_info):
        # check the input
        pass
    

        

if __name__=="__main__":
    client1 = MaliciousClient(1)
    client2 = MaliciousClient(2)
    print(MaliciousClient.clients)