# Nomeroff-net

Nomeroff-net on seisuga 24.09.19, asub kasustas "nomeroff-net".  
Python'i skriptid ja .txt failid asuvad kaustas "lihtsalt_failid".    
Kõik pildid peavad olema .jpg
Kaustas "nomeroff-net" asub nomeroff ja kõik vajalikud failid:
- .txt failid ja skriptid (kahes kohas siin "muudetud_nomeroff/nomeroff-net" ja siin "muudetud_nomeroff/nomeroff-net/examples/py")  
- dockerfile ja .sh skriptid mis teevad elu lihtsamaks. (dockerfile asub siin "nomeroff-net/docker/doc", .sh failid siin "/nomeroff-net/meie_docker/")  

## Docker
Docker image suurus umbes 3 GB.

### Kuidas Docker installida
- sudo apt-get update
- sudo apt install docker.io
- sudo docker --version  

### Kuidas build Docker image
- laadida alla kaust "nomeroff-net"
- 'cd nomeroff-net/meie_docker/'
- Build Docker image käsuga 'sudo sh build.sh'
- ... ootame... image valmis  

### Kuidas kasutada Docker
- Pildid paneme kausta nomeroff-net/images  
- Käivitame Docker 'sudo sh run.sh'  
NB! Docker näeb kausta nomeroff-net/ realajas
- Käivitame nomeroff-net käsuga 'python3 minudemo.py', skript teeb väljundi "output.txt" faili.  
(Kui on vaja, siis on võimalus käivitada kohe võrdlemis skriptid nom.py või nom_1.py. Et saada rohkem infot vt "võrdlemisjuhend")
- stop Docker käsuga 'exit', või on võimalus teises terminalis käivitada stop.sh file käsuga "sudo sh stop.sh", mis asub docker/ kaustas

## Paigaldamis juhend  (Installation from source), Linux (ubuntu)  

### Paigaldada VitualBox'i ubuntu 18.04
General:  
- ubuntu-18.04.3-desktop-amd64, ubuntu (64-bit)  
System:
- Base Memory: 2048  
- Processors: 2  
- Acceleration: VT-x/AMD-V,Nested Paging, KVM Paravirtualization  
Display:  
- Video Memory: 64 MB
Graphics Controller: VMSVGA  
Storage:  
- controller: SATA: XXX.vdi(Normal,20.00 GB)    
  
### Python3.6 (võib ka 3.5 ja 3.7, aga 3.5 ei tulnud välja ning 3.7 ei proovinud)
- sudo apt  install python3
- python3 -V  
  Output: Python 3.6.8
- sudo apt install python3-pip
- pip3 -V  
  Output: pip 9.0.1 from /usr/lib/python3/dist-packages (python 3.6)
- sudo apt install python3-opencv
- python3 -c

- python3 -c "\ 
  import cv2
  print(cv2.__version__)
  "  
  Output: 4.1.1
  
### Git
- sudo apt install git
- git --version  
  Output: git version 2.17.1

### laadida alla nomeroff
- git clone https://github.com/ria-com/nomeroff-net.git
- cd nomeroff-net (edasi kõik teha selles kaustas)

### gcc kompilaator
- sudo apt-get install gcc

### OpenCV
- sudo apt-get install -y libglib2.0
- sudo apt-get install -y libsm6
- sudo apt-get install -y libfontconfig1 libxrender1
- sudo apt-get install -y libxtst6

### pycocotools
- sudo apt-get install python3.6-dev (vajalik pakett sõltub python'i versioonist)

### paigaldada requirments.txt
- pip3 install Cython
- pip3 install numpy
- pip3 install git+https://github.com/matterport/Mask_RCNN  
 NB! muuta failis requirements.txt, setup.py ja setup-gpu.py tensorflow versioon 1.15, versioonile 1.14.0
- pip3 install -r requirements.txt

### kontrolli, kas tensorflow on õigesti paigaldatud
- python3 -c "
  import tensorflow as tf;
  print(tf.__version__)"
  Output: 1.14.0
  
### reinstall keras (See on tähtis)
- pip3 uninstall keras
- pip3 install keras==2.2.5 --upgrade

## Nomeroff-net kasutamisjuhend
- Skript minudemo.py peab olema siin - .../nomeroff-net/examples/py ja siin .../nomeroff-net/
- Pildid peaksid olema kaustas siin - .../nomeroff-net/examples/images ja siin .../nomeroff-net/images
- Skript minudemo.py käivitatakse terminalis käsuga "python3 minudemo.py" 
(NB! terminal peab olema samas kaustas, kus asub skript)
- Skript minudemo.py salvestab resultaad failis nimega "output.txt"

## Võrdlemisjuhend
output.txt - nomeroff-net väljastamis fail. 3.txt - võrdlemisfail

### Variant 1 - õige_number.jpg|tuvastatud_number
Skript võrdleb pildi nimi tuvastatud numbritega
- Kopeerime output.txt kaustasse kus asub skript nom.py
- Käivitame skript käsuga "python3 nom.py"  
NB! fail salvestab sorteerimis resiltaad samas failis, aga mini väljastamisfaili ta ei salvesta. Kui on vaja väjastamis fiali, siis käivitada skript käsuga "python3 nom.py >> faili_nimi" 

### Variant 2 - pildi_nimi.jpg|tuvastatud_number
Skript võrdleb kaks faili (on vaja võrdlemisfail formaadis "pildi_nimi.jpg|õige_number")

- Kopeerime output.txt kaustasse kus asub skript nom_1.py
- Kopeerime võrdlemis faili kaustasse kus asub skript nom_1.py (baas.txt)
- Käivitame skript käsuga "python3 nom_1.py"  
NB! fail salvestab sorteerimis resiltaad samas failis, aga mini väljastamisfaili ta ei salvesta. Kui on vaja väjastamis fiali, siis käivitada skript käsuga "python3 nom.py >> faili_nimi" 
