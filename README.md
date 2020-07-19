# Wiki_Extractor
抓取維基百科內文

## 檔案說明

opencc資料夾為簡體中文轉繁體中文之套件

Wiki_Extractor.py 萃取維基百科內文 （ 使用 https://github.com/attardi/wikiextractor 所提供的 code ）

Wiki_Cleaning.py 將資料轉換為 json 格式

Wiki_Tokenize.py 將內文進行斷詞

Wiki_to_Word2vec_Data. 轉換成 Word2vec 的訓練資料格式

## 初始化

``` 
git clone https://github.com/UDICatNCHU/Wiki_Extractor.git
```
或者使用下載方式把 github 上的資料載到本地端（ 解壓縮後資料夾名稱為 Wiki_Extractor-master ）

## 安裝所需套件

``` 
pip3 install -r requirements.txt
```

## 下載維基百科資料

資料下載處：https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2

在 linux 可直接下指令 
``` 
wget https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2
```

## 萃取維基百科內容

``` 
python3 Wiki_Extractor.py -b 1024M -o extracted zhwiki-latest-pages-articles.xml.bz2
```
萃取完的資料會跑到 /extracted/AA/

## 將內容簡轉繁並整理成json格式

``` 
python3 Wiki_Cleaning.py
```

轉換後資料格式
``` 
[
  { 
    "id" : (int) 編號 ,
    "title" : (str) 文章標題  ,
    "articles" : (str) 文章內容
  },
...
]
```
<img src="https://i.imgur.com/gkHUe14.jpg" width="900px"/>

## 將內容依照每一句的內容進行斷詞
``` 
python3 Wiki_Tokenize.py
```
轉換後資料格式
``` 
[
  { 
    "id" : (int) 編號 ,
    "title" : (str) 文章標題  ,
    "tokens" : (list) 每一句斷詞內容
  },
...
]
```
<img src="https://imgur.com/4zn4w3Y.jpg" width="900px"/>

## 將維基百科內容轉換成 Word2vec 訓練資料格式
``` 
python3 Wiki_to_Word2vec_Data.py
```
轉換後資料為

<img src="https://imgur.com/eCxwp7b.jpg" width="900px"/>

## 下載資料

底下的連結有我們整理好的 wiki data

https://drive.google.com/drive/folders/1BvVVbRLD-W_954UchTi2KJTYPjqD-LJX?usp=sharing

