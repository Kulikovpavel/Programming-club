import json
from time import sleep

from tornado import httpserver, ioloop, web, websocket

connections = []
messages = []

class MainHandler(web.RequestHandler):
    def get(self):
        self.render("test.html")

class EchoWebSocket(websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)
        sleep(5)
        self.write_message("NEW THING")
        self.write_message("NEW 666")

    def on_close(self):
        print("WebSocket closed")

application = web.Application([
    (r'/', MainHandler),    # HTML chat homepage
    (r'/websocket', EchoWebSocket),  # WebSocket server
])

if __name__ == "__main__":
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8888)
    ioloop.IOLoop.instance().start()