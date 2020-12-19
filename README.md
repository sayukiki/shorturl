# ShortURL

よくあるURL短縮アプリです。  
誰でも簡単にプライベートな環境で使えるようにと思い作りました。  
手軽さ全振り。セキュリティーは全く考慮しておりません。  

このアプリ利用によるトラブルについて責任は持てませんのでご了承ください。

# Description

https<span>://</span>helpdesk.sayukiki.com/api/hooks/line/v1/accounts/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/message

↓

http<span>://</span>192.168.1.1/ghdDAGb

長いURLを短い文字列のディレクトリとして表現します。

# Requirement

Dockerをインストールしたサーバーを1台

# Installation

docker build -t sayukiki/shorturl .

docker run -d -p 80:8000 -e ROOT_URL={このサービスのURL} sayukiki/shorturl

サーバーの名前（名前解決できる名前かIP）

- https<span>://</span>shorturl.sayukiki.com  (フロントにNginxなどがあってHTTPSで受け付けたい場合)
- http<span>://</span>shorturl.intranet  (社内システムのhostsに設定できる場合)
- http<span>://</span>192.168.1.1  (IPを直に指定する場合)

など

# Usage

## URLを短縮したい

### Request

[GET]http<span>://</span>192.168.1.1/?url=https%3A%2F%2Fhelpdesk.sayukiki.com%2Fapi%2Fhooks%2Fline%2Fv1%2Faccounts%2Fxxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx%2Fmessage

パラメーターurlに与えるURLはエンコードしてください。

### Response

[200]http<span>://</span>192.168.1.1/ghdDAGb

## 短縮したURLを使いたい

### Request

[GET]http<span>://</span>192.168.1.1/ghdDAGb

### Response

[302]https<span>://</span>helpdesk.sayukiki.com/api/hooks/line/v1/accounts/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/message
