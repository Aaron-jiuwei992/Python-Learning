# -*- encoding:utf-8 -*-

import tornado.ioloop
import tornado.web
import argparse
import os
import platform
import asyncio
import logging
from dal import database

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='search.log',
                    filemode='w')


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class SearchHandler(tornado.web.RequestHandler):
    def initialize(self, db):
        self.__db = db

    def get(self):
        query = self.get_argument('query', '')
        sql = "select url,title,content from pages where match(title, content) against(%s) limit 10"
        pages = self.__db.query(sql, query)
        self.render("result.html", pages = pages)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--host", type=str, default="localhost")
    parser.add_argument("-P", "--port", type=int, default=8090)

    FLAGS, unknown = parser.parse_known_args()
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # 定义字典变量 settings,保存静态文件和模板文件的路径
    settings = {
        # 在static_path中指定静态文件的路径
        "static_path": os.path.join(os.path.dirname(__file__), "static"),

        # 在template_path中指定模板文件的路径
        "template_path": os.path.join(os.path.dirname(__file__), "templates"),

        # debug表示是否开启调试模式，在调试模式中，对项目文件的修改会立即生效
        "debug": True,
    }

    mysql_instance = database.Database.get_instance()

    application = tornado.web.Application(
        [
            (r"/", IndexHandler),
            (r"/search/", SearchHandler, dict(db=mysql_instance)),
        ],
       **settings
    )

    application.listen(FLAGS.port)
    tornado.ioloop.IOLoop.instance().start()
