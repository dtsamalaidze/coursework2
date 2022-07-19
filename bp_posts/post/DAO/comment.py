import json

from config import Config
from exceptions.exceptions import FileTypeError


class Comment:
    def __init__(self, path=Config.COMMENT_PATH):
        self.path = path

    def get_comments_all(self) -> list[dict]:
        """
        Загружает все комментарии из файла json
        :return: Список словарей с комментариями
        """
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                comments = json.load(f)
            return comments
        except AttributeError:
            raise FileTypeError()

    def get_comments_by_post_id(self, post_id: int) -> list[dict]:
        """
        Из списка словарей всех комментариев получает список словарей комментариев к выбранному посту
        :param post_id: id поста
        :return: список словаей
        """
        comments = []

        for comment in self.get_comments_all():
            if comment['post_id'] == post_id:
                comments.append(comment)
        return comments

