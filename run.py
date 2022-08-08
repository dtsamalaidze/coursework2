import pytest
from flask import Flask, render_template
from bp_posts.post.DAO.post.post_views import post_app
from bp_posts.post.DAO.main.main_views import main_app
from bp_posts.post.DAO.user_feed.user_feed_views import user_feed_app
from bp_posts.post.DAO.search.search_views import search_app
from exceptions.exceptions import BaseAppExceptions

app = Flask(__name__)


@app.errorhandler(BaseAppExceptions)
def page_not_found(e: BaseAppExceptions):
    return render_template(f'{e.code}.html'), e.code


app.register_blueprint(main_app, url_prefix='/')
app.register_blueprint(post_app, url_prefix='/post')
app.register_blueprint(search_app, url_prefix='/search')
app.register_blueprint(user_feed_app, url_prefix='/user_feed')

if __name__ == '__main__':
    app.run(host='localhost', debug=True)
