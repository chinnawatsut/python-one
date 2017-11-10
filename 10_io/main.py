import os
import sys

test_file = open("test.txt", "wb")
# ab+ for Read+Append ,open or create file
print(test_file.mode)
print(test_file.name)
test_file.write(bytes("Write me to the file\n", 'UTF-8'))
test_file.close()

test_file = open("test.txt", "r+")
text_in_file = test_file.read()
print(text_in_file)

os.remove("test.txt")