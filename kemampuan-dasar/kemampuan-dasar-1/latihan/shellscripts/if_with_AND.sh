!/bin/bash

echo "masukkan username andaaa"
read username
echo "password cepetan tulis"
read password
if [[ ( $username == "admin" && $password == "secret" ) ]]; then
echo "anda di jalan yang benarrr"
else
echo "salah kamar gan"
fi
