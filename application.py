import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.autoreload
import settings
from tornado.options import options
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import urls

class Application(tornado.web.Application):
    def __init__(self):
        database_url = 'mysql+mysqldb://{}:{}@{}/{}?charset=utf8'.format(options.mysql_user, options.mysql_password,
                                                                         options.mysql_host, options.mysql_database)
        engine = create_engine(database_url, encoding='utf8', pool_size=options.pool_size, echo=False)
        self.session = scoped_session(sessionmaker(bind=engine, autocommit=False))

        super(Application, self).__init__(urls.handlers)

    def reload_handle(self):
        self.session.remove()


def main():
    tornado.options.parse_command_line()
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app, xheaders=True)
    http_server.listen(8000)
    loop = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.add_reload_hook(app.reload_handle())
    loop.start()


if __name__ == '__main__':
    main()