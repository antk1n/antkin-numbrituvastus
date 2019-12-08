faili_nimi = "output.txt" #tulemuste fail
faili_nimi_1 = "3.txt" #v6rdlemis fail
try:
	#Sorteerib filid
	file = open(faili_nimi, "r+")
	pos = 0
	line = file.readlines()
	file.seek(pos)
	sort_text = sorted(line)
	for new_line in sort_text:
		file.write(new_line)
		pos = file.tell()
	#print("fail 1 sorteeritud")
	file.close()
	
	file = open(faili_nimi_1, "r+")
	pos = 0
	line = file.readlines()
	file.seek(pos)
	sort_text = sorted(line)
	for new_line in sort_text:
		file.write(new_line)
		pos = file.tell()
	#print("fail 2 sorteeritud")
	file.close()
	
	#V6rdleb kas nomeroff tuvastas number
	file = open(faili_nimi, "r")
	file2 = open(faili_nimi_1, "r")
	i=0
	k=0
	for line1, line2 in zip(file, file2):
		k=k+1
		if line1==line2:
			print (line1.split(".jpg|", 1)[0], "True")
			i=i+1
		else: print (line1.split(".jpg|", 1)[0], "False")
	print("Nomeroff tuvastas", i, "/", k)
	file.close()
	file2.close()
except IOError:
	print("Tekkis viga")
	
