 ## Assignment 5

## Inline vs External vs Internal CSS

Dalam menggunakan CSS ada beberapa cara yang dapat diterapkan. Inline, External, atau Internal CSS. Perbedaannya ada pada letak penulisan styling. Untuk inline berarti meletakkan CSS property pada attribute atau props html tag. Misalnya, `<p style="font-size:21px;">Hello Bakung!</p>`. Selain itu, untuk External CSS adalah meletakkan CSS atribute di luar dari file html. Caranya dengan membuat file baru dengan extension .css dan melakukan import pada html yang ingin diaplikasikan style dari file css tersebut. Import dapat dilakukan seperti ini ` <link rel="stylesheet" href="bakung21.css"/>` dengan anggapan file .css bernama bakung21.css. Selain itu CSS juga bisa diaplikasikan secara internal di dalam html dengan memanfaatkan `<style>` tag. Isi dari tag tersebut sama caranya dengan mengisi css property pada file external. 

Menurut saya pribadi, untuk inline kelebihannya adalah pada saat kasus hanya ingin mengaplikasikan untuk beberapa tag saja dan stylingnya tidak banyak. Kelemahannya untuk styling yang sudah complex menurut saya akan menimbulkan code smell karena property atau attribute style akan jadi panjang sekali. Untuk external menurut saya merupakan best practice untuk mengaplikasikan banyak styling atau yang sudah complex karena bisa membuat banyak css property. Namun menurut saya kurang efektif untuk style yang hanya sedikit dan dibeberapa tag/line saja. Untuk internal, menurut saya kurang lebih mirip kasusnya dengan inline, baik untuk kasus styling yang tidak kompleks karena ketika sudah banyak akan menjadi code yang tidak clean. Namun kelebihannya, kalian tidak perlu untuk membuat style.css dan tidak perlu melakukan import file. Dengan menggunakan <style> tag bisa langsung mengaplikasikan CSS di HTML-nya. 

## HTML Tags

HTML tag yang saya tau adalah `<div>` tag, div tag ini adalah suatu tag yang merepresentasikan sebuah section atau block. Kemudian ada tag <input> untuk menerima input dari user, bisa berupa text field atau button submit, checkbox, dll. Kemudian ada tag <title></title> tag title ini merupakan tag yang berhubungan title yang ada di tab browser. Kemudian ada <button> yang merupakan tag implentasi button. Kemudian ada <a> untuk hyperlink. <img> untuk menampilkan gambar dan masih banyak lagi tag-tag HTML yang selain saya mention di sini. 

## CSS Selector

CSS selector yang saya ketahui ada .class, dengan awal dot(.) berarti merujuk pada value dari property class. #id merujuk pada penggunaan property id pada html tag. * untuk apply ke semua element. kemudian selector juga bisa terdiri dari banyak selector misalnya .class1 .class2. Kemudian juga selector html tag misalnya p, berarti merujuk untuk semua p tag, dll.


## Implementation Assignment 5

Dalam tugas 5 ini tujuan utamanya untuk memberikan styling pada semua halaman yang ada di app todo. Hal yang pertama saya lakukan adalah menentukan styling. Saya memilih menggunakan tailwind karena saya telah familiar dengan tailwind dan menurut saya banyak hal yang dimudahkan dengan menggunakan tailwind. 

Setelah itu, mulai melakukan styling. pertama-tama karena saya menggunakan tailwind maka library dari tailwind harus di-init dengan menambahkan `<script src="https://cdn.tailwindcss.com"></script>` pada head di base.html. Setelah itu tailwind sudah dapat digunakan. Kemudian saya mulai melakukan styling pada login. Idenya adalah dengan meletakkan input username dan passwordnya ditengah agar secara user experience lebih baik dan lebih mudah juga untuk dibuat responsive. Kemudian untuk register kurang lebih ide stylingnya sama akan tetapi ada beberapa hal yang saya harus custom terutama karena register menggunakan form bawaan dari django sehingga untuk melakukan styling pada form tersebut awalnya menggunakan form.as_table harus dipecah menjadi section section sehingga lebih mudah distyling. 

Pada page todo idenya adalah dengan mengubah table todo menjadi card sehingga harus membuat section/div untuk membuat block card tersebut dan diberikan grid-cols-4 atau grid 4 column agar lebih rapi. Untuk create task kurang lebih sama dengan register dan login secara UI. Untuk responsive saya sangat dibantu oleh tailwind, misalnya untuk screen lebih besar dari mobile saya ingin memberikan grid, dengan tailwind saya bisa melakukan `grid sm:grid-cols-4` aritnya untuk sm keatas apply `grid-cols-4` untuk yang lebih kecil dari 640 tidak perlu dilakukan grid sehingga pada tampilan mobile tidak overflow ke kanan karena tanpa grid-cols-4 card akan otomatis menjadi tersusun vertical. 



