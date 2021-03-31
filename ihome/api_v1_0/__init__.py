from flask import Blueprint

# 创建蓝图对象
api = Blueprint('api_1_0', __name__, url_prefix='/api/v1.0')

# 导入蓝图的视图函数
from . import views