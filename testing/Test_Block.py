import datetime as _dt
import hashlib


class Block:
    def __init__(self, hash_sebelumnya, data):
        self.data = data
        self.hash_sebelumnya = hash_sebelumnya
        string = "".join(data) + hash_sebelumnya
        self.block_hash = hashlib.sha256((string).encode()).hexdigest()
