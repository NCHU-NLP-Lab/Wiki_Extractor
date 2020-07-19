# extract.py
# 這個檔案主要是把wiki的所有文章，一篇一篇擷取出來，做成一個dictionary的json檔案
import pickle
from opencc import OpenCC
import os.path
import bz2
import json
import re

import os

key_num=0 # 每篇文章的流水編號
data_dict=dict()

# 簡體繁體中文編碼
opencc=OpenCC('s2t') 

# 找到所有檔案
for root, dirs, files in os.walk("wiki_extractor"): # wiki_extractor 為資料夾名稱
    for file in files:
        print(os.path.join(root, file))
        with bz2.BZ2File(os.path.join(root, file), 'r', 'rb') as f:
            # read the content
            data=""
            for line in f:
                content=line.decode("utf-8").replace('\n','')
                if content is not "":
                    if "</doc>" in content and data is not "":
                        data=opencc.convert(data)
                        data_dict[key_num]=data
                        key_num+=1
                        data=""
                    elif "<doc" not in content:
                        data+=content+'\n'
                    
jsonString = json.dumps(data_dict,ensure_ascii=False,indent=4)
fname = "wiki_data.json"
fout = open(fname,'w',encoding = 'UTF-8')
fout.write(jsonString)
fout.close()
