#! /bin/bash

sed -f sed.txt input.txt > output.txt
sed -f sed2.txt input.txt > output2.txt
sed -f sed_del.txt input.txt > del_nsi.sql