import glob
import os
import shlex, subprocess

jpg_basic = [glob.glob("/home/ubuntu/samples/*.jpg")]
mp4_basic = [glob.glob("/home/ubuntu")]
tmp_jpg = []
tmp_mp4 = []

for jpg in jpg_basic[0]:
    tmp_jpg.append(jpg[jpg.find("samples") + 8:])
for mp4 in mp4_basic[0]:
    tmp_mp4.append(mp4[mp4.find("samples") + 8:])

f = open("tulemused.txt", "w+")

print("Recognize a plate")
for i in tmp_jpg:
    os.system("alpr -n 2 -c eu samples/" + i)
    
    command = "alpr -n 2 -c eu samples/" + i
    print(command)
    args = shlex.split(command)
    
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    tmp = proc.stdout.read().decode("utf-8")
    f.write(tmp)
f.close()


found_plates = []
right_plates = []
f = open("tulemused.txt", "r")
c = open("6igednumbrid.txt", "r")

for line in f:
    if "confidence:" in line:
        found_plates.append(line[line.index("-") + 2: line.index("\t")])

for line in c:
    right_plates.append(line.strip())
    

count = 0
full_count = len(right_plates)

for i in found_plates:
    if i in right_plates:
        count += 1

f.close()
c.close()

right = round(count * 100 / full_count, 1)
print("Oigete tulemuste % on: " + str(right))
print(found_plates)
print(right_plates)

print(input("press any key to exit."))
