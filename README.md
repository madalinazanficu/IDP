Proiectul reprezinta backend-ul unei aplicatii de online selling, cu suport pentru urmatoarele functionalitati:
- autentificare utilizatori si vanzatori
- listare/stergere si actualizare informatii produse (vanzatori)
- cautare produse dupa nume
- cautare produse dupa categorie
- cautare produse dupa vanzatori
- vizualizare produse proprii

Microservicii relevante:
- autentificare: auth-server (se ocupa de inregistrare/autentificare, generare tokeni de acces)
- gestiune produse: io-service (se ocupa de interactiunea directa cu baza de date, operatii CRUD)
- interactiune cu utilizatorii: business-service (rutele accesibile direct utilizatorilor pentru interactiunea
  cu produsele)
- kong: rutare balansata a cererilor catre microservicii
- grafana: monitorizare statistici ale aplicatiei
- mongo/influx: baze de date pentru stocarea datelor
- portainer: interfata grafica pentru monitorizarea si administrarea containerelor

Utilizatorii vor folosi portul 8000 pentru a accesa orice ruta din aplicatie, Kong se va ocupa de a redirecționa
cererile catre microserviciile corespunzatoare.

## Docker Compose

1. docker-compose -f ./docker-compose-local.yml up --build
2. docker-compose -f ./docker-compose-local.yml down

## Docker Swarm

1. Init a manager node: docker swarm init
2. Deploy the stack: docker stack deploy -c docker-compose.yml idp-project
3. Deploy the portainer stack: docker stack deploy -c portainer-agent-stack.yml portainer
4. Stop the stack: docker stack rm idp-project
5. View services: docker service ls
6. View nodes: docker node ls
7. docker stack ps idp-project

### Removing nodes (managers should be downgraded to workers before removing them)

- docker node update --role worker <node_name>
- docker node rm <node_name>

docker node update --availability drain <node_name>
docker node update --availability active <node_name>

Removing the last manager node, means disolving the cluster: docker swarm leave --force

## Portainer

Am descarcat fisierul .yml de pe site-ul oficial:
https://docs.portainer.io/start/install-ce/server/swarm/linux

Pentru accesarea platformei web: https://localhost:9443

User: admin
Parola: madalinazanficu

## Mango express credentials

Accesibil pe portul 8081.
user: admin
password: pass

## Grafana

Accesibila pe portul 80. Dashboardurile sunt predefinite.
user: admin
password: pass

## Testare

Link catre setul de teste Postman (relevante doar cele din folderul business-service): https://lunar-crater-549936.postman.co/workspace/New-Team-Workspace~ceebe05a-cb82-4901-a399-fac928c8f417/folder/30980161-678e7476-578d-4054-8ea0-069f7550efa4?action=share&source=copy-link&creator=30980864&ctx=documentation

1. Se creaza o instanta de Play With Docker
2. Se trage repo-ul de pe GitHub
3. Se initiaza swarm-ul: docker swarm init --advertise-addr <IP>
4. Se deployeaza stack-urile: docker stack deploy -c docker-compose.yml idp-project si docker stack deploy -c portainer-agent-stack.yml portainer
5. Se copiaza adresa de acces a aplicatiei si se seteaza variabila globala 'url_addr' in Postman