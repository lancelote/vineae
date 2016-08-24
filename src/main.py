import binascii

with open('../tests/test_dbs/keepass2_db.kdbx', 'rb') as database_file:
    binary_data = database_file.read()
    ascii_data = binascii

base_signature = byte_list[:4]      # Primary identifier
version_signature = byte_list[4:8]  # Secondary identifier

print(base_signature)
print(version_signature)
