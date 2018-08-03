import hashlib as hasher
import datetime as date
from flask import Flask
from flask import request
node = Flask(__name__)

class Block: # Defining what a GitCoin consists of
    def __init__(self,index,timeStamp,data,previousHash):
        self.index = index
        self.timeStamp = timeStamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.hashBlock()
    
    def hashBlock(self):
        sha = hasher.sha256() # sha256 is a hashing algorithm
        sha.update(str(self.index).encode('utf-8') + str(self.timeStamp).encode('utf-8') + str(self.data).encode('utf-8') + str(self.previousHash).encode('utf-8'))
        return sha.hexdigest() # returns the combined hash value in Hexadecimals

def createGenesisBlock(): # Pre-Defining a block with index 0 and an arbitrary previous hash 
    return Block(0, date.datetime.now, "Genesis Block", 0)

def createNextBlock(prevBlock): # Creating all the later blocks in the blockchain
    currIndex = prevBlock.index + 1
    currTimeStamp = date.datetime.now()
    currData = "Block" + str(currIndex)
    currHash = prevBlock.hash
    return Block(currIndex, currTimeStamp, currData, currHash)

blockChain = [createGenesisBlock()] # Creating the BlockChain
prevBlock = blockChain[0] # Adding the Genesis block

blocksToCreate = 20 # No. of blocks to be added after the Genesis Block

for i in range(0,blocksToCreate):
    blockToAdd = createNextBlock(prevBlock)
    blockChain.append(blockToAdd)
    prevBlock = blockToAdd
    print("Block %s has been added to the blockchain!" % (blockToAdd.index))
    print("Hash: %s\n" % (blockToAdd.hash))  

thisNodesTransactions =[]

@node.route('/txions', methods = ['POST'])
def transaction():
    if request.method == 'POST':  # On each new post request,we extract the transaction data.
        newTxion = request.get_json()
        thisNodesTransactions.appennd(newTxion) # We add the transcation to our list
        print("New transaction")
        print("FROM: {}".format(new_txion['from'])) # Because the transaction was successfully
        print("TO: {}".format(new_txion['to']))     # submitted we print it to our console log
        print("AMOUNT: {}\n".format(new_txion['amount']))
        return "Transaction submission successfull!\n"  # We let the client know it worked
node.run()


