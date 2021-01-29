import os
import shutil
from PIL import Image
from flask import request
from flask_restful import Resource


class DeletePicture(Resource):
    """删除图片，将图片存到回收站
    """
    def get(self):
        imgs_li = os.listdir('./static/images')
        pic_name = request.form.get('name')
        pw = request.form.get('pw')
        if pic_name in imgs_li and pw == 'admin':
            file_name = './static/images/%s' % pic_name
            file_name2 = './static/recycle/%s' % pic_name
            shutil.move(file_name, file_name2)
            return "200"
        else:
            return "401"

    def post(self):
        return self.get()


class Revolve(Resource):
    def get(self):
        """
        旋转图片，将图片存到images文件夹里
        :return: 200
        """
        pic_name = request.form.get('name')
        pw = request.form.get('pw')
        imgs_li = os.listdir('./static/images')
        print(pic_name, imgs_li, pw, pic_name)
        if pic_name in imgs_li and pw == 'admin':
            file_name = './static/images/%s' % pic_name
            img = Image.open(file_name)  # 打开图片
            img3 = img.transpose(Image.ROTATE_90)  # 旋转 90 度角。
            img3.save(file_name)
            return "200"
        else:
            return "401"

    def post(self):
        return self.get()