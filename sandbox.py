# textFile = open("7.1.txt", "rt")
# print(textFile.readlines())
# textFile.close()
# binFile = open("7.1.txt", "rb")
# print(binFile.readlines())
# binFile.close()
#一维数据
from typing import List

ls = [[1,2,3], [4,5,6],[8,9]]
# print(ls[0])
for row in ls:
    for column in row:
        print(column)
# for row in range(len(ls)):
#     for column in :
#         print(column)
