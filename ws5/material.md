# Flask and Open APIs

Flask docs are here: [Flask Doc](http://flask.pocoo.org/)

For a nice Flask tutorial which covers the stuff here and a lot more, see [Flask Quickstart guide](http://flask.pocoo.org/docs/0.10/quickstart/#quickstart).

* List of Finnish open APIs: 
[API suomi](http://apisuomi.fi/rajapinnat-kompaktisti/) 
* API search: [http://apis.io/](APIs.io) 

### Pre-Requirements
* [Python](https://github.com/HkiPythonWorkshops/Workshops)
* install flask with **Pip**  
```pip install flask```
* or see this [doc](http://webprojects.eecs.qmul.ac.uk/fa303/pgs/install.html) (win/linux/osx)

Note: This tutorial should work with both Python 2 and 3. 

## Import and set up Flask

Create a new file and call it app.py. 

The first thing we want to do is import Flask to check that it's installed correctly:
```python
import flask
```

Once we've done that, we can build the smallest possible Flask app, e.g. in a file called _app.py_: 

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main_page():
    return "<h1>Hello World!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
```

Now run your app with ``python app.py`` and head to http://localhost:5000.

## Flask: the basics

What happens in our small Flask app? For a bit more in-depth explanation go to [Flask Quickstart guide](http://flask.pocoo.org/docs/0.10/quickstart/#quickstart), but here's a short version: 

1. Import the Flask class; 
2. Create an instance of it. Using the ``__name__`` tells Flask this is main (and currently only) file of the app. 
3. Create a function that returns a HTML fragment, then use a ``route()`` decorator to tell Flask which URLs should use it
4. If we call the file directly, it will run the app with debug mode active.

### Exercises

Add another page with a different route. Note that the current ``main_page()`` function is the root page at *localhost:5000*, and adding a route like ``route('/url2')`` can be accessed at the address *localhost:5000/url2*.

## Flask templates

Instead of having HTML inside our Python functions, which is not very nice or maintainable, Flask offers *templates*. By default the [Jinja2](http://jinja.pocoo.org/) template engine. 

Let's add our first template. First add a ``templates``folders in the same folder as your main app. Inside that folder, add a new HTML file called e.g. ``layout.html``.

Next, let's give our layout a basic skeleton: 

```html
<!DOCTYPE html>
<html>
<head />
<body>
	<h1>Hello world from the template!</h1>
</body>
</html>
```

Next, let's add an import statement and modify our main_page() so it uses this new template: 

```python
from flask import Flask, render_template

...

@app.route('/')
def main_page():
    return render_template("layout.html")
```

### Template inheritance

If we're building an app any bigger than one page, we probably don't want to cram everything into the same template file. Instead, we can use *template inheritance*, where our main template consists of *blocks* that are implemented in smaller child templates. For a longer explanation, go to [Flask docs](http://flask.pocoo.org/docs/0.10/patterns/templateinheritance/). 

Let's create a child template that will hold the actual content of our app. Under the *templates* directory, add a new file called e.g. ``mainpage.html``. Now the key thing is to link this new template to our existing template, which we do by adding an ``extends``statement to the top: 

```html
{% extends "layout.html" %}
{% block content %}
<div>
	<h1>Hello from a child template!</h1>
</div>
{% endblock %}
```

In our ``layout.html``, we change the body: 

```html
<body>
	<div id="content">{% block content %}{% endblock %}</div>
</body>
```

And in our ``app.py``, we change which template is being rendered: 

```python
@app.route('/')
def main_page():
    return render_template("mainpage.html")
```
Now when you refresh your page, it will loaded from the child template. 

### Exercises

Add a footer block to your ``layout.html`` and a new template that implements that block. Add e.g. a copyright string as the content of the block. 

## Let's add some data! 

So far, we've just been creating empty pages. The power of templates comes from how they can render data.

Let's start by making a simple list and passing it as the data to our mainpage. 

```python
@app.route('/')
def main_page():
    months = ["January", "February", "March", "April"]
    return render_template("mainpage.html", months=months)
```

In our template, let's make an ordered list of the items in the list inside the *content* block:

```html
<ol>
	{% for month in months %}
		<li>{{ month }}</li>
	{% endfor %}
</ol>
``` 

### Exercises

Experiment with passing different kinds of and more than one variable to the template. Go to  [Jinja template docs](http://jinja.pocoo.org/docs/dev/templates/) to see what kinds of operations and statements are supported by Jinja. 

## Data from an external source

Here's where the fun really begins. Let's finally start integrating data from an API to our Flask app. In this example we'll use the [Finnkino XML API](http://www.finnkino.fi/XML) as an example, but feel free to use any other data source. 

Instead of putting the logic for our API managers inside our Flask app, let's create a new directory called ``services``.

Inside it, let's create a new file called e.g. ``finnkino.py`` and an empty ``__init__.py`` file. The `finnkino` module will handle making requests to the Finnkino API and parsing the data we want. 

Let's start by importing some modules we'll need and creating a class with some variables. 

```python
import requests

class FinnKinoXML(object):
    areas = {}
    area_url = "http://www.finnkino.fi/xml/TheatreAreas"
    schedule_url = "http://www.finnkino.fi/xml/Schedule/"
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }
```
To do anything useful with the Finnkino API, we need to use an **area code**. Take a look at the [Areas XML](http://www.finnkino.fi/xml/TheatreAreas) and pick one area ID. Let's make a function that fetches the movies for one area. First make a GET request with the [requests library](http://docs.python-requests.org/en/latest/user/quickstart/) and then parse the XML from the response. 

```python
def get_movies_for_area(self, area_code):
    request_url = "{}?area={}".format(self.schedule_url, 
    			     area_code)
    response = requests.get(request_url, headers=self.headers)
    root = ET.fromstring(response.content)
    # Check out ElementTree docs to find out how to parse 
    # elements from the response data
    
    #return some data, e.g. a list of movie titles
    return []
```

Now call this new method in your app.py to get the data into your mainpage template. Start by importing the FinnKinoXML class from the services.finnkino package, then create an instance of the class and use its method. Then pass that as the data to your template.


When all of that works, take a look at the information in the [showsXML](http://www.finnkino.fi/xml/Schedule/?area=1038) and parse some more data out of it. Maybe an image, maybe the genres,  length, or any other data you like. 

 