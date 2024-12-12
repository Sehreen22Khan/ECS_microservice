from flask import Flask
import socket

app = Flask(__name__)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

@app.route('/')
def hello_cloud():
  return 'Hello from Khan ECS Container'

app.run(host='0.0.0.0')