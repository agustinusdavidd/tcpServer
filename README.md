### Features
- Binding dengan address dan port
- Parsing HTTP request
- Mencari file yang dibutuhkan client
- Memberikan response atas request yang dilakukan
- Mengirimkan pesan Error

# TCP Server
**Table of Contents**
- Introduction
- How its works
- Contributor

### Introduction
Disini kami membuat Server dengan protokol TCP sederhana yang diimplementasikan dengan Python untuk server dan HTML untuk membuat UI yang akan digunakan oleh client untuk berinteraksi dengan server

### How its Works
Langkah pertama yang kami lakukan ialah melakukan import library yang kami butuhkan
`import socket`

Selanjutnya kami membuat fungsi server tcp yang dipanggil melalui fungsi main
```Python
if __name__ == "__main__" :
    tcp_server()
```

```Python
def tcp_server()
```
Kita terhubung dengan socket 
`SERVER_HOST = 127.0.0.1`
dan port
`SERVER_PORT = 8081`

setelah itu kita membuat socket TCP dan melakukan binding
```Python
    sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
```

Setelah itu server siap menerima koneksi dari client
```Python
    sock_server.listen()
    print("Server ready...\n")
```

Seluruh perimintaan yang dilakukan oleh user akan di handle oleh sistem
```Python
def handle_request(request)
```

didalam fungsi `handle_request(request)`
request dari user akan diparsing

`GET /<file_requested>` menjadi `['GET', '/<file_requested>']`

dengan kode dibawah ini sistem akan mengirimkan response file yang diminta kepada user
```Python
splitRequest = request.split()
fileReq = splitRequest[1]
fileReq = fileReq[1::]
if fileReq == "":
    print(fileReq)                                                          
    fileReq = "index.html"
elif fileReq[0:6] == "search":
    fileReq = "search.html"
```
setelah itu sistem akan memparsing tipe file yang akan digunakan untuk mengisi header content type dengan memanggil fungsi
```Python
def contentType(file) :
```

apabila sudah ditentukan contentType dari file tersebut, akan disusun header serta dicari file yang diminta oleh client
Header disusun oleh 3 variabel yaitu
```Python
response_line = "HTTP/1.1 200 OK\r\n"
content_type = "Content-Type: " + type + "\r\n\r\n"
content_length = "Content-Length: " + length
```
variabel `content_type` akan diisi oleh kode IANA dari file yang diminta
`response_line` akan diisi oleh kode 200 apabila request dapat dijalankan
dan variabel `content_length` akan diisi oleh panjang dari file yang dikirim dalam byte
atau dibiarkan kosong apabila file bertipe teks.

untuk file yang di request pertama-tama akan dimasukkan ke variabel dengan catatan
apabila file bertipe teks atau application e.g. text/html, application/javascript.
maka akan dilakukan
```Python
with open(fileReq, 'r') as requestedFile:
```
dan apabila bertipe media e.g. image/x-icon, image/jpeg
akan dilakukan
```Python
with open(fileReq, 'rb') as requestedFile:
```
kemudian file akan dibaca menggunakan `readlines()`
dan disimpan ke variabel `message_body`

setelah diberi flag untuk memberi tahu apakah file berbentuk byte atau text, file akan digabungkan kedalam
sebuah list dengan urutan sebagai berikut:
```Python
response = [flag, response_line + content_length + content_type, message_body]
```
sebelum dioper ke fungsi `send_response` agar dapat dikirmkan ke client

Fungsi `send_response` cukup sederhana, fungsi ini hanya untuk mengirimkan file yang diminta client
kembali ke client sekaligus menutup socket tersebut.

pertama akan dikirmkan header berbentuk seperti berikut
```
HTTP/1.1 200 OK
Content-Length: 1710
Content-Type: image/webp
```
kemudian berdasarkan flag, file yang di request akan dikirimkan dengan encoding atau tanpa encoding kepada client
```Python
if response[0] == "media":
    for i in response[2]:
        sock_client.send(i)
else:
    for i in response[2]:
        sock_client.send(i.encode())
```

setelah itu akan dikirmkan string penutup 
```Python
sock_client.send("\r\n".encode())
``` 
diikuti oleh penutupan dari socket tersebut
```Python
sock_client.close()
```


### Cara Menggunakan
* Buka link [Github](https://github.com/agustinusdavidd/tcpServer) berikut
* Lakukan clone repositori atau download file
* Buka terminal atau IDE Python
* Ubah direktori menjadi tempat repositori disimpan
* Jalankan `python tcpServer.py`
* Buka browser anda dan ketikan `localhost:8081`
 
### Contributor
TUBES JARINGAN KOMPUTER
* Agustinus David
* Novia Natasya
* Muhammad Nadine Zuhdan Azra
