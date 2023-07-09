
import sys
sys.path.append('/Users/solar/Documents/PROGRAMS/python')
from BITCOIN.Backend.core.block import Block
from BITCOIN.Backend.core.Blockheader import BlockHeader
from BITCOIN.Backend.util.util import hash256
import  time 
import json       
ZERO_HASH ='0' *64   
VERSION =1  

class Blockchain :  
    def _init_(self):
        self.chain =[]
        self.GenesisBlock()
    #creating the Genesis block
    def GenesisBlock(self):
        BlockHeight =0
        prevBlockHash =ZERO_HASH  
        self.addBlock(BlockHeight,prevBlockHash)
     
    #creating the function that adds the blocks
    #It takes the blockheight and the previous blockhash as input
    def addBlock(self,BlockHeight,prevBlockHash):
        timestamp = int(time.time())
        Transaction = f"Marvine sent {BlockHeight} Bitcoins to SolarCrash"
        #markleRoot is the combined Hash of all the Transactions
        markleRoot =hash256(Transaction.encode()).hex()
        bits = 'ffff001f' 
        blockheader =BlockHeader(VERSION,prevBlockHash,markleRoot,timestamp,bits)
        blockheader.mine()
        self.chain.append(Block(BlockHeight,1,blockheader.__dict__,1,Transaction).__dict__)
        print(json.dumps(self.chain,indent =4))
if __name__ == " __main__":
    blockchain =Blockchain()