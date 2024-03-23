class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(category, str):
            raise TypeError("Category must be a string")
        if not 2 <= len(name) <= 16:
            raise ValueError("Name must be between 2 and 16 characters long")
        if len(category) == 0:
            raise ValueError("Category must not be empty")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors = [author for author in self.contributors() if len(author.articles()) > 2]
        return authors if authors else None