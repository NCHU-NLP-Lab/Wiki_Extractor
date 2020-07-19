# Wiki_Extractor
``` 
git clone https://github.com/UDICatNCHU/Wiki_Extractor.git
```
或者使用下載方式把 github 上的資料載到本地端（ 解壓縮後資料夾名稱為 Wiki_Extractor-master ）

opencc資料夾為簡體中文轉繁體中文之套件

Wiki_Extractor.py 萃取維基百科內文 （ 使用 https://github.com/attardi/wikiextractor 所提供的 code ）

Wiki_Cleaning.py 將資料轉換為 json 格式

Wiki_Tokenize.py 將內文進行斷詞

Wiki_to_Word2vec_Data 轉換成 Word2vec 的訓練資料格式




## 下載維基百科資料

資料下載處：https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2

在 linux 可直接下指令 
``` 
wget https://dumps.wikimedia.org/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2
```

## 切割維基百科、整理資料

因為一個維基百科的檔案過大，需要將他分割成多個小檔案

* 開啟cmd，切換路徑至此專案目錄(切換至Wiki_Extractor-master目錄下)

* 輸入分割檔案指令

``` 
python WikiExtractor.py -cb 250K -o wiki_extractor zhwiki-latest-pages-articles.xml.bz2
```

這個指令會將1G大的維基百科資料切割為每一份250K大小、檔案型態為.bz2的檔案

-cb 會將每個切割檔案壓縮成.bz2的型態

-o 為輸出檔案

指令中的"wiki_extractor"將每個分割好的檔案放入至此資料夾(它會自動新增資料夾，不用手動新增)

* 切割檔案後將資料整理為一個字典之json檔(wiki_data.json)

接著執行 extractor.py 取得一個json檔案，內容如下：
``` 
python extractor.py
```

<img src="https://i.imgur.com/8Xk3rIr.jpg" width="900px"/>

## 下載資料

底下的連結有我們整理好已斷詞的wiki data

https://drive.google.com/open?id=1jl_D2jPDo83qHkpXMliZBsp2Pk6B5RWy

分成兩種不同的資料格式

每一種資料格式都有兩種資料，其一為斷詞後無標記詞性，另一個為斷詞後有標記詞性

至於資料格式.....
### 一個是使用空白將每個詞給斷開
<img src="https://i.imgur.com/IBy9Y8r.jpg" width="900px" />

<img src="https://i.imgur.com/WbHfgwf.jpg" width="900px" />

### 一個是將每個詞給斷開放入List中
<img src="https://i.imgur.com/LjVKIy9.jpg" width="900px" />

<img src="https://i.imgur.com/Nd73Joy.jpg" width="900px" />

