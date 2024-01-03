# Write a script to rename all files in a specific directory.
# Create a program to organize files by moving them to subdirectories based on their extensions.
import os

print(os.listdir('files'))

for file in os.listdir('files'):
    f, e = os.path.splitext(file)

    src = "files/" + file
    dest_txt = "files/txt/rename" + file
    dest_sql = "files/sql/rename" + file

    if e == '.sql':
        os.rename(src, dest_sql)
    elif e == '.txt':
        os.rename(src, dest_txt)
    else:
        pass
