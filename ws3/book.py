class Book(object):

	def __init__(self, id, title, author, pagecount):
		self.id = id
		print "Creating new book"
		print title, author, pagecount
		self.update_book(title, author, pagecount)

	def get_book(self):
		data = {
			'id': self.id,
			'title': self.title,
			'author': self.author,
			'pagecount': self.pagecount
		}
		return data

	def get_index(self):
		data = {
			'id': self.id,
			'title': self.title,
			'author': self.author,
		}
		return data

	def update_book(self, title, author, pagecount):
		self.title = title
		self.author = author
		self.pagecount = pagecount
		print title, author, pagecount
