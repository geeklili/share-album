import os
import shutil
from flask import request
from flask_restful import Resource


class CopyImage(Resource):
    """恢复图片
    """
    def get(self):

        pic_name = request.form.get('name')
        pw = request.form.get('pw')
        imgs_li = os.listdir('./static/img/keep/')
        imgs_li2 = os.listdir('./static/img/images/')
        if pic_name in imgs_li and pic_name not in imgs_li2 and pw == 'admin':
            file_name = './static/img/keep/%s' % pic_name
            file_name2 = './static/img/images/%s' % pic_name
            shutil.copy(file_name, file_name2)
            return "200"
        else:
            return '401'

    def post(self):
        return self.get()


class DeleteKeep(Resource):
    """恢复图片
    """
    def get(self):

        pic_name = request.form.get('name')
        pw = request.form.get('pw')
        imgs_li = os.listdir('./static/img/keep/')

        if pic_name in imgs_li and pw == 'admin':
            file_name = './static/img/keep/%s' % pic_name
            os.remove(file_name)
            return "200"
        else:
            return '401'

    def post(self):
        return self.get()