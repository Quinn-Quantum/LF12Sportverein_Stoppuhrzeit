# Voraussetzungen für TensorFlow
- NVIDIA GPU für die Hardwarebeschleunigung mit CUDA Kernen.
- Python >= 3.8 (Achtung hier sollten die PATH Variablen vom Installer korrekt angelegt werden!)
- pip3
- Umgebungsvariablen korrekt angelegt
## PIP Kommandos für das Installieren von TensorFlow
### Aktualisieren von Python und allen vorhandenen Packages
In Powershell folgendes eingeben:
- pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}
### Installieren von TensorFlow per pip
Systemweite Installation: 
- pip3 install --user --upgrade tensorflow  # install in $HOME
