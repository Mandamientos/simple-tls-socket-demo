# 🔐 Simple TLS Socket Demo

A minimal example of a secure TLS connection using Python's built-in `ssl` and `socket` libraries.  
This project includes a simple **TLS server** and **TLS client**, secured with self-signed certificates.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/simple-tls-socket-demo.git
cd simple-tls-socket-demo

### 2. Generate self-signed certificates

⚠️ Be careful, when prompted for de CN (Common Name), enter: `localhost`

```bash
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes

