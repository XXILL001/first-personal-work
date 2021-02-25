# -*- coding: utf-8 -*-
import jieba
import json

txt = open("D:\PyCharm Community Edition 2020.2.2\zyq.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)     # 使用精确模式对文本进行分词
counts = {}     # 通过键值对的形式存储词语及其出现的次数

for word in words:
    if len(word) == 1:    # 单个词语不计算在内
        continue
    else:
        counts[word] = counts.get(word, 0) + 1    # 遍历所有词语，每出现一次其对应的值加 1

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)    # 根据词语出现的次数进行从大到小排序

tongji=[]
for ciyu in range(250):
    dict1={}
    word, count = items[ciyu]
    dict1['name']=word
    dict1['value']=count
    tongji.append(dict1)
print(tongji)

with open('词频统计.json', 'w', encoding='utf-8') as fi:
     fi.write(json.dumps(tongji,indent=2,ensure_ascii=False))