import os

file_path = "path_to_your_file"

split_tup = os.path.splitext(os.path.basename(file_path))

file_name = split_tup[0]
file_extension = split_tup[1]

print("File Name: ", file_name)
print("File Extension: ", file_extension)

over_extension = input("Enter Any Extension: ").lower()
print(over_extension)

unicode_char = '‮'

new_file_name = file_name + unicode_char + over_extension[::-1] + file_extension

os.rename (file_path , new_file_name)
