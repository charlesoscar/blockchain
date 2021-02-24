from block import Block
from blockhain import Blockchain

blockchain = Blockchain()

# mine for 10 blocks
for n in range(10):
    blockchain.mine(Block(f"Block {n + 1}"))

# prints mining output
while blockchain.head is not None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next
