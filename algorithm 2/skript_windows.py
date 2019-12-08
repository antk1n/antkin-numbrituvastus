import glob
import os
import subprocess

jpg_basic = [glob.glob("C:/Users/Laptop/Desktop/OPENALPR/openalpr_64/samples/*.jpg")]
tmp_jpg = []

for jpg in jpg_basic[0]:
    tmp_jpg.append(jpg[jpg.find("samples") + 8:])

f = open("tulemused.txt", "w+")

print("Recognize a plate")
for i in tmp_jpg:
    os.system("alpr -n 2 -c eu samples/" + i)
    proc = subprocess.Popen("alpr -n 2 -c eu samples/" + i, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
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
    right_plates.append(line.rstrip())

count = 0
full_count = len(right_plates)

for i in found_plates:
    if i in right_plates:
        count += 1

f.close()
c.close()

right = round(count * 100 / full_count, 1)
print("Oigeid tulemusi on: " + str(count), "/" + str(full_count))
print("Oigete tulemuste % on: " + str(right))
print(found_plates)
print(right_plates)

print(input("press any key to exit."))
