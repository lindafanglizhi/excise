import itchat

itchat.auto_login()

# 获取自己的用户信息，返回自己的属性字典
print(itchat.search_friends())
# 获取任何一项等于name键值的用户
req =itchat.search_friends(name='梅林花开')
print(req)

print(req[0]['User']['UserName'])
print(itchat.get_msg())

# itchat.send('Hello, filehelper', toUserName='filehelper')
