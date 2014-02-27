#!/usr/bin/python

import sys
import zmq
import json
from Handlers import Handlers

handlers = Handlers()
messageHandlers = {
'handshake': handlers.handshake,
'image': handlers.image,
}

def handleMessage(message):
 global handlers
 global messageHandlers
 if 'type' not in message:
  return handlers.noTypeField()
 else:
  return messageHandlers.get(message['type'], handlers.typeNotSupported)(message)

def startServer():
 host = sys.argv[1] if len(sys.argv) > 1 else "*"
 port = int(sys.argv[2]) if len(sys.argv) > 2 else 61455
 proto = sys.argv[3] if len(sys.argv) > 3 else "tcp"
 addr = "{}://{}:{}".format(proto, host, port)

 context = zmq.Context()
 socket = context.socket(zmq.REP)
 socket.bind(addr)

 while True:
  messageFrame = socket.recv(copy=False)
  index = messageFrame.bytes.find("\n")
  print "indexed at ", index
  messageString = str(messageFrame.bytes[:index]) if index > 0 else str(messageFrame.bytes)
  print "messageString: ", messageString
  handlers.messageData = messageFrame.bytes[index+1:]
  messageJson = json.loads(messageString)
  socket.send(b"%s"%(handleMessage(messageJson)))
  
def main():
 startServer()

if __name__ == "__main__":
 main()
