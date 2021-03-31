import redis

class Config:
    '''配置信息'''
    SECRET_KEY = "jdfisdfijfd"
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:xiayanxia12@127.0.0.1:3306/ihome"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    #redis 配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    #flask-session配置
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.StrictRedis(host='127.0.0.1', port=6379, db=2)
    SESSION_USE_SIGNER = True # 对cookie中的session_id 进行影藏
    PERMANENT_SESSION_LIFETIME = 3600 #设置session的有效期时间

class DevelopmentConfig(Config):
    '''开发模式的配置信息'''
    DEBUG = True

class ProductConfig(Config):
    '''生产环境的配置信息'''
    DEBUG = False

# 配置模式的映射关系
config_map = {
    'develop': DevelopmentConfig,
    'product': ProductConfig
}