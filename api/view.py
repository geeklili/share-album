# encoding=utf-8
import datetime
import os
import shutil
import requests
from PIL import Image
from flask import render_template, Response, request, redirect, Blueprint, send_file
from lxml import etree

view = Blueprint('view', __name__)


@view.route("/upload_row/", endpoint="upload_row", methods=["GET", "POST"])
def upload_row():
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


@view.route("/pic", methods=["GET", "POST"])
def static_picture():
    """
    网页获取图片的接口，根据图片的名字来获取
    :return: 返回图片流
    """
    pic_name = request.args.get('name')
    pic_name = pic_name[:23]
    file = request.args.get('file')
    file_name = './static/%s/%s' % (file, pic_name)
    with open(file_name, 'rb') as f:
        content = f.read()
    resp = Response(content, mimetype="image/jpeg")
    return resp


@view.route("/delete", methods=["GET", "POST"])
def delete():
    """
    删除图片的接口，将图片存到回收站的文件夹里
    :return: 重定向到主页
    """
    imgs_li = os.listdir('./static/images')

    pic_name = request.form.get('name')
    pw = request.form.get('pw')
    if pic_name in imgs_li and pw == 'admin':
        file_name = './static/images/%s' % pic_name
        file_name2 = './static/images_delete/%s' % pic_name
        shutil.move(file_name, file_name2)
        return "200"
    else:
        return "401"



@view.route("/revolve", methods=["GET", "POST"])
def revolve():
    """
    旋转图片的接口，将图片存到images文件夹里
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
    else:
        return redirect("/")
    return "200"


@view.route("/delete_recycle", methods=["GET", "POST"])
def delete_recycle():
    """
    删除图片的接口，将图片存到清空站
    :return: 200
    """
    imgs_li = os.listdir('./static/images_delete')
    pic_name = request.args.get('name')
    if pic_name in imgs_li:
        file_name = './static/images_delete/%s' % pic_name
        file_name2 = './static/images_clear/%s' % pic_name
        shutil.move(file_name, file_name2)
    else:
        return redirect("/")
    return "200"


@view.route("/delete_clear", methods=["GET", "POST"])
def delete_clear():
    """
    删除清空站里的图片
    :return: 200
    """
    imgs_li = os.listdir('./static/images_clear')

    pic_name = request.args.get('name')
    if pic_name in imgs_li:
        file_name2 = './static/images_clear/%s' % pic_name
        os.remove(file_name2)
    else:
        return redirect("/")
    return "200"


@view.route("/delete_keep", methods=["GET", "POST"])
def delete_keep():
    """
    删除图片的接口，删除保有的图片
    :return: 200
    """
    imgs_li = os.listdir('./static/images_keep')
    pic_name = request.args.get('name')
    if imgs_li in imgs_li:
        file_name2 = './static/images_keep/%s' % pic_name
        os.remove(file_name2)
    else:
        return redirect("/")
    return "200"


@view.route("/add_clear", methods=["GET", "POST"])
def add_clear():
    """
    将清空站的照片恢复到回收站
    :return: 200
    """
    pic_name = request.args.get('name')
    imgs_li = os.listdir('./static/images_delete')
    if pic_name in imgs_li:
        file_name = './static/images_delete/%s' % pic_name
        file_name2 = './static/images_clear/%s' % pic_name
        shutil.move(file_name2, file_name)
    else:
        return redirect("/")
    return "200"


@view.route("/add", methods=["GET", "POST"])
def add():
    """
    添加图片的接口，将图片恢复到images文件夹里
    :return: 重定向到主页
    """
    pic_name = request.args.get('name')
    imgs_li = os.listdir('./static/images_delete')
    if pic_name in imgs_li:
        file_name = './static/images/%s' % pic_name
        file_name2 = './static/images_delete/%s' % pic_name
        shutil.move(file_name2, file_name)
    else:
        return redirect("/")
    return redirect('/miss')


@view.route('/', methods=["GET", "POST"])
@view.route('/love', methods=["GET", "POST"])
@view.route("/index", methods=["GET", "POST"])
def index():
    """
    主页，获取传递过去的图片所有信息
    :return: 返回主页html
    """
    pic_li = os.listdir('./static/images/')
    pic_li.sort(reverse=True)
    a = datetime.datetime.now()
    a = a + datetime.timedelta(0)
    time_now = datetime.datetime.strftime(a, "%Y-%m-%d")
    context = {'name': "xiaohua", 'li': pic_li, "time": time_now}
    return render_template('home.html', context=context)


@view.route("/miss", methods=["GET", "POST"])
def miss():
    """
    回收站主页，获取回收站里的图片所有信息
    :return: 返回回收站主页html
    """
    pic_li = os.listdir('./static/images_delete/')
    pic_li.sort(reverse=True)
    a = datetime.datetime.now()
    a = a + datetime.timedelta(0.5)
    time_now = datetime.datetime.strftime(a, "%Y-%m-%d")
    context = {'name': "xiaohua", 'li': pic_li, "time": time_now}
    return render_template('home_miss.html', context=context)


@view.route("/keep", methods=["GET", "POST"])
def keep():
    """
    所有照片主页，获取所有照片的图片所有信息
    :return: 返回所有照片主页html
    """
    pic_li = os.listdir('./static/images_keep/')
    pic_li.sort(reverse=True)
    a = datetime.datetime.now()
    a = a + datetime.timedelta(0.5)
    time_now = datetime.datetime.strftime(a, "%Y-%m-%d")
    context = {'name': "xiaohua", 'li': pic_li, "time": time_now}
    return render_template('home_keep.html', context=context)


@view.route("/clear", methods=["GET", "POST"])
def clear():
    """
    清空站主页，获取清空站里的图片所有信息
    :return: 返回清空站主页html
    """
    pic_li = os.listdir('./static/images_clear/')
    pic_li.sort(reverse=True)
    a = datetime.datetime.now()
    a = a + datetime.timedelta(0.5)
    time_now = datetime.datetime.strftime(a, "%Y-%m-%d")
    context = {'name': "xiaohua", 'li': pic_li, "time": time_now}
    return render_template('home_clear.html', context=context)


@view.route("/clear_all", methods=["GET", "POST"])
def clear_all():
    """
    清空回收站
    :return: 返回回收站主页html
    """
    pic_li = os.listdir('./static/images_delete/')
    for name in pic_li:
        file_name = './static/images_delete/%s' % name
        file_name2 = './static/images_clear/%s' % name
        shutil.move(file_name, file_name2)
    return "200"


@view.route('/page', methods=["GET", "POST"])
def page():
    title, author, content_li = get_one_page()
    context = dict()
    context['title'] = title
    context['author'] = author
    context['content_li'] = content_li
    a = datetime.datetime.now()
    a = a + datetime.timedelta(0.5)
    time_now = datetime.datetime.strftime(a, "%Y-%m-%d")
    context['time'] = time_now
    return render_template('home_page.html', context=context)


@view.route('/detail', methods=["GET", "POST"])
def detail():
    pic_name = request.args.get('name')
    context = dict()
    context['detail_name'] = pic_name
    return render_template('home_detail.html', context=context)


@view.route('/robots.txt', methods=["GET", "POST"])
def robots():
    return send_file('./static/robots/robots.txt')


@view.route('/favicon.ico', methods=["GET"])
def favicon():
    return send_file('./static/favicon/favicon.ico')


def get_one_page():
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
               "Accept-Encoding": "gzip, deflate, br",
               "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
               "Connection": "keep-alive",
               "Host": "www.meiriyiwen.com",
               "Upgrade-Insecure-Requests": "1",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36", }

    ret = requests.get('https://meiriyiwen.com/random', headers=headers)
    selector = etree.HTML(ret.text)
    title = selector.xpath('//*[@id="article_show"]/h1/text()')[0]
    author = selector.xpath('//*[@id="article_show"]/p/span/text()')[0]
    content_li = selector.xpath('//*[@id="article_show"]/div[1]/p/text()')
    return title, author, content_li
