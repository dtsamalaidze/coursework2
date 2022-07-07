import json


class Posts:
    def __repr__(self):
        return 'Класс постов'

    def __init__(self):
        ...

    def get_posts_all(self) -> list[dict]:
        with open('data/data.json', 'r', encoding='utf-8') as f:
            posts = json.load(f)
            return posts

    def get_comments_all(self) -> list[dict]:
        with open('data/comments.json', 'r', encoding='utf-8') as f:
            comments = json.load(f)
            return comments

    def get_post_by_post_id(self, post_id) -> list[dict]:
        p = None
        for post in self.get_posts_all():
            if post['pk'] == post_id:
                p = post
        return p

    def get_comments_by_post_id(self, post_id: int) -> list[dict]:
        comments = []
        for comment in self.get_comments_all():
            if comment['post_id'] == post_id:
                comments.append(comment)
        return comments


"""
    def get_posts_by_user(self, user_name: str) -> [list, str]:
        result = []
        is_author = False
        for post in self.get_posts_all():
            if post['poster_name'].lower() == user_name.lower():
                is_author = True
                result.append(post)
        if not is_author:
            return 'Пользователь не зарегистрирован'
        else:
            return result

"""