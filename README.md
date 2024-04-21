Rulare docker compose:

1. docker-compose -f ./docker-compose.yml up --build
2. docker-compose -f ./docker-compose.yml down

Kong listens for incoming user requests on port 8000. The Admin API listens on port 8001. User requests are routed
to the appropiate service based on the request path (either auth or io).