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

    def get_post_by_word(self, word):
        posts = []
        for post in self.get_posts_all():
            if word.lower() in post['content'].lower():
                posts.append(post)
        return posts

"""s = Posts()


print(len(s.get_post_by_word('опять')))

"""