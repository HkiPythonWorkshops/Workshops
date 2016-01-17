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

Let's create a child template that will hold the actual content of our app. Under the *templates* directory, add a new file called e.g. ``mainpage.html``. Now the key thing is to link this new template to our existing template, which we do by adding an ``extend``statement to the top: 

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