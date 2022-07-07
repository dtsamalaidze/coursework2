from flask import Flask
from post.post_views import post_app
from main_views import main_app

app = Flask(__name__)

app.register_blueprint(main_app, url_prefix='/')
app.register_blueprint(post_app, url_prefix='/post')

if __name__ == '__main__':
    app.run(host='localhost', debug=True)
