# import re
# from bs4 import BeautifulSoup
# import requests
#
# sel = requests.get('http://tech.sina.com.cn/i/2018-02-11/doc-ifyrkrva7278723.shtml')
# sel.encoding = 'utf-8'
# sel = sel.text
# pattern = "<meta name=\"sudameta\" content=\"comment_channel:(\w+);comment_id:comos-([a-zA-Z0-9]{14})\" />"
# pat = re.compile(pattern)
# next_urls = re.findall(pat, str(sel))
#
# soup = BeautifulSoup(sel,'html.parser')
# title = soup.find('h1',class_='main-title').text
# print(title)
# passage = BeautifulSoup(str(soup.find('div',id='artibody')),'html.parser')
# passage = passage.find_all('p')
# str = ''
# for new in passage:
#     str+=new.text
# print(str)
#
# # import re
# #
# # a = ["<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />",
# #    '<meta http-equiv=Content-Type content="text/html;charset=gb2312">',
# #    '<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">',
# #    '<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />',
# #    '<meta http-equiv="content-type" content="text/html; charset=utf-8" />',
# #    '<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />',
# #    '<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />'
# #    ]
# #
# #
# #
# # b = "<meta[ ]+http-equiv=["']?content-type["']?[ ]+content=["']?text/html;[ ]*charset=([0-9-a-zA-Z]+)["']?"
# #
# #
# # B = re.compile(b, re.IGNORECASE)
# #
# #
# # for ax in a:
# #   r1 = B.search(ax)
# #
# #   if r1:
# #     print (r1.group())
# #     print (r1.group(1), len(r1.group()))
