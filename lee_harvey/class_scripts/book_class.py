class Booklist():
	def __init__(self):
		self.books = []

	def add(self, title, author):
		self.books.append({'title': title, 'author' : author})

	def count_books(self):
		return len(self.books)

	def remove_title(self, title):
		for book in self.books:   
			if book['title'] == title:
				self.books.remove(book)

	def display_titles(self):
		sorted_list = unsorted = []
		for book in self.books:
			unsorted.append(book['title'])
		sorted_list = sorted(unsorted)
		sorted_titles = []
		for title in sorted_list:
			for book in self.books:
				if title == book['title']:
					sorted_titles.append(book)
		self.books = sorted_titles
		for book in self.books:
			print(book['title'])
		
		## This worked for someone else, why won't it work for me?
		# for book in self.books:
		# 	self.books.sort()
		# print(self.books)