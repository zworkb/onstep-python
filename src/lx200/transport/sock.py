import socket
import sys
from dataclasses import dataclass
from typing import Optional, Union


MAX_LEN = 32

@dataclass
class sock:
  
  
  host: str = ''
  port: Optional[Union[int, str]] = ''
  
  socktype: socket.AddressFamily = socket.AF_INET
  proto: int = -1
  sock: Optional[socket.socket] = None
  connected: bool = False
  

  def connect(self, host = '', port = '', socktype=socket.AF_INET, proto=-1):

    try:
      self.sock = socket.socket(socktype, socket.SOCK_STREAM, proto)
    except socket.error as e:
      sys.stderr.write('Error opening host: %s, port %s - %s\n' % (host, port, str(e)))
      raise

    if host != '':
      self.host = host
    if port != '':
      self.port = port

    try:
      self.sock.connect((self.host, self.port))
    except socket.error as e:
      sys.stderr.write('Error opening host: %s, port %s - %s\n' % (host, port, str(e)))
      raise
    self.connected = True

  def close(self):
    self.sock.close()

  def send(self, msg: str) -> None:
    if self.connected == False:
      self.connect(self.host, self.port)
      self.connected = True

    self.sock.sendall(msg.encode('utf-8'))

  def recv(self) -> str:
    data = self.sock.recv(MAX_LEN)
    return data.decode('utf-8')
