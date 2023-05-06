import socket
#oleh david
def tcp_server() :
    SERVER_HOST = "127.0.0.1"
    SERVER_PORT = 8081

    sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock_server.bind((SERVER_HOST,SERVER_PORT))

    sock_server.listen()

    print("Server ready...\n")

    while True:
        sock_client, client_address = sock_server.accept()

        request = sock_client.recv(1024).decode()
        print("From Client : " + request)

        response = handle_request(request) #modified by nadine
        #response = "From Server : " + request
        #sock_client.send(response.encode()) #modified by nadine
        try:
            for i in response[1]:   #modified by nadine
                sock_client.send(i.encode())
            if response[0] == "media":
                for i in response[2]:
                    sock_client.send(i)
            else:
                for i in response[2]:
                    sock_client.send(i.encode())
        except Exception as error:
            print("[WARNING]", error)
            print("From Client : " + request)
            print("Client IP : ", client_address)
            print("Response : ", response)
        sock_client.close()

    sock_server.close()
#oleh david
def handle_request(request) :
    #spliRequest = request.split()#.split("/")[-1]    } modified by nadine
    #fileReq = spliRequest[1]                        # } mendapatkan nama file yang diminta oleh client
    #fileReq = fileReq[1::]                      # } menghapus / di bagian awal file

    #if fileReq == "":
    #    fileReq = "web_page.html"
    flag = "text"
    try:
        splitRequest = request.split()#.split("/")[-1]    } modified by nadine
        fileReq = splitRequest[1]                        # } mendapatkan nama file yang diminta oleh client
        fileReq = fileReq[1::]                      # } menghapus / di bagian awal file
        type = contentType(fileReq)
        if fileReq == "":
            fileReq = "index.html"
    #modified by nadine
        if type.split('/')[0] != "text":
            with open(fileReq, 'rb') as requestedFile: # membuka file yang diminta
                content_file = requestedFile.readlines()
                flag = "media"
                response_line = "HTTP/1.1 200 OK\r\n"
                content_type = "Content-Type: " + type + "\r\n\r\n" # header untuk memberi tahu client tipe file yang akan diterima
                message_body = content_file
                length = 0
                for i in content_file:
                    length += len(i)
                content_length = "Content-Length: " + str(length) + "\r\n" # header agar browser tahu kapan file yang diminta selesai dikirimkan untuk bentuk selain text html
            
        else:
            with open(fileReq, 'r') as requestedFile: # membuka file yang diminta
                content_file = requestedFile.read()
                response_line = "HTTP/1.1 200 OK\r\n"
                content_type = "Content-Type: " + type + "\r\n\r\n" # header untuk memberi tahu client tipe file yang akan diterima
                content_length = ""
                message_body = content_file
    
    except FileNotFoundError: # error handling apabila file yang diminta tidak ditemmukan
        response_line = "HTTP/1.1 404 Not Found\r\n"
        content_type = "Content-Type: text/html\r\n\r\n"
        message_body = "<html><body><h1>404 Not Found</h1></body></html>"
        content_length = ""
    except Exception: #oleh nadine
        response_line = "HTTP/1.1 403 Bad Request\r\n"
        content_type = "Content-Type: text/html\r\n\r\n"
        message_body = "<html><body><h1>403 Bad Request</h1></body></html>"
        content_length = ""
        print(request.split())
    #oleh nadine
    response = []
    response.append(flag)
    response.append(response_line + content_length + content_type)
    print(response[1])
    response.append(message_body)
    return response

#oleh nadine
def contentType(file) :
    type = file.split('.')[-1] # parsing tipe file yang diminta untuk mengisi header content-type
    if type=="html":
        return "text/html"
    elif type=="jpg":
        return "image/jpeg"
    elif type=="gif":
        return "image/gif"
    elif type=="png":
        return "image/png"
    elif type=="webp":
        return "image/webp"
    elif type=="ico":
        return "image/x-icon"
    else:
        return "text/plain"

if __name__ == "__main__" :
    tcp_server()
