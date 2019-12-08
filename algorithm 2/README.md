# OpenALPR

## for Linux
### skript.py
skript.py käivitab OpenALPR, kirjutab väljundi faili "tulemused", seejärel võrdleb seda failiga, kus on kirjas kõik õiged numbrid (6igednumbrid.txt)  
käivitada käsuga "python skript.py"   
### Docker  
NB! docker peab olema eelnevalt installitud
- mine kausta openalpr_docker
- käivitada build script käsuga "sudo sh build.sh"
- luua HOME kataloogis kaust "samples" ja salvestada sinna pildid formaadis .jpg
- käivitada docker "sudo sh run.sh"
- käivitada script docker-is
- väljuda dockerist käsuga "exit" või kirjutada uues terminalis "sudo sh stop.sh"

## for Windows
### skript_windows.py
