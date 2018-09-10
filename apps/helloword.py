from .base import BaseHandler
from tornado.concurrent import run_on_executor


class HelloWorld(BaseHandler):
    @run_on_executor
    def get(self, *args, **kwargs):
        try:
            self.write("Hello word")
        except Exception as e:
            return self.response()

