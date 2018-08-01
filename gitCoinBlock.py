import hashlib as hasher
import datetime as date

class Block: # Defining what a GitCoin consists of
    def __init__(self,index,timeStamp,data,previousHash):
        self.index = index
        self.timeStamp = timeStamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.hashBlock()
    
    def hashBlock(self):
        sha = hasher.sha256() # sha256 is a hashing algorithm
        sha.update(str(self.index)+str(self.timeStamp)+str(self.data)+str(self.previousHash))
        retrun sha.hexdigest() # returns the combined hash value in Hexadecimals

def createGenesisBlock(): # Pre-Defining a block with index 0 and an arbitrary previous hash 
    return Block(0, date.datetime.now, "Genesis Block", 0)

def createNextBlock(prevBlock): # Creating all the later blocks in the blockchain
    currIndex = prevBlock + 1
    currTimeStamp = date.datetime.now()
    currData = "Block" + str(currIndex)
    currHash = prevBlock.hash
    return Block(currIndex, currTimeStamp, currData, currHash)

BlockChain = [createGenesisBlock()] # Creating the BlockChain
prevBlock = BlockChain[0] # Adding the Genesis block

blocksToCreate = 20 # No. of blocks to be added after the Genesis Block





