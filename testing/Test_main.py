from Test_Block import Block

blockchain = []

genesis_block = Block("Sekarang bulan march tahun 2024", [
                      "Dito Aditya", "100", "100", "100", "100"])

second_block = Block(genesis_block.block_hash, [
                     "Agam Syahputra", "50", "100", "100", "100"])

third_block = Block(second_block.block_hash, [
    "Putri Permata", "100", "100", "100", "100"])

print("block pertama")
print(genesis_block.block_hash)
print("block kedua")
print(second_block.block_hash)
print("block ketiga")
print(third_block.block_hash)
