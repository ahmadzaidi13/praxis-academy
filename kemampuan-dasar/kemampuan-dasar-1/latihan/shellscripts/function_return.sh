#!/bin/bash
function greeting() {

str="Hai gaes, $name"
echo $str

}

echo "Tulis nama anda"
read name

val=$(greeting)
echo "Return value of the function is $val"
