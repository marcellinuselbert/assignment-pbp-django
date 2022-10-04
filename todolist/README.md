## Assignment 4

This app is dedicated to Platform Based Development course assignment 4 and 5
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
  
  ## Assignment 5

## Inline vs External vs Internal CSS

Dalam menggunakan CSS ada beberapa cara yang dapat diterapkan. Inline, External, atau Internal CSS. Perbedaannya ada pada letak penulisan styling. Untuk inline berarti meletakkan CSS property pada attribute atau props html tag. Misalnya, `<p style="font-size:21px;">Hello Bakung!</p>`. Selain itu, untuk External CSS adalah meletakkan CSS atribute di luar dari file html. Caranya dengan membuat file baru dengan extension .css dan melakukan import pada html yang ingin diaplikasikan style dari file css tersebut. Import dapat dilakukan seperti ini ` <link rel="stylesheet" href="bakung21.css"/>` dengan anggapan file .css bernama bakung21.css. Selain itu CSS juga bisa diaplikasikan secara internal di dalam html dengan memanfaatkan `<style>` tag. Isi dari tag tersebut sama caranya dengan mengisi css property pada file external. 

Menurut saya pribadi, untuk inline kelebihannya adalah pada saat kasus hanya ingin mengaplikasikan untuk beberapa tag saja dan stylingnya tidak banyak. Kelemahannya untuk styling yang sudah complex menurut saya akan menimbulkan code smell karena property atau attribute style akan jadi panjang sekali. Untuk external menurut saya merupakan best practice untuk mengaplikasikan banyak styling atau yang sudah complex karena bisa membuat banyak css property. Namun menurut saya kurang efektif untuk style yang hanya sedikit dan dibeberapa tag/line saja. Untuk internal, menurut saya kurang lebih mirip kasusnya dengan inline, baik untuk kasus styling yang tidak kompleks karena ketika sudah banyak akan menjadi code yang tidak clean. Namun kelebihannya, kalian tidak perlu untuk membuat style.css dan tidak perlu melakukan import file. Dengan menggunakan <style> tag bisa langsung mengaplikasikan CSS di HTML-nya. 

## HTML Tags

HTML tag yang saya tau adalah `<div>` tag, div tag ini adalah suatu tag yang merepresentasikan sebuah section atau block. Kemudian ada tag <input> untuk menerima input dari user, bisa berupa text field atau button submit, checkbox, dll. Kemudian ada tag <title></title> tag title ini merupakan tag yang berhubungan title yang ada di tab browser. Kemudian ada <button> yang merupakan tag implentasi button. Kemudian ada <a> untuk hyperlink. <img> untuk menampilkan gambar dan masih banyak lagi tag-tag HTML yang selain saya mention di sini. 

