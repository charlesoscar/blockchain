from block import Block


class Blockchain:
    difficulty = 20
    # maximum 32-bit number
    maxNonce = 2 ** 32
    target = 2 ** (256 - difficulty)

    # the first block on the blockhain
    block = Block("Genisis")
    dummy = head = block

    def add(self, block):
        block.previous_hash = self.block.hash()
        block.blockNr = self.block.blockNr + 1

        # pointer to the next block
        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1
