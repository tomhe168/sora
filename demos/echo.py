from tornado.tcpserver import TCPServer
from tornado.ioloop import IOLoop

from sora.datahandler import DataHandler
from sora.parser import UnsizedParserBuffer

class EchoServer(TCPServer):
    def handle_stream(self, stream, address):
        def callback(data):
            stream.write(data)
        stream.read_until_close(streaming_callback=DataHandler(UnsizedParserBuffer('\n', include=True), callback))


if __name__ == '__main__':
    server = EchoServer()
    server.listen(8888)
    IOLoop.instance().start()
    