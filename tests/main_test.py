import pytest

from bp_posts.post.DAO.comment import Comment
from bp_posts.post.DAO.posts import Posts


class TestMain:

    @pytest.fixture
    def post_dao(self):
        posts_instance = Posts('post_mock.json')
        return posts_instance

    @pytest.fixture
    def comment_dao(self):
        comment_instance = Comment('comment_mock.json')
        return comment_instance

    def test_get_all_types(self, post_dao):
        posts = post_dao.get_posts_all()
        assert type(posts) == list, "Не правильный тип данных"

        post = post_dao.get_posts_all()[1]
        assert type(post) == dict, "Не правильный тип данных"

    def test_get_post_by_user(self, post_dao):
        name = 'leo'
        posts = post_dao.get_post_by_user(name)
        assert type(posts) == list, "Не правильный тип данных"
        for post in posts:
            assert name in post['poster_name'], f'Пост не принадлежит {name}'

    def test_get_post_by_word(self, post_dao):
        word = 'кот'
        posts = post_dao.get_post_by_word(word)
        assert type(posts) == list, "Не правильный тип данных"
        for post in posts:
            assert word in post['content'], f"Слово {word} -  не содержится в посте"

    def test_get_all_fields(self, post_dao):

        post = post_dao.get_posts_all()[1]
        fields = [
            'poster_name',
            'poster_avatar',
            'pic',
            'content',
            'views_count',
            'likes_count',
            'pk'
        ]

        for field in fields:
            assert field in post.keys(), f'Нет поля {field}'

    def test_get_post_by_post_id(self, post_dao):
        posts = post_dao.get_post_by_post_id(1)
        assert type(posts) == dict, "Не правильный тип данных"
        assert posts["pk"] == 1, "Не правильный ID поста"

    def test_get_comments_all(self, comment_dao):
        comment = comment_dao.get_comments_all()
        assert type(comment) == list, "Не провильный тип данных"

    def test_get_comment_by_post_id(self, comment_dao):
        post_id = 1
        comments = comment_dao.get_comments_by_post_id(post_id)
        for comment in comments:
            assert post_id == comment['post_id'], 'Не верный ИД поста'
