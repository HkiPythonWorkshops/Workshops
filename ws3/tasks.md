# Workshop 3 Material

### Important Links

**Requests Library**

* [Requests Library](http://docs.python-requests.org/)
* [Requests API documentation](http://docs.python-requests.org/en/latest/api/)


### Pre-Requirements
* Install the needed libraries: 

```python
pip install -r requirements.txt
```

## Run the demo app

```python
python app.py
```

Then go to **http://localhost:8080**. You should see **[]**, which is the empty list of books we currently have there.

## API Documentation for the demo app

HTTP method | url | params | returns
------------|-----|--------|--------
GET | / | None | [{id:0, title:"...", author:"..."}, ...]
GET | /book/`<id>` | None | {id:0, title:"...", author: "...", pagecount:"..."} / 404
PUT | /book/`<id>`/update | title (string), author (string), pagecount (string) | 200 / 404
POST | /book/new | title (string), author (string), pagecount (string) | 201
DELETE | /book/`<id>`/delete | None | 200 / 404

## Create a book

Our website isn't very interesting until we create our first book. As usual, we use POST to create a new resource in our collection of books:

```python
new_book = {'title': "Pride and Prejudice", "author":"Jane Austen", "pagecount":"400"}
response = requests.post("http://localhost:8080/book/new", data=new_book)
```

As the response, you get a Response object. See the documentation for them here: [Response objects](http://docs.python-requests.org/en/latest/api/#requests.Response)

The response has multiple properties we're interested in: 

```python
response.status_code
response.text
response.url
```

Now if you open http://localhost:8080 again, you should see your new book there. 

Create a few more books!

## Get book data

Find the book's ID that you want to get. Then we'll use GET to request the data for that book:

```python
response = requests.get("http://localhost:8080/book/<id>")
```

Check the response code and then the text to see we got the data we wanted. 

Try getting data for a book that doesn't exist and see what happens!

## Update a book

Find the book's ID that you want to update. Then use PUT:

```python
update_data = {'title': "Sense and Sensibility", "author":"Jane Austen", "pagecount":"390"}
response = requests.post("http://localhost:8080/book/<id>/update", data=update_data)
```

Check the response code to see that the update was successfull. 

Try updating a book with an ID that doesn't exist and see what happens. 

To confirm the book was updated, GET the book data for the book we just updated using the GET from the previous task. 

## Delete a book

Find the book's ID that you want to update. Then use DELETE to delete the resource:

```python
response = requests.delete("http://localhost:8080/book/<id>/delete")
```

Check the response code to see that the update was successfull and try GET on that ID to see the resource was really deleted. 

## Real-world API examples

### GitHub API

** [GitHub API docs](https://developer.github.com/v3/)**

* Entrypoint: https://api.github.com

E.g. getting the commits for this repo:

* GET /repos/:owner/:repo/commits

```python
requests.get("https://api.github.com/repos/HkiPythonWorkshops/Workshops/commits").json()
```
### WikiMedia API

** [WikiMedia API docs](http://www.mediawiki.org/wiki/API:Main_page)**

* Entrypoint:   http://en.wikipedia.org/w/api.php
* 
Get English Wikipedia's Main Page: 

```python
headers = {"User-Agent":"Learning Python"}
query = {"action":"query", "prop":"revisions", "titles":"Main Page", "rvprop":"content", "format":"json"}
r= requests.get("http://en.wikipedia.org/w/api.php", headers=headers,params=query)
```
