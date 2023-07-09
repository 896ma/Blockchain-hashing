
from BITCOIN.Backend.util.util import hash256
class BlockHeader:
    def _init_(self,Version,prevBlockHash,merkleRoot,timestamp,bits):
        self.Version=Version
        self.prevBlockHash=prevBlockHash
        self.merkleRoot=merkleRoot
        self.timestamp=timestamp
        self.bits=bits
        self.nonce =0
        self.blockHash =''
    def mine(self): 
        while(self.blockHash[0:4]) !='0000':
            self.blockHash =hash256((str(self.Version)+self.prevBlockHash+self.merkleRoot+str(self.timestamp)
                                   +self.bits+str(self.nonce)).encode()).hex()

            self.nonce+=1 
            print(f"mining started {self.nonce}",end ='\r')
            
