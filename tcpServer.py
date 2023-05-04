import socket

def tcp_server() :
    SERVER_HOST = "127.0.0.1"
    SERVER_PORT = 8080

    sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock_server.bind((SERVER_HOST,SERVER_PORT))

    sock_server.listen()

    print("Server ready...\n")

    while True:
        sock_client, client_address = sock_server.accept()

        request = sock_client.recv(1024).decode()
        print("From Client : " + request)

        response = handle_request("")
        #response = "From Server : " + request
        sock_client.send(response.encode())

        sock_client.close()

    sock_server.close()

def handle_request(request) :
    fileReq = request.split()[1].split("/")[-1]                    #mendapatkan nama file yang diminta oleh client

    if fileReq == "":
        fileReq = "web_page.html"

    try:
        with open(fileReq, 'r'):
            content_file = fileReq.read()
            response_line = "HTTP/1.1 200 OK\r\n"
            content_type = "Content-Type: text/html\r\n\r\n"
            message_body = content_file.decode()
    
    except FileNotFoundError:
        response_line = "HTTP/1.1 404 Not Found\r\n"
        content_type = "Content-Type: text/html\r\n\r\n"
        message_body = "<html><body><h1>404 Not Found</h1></body></html>"
    
    response = response_line + content_type + message_body
    return response

if __name__ == "__main__" :
    tcp_server()