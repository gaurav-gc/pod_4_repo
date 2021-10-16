class Booklist():
	def __init__(self):
		# create an empty list attribute
		self.books = []
		# create an empty list attribute for storing just titles, so this info can be accessed later w/o needing to call the display_titles method again; you could also just create an empty list variable for title_list in the display_titles methods
		self.title_list = []
	# method that adds a book to books attribute
	def add(self, title, author):
		# create a dictionary called book to hold title and author values
		book = {'title': title, 'author': author}
		# add book to an attribute list called books
		self.books.append(book)
	# method that counts the number of books in the books attribute
	def count_books(self):
		# return the number of elements in the books attribute
		return len(self.books)
	# method that removes a book from the books attribut
	def remove_title(self, title):
		#loop through each book in the books attribute
		for book in self.books:
			# compare if the title of a book equals the parameter
			if book['title'] == title:
				# remove the book if it is the same as the parameter
				self.books.remove(book)
	# method that adds all the titles of the books attribute to the title_list attribute in alphabetical order
	def display_titles(self):
		# create an integer variable for counting
		count = 0
		# loop through each book in the books attribute
		for book in self.books:
			# add just the title of each book to book_list
			self.title_list.append(self.books[count]['title'])
			# add to the count variable 
			count += 1
		# sort the list of titles alphabetically
		self.title_list.sort()
		# return the list of alphabetically sorted titles
		return self.title_list

			

