import hashlib
import os
filename = "important.txt"
hash_file = "hash.txt"
with open(filename, "rb") as file:
    file_data = file.read()
current_hash = hashlib.sha256(file_data).hexdigest()
if os.path.exists(hash_file):
    with open(hash_file, "r") as file:
        saved_hash = file.read()
    if current_hash == saved_hash:
        print("File has not changed.")
    else:
        print("WARNING: File has been modified!")
else:
    with open(hash_file, "w") as file:
        file.write(current_hash)
    print("Hash saved. Run the program again to check for changes.")