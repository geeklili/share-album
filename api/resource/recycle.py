import os
import shutil
from flask import request
from flask_restful import Resource


class Recover(Resource):
    """恢复图片
    """
    def get(self):

        pic_name = request.form.get('name')
        pw = request.form.get('pw')
        imgs_li = os.listdir('./static/recycle')
        if pic_name in imgs_li and pw == 'admin':
            file_name = './static/images/%s' % pic_name
            file_name2 = './static/recycle/%s' % pic_name
            shutil.move(file_name2, file_name)
            return "200"
        else:
            return '401'

    def post(self):
        return self.get()


class DeleteRecyclePicture(Resource):
    """删除回收站图片
    """

    def get(self):
        """
        删除图片的接口，将图片存到清空站
        :return: 200
        """
        imgs_li = os.listdir('./static/recycle')
        pic_name = request.args.get('name')
        pw = request.form.get('pw')
        if pic_name in imgs_li and pw == 'admin':
            file_name = './static/recycle/%s' % pic_name
            os.remove(file_name)
            return "200"
        else:
            return '401'

    def post(self):
        return self.get()


class DeleteAllRecyclePicture(Resource):
    """删除所有回收站里的图片
    """
    def get(self):
        pic_li = os.listdir('./static/recycle/')
        pw = request.form.get('pw')
        if pic_li and pw == 'admin':
            for name in pic_li:
                file_name = './static/recycle/%s' % name
                os.remove(file_name)
            return '200'
        else:
            return '401'

    def post(self):
        return self.get()
