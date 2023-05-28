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
