from server import Server
from util import *
from seal import *
import numpy as np

class MaliciousServer(Server):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._malicious = True
        self.evaluator = Evaluator(self.context.seal_context)
    
    def verify_enc_proof(self, enc_proof):
        # check the encryption proof of clients
        pass

    def verify_input_validation(self, validation_proof):
        # check the input validation proof of clients
        pass

    def verify_partial_decryption(self, partial_decryption_proof):
        # check the partial decryption proof of clients
        pass

    def __partial_decrypt_malicious(self,ctx):
        # decrypt the ciphertext, giving a proof of partial decryption circuit
        pass

    def decrypt_malicious(self,ctx):
        # decrypt the ciphertext:
        #   - choose the set of servers to jointly decrypt the ciphertext
        #   - verifying the partial decryption proof
        #   - give proof of final decryption
        pass

    def aggregate(self, ctxs, proofs):
        # aggregate the ciphertexts
        # store the aggregated ciphertext in self.ctx_total
        # also return the aggregated ciphertext in case other parties need it
        self.all_ciphertexts = []
        for ctx,proof in zip(ctxs, proofs):
            enc_proof, validation_proof = proof
            if self.verify_enc_proof(enc_proof) and self.verify_input_validation(validation_proof): # if the ciphertext has been verified
                self.all_ciphertexts.append(ctx)
        self.ctx_total = [self.evaluator.add_many([ciphertext[i] for ciphertext in self.all_ciphertexts]) for i in range(len(self.all_ciphertexts[0]))]
        return self.ctx_total
    
    

