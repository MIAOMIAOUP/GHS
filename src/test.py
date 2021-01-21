from src.ghs import ghs
# , 'E:\QAQ'
types, names = ghs(['D:\迅雷下载完成\QAQ55'], tbs=['.exe', '.jpg', '.torrent', '.jpeg', '.gif', '.xltd', '.txt'])
# print(types)
# print(names)
for k, v in names.items():
    # print(k)
    if len(names[k]) > 1:
        print(k + ':::' + ','.join(v))




