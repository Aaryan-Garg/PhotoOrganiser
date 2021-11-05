#opencv --> comp vision

import os

num = os.getcwd()

os.chdir(num+ "/photo")

num = os.getcwd()

list = os.listdir(num)

for i in range(len(list)):
    print(list[i])


