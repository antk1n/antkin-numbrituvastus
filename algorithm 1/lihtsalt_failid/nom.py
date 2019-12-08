faili_nimi = "output.txt"
try:
	#Sorteerib file
	file = open(faili_nimi, "r+")
	pos = 0
	line = file.readlines()
	file.seek(pos)
	sort_text = sorted(line)
	for new_line in sort_text:
		file.write(new_line)
		pos = file.tell()
	#print("fail sorteeritud")
	file.close()
	
	#V6rdleb kas nomeroff tuvastas number
	file = open(faili_nimi, "r")
	i=0
	k=0
	for line in file:
		x = line.split(".jpg|", 1)
		k=k+1
		if x[0].strip() == x[1].strip():
			print (line.split(".jpg|", 1)[0], "True")
			i=i+1
		else: print (line.split(".jpg|", 1)[0], "False")
	print("Nomeroff tuvastas", i, "/", k)
	file.close()
except IOError:
	print("Tekkis viga")
	
