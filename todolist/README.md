# Tugas 4: ToDoList App

Link App Heroku: https://tugas-2-app.herokuapp.com/todolist/  
Link Repo: https://github.com/joselinprmt/repo-tugas-pbp
<br>

1. Apa kegunaan {% csrf_token %} pada elemen < form >? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen < form >?
    * CSRF atau Cross-Site Request Forgery token adalah value yang unik dan rahasia, yang digenerate oleh server-side  
    application, untuk mencegah serangan CSRF. Cara kerjanya adalah token diletakan pada parameter yang tersembunyi pada  
    HTML form, dan token harus bersifat unik tiap sesi dan berisi random value dengan jumlah karakter yang banyak agar  
    tidak mudah ditebak.
    * Jika potongan csrf token tidak ada, ini akan membuat request form oleh user bisa disalahgunakan dan dipalsukan oleh  
    orang tidak bertanggungjawab. Ditambah lagi, csrf token dimanfaatkan untuk memvalidasi request pada server, sehingga  
    jika kita tidak memasukan potongan kode tersebut pada form, akan menimbulkan error ketika app dijalankan.
   

2. Apakah kita dapat membuat elemen < form > secara manual (tanpa menggunakan generator seperti {{ form.as_table }})?   
   Jelaskan secara gambaran besar bagaimana cara membuat < form > secara manual.
    * Bisa. Sesuai docs pada Django, terdapat beberapa opsi yang disediakan untuk merender forms. Namun, kita bisa merender  
    form secara manual, misalnya jika kita ingin mengganti urutan dari attribute pada form, dengan memanfaatkan sintaks  
    {{ form.nama_field }} dan mengubah tata letak dari masing-masing attribut field sesuai keinginan.
    

3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database,  
   hingga munculnya data yang telah disimpan pada template HTML.
    * Pertama, pengguna mengisi form pada field masing-masing. Lalu, tiap input pada fieldnya dipetakan pada form yang  
    dipassing ke dalam views.py. Setelah itu, dilakukan validasi sesuai jenis request. Jika sudah valid, akan dipanggil  
    method save() yang akan menyimpan data tersebut ke dalam database. Setelah itu, untuk menampilkan data yang telah  
    disimpan pada database, dilakukan pemanggilan objek models pada views, yang akan dipassing kembali agar dapat di-  
    tampilkan pada template HTML.  
   

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
    * Pertama, dinialisasi folder baru 'todolist' pada root directory tugas yang telah digunakan sebelumnya
    * Pada folder project_django, ditambahkan path 'todolist/' dan men-include todolist.url pada url.py, dan menambah   
    'todolist' pada INSTALLED_APPS di settings.py
    * Membuat file models.py pada todolist dengan class Task, dengan attribut user, date, title, description. Dibuat juga  
    file forms.py dengan class TaskForm dengan model Task, sesuai spesifikasi pada soal
    * Pada views.py, diimplementasikan fungsi register, login_user, dan logout_user, serta mengimplementasikannya fungsi  
    tersebut pada login.html dan register.html
    * Diimplementasikan juga fungsi show_todolist yang memanggil database objek Task, yang kemudian dipassing saat  
    rendering todolist.html, selain itu dibuat juga tombol Tambah Task dan Logout  
    * Pada tombol Tambah task di todolist.html akan memanggil form tambah task untuk menambah task baru. Pada halaman  
    tersebut, user akan bisa menambah objek model task baru, yang akan dimasukkan pada database dengan method save() pada  
    views, yang selanjutnya data pada database akan dapat ditampilkan pada todolist.html
    * Dilakukan routing pada path ' ', 'login/', 'register/', 'logout/', dan 'create-task/' pada urls.py agar dapat diakses  
    oleh pengguna. Namun, diperlukan login terlebih dahulu untuk mengakses create-task dan todolist
    * Setelah itu, dilakukan deployment pada app heroku pada https://tugas-2-app.herokuapp.com/todolist/
    * Setelah berhasil dideploy, pada app heroku dilakukan inisialisasi 2 akun pengguna dengan 3 dummy data, yang datanya  
    dapat diakses pada https://tugas-2-app.herokuapp.com/admin .
    2 akun pengguna tersebut adalah:
   
      * username: Aku
      * password: akuwkwk123  

      * username: Siapa
      * paswword: XENHr8t86BAXuvx  



# Tugas 5

1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?  
    * Inline: Styling dilakukan di masing-masing tag HTML, digunakan untuk mengubah style pada elemen HTML yang spesifik.
      * Kelebihan: Berguna jika kita hanya ingin mengubah style dari elemen yang khusus/spesifik
      * Kekurangan: Membutuhkan banyak waktu untuk mengubah style dari masing-masing elemen, terutama untuk projek web   
       yang berskala besar. Selain itu, penggunaan inline HTML yang banyak dapat memperlambat waktu loading web.
       
    * Internal: Styling dilakukan di < head > section dalam 1 file HTML
      * Kelebihan: Load time web lebih cepat daripada inline CSS. Selain itu, Untuk web yang hanya membutuhkan sedikit  
       file HTML, internal CSS lebih hemat waktu daripada implementasi inline CSS.
      * Kekurangan: Relatif membutuhkan banyak waktu untuk menambahkan style pada web project yang berskala besar

    * Eksternal: Styling dilakukan di luar file HTML, yaitu pada file .css
      * Kelebihan: Lebih efisien untuk project web yang berskala  besar, karena kita bisa mengubah style dari situs hanya  
       dengan 1 file CSS. Selain itu, struktur dari file kita juga lebih rapi dan mudah untuk di kostumisasi.
      * Kekurangan: Style dari web baru bisa dilihat setelah file CSS eksternal selesai di load.
      

2. Jelaskan tag HTML5 yang kamu ketahui.
    * 