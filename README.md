# HTTP2 技術研究

本研究針對 HTTP2 功能與不同伺服器的啟動方式進行研究。

## 簡介

HTTP 協定自 1997 年 HTTP 1.1 後，於 2015 年才迎來一個主要更新 HTTP 2.0，簡稱為h2 ( 基於TLS/1.2或以上版本的加密連接 ) 或 h2c ( 非加密連接 )。

相對於 HTTP 1.1，其協定增加以下優點：

+ Request multiplexing
+ head-of-line blocking

由於 HTTP/1.1 使用 Pipelining 的機制，以此達到單一 TCP 可以多個請求，避免請求排隊導致的延遲，但由於伺服器必需依據這方式逐一回應，但相應接受處理並非所有瀏覽器皆有實；此外，Pipelining 機制也會因為單一請求耗時或遺失導致整個處理工作流阻塞。

對此，HTTP 2.0 則實作多路復用 ( multiplexing ) 確保請求同時接收並行處理與回應；此外，亦針對 HTTP 訊息進行壓縮來減少訊息量與提高安全性，以及伺服器推送機制來達到伺服器主動推送資源進而避免資源重複請求。

## 測試命令

使用 curl 指令檢查目標主機的 http 版本

```
# 使用 CLI 進入容器環境
do curl
# 執行檢查指令
curl -sI http://nginx -o/dev/null -w '%{http_version}\n'
# 執行 HTTP/2 協定
curl --http2 http://nginx
# 執行 HTTP/2 協定但不包括 HTTP/1.1 更新
curl --http2-prior-knowledge http://nginx
```

## 範本執行

### Nginx

```
do nginx
```

由於 Nginx 在不同版本啟動方式並不相同，且預設為 HTTP/1 的情況，對此同步啟動多個 Nginx 服務並執行交錯檢查指令

```
curl --http2 http://nginx-1.24-d -SI
curl --http2-prior-knowledge http://nginx-1.24-d -SI
curl --http2 http://nginx-1.24 -SI
curl --http2-prior-knowledge http://nginx-1.24 -SI
curl --http2 -SI http://nginx-1.25 -SI
curl --http2-prior-knowledge -sI http://nginx-1.25 -SI
```

依據 Nginx 文獻所述 **Nginx has HTTP/2 support since version 1.9.5.**，詳細可以參考 HTTP 2.0 模組說明，但為了配合大多數的瀏覽器使用，HTTP 2.0 預設並未開啟。

但對於 HTTP 2.0 啟動文件多數是伴隨 SSL 機制，若考量 HTTP 2.0 對安全性的設計不難理解需要 HTTPS 配合的原因，然而這就導致如何設定 h2c ( 非加密連接 ) 成為問題；在本範本中，一共啟動三個 Nginx 伺服器，並分別檢測其資訊與狀態。

+ Nginx 1.24 無設定
+ Nginx 1.24 設定 ```listen 80 http2```
+ Nginx 1.25 設定 ```http2 on```
    - 在 Nginx 的 HTTP 2.0 模組說明中提到，於 1.25  版本後廢棄在 listen 宣告中設定 http2 的規則。

透過上述服務與檢測，出現以下狀況

| Nginx | --http2 | --http2-prior-knowledge | browser |
| :--: | :--: | :--: | :--: |
| 1.24 non HTTP2 | 正常回應 | 說明不支援 2.0 | 可開啟網頁 |
| 1.24 with HTTP2 | HTTP 0.9 協定不允許 | 正常回應 | 無法開啟網頁 |
| 1.25 with HTTP2 | 正常回應 | 正常回應 | 無法開啟網頁 |

參考相關文獻對於 1.24 設定 HTTP2 的討論，多數提到即使設定 h2c 也會因為瀏覽器支援度導致降到 HTTP 1.1 的 Pipelining 而異常，對此建議若不使用 1.25 版本還請勿開啟 HTTP 2.0。

## 文獻

+ [HTTP2 Wiki](https://zh.wikipedia.org/zh-tw/HTTP/2)
    - [Http/2 是什麼?](https://totoroliu.medium.com/http-2-%E6%98%AF%E4%BB%80%E9%BA%BC-d7de699bdbae)
    - [什麼是 HTTP？為什麼 HTTP/2 比 HTTP/1.1 更快？](https://www.cloudflare.com/zh-tw/learning/performance/http2-vs-http1.1/)
    - [HTTP/1、HTTP/1.1 和 HTTP/2 的區別](https://www.explainthis.io/zh-hant/swe/http1.0-http1.1-http2.0-difference)
    - [HTTP2 Multiplexing: The devil is in the details](https://blog.codavel.com/http2-multiplexing)
    - [HTTP/2 Test](https://tools.keycdn.com/http2-test)
+ Nginx
    - [Module ngx_http_v2_module](https://nginx.org/en/docs/http/ngx_http_v2_module.html)
    - [Allow h2c and HTTP/1.1 support on the same listening socket](https://trac.nginx.org/nginx/ticket/816)
+ .NET
    - [How to use HTTP/2 with HttpClient in .NET 6.0](https://www.siakabaro.com/use-http-2-with-httpclient-in-net-6-0/)
+ Node
    - [How to use HTTP2 with Express.js and test it locally](https://typeofnan.dev/how-to-use-http2-with-express/)
+ curl
    - [HTTP/2 with curl](https://curl.se/docs/http2.html)
