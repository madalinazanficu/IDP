# Build Docker images
build-auth:
	docker build -t auth-server -f ./auth-server/Dockerfile ./auth-server

build-io:
	docker build -t io-service -f ./io-service/Dockerfile ./io-service

build-business:
	docker build -t business-service -f ./business-service/Dockerfile ./business-service

build: build-auth build-io build-busines

# Run Docker Compose
up:
	docker-compose up

# Stop Docker Compose
down:
	docker-compose down

# Delete all docker containers, images and volumes
clean-docker:
	-docker stop $(shell docker ps -a -q)
	-docker rm $(shell docker ps -a -q)
	-docker rmi $(shell docker images -q)
	-docker volume rm $(shell docker volume ls -q)