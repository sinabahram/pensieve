from handlers import HandlerInterface
from helpers import ok, checkValue, MessageError


class Handshake(HandlerInterface):
    def handle(self, header, data):
        print "Handshake got called"
        try:
            return checkValue(header, 'value', 'ping', ok('handshake', 'pong'))
        except MessageError, e:
            print "Got exception: ", e
            return e.json
