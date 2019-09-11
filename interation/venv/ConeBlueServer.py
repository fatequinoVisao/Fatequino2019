from bluetooth import *

def server( s ) :
   conn, addr = s.accept()
   print 'Connected by', addr

   while True:
       data = conn.recv(1024)
       if not data: break
       conn.send(data)
   conn.close()
s=BluetoothSocket( RFCOMM )
s.bind(('', 8888))
s.listen(1)
server( s )