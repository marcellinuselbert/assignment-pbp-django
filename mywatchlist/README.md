## Assignment 3

This app is dedicated to Platform Based Development course assignment 3
<br>Deployed on Heroku [https://marcell-assignment-pbp.herokuapp.com](https://marcell-assignment-pbp.herokuapp.com).

## JSON vs XML vs HTML

JSON or JavaScript Object Notation big difference between XML and HTML is JSON doesnt use any tag. JSON can be parsed by standad Java Script function. While XML
need to be parsed by XML parser. Furthermore, JSON supports array which more structured than XML. XML and JSON is more focused on delivering data. HTML is focused on presentation of the data

## Why We need Data Delivery on a Platform

Using any data delivery make data easily to sent between computers or maybe platform. 

## Assignment Implementation

Create an app called mywatchlist using `python3 manage.py startapp mywatchlist`

Next step, add mywatchlist app into `INSTALLED_APPS` on project_django/settings.py. After that on project_django/urls.py add an url to mywatchlist, `path('mywatchlist/',include('mywatchlist.urls'))`
then create urls.py on /mywatchlist to route the /mywatchlist to views.py

After that, create MyWishList model with watched boolean field, title charfield limit to 100, rating 0-5 integer field, release_date date field, and review text field and migrate the models
`python3 manage.py makemigrations` and `python3 manage.py migrate`

## Postman 

### HTML Response
<img width="1277" alt="Screen Shot 2022-09-17 at 23 08 00" src="https://user-images.githubusercontent.com/51221428/190867648-d6aa540d-ac09-4621-975a-8e86a2658b77.png">

### XML Response
<img width="1274" alt="Screen Shot 2022-09-17 at 23 08 10" src="https://user-images.githubusercontent.com/51221428/190867659-1dc5a4c0-52d6-42ac-9da8-f3404b0bc6f2.png">

### JSON Response
<img width="1270" alt="Screen Shot 2022-09-17 at 23 08 21" src="https://user-images.githubusercontent.com/51221428/190867663-c6c2f4a5-508d-4f67-9357-8f9220d1ed0a.png">
