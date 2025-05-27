import socket
import ssl

context = ssl.create_default_context()
context.load_verify_locations('cert.pem')
hostname = 'localhost'

with socket.create_connection((hostname, 8443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(f"Connected to {hostname} on port 8443")
        try:
            ssock.sendall(b"Hello, secure server!")
            data = ssock.recv(1024)
            print(f"Received data: {data.decode()}")
        except Exception as e:
            print(f"Error during communication: {e}")
        finally:
            ssock.close()