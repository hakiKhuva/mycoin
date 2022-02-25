import time
from mycoin import Blockchain,Block,Transactions

print("mycoin".center(50,"*"))

chain = Blockchain()
chain.MAX_TRANSACTIONS = 2
chain.DIFFICULTY_TIME = 2

print("creating genesis block ",end="")
chain.genesis_block("abc",912)
print("done.")

print("custom block without mining adding to the chain")
t = Transactions()
t.add({
    "sender" : "abc",
    "receiver" : "def",
    "txn_amount" : 9.12,
    "time" : time.time()
})

Block(t,time.time())
chain.add_verified_block(Block)

print("getting block to mine")
m = chain.block_to_mine()
print("response : ",m)

print("add transaction")
chain.add_transaction("abc","def",9.12,time.time())
print("add transaction")
chain.add_transaction("ghi","jkl",12.41,time.time())

print("getting block to mine")
mine_to = chain.block_to_mine()
print("response : ",mine_to)

print("adding to chain")
chain.add_verified_block(mine_to["block"])

print("mining block")
if mine_to["status"]:
    block = mine_to["block"]
    diff = block["diff"]
    block["block"].mine(diff,chain.MAX_NONCE)

print("adding to chain")
chain.add_verified_block(mine_to["block"])

print("Blockchain")
print(chain._chain)

print("waiting for 3 seconds")
time.sleep(3)

print("chain verification : ",chain.verify_chain())

print("add transaction")
chain.add_transaction("abcdef","ghijkl",9.12,time.time())
print("add transaction")
chain.add_transaction("mnopqr","stuvwx",12.41,time.time())

print("getting block to mine")
mine_to = chain.block_to_mine()
print("response : ",mine_to)

print("adding to chain")
chain.add_verified_block(mine_to["block"])

print("mining block")
if mine_to["status"]:
    block = mine_to["block"]
    diff = block["diff"]
    block["block"].mine(diff,chain.MAX_NONCE)

print("adding to chain")
chain.add_verified_block(mine_to["block"])

print("Blockchain")
print(chain._chain)

print("chain verification : ",chain.verify_chain())


print("waiting for 5 seconds")
time.sleep(5)

print("add transaction")
chain.add_transaction("def","abc",2.12,time.time())
print("add transaction")
chain.add_transaction("asi","mnol",2.41,time.time())

print("getting block to mine")
mine_to = chain.block_to_mine()
print("response : ",mine_to)

print("adding to chain")
chain.add_verified_block(mine_to["block"])

print("mining block")
if mine_to["status"]:
    block = mine_to["block"]
    diff = block["diff"]
    block["block"].mine(diff,chain.MAX_NONCE)

print("adding to chain")
chain.add_verified_block(mine_to["block"])

print("Blockchain")
print(chain._chain)

print("chain verification : ",chain.verify_chain())


chain.DIFFICULTY_TIME = 60

print("add transaction")
chain.add_transaction("def","abc",2.12,time.time())
print("add transaction")
chain.add_transaction("asi","mnol",2.41,time.time())

print("getting block to mine")
mine_to = chain.block_to_mine()
print("response : ",mine_to)

print("adding to chain")
chain.add_verified_block(mine_to["block"])

print("mining block")
if mine_to["status"]:
    block = mine_to["block"]
    diff = block["diff"]
    block["block"].mine(diff,chain.MAX_NONCE)

print("adding to chain")
chain.add_verified_block(mine_to["block"])

print("Blockchain")
print(chain._chain)

print("chain verification : ",chain.verify_chain())
