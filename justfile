
@start-backend:
    docker compose -f docker-compose.yaml up --build

@stop-backend:
    docker image prune -f
    docker compose -f docker-compose.yaml down
