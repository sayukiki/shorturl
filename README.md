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
http<span>://</span>192.168.1.1/ghdDAGb53q  
に短縮します。

# Requirement

Docker と Docker Compose をインストールしたサーバーを1台

# Installation

.env の ROOT_URL をサービスURLに変更。

```
ROOT_URL=http://172.16.1.1
```

サービスを起動。

```
docker-compose up -d
```

# Usage

## URLを短縮したい

### Request

[GET]http<span>://</span>192.168.1.1/?url=https%3A%2F%2Fhelpdesk.sayukiki.com%2Fapi%2Fhooks%2Fline%2Fv1%2Faccounts%2Fxxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx%2Fmessage

パラメーターurlに与えるURLはエンコードしてください。

### Response

[200]http<span>://</span>192.168.1.1/ghdDAGb53q

半角英数字大文字小文字10文字に短縮します。  
有効期限は60日です。  
有効期限切れになると、別のURLに再利用されます。

## 短縮したURLを使いたい

### Request

[GET]http<span>://</span>192.168.1.1/ghdDAGb53q

### Response

[302]https<span>://</span>helpdesk.sayukiki.com/api/hooks/line/v1/accounts/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/message
