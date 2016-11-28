# -*- coding:utf-8 -*-
from flask import Flask, Blueprint, url_for

app = Flask(__name__)


shop = Blueprint("shop", __name__)
admin = Blueprint("admin", __name__, static_folder='ezstatic', static_url_path='/assets')

@shop.route('/')
def shop_index():
    return 'shop index. go to <a href="{}">admin</a>'.format(url_for("admin.admin_index"))

@admin.route('/')
def admin_index():
    return 'admin index. go to <a href="{}">shop</a>'.format(url_for("shop.shop_index"))


# register blueprint on app
app.register_blueprint(shop, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')
print app.url_map

if __name__ == '__main__':
    app.run()
