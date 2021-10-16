class Booklist():
    def __init__(self):
        self.books = []

    def add(self, title: str, author: str):
        book = {}
        book['title'] = str(title)
        book['author'] = str(author)
        self.books.append(book)

    def count_books(self):
        return len(self.books)

    def remove_title(self, title: str):
        for index, book in enumerate(self.books):
            if title in book['title']:
                self.books.pop(index)

    def display_titles(self):
        titles = []
        for book in self.books:
            titles.append(book['title'])
        titles.sort()
        print(titles)


books = [{"title": "title0", "author": "author0"},
         {"title": "title1", "author": "author1"}]
print(type(books))
book_dict = books[0]
# book_dict = {"title": "title0", "author": "author0}
print(book_dict["title"])

print(books[0]["title"])
