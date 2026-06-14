import hashlib

filename = input("Enter file name: ")

try:
    with open(filename, "rb") as file:
        data = file.read()

    sha256_hash = hashlib.sha256(data).hexdigest()

    print("\nSHA256 Hash:")
    print(sha256_hash)

except FileNotFoundError:
    print("File not found.")