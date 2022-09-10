## Assignment 2

This project is dedicated to Platform Based Development course assignment 2
<br>Deployed on Heroku [https://marcell-assignment2-pbp.heroku.app](https://marcell-assignment2-pbp.heroku.app).

## Diagram Django Flow
<img width="1136" alt="Screen Shot 2022-09-10 at 11 45 57" src="https://user-images.githubusercontent.com/51221428/189469316-aceb8dc4-9a23-4c72-9424-6992b9ea74b2.png">

First, client requests is processed by middlewares and then passed the request to URL router. If URL match or defined, the function in views.py called. Then views will query to models and the models return result of the query to the views. After that the views will return response to user in the form of html

## Can We Build a Django App Without Virtual Env?
Absolutely! You can build and run Django app without virtual environment initialized. However, when you try to install any Django package, it will be installed on your global package. Virtual environment prevents you from installing Python packages globally by making an isolated python environment for each project. 

Creating virtual env is highly recommended because when you have your virtualenv activated and try to `pip freeze < requirements.txt` it allows you to write all the dependencies used for the project, not all dependencies globaly. 

## About This Assignment
This assignment main goal is to <b>show catalog list on `/katalog`</b>. First thing first is to create a katalog app. If you are using the assignment template, creating a new catalog app isn't necessary.

### Configuring views.py

In template, there's an katalog.html created, all we need to do is to render the html in `/katalog`. First we need to create a function to render in views.py. We can define a function that accept an argument and returns a rendered html using the render method from Django. This render method accepts request and html file as an argument. 

Since we need to show some data such as, name, student id, and catalog data from initial_catalog_data.json in CatalogItem objects so we need to create a dictionary context that stores name, student_id, and catalog data. To use catalog data we need to import CatalogItem models from katalog models and get all the catalog items objects. After that, we need to put context as the third argument in render method. 

### Configuring urls.py in project_django folder

In the previous step, views.py is configured and we need to use the function we created before. As we create the function we need to show it on the page. Our goal is to display the catalog on `/katalog` so we need to configure the routing in urls.py project_django folder. Add another path in urlpatterns list with first argument 'katalog' since we want to show it on `/katalog`, first argument in path method is the route and the second argument is the katalog.urls to point urls in katalog app. 

### Configuring urls.py in katalog app
We have configured routing in base project, the next step is to configure routing in `/katalog`. Since we want to show it on `/katalog` so we need to configure the katalog urls pattern with empty string for the route, fill second argument with function we made before, and third argument with app name.
Tada! the html is rendered on `/katalog`

### Use the context in katalog.html
Previously in views.py method we have created a context and pass it to the render method. So we can use the context in html using {{[variable]}} syntax, such as {{name}} to render name variable in context. Then we can iterate through the data catalog using for loop and show each katalog data on table row.

### Deployment

Since in the template the Procfile, settings.py, github actions is configured, we just need to add secrets variable on github actions. 
Go to the repository -> settings -> secrets -> github action. Then add new variable with key HEROKU_API_KEY and value is your Heroku Account Key (Heroku -> Account Settings -> API key). Also add another variable with key HEROKU_APP_NAME and value is your heroku_app_name.

