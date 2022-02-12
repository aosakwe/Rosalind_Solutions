#Bash script to convert files from DOS /r to UNIX /t
cat $1 > backup_file.txt
sed -i.bak 's/\r$//' $1

