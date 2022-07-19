import json
import config


class Comment:
    def __init__(self):
        ...

    def get_comments_all(self) -> list[dict]:
        """
        Загружает все комментарии из файла json
        :return: Список словарей с комментариями
        """

        with open(config.Config.COMMENT_PATH, 'r', encoding='utf-8') as f:
            comments = json.load(f)
        return comments

    def get_comments_by_post_id(self, post_id: int) -> list[dict]:
        """
        Из списка словарей всех комментариев получает список словарей комментариев к выбранному посту
        :param post_id: id поста
        :return: список словаей
        """
        comments = []
        if type(post_id) != int:
            raise TypeError(f'{post_id} не является числом')
        for comment in self.get_comments_all():
            if comment['post_id'] == post_id:
                comments.append(comment)
        return comments

