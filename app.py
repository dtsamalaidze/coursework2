from flask import Flask
from post.post_views import post_app
from main_views import main_app
from user_feed.user_feed_views import user_feed_app
from search.search_views import search_app

app = Flask(__name__)

app.register_blueprint(main_app, url_prefix='/')
app.register_blueprint(post_app, url_prefix='/post')
app.register_blueprint(search_app, url_prefix='/search')
app.register_blueprint(user_feed_app, url_prefix='/user_feed')

if __name__ == '__main__':
    app.run(host='localhost', debug=True)
