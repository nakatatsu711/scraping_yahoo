## 概要
Yahoo検索を自動化するプログラムです。

<br>

[Yahoo!JAPAN](https://www.yahoo.co.jp)のトップページからコマンドラインで入力したキーワードを検索します。  
1番目にヒットしたページに遷移し、URLを取得します。  
取得したURLはコマンドラインに出力します。



## システム環境
以下で動作確認済みです。  
`OS`：macOS 10.15.6  
`Python`：3.6.9



## 実行方法
### ライブラリインストール
以下の2通りの方法がありますので、どちらかでインストールしてください。
```
$ pip install selenium
```
```
$ pip install -r requirements.txt
```


### ChromeDriverについて
ブラウザはGoogleChromeを使用します。  
ブラウザを自動操作するためにはChromeDriverが必要です。

以下から自分のGoogleChromeと同じバージョンのドライバーをダウンロードします。  
https://sites.google.com/a/chromium.org/chromedriver/downloads

ChromeDriverをダウンロードしたら解凍して、任意の場所に配置します。  
そして、`chromedriver_path`のところに自分がダウンロードした場所を指定します。


### 実行
コマンドラインで実行します。`キーワード`には検索したいキーワードを入力します。
```
$ python scraping_yahoo.py キーワード
```
