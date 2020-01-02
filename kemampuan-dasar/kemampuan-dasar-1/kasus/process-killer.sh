#!/bin/bash
read -p 'Masukkan nama program: ' pidprogram
ps -ef | grep $pidprogram | grep -v grep | awk '{print $2}' | xargs kill
