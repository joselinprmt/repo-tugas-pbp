# Tugas 6: Javascript dan AJAX

1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.  
   * Synchronous programming berarti program berjalan secara sequential, artinya operasi berjalan berurutan, harus menunggu  
     sampai perintah sebelumnya selesai dulu, baru berlanjut ke perintah selanjutnya.
   * Asynchronous programming artinya program dapat berjalan secara paralel, eksekusi program tidak bergantung pada apakah  
     program sebelumnya sudah dijalankan atau belum.
   

2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari   
   paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.  
    Event-Driven Programming adalah paradigma pemrograman dimana flow dari suatu program ditentukan oleh suatu event  
    seperti user input (klik mouse, tombol key ditekan), sensor output, ataupun message passing dari program atau thread lain.  
    Artinya, berjalannya program dengan paradigma ini bergantung pada event dari luar.


3. Jelaskan penerapan asynchronous programming pada AJAX.  
    AJAX, yang merupakan asynchronous JavaScript and XML, adalah teknik yang memungkinkan page terupdate secara asinkronus,  
    artinya browser tidak perlu direload ketika ada sedikit perubahan atau penambahan data. AJAX hanya akan melakukan passing  
    pada data yang di update ke server. Contohnya, pada tugas 6 ini task baru akan langsung ditambahkan tanpa perlu mereload  
    keseluruhan page.
    

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.  
    Pertama, dibuat views `show_json_todo` yang akan mengembalikan data task dalam bentuk json. Selanjutnya dibuat path  
    `/todolist/json/` yang akan menampilkan hasil dari json dari views. Selanjutnya akan dibuat script yang melakukan AJAX  
    get pada url `todolist/json/` tadi. Lalu akan dilakukan iterasi yang akan memasukan tiap elemen ke dalam card. Dan cards  
    tersebut akan muncul pada page todolist secara asinkronus.
    Selanjutnya, pada AJAX post, dibuat button Add task yang akan membuka modal dengan form untuk menambah task. Modal  
    berisi title dan description, serta tombol untuk trigger AJAX post ketika diklik. Jika post sukses maka akan diappend  
    card baru sesuai data yang akan direturn pada views. Jika berhasil, card akan bertambah tanpa dilakukan reload. Dibuat  
    pula `todolist/add/` yang akan diarahkan ke function `create_task_ajax` pada views tadi, untuk membuat object Task baru.  
    Function akan mereturn JSON response agar nantinya dapat dikenali pada AJAX get dan untuk pembuatan card.