## Environment
python => 3



## 安装依赖包

    pip install -r requirements.txt



## 使用flask命令，必须先设置：

设置flask的app(windows和linux的环境变量命令不一样，项目根目录下执行)

    set FLASK_APP=manage.py(windows)

    export FLASK_APP=manage.py(linux)


然后创建管理员账号（账号：admin，密码：123456，项目根目录下执行）

    flask initdata


## 开发环境

    python manage.py


## 生产环境

    gunicorn -c gunicorn_config.py manage:app
