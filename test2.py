F = open('test.txt','w',encoding='UTF-8')
msg="""
我是一个中国人
woaizhongguo
我爱中国！
"""
count = F.write(msg)
print(count)
F.close

# feeee = open('test.txt','r',encoding='utf-8')
# # text = feeee.read()
# print(feeee.read())
# feeee.close

# msg = "Hello world!"
# file = open("newfile.txt", "w")
# amount_written = file.write(msg)
# print(amount_written)
# file.close()