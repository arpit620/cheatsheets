docker version
docker info

docker container run --publish 80:80 nginx

Run in background
docker container run --publish 80:80 --detach nginx

docker container run --publish 80:80 --detach --name webhost nginx
docker container logs webhost
docker container top webhost    # To check processes running inside container
docker container --help     # For list of supported commands


# Show all running containers
docker container ls

# Show all containers
docker container ls -a


docker container stop <id>

# Run vs Start
Run will spin up a new container while start will start a stopped container.

# To remove stopped containers. Not for running container
docker container rm <id1> <id2> <id3>
docker container rm -f <id1> <id2> <id3>    # Force stop a running container

# Assignment
docker container run --publish 80:80 --detach --name webhost nginx
docker container run --publish 3306:3306 --detach --name db --e MYSQL_RANDOM_VAR=yes nginx
docker container run -p 3306:3306 -d --name db --e MYSQL_RANDOM_ROOT_PASSWORD=yes nginx

docker container run -p 8080:80 -d --name webhost httpd
docker ps

curl localhost              # For nginx
curl localhost:8080            # For Apache

# Show all images on your local machine
docker image ls



# Whats inside container
docker container top        # process details
docker container inspect    # config details
docker container stats      # performance stats for all containers



docker container run -it    # Start new container interactively
docker container exec -it   # run additional command in existing container


docker container run -it --name proxy nginx bash
docker container start -ai <container_name>     # To enter into a stopped container
docker container exec -it mysql bash        # To enter into a running container. Exiting this will not stop container












