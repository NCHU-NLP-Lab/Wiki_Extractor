# Wiki_Extractor

先把github上的資料clone到本地端

## 下載維基百科資料

下載MobaXterm並安裝完成、登入

https://mobaxterm.mobatek.net/ 

### 登入方式: 

* 開啟mobaXterm => 點選左上角Session => 點選SSH  

* Remote host: 140.120.13.242

* Specify username: amd

* port: 15555

* 點選"OK"

* 輸入密碼: 123


<img src="https://i.imgur.com/Y9lolhT.jpg" align="left"/>

--

* 將左方視窗中zhwiki-latest-pages-articles.xml.bz2檔案下載並放於此專案中

這裡有圖片!!!!!!!!!!!!!


## 切割維基百科

因為一個維基百科的檔案過大，需要將他分割成多個小檔案

* 開啟cmd，切換路徑至此專案目錄

* 輸入分割檔案指令

``` 
python WikiExtractor.py -cb 250K -o wiki_extractor zhwiki-latest-pages-articles.xml.bz2
```

* 切割檔案後將資料整理為一個dict之json檔
``` 
python extractor.py
```

<img src="https://i.imgur.com/8Xk3rIr.jpg" width="900px"/>




