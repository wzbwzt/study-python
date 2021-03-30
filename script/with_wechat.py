import wxpy

# 初始化机器人，扫码登陆
bot = wxpy.Bot()

# 搜索名称含有 "游否" 的男性深圳好友
my_friends = bot.friends()
print(my_friends)
my_friend = my_friends.search(keywords="小明")
print(my_friend)
bot.join()
