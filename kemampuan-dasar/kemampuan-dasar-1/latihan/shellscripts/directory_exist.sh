#!/bin/bash
echo "masukkan nama folder"
read ndir
if [ -d "$ndir" ]
then
echo "folder nya ada, tenang aja"
else
	`mkdir $ndir`
echo "folder sudah dibuat komandan"
fi
