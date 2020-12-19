# ShortURL

よくあるURL短縮サービスです。  
誰でも簡単にプライベートな環境で使えるようにと思い作りました。  
手軽さ全振り。セキュリティーは全く考慮しておりません。  

このアプリ利用による損害やトラブルについて一切の責任が持てませんので、ご利用になる場合はそれに同意の上ご利用ください。

# Description

長いURLを短い文字列のディレクトリとして表現します。

Example

```
https://helpdesk.sayukiki.com/api/hooks/line/v1/accounts/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/message
```

<span style="margin-left: 5rem">↓</span>

```
http://192.168.1.1/ghdDAGb53q
```

# Requirement

Docker と Docker Compose をインストールしたサーバーを1台

# Installation

.env の ROOT_URL をサービスURLに変更。

```
ROOT_URL=http://172.16.1.1
```

サービスの作成と起動。

```
docker-compose build
docker-compose up -d
```

# Usage

## URLを短縮したい

### Request

```
[GET]http://192.168.1.1/?url={短縮したいURL}
```

Example

```
[GET]http://192.168.1.1/?url=https%3A%2F%2Fhelpdesk.sayukiki.com%2Fapi%2Fhooks%2Fline%2Fv1%2Faccounts%2Fxxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx%2Fmessage
```

短縮したいURLはエンコードしてください。


### Response

```
[200]http://92.168.1.1/{短縮文字列}
```

Example

```
[200]http://92.168.1.1/ghdDAGb53q
```

(*1)文字の半角英数字大文字小文字に短縮します。  
有効期限は(*2)秒です。  
有効期限切れになると、別のURLに再利用されます。

<span style="display:inline-block; width: 1.3rem">*1</span> .env の STR_LENGTH で指定した長さです。  
<span style="display:inline-block; width: 1.3rem">*2</span> .env の EXPIRE で指定した秒数です。  

## 短縮したURLを使いたい

### Request

```
[GET]http://192.168.1.1/{短縮文字列}
```

Example

```
[GET]http://192.168.1.1/ghdDAGb53q
```

### Response

```
[302]{短縮前のURL}
```

Example

```
[302]https://helpdesk.sayukiki.com/api/hooks/line/v1/accounts/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/message
```