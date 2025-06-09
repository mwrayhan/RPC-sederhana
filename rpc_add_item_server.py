from xmlrpc.server import SimpleXMLRPCServer

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity):
        if quantity < 0:
            return "Error: Quantity tidak boleh negatif"
        self.items[name] = self.items.get(name, 0) + quantity
        return f"Item '{name}' berhasil ditambahkan. Total stok: {self.items[name]}"

# Membuat server di localhost port 8000 dengan allow_none=True agar bisa mengirim None jika diperlukan
server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
inventory = Inventory()

# Daftarkan instance Inventory sehingga semua metodenya bisa diakses via RPC
server.register_instance(inventory)

print("Server berjalan di port 8000...")
server.serve_forever()
