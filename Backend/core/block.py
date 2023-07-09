class Block:
    """
    Block is a storage conainer that stores Transactions
    """
    def _init_(self,Height,Blocksize,BlockHeader,Txcount,Txs):
        self.Height=Height
        self.Blocksize=Blocksize
        self.BlockHeader=BlockHeader
        self.Txcount=Txcount
        self.Txs=Txs
        
