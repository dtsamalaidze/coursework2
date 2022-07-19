import json
import config

class Posts:
    def __init__(self,
                 poster_name='',
                 poster_avatar='',
                 pic='',
                 content='',
                 views_count=0,
                 likes_count=0,
                 pk=0
                 ):
        self.poster_name = poster_name
        self.poster_avatar = poster_avatar
        self.pic = pic
        self.content = content
        self.views_count = views_count
        self.likes_count = likes_count
        self.pk = pk

    def __repr__(self):
        return f'Posts('\
                f'{self.poster_name}, '\
                f'{self.poster_avatar}, '\
                f'{self.pic}, '\
                f'{self.content}, '\
                f'{self.views_count}, '\
                f'{self.likes_count}, '\
                f'{self.pk}'\
                f')'

    def get_posts_all(self) -> list[dict]:
        """
        Функция загружает все посты из файла json
        :return: Список словарей с постами
        """
        with open(config.Config.POSTS_PAHT, 'r', encoding='utf-8') as f:
            posts = json.load(f)
            return posts

    def get_post_by_post_id(self, post_id: int) -> dict:
        """
        из списка словаерей получает словарь с указанным id
        :param post_id: id поста
        :return: словарь с постом
        """
        p = None
        if type(post_id) != int:
            raise TypeError(f'{post_id} не является числом')
        for post in self.get_posts_all():
            if post['pk'] == post_id:
                p = post
        return p


    def get_post_by_word(self, word: str) -> list[dict]:
        """
        Из списка словаерей с постами получает словарь с постам в тексте которых встречается искомое слово
        :param post_id: Искомое слово или строка
        :return: словарь с постом
        """
        posts = []
        if type(word) != str:
            raise TypeError(f'{word} не является строкой')
        for post in self.get_posts_all():
            if word.lower() in post['content'].lower():
                posts.append(post)
        return posts

    def get_post_by_user(self, user: str) -> list[dict]:
        """
        Возвращает список словарей всех постов выбранного пользователя
        :param user: имя пользователя
        :return: список словарей
        """
        posts = []
        if type(user) != str:
            raise TypeError(f'{user} не является строкой')
        for post in self.get_posts_all():
            if post['poster_name'].lower() == user.lower():
                posts.append(post)
        return posts


