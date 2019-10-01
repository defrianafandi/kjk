# TUGAS 1 Keamanan Jaringan Komputer

#### Nama : Defrian Afandi
#### NIM  : 09021281722075

**a.1)**

```python
import hashlib, binascii

text = "hello"
data = text.encode("utf8")

sha224hash = hashlib.sha224(data).digest()
sha384hash = hashlib.sha384(data).digest()
sha3_224hash = hashlib.sha3_224(data).digest()
sha3_384hash = hashlib.sha3_384(data).digest()

print("Text: ", text)
print("sha224 hash: ",binascii.hexlify(sha224hash))
print("sha384 hash: ",binascii.hexlify(sha384hash))
print("sha3-224 hash: ",binascii.hexlify(sha3_224hash))
print("sha3-384 hash: ",binascii.hexlify(sha3_384hash))
```
outputnya :
```
Text:  hello
sha224 hash:  b'ea09ae9cc6768c50fcee903ed054556e5bfc8347907f12598aa24193'
sha384 hash:  b'59e1748777448c69de6b800d7a33bbfb9ff1b463e44354c3553bcdb9c666fa90125a3c79f90397bdf5f6a13de828684f'
sha3-224 hash:  b'b87f88c72702fff1748e58b87e9141a42c0dbedc29a78cb0d4a5cd81'
sha3-384 hash:  b'720aea11019ef06440fbf05d87aa24680a2153df3907b23631e7177ce620fa1330ff07c0fddee54699a4c3ee0ee9d887'
```

**a.2)**

intalasi openssl:
```
$ sudo apt install openssl
```
generate text file berisikan string:
```
$ echo "hello" > text-original.txt
```
generate file enkripsi dari original file:
```
$ openssl enc -aes-128-cbc -in text-original.txt -out text-encoded-aes128cbc.txt
```
enter aes-128-cbc encryption password:                                          
Verifying - enter aes-128-cbc encryption password:                               
*** WARNING : deprecated key derivation used.                                    
Using -iter or -pbkdf2 would be better.                                            
```
$ openssl enc -aes-192-cbc -in text-original.txt -out text-encoded-aes192cbc.txt
```
enter aes-192-cbc encryption password:                                          
Verifying - enter aes-192-cbc encryption password:                               
*** WARNING : deprecated key derivation used.                                    
Using -iter or -pbkdf2 would be better.                                            
```
$ openssl enc -aes-256-cbc -in text-original.txt -out text-encoded-aes256cbc.txt
```
enter aes-256-cbc encryption password:                                          
Verifying - enter aes-256-cbc encryption password:                               
*** WARNING : deprecated key derivation used.                                    
Using -iter or -pbkdf2 would be better.                                            

melihat isi encode nya pada output dari generate file enskripsi:                
```
$ cat text-encoded-aes128cbc.txt
```
Salted__���e8�*c��"([�m&����7                               
```
$ cat text-encoded-aes192cbc.txt
```
Salted__��r�׿�A��}G`�����>�\                               
```
$ cat text-encoded-aes256cbc.txt
```
Salted__�J��=��.5�;߬I��jMgp��                               

**b.1)**

intalasi bruteforce-salted-openssl:
```
$ sudo apt install bruteforce-salted-openssl
```
penggunaannya terhadap file enkripsi yang sudah dilakukan dengan openssl aes-256-cbc:
```
$ bruteforce-salted-openssl -t 50 -f list-key-punya-defri.txt -d sha256 text-encoded-aes256cbc.txt
```
Warning: using dictionary mode, ignoring options -b, -e, -l, -m and -s.                           

Tried passwords: 38                                                                               
Tried passwords per second: inf                                                                    
Last tried password: ieueyywk                                                                      

Password candidate: 54321                                                                            

---
**Penjelasan konsep dari serangan brute-force :**                                                      
>Serangan bruto force bekerja dengan menghitung jumlah kata sandi dan mengujinya untuk melihat apakah itu
adalah kata sandi yang benar.  Seiring bertambahnya panjang kata sandi, jumlah waktu untuk menemukan kata
sandi yang benar meningkat secara eksponensial.
