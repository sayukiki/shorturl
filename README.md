# ShortURL

よくあるURL短縮アプリです。  
誰でも簡単にプライベートな環境で使えるようにと思い作りました。  
手軽さ全振り。セキュリティーは全く考慮しておりません。  

このアプリ利用によるトラブルについて責任は持てませんのでご了承ください。

# Description

長いURLを短い文字列のディレクトリとして表現します。

例えば、  
https<span>://</span>helpdesk.sayukiki.com/api/hooks/line/v1/accounts/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/message  
を  
http<span>://</span>192.168.1.1/ghdDAGb  
に短縮します。

# Requirement

Docker と Docker Compose をインストールしたサーバーを1台

# Installation

.env の ROOT_URL をサービスURLに（例えば、http<span>://</span>172.16.1.1）

```
docker-compose up -d
```

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
