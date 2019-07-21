echo -n "Qual a url? "
read sitezinsafado
nomearquivo=$(date +"%H:%M")
pontotxt='.txt'
# echo $nomearquivo
curl $sitezinsafado >> $nomearquivo$pontotxt
nomearquivo=$nomearquivo$pontotxt
# echo $nomearquivo
echo 
echo
echo
python3 fdl.py $nomearquivo
