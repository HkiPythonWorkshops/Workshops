# Workshop 3 Material

### Important Links

**Requests Library**

* [Requests Library](http://docs.python-requests.org/)
* [Requests API documentation](http://docs.python-requests.org/en/latest/api/)

**Background reading about REST APIs, HTTP Methods etc**: 
* [REST API tutorial](http://www.restapitutorial.com/)
* [RESTful API design](http://restful-api-design.readthedocs.org/en/latest/intro.html)

### Pre-Requirements
* [Python](https://github.com/HkiPythonWorkshops/Workshops)
* install requests with **Pip**  
```pip install requests```

#### Check your Requests installation

Create a new file and call it e.g. test_requests.py. 

The first thing we want to do is import Requests:
```python
import requests
```

## REST APIs and the underlying data


### Resources and collections

REST APIs are built around **resources** and **collections** of resources.

Let's say we have a REST API to communicate with a library database. 

We could have the following collections and sub-collections:

```
books 
    - cookbooks
    - non-fiction books
    - fiction books
audio
    - music
    - audio books
```

So here, **books** is a collection with 3 sub-collections, which then have the actual resources associated with them.

The idea of the REST API is to communicate with these resources and collections in a structured way. 

For example, we might want to make the following requests to the database:
* Give us a list of all the audio books.
* Change the name of the author for cookbook with the name "Delicious Soups" to "Kate Smith".
* Create a new book called "Learning Python"  by Mark Lutz, in the non-fiction collection. 
* Delete the non-fiction book with ID 8571415.

### REST API URLs

A REST API needs an **entry point**, which is usually an URL where we send the requests. 

For our library, it might be, for example: 

```
http://samplelibrarydatabase.com/api/
```

Building on this, each collection and resource type has its own URL where we send the requests. 

For our sample API, this could be: 


```
http://samplelibrarydatabase.com/api/books
http://samplelibrarydatabase.com/api/books/cookbooks
http://samplelibrarydatabase.com/api/books/fiction
http://samplelibrarydatabase.com/api/books/nonfiction
http://samplelibrarydatabase.com/api/audio
http://samplelibrarydatabase.com/api/audio/music
http://samplelibrarydatabase.com/api/audio/audiobooks
```
Usually in API documentation, you only give the entry point and then the address of the different resources: 

```
Entrypoint: 
http://samplelibrarydatabase.com/api/

Books API: 
 /books
 /books/cookbooks
 /books/fiction
 /books/nonfiction
 /audio
 /audio/music
 /audio/audiobooks
```

### Responses

The data returned is usually in XML or JSON format, depending on the API, the type of resource being requested, and the request itself.

Requests also return a **status code**.

| Status Code        | Meaning           | Comments  |
| ------------- |:-------------:| -----|
| 200      | OK | Request was successfull |
| 201      | Created      |   The resource was created successfully |
| 204 | No Content     |    The request was successfull but there's no content to send back |
| 400 | Bad Request | The requests could not be understood, e.g. due to bad syntax |
| 403 | Forbidden | The request was understood but you need authorization to get a proper response. |
| 404 | Not Found | The request didn't match any resource. |

See the full list of status codes [here](http://www.restapitutorial.com/httpstatuscodes.html)

## HTTP Methods

HTTP Methods or "verbs" are used to communicate with APIs. We send in a request using the appropriate verb, and get a response code as well as some data. 

### GET

GET is used for retrieving data. It's safe in the sense that it doesn't change any data, just reads it. 

You can use it to retrieve a **collection** of items, e.g. all customers, or a specific resource in a collection by specifying some criteria in the request.

Examples: 
```
GET http://samplelibrarydatabase.com/api/books
```
Retrieve all books in the books collection

```
GET http://samplelibrarydatabase.com/api/books/nonfiction/<id>
```
Retrieve the nonfiction book with this specific ID

### POST

POST is usually used for creating a new item in a collection. The new resource will be automatically added to the correct collection and usually assigned an ID. The information needed to create a new resource depends on the type of resource and should be documented in the API docs. 

E.g. to create a book we probably need a title and name at the very least. 

```
POST http://samplelibrarydatabase.com/api/books/nonfiction title:Learning Python author:Mark Lutz
```
Create a new non-fiction book resource called "Learning Python" by Mark Lutz

### PUT

PUT is usually used for updating existing resources in a collection. The information that can be updated depends on the type of resource and should be documented in the API docs. To update a resource, we usually have to know its ID or some other identifyind feature so the server knows which resource to update. 

E.g. to update a book title, we could try: 

```
PUT http://samplelibrarydatabase.com/api/books/cookbooks/5814425 author:Kate Smith
``` 
Update the author of the cookbook resource with ID 5814425 to "Kate Smith"


### DELETE

DELETE is usually used for deleting existing resources in a collection. 

E.g. to delete a book, we could try: 

```
DELETE http://samplelibrarydatabase.com/api/books/nonfiction/8571415 
``` 
Delete the non-fiction book with ID 5814425 to "Delicious Pastries"

## Using Requests Library to make HTTP requests

```python
r = requests.get('https://api.github.com/events')
r = requests.post("http://httpbin.org/post")
```

The other HTTP methods work just the same:
```python
r = requests.put("http://httpbin.org/put")
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")
```

Usually we want to also send some data with our request. 

For example, if we need to send URL parameters: 
```python
my_parameters = {"q": "python"}
r = requests.get("http://www.google.com/search", params=my_parameters)
```

We can do the same with headers and data: 
```python
my_headers = {"Content-Type": "application/json"}
r = requests.put("http://www.google.com/search", headers=my_headers)

my_data = {"title": "Pride and Prejudice", "author":"Jane Austen"}
r = requests.put("http://samplelibrarydatabase.com/api/books/nonfiction/8571415", data=my_data)
```

