import os
import shutil
import datetime
from PIL import Image
from flask_restful import Resource
from flask import redirect, request


class UploadPicture(Resource):
    """实体名称消歧联想"""

    def get(self):
        """
            上传图片，保存到服务器本地
            文件对象保存在request.files上，并且通过前端的input标签的name属性来获取
            :return: 重定向到主页
            """
        fp = request.files.get("f1")

        if fp is not None:
            now_date = datetime.datetime.now()
            uid = now_date.strftime('%Y-%m-%d-%H-%M-%S')

            # 保存文件到服务器本地
            file = "./static/images/%s.jpg" % uid
            file_keep = "./static/images_keep/%s.jpg" % uid
            fp.save(file)
            shutil.copy(file, file_keep)

            with open(file, 'rb') as f:
                if len(f.read()) < 100:
                    os.remove(file)
                    pass
                else:
                    im = Image.open(file)
                    x, y = im.size
                    y_s = int(y * 1200 / x)

                    out = im.resize((1200, y_s), Image.ANTIALIAS)

                    uid2 = now_date.strftime('%Y-%m-%d-%H-%M-%S')
                    # 保存文件到服务器本地
                    file2 = "./static/images/%s.jpg" % uid2
                    if len(out.mode) == 4:
                        r, g, b, a = out.split()
                        img = Image.merge("RGB", (r, g, b))
                        img.convert('RGB').save(file2, quality=10)
                    else:
                        out.save(file2)
        else:
            print('没有选择文件')
        return redirect("/")

    def post(self):
        return self.get()
