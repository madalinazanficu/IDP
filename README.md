Rulare docker compose:

1. docker-compose -f ./docker-compose.yml up --build
2. docker-compose -f ./docker-compose.yml down

Kong listens for incoming user requests on port 8000. The Admin API listens on port 8001. User requests are routed
to the appropiate service based on the request path (either auth or io).

## Docker Swarm

1. Init a manager node: docker swarm init
2. Deploy the stack: docker stack deploy -c docker-compose.yml idp-project
3. Stop the stack: docker stack rm idp-project
4. View services: docker service ls
5. View nodes: docker node ls
6. docker stack ps idp-project

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
docker stack deploy -c portainer-agent-stack.yml portainer

User: admin
Parola: madalinazanficu
