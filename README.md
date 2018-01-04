# Wiki_Extractor

* 先把github上的資料clone到本地端(解壓縮後資料夾名稱為Wiki_Extractor-master)

opencc資料夾為簡體中文轉繁體中文之套件

WikiExtractor.py為分割維基百科檔案之程式

extractor.py是將維基百科資料轉換為字典之json檔案

## 下載維基百科資料

* 下載MobaXterm並安裝完成、登入

https://mobaxterm.mobatek.net/ 

### 登入方式 : 

* 開啟mobaXterm => 點選左上角Session => 點選SSH  

* Remote host : 140.120.13.242

* Specify username : amd

* port : 15555

* 點選"OK"

* 輸入密碼 : 123


<img src="https://i.imgur.com/Y9lolhT.jpg" align="left"/>

--

* 將左方視窗中zhwiki-latest-pages-articles.xml.bz2檔案下載並放於此專案目錄下(Wiki_Extractor-master資料夾中)

<img src="https://i.imgur.com/JiYPVNG.jpg" align="left"/>

--

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
``` 
python extractor.py
```

<img src="https://i.imgur.com/8Xk3rIr.jpg" width="900px"/>




