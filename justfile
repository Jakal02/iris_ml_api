
@start-backend:
    docker compose -f docker-compose.yaml up --build

@stop-backend:
    docker image prune -f
    docker compose -f docker-compose.yaml down

@pytest pytestargs="":
    docker compose -f docker-compose-test.yaml up -d --build
    # sleep needed because docker compose up doesn't care
    # what point start.sh gets to when it decides the containers are built
    # (we want the database migrations to finish)
    sleep 2
    -docker compose -f docker-compose-test.yaml exec iris_backend_server_test python3 -m pytest {{pytestargs}}
    docker image prune -f
    docker compose -f docker-compose-test.yaml down

@down-test-services:
    # useful when pytest recipe fails before tearing down
    docker image prune -f
    docker compose -f docker-compose-test.yaml down