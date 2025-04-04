# 2025.4.4 演習その１　ファイル
file = open('myfile.txt', 'r')
data = file.read()
print("read data = ", data)
file.close()
