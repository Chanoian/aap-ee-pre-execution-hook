import os

print("Hello World !")

path = "/runner/env"
files = os.listdir(path)
print(files)

new_path = "/home/runner/env"
new_files = os.listdir(new_path)
print(new_files)
