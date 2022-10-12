## Assignment 6

<br>Deployed on Heroku [https://marcell-assignment-pbp.herokuapp.com/todolist](https://marcell-assignment-pbp.herokuapp.com/todolist).

## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Synchronous programming adalah progam yang berjalan secara sequential. Ketika suatu perintah dieksekusi maka harus menunggu sampai perintah tersebut selesai dieksekusi
dan pindah ke baris selanjutnya. Task akan berjalan secara urut. 

Pada Asynchrinous programming, program bisa dijalankan secara _concurrent_ karena program tidak perlu menunggu suatu proses selesai terlebih dahulu. Dengan asynchronous programming
suatu program bisa dieksekusi secara parallel

## Event-Driven Programming

Event Driven Programming adalah ketika suatu program dieksekusi berdasarkan event yang ada. Misalnya ketika sebuah button di click maka akan dijalankan fungsi sesuatu
Fungsi ini dijalankan setiap kali button diclick. Dengan kata lain fungsi tersebut dijalankan jika terdapat event yaitu berupa click


## Jelaskan penerapan asynchronous programming pada AJAX.

Asynchronous pada AJAX berarti ketika method POST selesai dieksekusi maka langsung dieksekusi method setelah postnya. Misalnya pada tugas 6 ini ketika 
POST dijalankan dan memanggil fungsi add pada views. ketika selesai dibuat object baru maka langsung dieksekusi penambahan card sehingga tidak memerlukan reload
untuk menampilkan card barunya

## Implementation

Pertama-tama buat endpoint /todolist/json sebagai endpoint yang berisi data todo. Kemudian buat script jquery yang melakukan request get ke endpoint /todolist/json
Setelah itu, lakukan map function pada data. Map mirip dengan for yaitu melakukan iterasi setiap elemen. setiap iterasinya tambahkan card. Lalu card akan muncul
pada halaman utama todolist

Kemudian untuk post, buat endpoint /todolist/add dan arahkan ke function di views untuk membuat object baru pada Django. Setelah itu buat dictionary untuk 
me-return hasil dari post. Hal ini dilakukan supaya setiap elemen yang dibuat attributenya bisa dipakai atau dikenal oleh jQuery karena nanti akan digunakan pada card.

Setelah endpointnya sudah dibuat, kemudian buat modal sebagai tempat input title dan description. Modal saya menggunakan bootstrap dan tinggal disesuaikan stylingnya. Kemudian pada jQuery dibuat function post yang akan dilakukan apabila button pada modal di click. Ketika post dilakukan, maka kirim body dengan
title dan description yang diselect dari input. Jika post success maka append card baru sesuai data yang direturn oleh fungsi add di views.py. Dengan demikian
ajax sudah diimplementasi karena tidak perlu refresh untuk menampilkan data baru yang dibuat
