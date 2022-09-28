## Assignment 4

This app is dedicated to Platform Based Development course assignment 4
<br>Deployed on Heroku [https://marcell-assignment-pbp.herokuapp.com/todolist](https://marcell-assignment-pbp.herokuapp.com/todolist).

##  Kegunaan CSRF Token

`{% csrf_token %}` merupakan salah satu cara untuk mencegah adanya serangan CSRF yang disediakan oleh Django. Tanpa menggunakan `{% csrf_token %}` 
dapat menyebabkan error pada django project kita. 

##  Apakah kita dapat membuat elemen <form> secara manual

Bisa, dengan tag <form> kemudian dengan tag <input> untuk user mengetik dan <input type="submit"> sebagai input untuk click submit.

## Alur data
  
Ketika user menekan tombol submit maka akan dilakukan https request berupa post, dari request tersebut dicheck jika valid maka data dibuatkan di database, sedangkan jika
tidak maka user akan diminta untuk input ulang. Kemudian data bisa ditampilkan di html jika dibutuhkan

  
## Implementasi Tugas

  Pada tugas 4 ini pertama-tama buat app dulu menggunakan `python3 manage.py startapp todolist` , kemudian tambahkan 'todolist' di settings.py project_django
  kemudian tambahkan di urls.py project_django /todolist yang mengarahkan ke urls.py pada folder todolist. Setelah itu buat base route atau '' nya mengarahkan ke 
  function show_todolist. setelah itu buat model dengan nama Task dengan field user, date, title, dan description. Untuk user fieldnya foreinkey dengan parameter User dari `from django.contrib.auth.models import User
`.
  Form registrasi dan login kurang lebih caranya sama, yaitu dengan tag <form> dan inputnya seperti username password. Kemudian untuk handling pada views menggunakan
  auth dari module yang ada pada django. 
  
  Kemudian buat form di create.html dengan input title dan input description kemudian ada tombol submit untuk mensubmit todo baru. selain membuat form perlu juga dibuat handlenya pada views.py
  jika ditekan buttonnya maka create task baru pada model. setelah itu buat routingnya sesuai dengan kebutuhan misalnya /login, /register, /create-task. 
  
  untuk deployment kurang lebih caranya sama dengan tugas 3. karena repo ini sudah terhubung dengan github action maka hal yang dilakukan untuk deployment hanya melakukan
  git push di repository ini dan deployment sudah diotomasi oleh github action yang sudah dibuat pada tugas-tugas sebelumnya
