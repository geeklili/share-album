from flask import Blueprint
from flask_restful import Api

from .resource.upload import UploadPicture
from .resource.page import GetIndex, GetRecycleBin, GetDetail, GetAllUpload, GetArticle
from .resource.file import Robots, Favicon, Picture
from .resource.recycle import DeleteRecyclePicture, DeleteAllRecyclePicture, Recover
from .resource.index import DeletePicture, Revolve
from .resource.keep import CopyImage, DeleteKeep

bp = Blueprint('api', __name__, url_prefix='')
api = Api(bp, catch_all_404s=True)

# 上传图片
api.add_resource(UploadPicture, '/api/upload_row', '/upload_row')

# 获取页面
api.add_resource(GetIndex, '/', '/index')
api.add_resource(GetArticle, '/api/page', '/page')
api.add_resource(GetAllUpload, '/api/keep', '/keep')
api.add_resource(GetDetail, '/api/detail', '/detail')
api.add_resource(GetRecycleBin, '/api/recycle ', '/recycle')

# 获取静态文件
api.add_resource(Picture, '/api/pic', '/pic')
api.add_resource(Robots, '/api/robots.txt', '/robots.txt')
api.add_resource(Favicon, '/api/favicon.ico', '/favicon.ico')

# 主页图片操作
api.add_resource(Revolve, '/api/revolve', '/revolve')
api.add_resource(DeletePicture, '/api/delete', '/delete')

# 回收站图片操作
api.add_resource(Recover, '/api/add', '/add')
api.add_resource(DeleteAllRecyclePicture, '/api/clear_all', '/clear_all')
api.add_resource(DeleteRecyclePicture, '/api/delete_recycle', '/delete_recycle')

# 保有图片恢复到主页
api.add_resource(CopyImage, '/api/copy', '/copy')
api.add_resource(DeleteKeep, '/api/delete_keep', '/delete_keep')

