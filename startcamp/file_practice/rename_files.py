import os

os.chdir(r'C:\Users\aclass\Desktop\임지성\TIL\startcamp\file_practice\dummy')

filenames = os.listdir('.')

for filename in filenames:
    os.rename(filename,f'SAMSUNG_{filename}')
