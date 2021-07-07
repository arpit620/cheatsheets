
# Docker

## Docker commands

Hello world\
`docker run hello-world`  
`docker --version`  


Check all images on local:\
`docker images`


Docker run:\
(Takes image and start container out of it)

-ti: terminal interactive. Useful when typing commands inside docker otherwise not required\
`docker run -ti ubuntu:18.04 bash`\
`docker run -ti ubuntu bash`

type `exit` to get out of container or `Ctrl + D` (Mac)


To get details of running containers:\
`docker ps`\
To display result vertically instead horizontally:\
`docker ps --format $FORMAT`

To get details of all / stopped containers:
`docker ps -a`

Make changes in a docker image and save it as a new image with changes:\
`docker commit <container_id>`\
Tag that image with a image name:\
`docker tag <sha_id from commit> <new_image_name>`


Other way:\
`docker commit <container_name> <new_image_name>`

--rm: delete the container when it exits
`docker run --rm -ti ubuntu:18.04 sleep 5`\
`docker run -ti ubuntu:18.04 bash -c "sleep 3; echo all done"`



Remove all stopped containers:\
`docker container prune`\
Remove specific stopped container:\
`docker rm <image_name>`
`docker kill <image_name>`


Leave a docker image running with some job inside:\
-d: detach\
`docker run -d -ti ubuntu bash`

Attach to a detached container:\
`docker attach <container_name>`

Detach from running container:\
`Ctrl + P + Q`

Execute another process within same container:\
`docker exec -it <container_name> bash`

Docker logs:
`docker logs <container_name>`


Resource Constraints:\
Memory limits:\
`docker run --memory maximum-allowed-memory image-name command`

CPU Limits:\
`docker run --cpu-shares` (relave to other continers)\
`docker run --cpu-quote` (to limit in general)

Check ports:
`docker run --rm -ti -p 45678:45678 -p 45679:45679 --name echo-server ubuntu bash`

Run NetCat listen port (lp) inside:
nc -lp 45678 | nc -lp 45679


From outside container: `nc localhost 45678`
From outside container: `nc localhost 45679`

host.docker.internal : Gets you IP of host machine
if run from inside container: `nc host.docker.internal 45678`

Expore port dynamically:
Dont' mention outside port, it will automatically assign:

`docker run --rm -ti -p 45678 -p 45679 --name echo-server ubuntu bash`
`docker port echo-server`


## Network

Give list of networks:
`docker network ls`

Create new network
docker network create learning

docker run --rm -it --net learning --name catserver ubuntu bash
ping catserver

docker run --rm -it --net learning --name dogserver ubuntu bash
ping dogserver
ping catserver

docker network create catsonly
docker network connect catsonly catserver

docker run --rm -it --net catsonly --name bobcatserver ubuntu bash
ping catserver
ping dogserver - Not allowed

## Legacy Linking

docker run --rm -it -e SECRET=secretKey --name catserver ubuntu bash
docker run --rm -it --link catserver --name dogserver ubuntu bash

In above, dogserver can connect to catserver but not other way round.

# Images

docker images

Remove image:
docker rmi image-name:tag
docker rmi image-id








