import asyncore, socket
from ctypes import *
import binascii
import struct
import sys
import time
import thread  
import threading  

class AsyncClient(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect( (host, port) )
        self.buffer = '' 

    def handle_connect(self):
        pass

    def handle_close(self):
        self.close()
    def handle_read(self):
        buf=self.recv(1060)
        if (len(buf)==1060):
            info=struct.unpack_from('>i132d', buf, 0)
            #print 'movej([',info[32],',',info[33],',',info[34],',',info[35],',',info[36],',',info[37],'], a = 0.10, v = 0.10)'
            #print 'movel(p[',info[56],',',info[57],',',info[58],',',info[59],',',info[60],',',info[61],'], a = 0.10, v = 0.10)'
            #print '\r\n'

    def writable(self):
        return (len(self.buffer) > 0)

    def handle_write(self):
        print len(self.buffer)
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]


class WorkThread(threading.Thread):			#The timer class is derived from the class threading.Thread  
    def __init__(self, interval):  
        threading.Thread.__init__(self)      
        self.interval = interval  
        self.thread_stop = False
        self.client = AsyncClient('192.168.31.52',30003)

    def run(self): #Overwrite run() method, put what you want the thread do here  
        while not self.thread_stop:  
            asyncore.loop(1, False, None,2)  

    def stop(self):  
        self.thread_stop = True  


def main():
    client = AsyncClient('192.168.1.2',30003)
	x=5
	y=6
	z=7
	rx=1
	ry=2
	rz=3
	#��������ֵ
    client.send('movel(p[',x,',',y,',',z,',',rx,',',ry,',',rz,'], a = 0.10, v = 0.10)')
   

if __name__ == '__main__':  
    main() 