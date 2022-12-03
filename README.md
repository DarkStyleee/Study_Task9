### Install

`docker swarm init`

`docker service create --name test_swarm-registry --publish published=10000,target=8000 registry:2`

`docker compose build web`

`docker compose push web`

`docker compose push`

`docker stack deploy --compose-file docker-compose.yaml test_swarm-app`

`docker stack services test_swarm-app`

### Delete

`docker stack rm test_swarm-app`

`docker service rm test_swarm-registry`

`docker swarm leave --force`
