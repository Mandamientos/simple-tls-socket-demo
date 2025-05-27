import socket
import ssl

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')

bindsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bindsocket.bind(('localhost', 8443))
bindsocket.listen(5)

print("Server is listening on port 8443...")

while True:
    newsocket, fromaddr = bindsocket.accept()
    with context.wrap_socket(newsocket, server_side=True) as ssock:
        print(f"Connection from {fromaddr}")
        try:
            data = ssock.recv(1024)
            if data:
                print(f"Received data: {data.decode()}")
                ssock.sendall(b"Hello, secure world!")
            else:
                print("No data received.")
        except Exception as e:
            print(f"Error during communication: {e}")
        finally:
            ssock.close()