import os
from flask import Flask


def create_app(test_config=None):
    # 创建一个app并返回
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # 保证数据安全
        SECRET_KEY='dev',
        # 数据库存放路径
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # 确保当前路径存在
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # 示例
    @app.route('/hello')
    def hello():
        return "Hello Flask!"

    return app
