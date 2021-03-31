from flask import Flask
from config import config_map, Config
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_session import Session
from flask_wtf import CSRFProtect
import logging
from logging.handlers import RotatingFileHandler

# 创建数据库对象
db = SQLAlchemy()

# 创建redis连接对像
redis_story = None

# # 为flask补充csrf防护机制
# csrf = CSRFProtect()


# 设置日志的记录登记
logging.basicConfig(level=logging.DEBUG) # 调试debug级
# 创建日志记录器，指明日志保存的路径，每个日志文件的最大大小，保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*124*100, backupCount=10)
# 创建日志记录的格式
formatter = logging.Formatter("%(levelname)s %(filename)s:%(lineno)d %(message)s")
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象添加日志记录器
logging.getLogger().addHandler(file_log_handler)


# 将app对象设置成工厂模式
def create_app(config_name):
    '''
    创建flask的应用对象
    :param config_name: str 配置模式的名字（'develop','product'）
    :return: 返回具体的app对象
    '''

    app = Flask(__name__)
    # 启动项目的时候选择模式
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)
    # 将数据库和flask app绑定
    db.init_app(app)

    # 初始化连接redis数据库
    global redis_story
    redis_story = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT, db=2)

    # 利用flask-session，将session数据保存到redis中
    Session(app)  # 修改flask里面的session机制
    # 为flask补充CSRF机制
    CSRFProtect(app)  # 就是flask的钩子函数实现的

    # 注册蓝图
    from .api_v1_0 import api
    app.register_blueprint(api)

    return app
