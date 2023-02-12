# Docker PyGeoApp
Template minimale per Docker container di sviluppo basato su Ubuntu LTS per applicazioni Python in campo geo. 

## Come si usa

Dopo aver scaricato il contenuto del repo, spostarsi nella cartella e lanciare il comando:

```
docker-compose up -d
```
Questo comando creerà l'immagine e lancerà il container in modalità detached. Si può usare VSCode con l'estensione remote development per lanciare l'IDE nel container e utilizzarlo come ambiente di sviluppo. Le modifiche apportate nella directory di lavoro saranno mappate automaticamente grazie al volume dichiarato nel docker-compose.yml.

## Requisiti
<a href="https://www.docker.com/products/docker-desktop/" target="_blank">Docker desktop</a> installato e funzionante. 

## Consigliati
Editor <a href="https://code.visualstudio.com/" target="_blank">VS Code</a> con l'estensione per lo sviluppo in Python (da installare dopo avere lanciato l'ide nel container attraverso remote development. 
