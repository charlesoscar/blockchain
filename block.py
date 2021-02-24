import hashlib
from datetime import datetime


class Block:
    blockNr = 0
    data = None
    next = None
    hash = None
    nonce = 0
    previous_hash = "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks"

    def __init__(self, data):
        self.data = data
        self.timestamp = datetime.now()

    # gives the block it's unique signature
    def hash(self):
        h = hashlib.sha256()
        h.update(f"{self.blockNr}"
                 f"{self.data}"
                 f"{self.next}"
                 f"{self.nonce}"
                 f"{self.previous_hash}"
                 f"{self.timestamp}".encode('utf-8'))
        return h.hexdigest()

    def __str__(self):
        return f"Block Hash: {self.hash()}\n" \
               f"Timestamp: {self.timestamp}\n" \
               f"BlockNr: {self.blockNr}\n" \
               f"Block Data: {self.data}\n" \
               f"Hashes: {self.nonce}\n" \
               f"---------------"
