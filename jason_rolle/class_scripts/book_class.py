class Booklist():
	def __init__(self):
# made the book attribute	
		self.books = []

	def add(self, title, author):
#creating empty dictionary
		book = {}
#creating key inside of dictionary
		book['title'] = title
		book['author'] = author
#appending the book dictionary to the books list in line 4, the books attribute.
		self.books.append(book)


	def count_books(self):
		return len(self.books)

	def remove_title(self, title):
		for book in self.books:
			if title == book['title']:
				self.books.remove(book)

	def display_titles(self):
		titles =[]
		for books in self.books:
			titles.append(books['title'])
		alphabetical_titles = sorted(titles)
		print (alphabetical_titles)
	


