# fastapi-mongo-async-plan
## Asynchronous rest api for lessons plan using FastAPI and MongoDB.

### docker setup:

cd docker

docker-compose up -d

### app setup:

export MONGODB_URL="mongodb://admin:supersecretpsw@localhost:6000/plan?authSource=admin&retryWrites=true&w=majority"

uvicorn app.main:server
