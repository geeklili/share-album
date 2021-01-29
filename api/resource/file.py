from flask_restful import Resource
from flask import send_file, request, Response


class Robots(Resource):
    """爬虫爬取权限
    """
    def get(self):
        return send_file('./static/robots/robots.txt')

    def post(self):
        return self.get()


class Favicon(Resource):
    """主页图标
    """
    def get(self):
        return send_file('./static/favicon/favicon.ico')

    def post(self):
        return self.get()


class Picture(Resource):
    """主页图标
    """
    def get(self):
        pic_name = request.args.get('name')
        pic_name = pic_name[:23]
        file = request.args.get('file')
        file_name = './static/%s/%s' % (file, pic_name)
        with open(file_name, 'rb') as f:
            content = f.read()
        return Response(content, mimetype="image/jpeg")

    def post(self):
        return self.get()
