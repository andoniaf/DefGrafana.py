<img src="./img/defGrafana.png" width="300">


Script para capturar imágenes dentro de Grafana.



## Modo de uso
- Modificar sección "VARS" dentro del script.
- Ejecutar: ```python3 DefGrafana.py '<URL a capturar>'```
  - Guarda la captura en el mismo directorio desde donde se ejecuta.
- La opcion '--cut-panel' permite añadir otra imagen con el panel recortado: ```python3 DefGrafana.py --cut-panel '<URL Dashboard>'```

## Dependencias
- **Python**: Probado con las versiones 3.4.2 y 3.5.2
  - Dependencias: ```pip3 install -r requirements.txt```
- **phantomJS**: Versión 2.1.1
  - Ver [Anexo I](#anexo-i-instalación-de-phantomjs-en-ubuntudebian) para instalación sobre Ubuntu/Debian






### Origen del nombre
* **Grafana**: Fácil, se usa con [Grafana](https://grafana.com/).
* **Def**: Si aun no has caído [pincha aqui](https://open.spotify.com/album/0IXPDVnECWSt6NFLDlgpoC).


-----

#### Anexo I: Instalación de PhantomJS en Ubuntu/Debian
```
apt-get update
apt-get upgrade
apt-get install libfreetype6 libfreetype6-dev
apt-get install build-essential chrpath libssl-dev libxft-dev
apt-get install libfreetype6 libfreetype6-dev
apt-get install libfontconfig1 libfontconfig1-dev
wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2
mv phantomjs-2.1.1-linux-x86_64 /usr/local/share
ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin
```
