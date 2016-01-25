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

Create a new folder for this project. Inside it, create a new python file and call it e.g. ``app.py``.

Once we've done that, we can build the smallest possible Flask app:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main_page():
    return "<h1>Hello World!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
```

Now run your app with ``python app.py`` and head to **http://localhost:5000**. Keep the app running in the background during the whole session. 

## Flask: the basics

What happens in our small Flask app? For a bit more in-depth explanation go to [Flask Quickstart guide](http://flask.pocoo.org/docs/0.10/quickstart/#quickstart), but here's a short version:

1. Import the Flask class;
2. Create an instance of it. Using the ``__name__`` tells Flask this is main (and currently only) file of the app.
3. Create a function that returns a HTML fragment, then use a ``route()`` decorator to tell Flask which URLs should use it
4. If we call the file directly, it will run the app with debug mode active.

### Exercises

Add another page with a different route. Note that the current ``main_page()`` function is the root page at *localhost:5000*, and adding a route like ``route('/url2')`` can be accessed at the address *localhost:5000/url2*.

## Flask templates

Instead of having HTML inside our Python functions, which is not very nice or maintainable, Flask offers *templates*. By default the [Jinja2](http://jinja.pocoo.org/) template engine is used.

Let's add our first template. First add a ``templates``folders in your project folder. Inside that folder, add a new HTML file called e.g. ``layout.html``.

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

To see this update, you just need to refresh the page in your browser, no need to stop and start the server.

### Template inheritance

If we're building an app any bigger than one page, we probably don't want to cram everything into the same template file. Instead, we can use *template inheritance*, where our main template consists of *blocks* that are implemented in smaller child templates. For a longer explanation, go to [Flask docs](http://flask.pocoo.org/docs/0.10/patterns/templateinheritance/).

Let's create a child template that will hold the actual content of our app. Under the ``templates`` directory, add a new file called e.g. ``mainpage.html``. Now the key thing is to link this new template to our existing template, which we do by adding an ``extends``statement to the top:

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
Now when you refresh your page, it will be loaded from the child template.

### Exercises
Add a second child template and a new function in ``app.py`` with a new route that renders the new template. 


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

You could also try passing a dictionary and accessing the keys and values in a loop: ``{% for key, value in my_dict.items() %}``

## Data from an external source

Here's where the fun really begins. Let's finally start integrating data from an API to our Flask app. In this example we'll use the [Finnkino XML API](http://www.finnkino.fi/XML) as an example, but feel free to use any other data source.

Instead of putting the logic for our API managers inside our Flask app, let's create a new directory called ``services``.

Inside it, let's create a new file called e.g. ``finnkino.py`` and an empty ``__init__.py`` file. The `finnkino` module will handle making requests to the Finnkino API and parsing the data we want.

Let's start by importing some modules we'll need and creating a class with some variables.

```python
import requests
import xml.etree.ElementTree as ET

class FinnKinoXML(object):
    area_url = "http://www.finnkino.fi/xml/TheatreAreas"
    schedule_url = "http://www.finnkino.fi/xml/Schedule/"
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }
```
To do anything useful with the Finnkino API, we need to use an **area code**. Take a look at the [Areas XML](http://www.finnkino.fi/xml/TheatreAreas) and pick one area ID. Let's make a function that fetches the movies for one area. First make a GET request with the [requests library](http://docs.python-requests.org/en/latest/user/quickstart/) and then parse the XML from the response from the [showsXML](http://www.finnkino.fi/xml/Schedule/?area=1038). 

```python
def get_movies_for_area(self, area_code):
    request_url = "{}?area={}".format(self.schedule_url,
    			     area_code)
    response = requests.get(request_url, headers=self.headers)
    root = ET.fromstring(response.content)
    # Check out ElementTree docs to find out how to parse
    # elements from the response data using find() and findall()

    #return some data, e.g. a list of movie titles
    return []
```

Now call this new method in your app.py to get the data into your mainpage template. Start by importing the FinnKinoXML class from the services.finnkino package, then create an instance of the class and use its method. Then pass that as the data to your template.

When all of that works, take a look at the information in the [showsXML](http://www.finnkino.fi/xml/Schedule/?area=1038) and parse some more data out of it. Maybe an image, maybe the genres, length, or any other data you like.

If you want to display more data, you can use e.g. something like this, assuming you're passing the correct type of data to the template: 

```html
<ul>
	{% for id, movie in movies.items() %}
	<li style="list-style: none;">
		<div class="movieTitle">
			Title: {{ movie["title"] }}<br />
			Genre(s): {{ movie["genres"] }}<br />
			Rating: <img src="{{ movie['rating'] }}" alt="Ikäluokitus" /><br />
            <div id="movieImage">Image: <img src="{{ movie['image'] }}" alt="Image from the movie" /></div>
		</div>
	</li>
	{% endfor %}
</ul>
```

## Adding JavaScript

Now we have a static page with some content, but that's pretty boring. Let's add the possibility for the user to select which area we want to see movies from. 

Start by adding a new folder ``static`` in the root of your project folder. In it, add another folder called ``js``. Inside the ``js``folder, add a new file called e.g. ``app.js``.

For the JQuery to work, you also need to copy the file [jquery-1.12.0.min.js](flask-app/static/js/jquery-1.12.0.min.js) into your ``js`` folder. Also make a new folder called ``media`` under your ``static`` folder and copy the file [ajax-loader.gif](flask-app/static/media/ajax-loader.gif) there. (**NOTE**: right-clicking and doing "Save as..." doesn't work for these two files. You have to either clone the repo and get them from there, or open the links and click "Raw", and then do "Save as..."). 

At this point, your folder tree should look something like this:

```
\ app.py
\ services
   \ __init__.py
   \ finnkino.py	
\ static
   \ js
       \ app.js
       \ jquery-1.12.0.min.js
   \ media
   	   \ ajax-loader.gif
\ templates
   \ mainpage.html
   \ layout.html
```

We also need to tell our app where to find these new JQuery files. Add these lines inside the ``<head>`` element in your ``layout.html``: 

```html
<script type="text/javascript" src="{{ url_for('static', filename='js/jquery-1.12.0.min.js') }}"></script>
<script type="text/javascript" src="{{ url_for('static', filename='js/app.js') }}"></script>
```

This uses Flask's ``url_for`` method so we don't need to write the url ourselves, just give the relative path inside the project.

In ``app.js``, let's add the following JQuery snippet: 

```javascript
$(document).ready(function(){
	var $theatreAreaCodes = $("#choose_theatre");
	var $movieContainer = $("#movie_container");
	var $loader = $("#loader");

	$movieContainer.load('/movies/'+1038+' ul', function(){
		$loader.hide();
	});

	$theatreAreaCodes.on('change', function(evt){
		var url = '/movies/'+$(this).val()+" ul";
		$movieContainer.children().remove();
		$loader.show();
		$movieContainer.load(url, function(){
			$loader.hide();
		});
	});
});
```

What it does it take a value from ``choose_theatre``, then updates the values in ``movie_container`` accordingly. But wait, we don't have either of things in our app yet...

Start by adding a method in the ``finnkino.py`` service that returns a dictionary in the format {id: 'Area name'} of all the possible areas and pass as the data for your ``mainpage`` method. 

Then let's add to our ``mainpage`` a dropdown for selecting the area we're interested in, the loader gif  and replace the static movie information with a placeholder:  

```html
<div>
	<h1>Choose area:</h1>
	<select name="theatre" id="choose_theatre">
    {% for id, name in areas.items() %}
    <option value="{{ id }}">{{ name }}</option>
    {% endfor %}
	</select>
	<h1>Movie list:</h1>
	<div id="movie_container"></div>
	<img id="loader" src="{{ url_for('static', filename='media/ajax-loader.gif') }}" />
</div>

```

We also need a new template. Let's call it ``movies.html``. Let's move the things related to showing the movies to their own template:

```html
<ul>
	{% for movie in movies %}
	<li>
		<div>
			Title: {{ movie }}</br>
		</div>
	</li>
	{% endfor %}
</ul>
```

Finally, let's add a new method in our ``app.py`` that returns the movies for a certain area. 

```python
@app.route('/movies/<area>')
def movies(area):
    movies = finnkino.get_movies_for_area(area)
    return render_template("movies.html", movies=movies)
```



## Adding styles

At the moment, our app is very ugly indeed. To use a CSS file with our app, let's add a ``styles`` folder inside our ``static`` folder. Then add a new CSS file, e.g. called main.css. 

In your ``layout.html``, add a reference to your new stylesheet inside the ``<HEAD>`` element: 

```html
<link rel= "stylesheet" type= "text/css" href= "{{ url_for('static',filename='styles/main.css') }}">
```

Then start cranking out CSS! You probably want to add ``class``or ``id`` attributes to your HTML so it's easier to add styles. 

## Adding data from another API

We're fetching data from Finnkino, but how about combining that with movie reviews from [Leffatykki's API](http://www.leffatykki.com/api)? 

By now you know how to add a new service, how to fetch data from an API with ``requests`` and how to use import that service in your main app. You'll probably want to add a method in your main app where you fetch data from both APIs and combine it before it passing it onto to the movie template. 

## Build something even cooler
You now know how to use Flask to build a small web app and how to bring in data from external sources. There is a huge number of open APIs offering all kinds of data out there. Some need you to register and request an API key to access the data, but after that you'll get access to enormous amounts of data. Use your imagination to make something cool!  
