import cv2
import cv2.cv as cv
import numpy as np
import json
from threading import Thread
from ImageTools import ImageTools

class Handlers:
 messageData = None
 displayThread = None
 imageTools = None

 def __init__(self):
  self.imageTools = ImageTools()
  self.displayThread = Thread(target=self.imageTools.display)
  self.displayThread.daemon = True
  self.displayThread.start()

 def errorMessage(self, status, message):
  return json.dumps({'status': status, 'type': 'error', 'message': message})

 def noTypeField(self):
  return self.errorMessage(403, "No type field found in message")

 def typeNotSupported(self, message):
  print "type not supported: %s" % (message['type'])
  return self.errorMessage(403, "Type not supported.")

 def handshake(self, message):
  if u'value' in message and u'ping' == message['value']:
   return json.dumps({'status': 200, 'type': 'handshake', 'value': 'pong'})
  else:
   return self.errorMessage(400, 'Missing or invalid value for handshake. Expecting "ping"')

 def image(self, message):
  height = message['height'] if u'height' in message else None
  width = message['width'] if u'width' in message else None
  format = message['format'] if u'format' in message else None
  imageData = self.messageData
  self.messageData = None

  if 'rgb' == format.lower() and height is not None and width is not None and imageData is not None:
   # Assuming 3-channel image in RGB format
   image = np.ndarray(shape=(height, width, 3), dtype=np.uint8, buffer=imageData)
   image = cv2.cvtColor(image, cv.CV_RGB2BGR)
   self.imageTools.image = image
   return json.dumps({'status': 200, 'type': 'image', 'value': 'ack'})
  else:
   return self.errorMessage(400, 'Missing or invalid value for height, width, format, or image data.')
