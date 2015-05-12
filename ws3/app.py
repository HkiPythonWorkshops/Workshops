from bottle import route, run, template, response, request, HTTPResponse
import json
from book import Book
import sys

books = []
cur_id = 0

def get_books():
	return books

def parse_content(request):
	title = request.forms.get('title')
	author = request.forms.get('author')
	pagecount = request.forms.get('pagecount')
	print("parse_content", title, author, pagecount)
	return title, author, pagecount

@route('/')
def index():
	data = []
	for book in books:
		data.append(book.get_index())
	json_val = json.dumps(data)
	response.content_type = "application/json"
	return json_val

@route('/book/new', method='POST')
def new_book():
	global cur_id
	print(request)
	title, author, pagecount = parse_content(request)
	print("new_book", title, author, pagecount)
	books.append(Book(cur_id,title,author,pagecount))
	cur_id+=1
	return HTTPResponse(status=201)

@route('/book/<id>/delete', method='DELETE')
def delete_book(id):
	if isinstance(id, str):
		id = int(id)
	ind = id-1
	book = None
	try:
		books.pop(ind)
		return HTTPResponse(status=200)
	except:
		return HTTPResponse(status=404)

@route('/book/<id>')
def book_info(id):
	if isinstance(id, str):
		id = int(id)
	try:
		book = books[id]
		response.content_type = "application/json"
		return json.dumps(book.get_book())
	except:
		return HTTPResponse(status=404)

@route('/book/<id>/update', method="PUT")
def update_book(id):
	title, author, pagecount = parse_content(request)
	if isinstance(id, str):
		id = int(id)
	try:
		books[id].update_book(title, author, pagecount)
		return HTTPResponse(status=200)
	except :
		print("Unexpected error:", sys.exc_info()[0])
		return HTTPResponse(status=404)

run(host='localhost', port=8080)

