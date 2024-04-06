# Build Docker images
build-auth:
	docker build -t auth-service -f ./auth_service/Dockerfile.auth ./auth_service

build-product:
	docker build -t product-service -f ./product_service/Dockerfile.product ./product_service

build-frontend:
	docker build -t frontend-service -f ./frontend/Dockerfile.frontend ./frontend

build: build-auth build-product build-frontend

# Run Docker Compose
up:
	docker-compose up

# Stop Docker Compose
down:
	docker-compose down
