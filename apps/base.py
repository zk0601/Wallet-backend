import tornado.web
from concurrent.futures import ThreadPoolExecutor
from tornado.escape import json_encode

class BaseHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(25)

    def initialize(self):
        self.set_status(200)
        self.set_header("Content-Type", "application/json")

    @property
    def session(self):
        return self.application.session

    def on_finish(self):
        self.session.remove()

    def on_connection_close(self):
        tornado.web.RequestHandler.on_connection_close(self)
        if self.get_status() >= 500:
            self.session.remove()

    def response(self, data=None, code=0, msg=""):
        if data is None:
            data = {}
        result = {"state": code, "msg": msg, "data": data}
        return self.write(json_encode(result))