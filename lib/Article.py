class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if not 5 <= len(title) <= 50:
            raise ValueError("Title must be between 5 and 50 characters long")
        self._author = author
        self._magazine = magazine
        self._title = title
        author.articles().append(self)
        magazine.articles().append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine
