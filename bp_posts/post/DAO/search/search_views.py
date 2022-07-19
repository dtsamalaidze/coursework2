from flask import Blueprint, request, render_template
from bp_posts.post.DAO.posts import Posts


search_app = Blueprint('search', __name__, template_folder='templates', static_folder='static')
posts = Posts()


@search_app.route('/')
def search_result():
    query = request.args.get('search')
    find_posts = posts.get_post_by_word(str(query))
    return render_template("search.html", posts=find_posts, count_posts=len(find_posts))
