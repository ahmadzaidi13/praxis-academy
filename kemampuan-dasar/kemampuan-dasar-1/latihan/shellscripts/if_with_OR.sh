#!/bin/bash

echo "masukkan angka ini bukan togel tapi"
read n

if [[ ( $n -eq 15 || $n -eq 45 ) ]]
then
echo "selamat anda kami scam"
else
echo "selamat gak jadi di scam"
fi
