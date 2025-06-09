import xmlrpc.client

s = xmlrpc.client.ServerProxy("http://localhost:8000/", allow_none=True)

# Contoh menambahkan item
print(s.add_item("keyboard", 10))
print(s.add_item("monitor", 5))
print(s.add_item("mouse", 5))

# Menambahkan item yang sama lagi
print(s.add_item("keyboard", 3))

# Coba tambah dengan quantity negatif (error handling)
print(s.add_item("mouse", -1))
