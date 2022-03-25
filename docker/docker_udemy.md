https://github.com/bretfisher/udemy-docker-mastery

docker version
docker info

docker <command> <sub-command>

<host_port:container_port>
docker container run --publish 80:80 nginx
docker container run --publish 8888:80 nginx

Run in background
docker container run --publish 80:80 --detach nginx
docker container run --publish 80:80 -d nginx

Add name to the container
docker container run --publish 80:80 --detach --name webhost nginx
docker container logs webhost

# Old way
docker logs webhost 

docker container top webhost    # To check processes running inside container
docker container --help     # For list of supported commands

docker container --help
docker ps

# Show all running containers
docker container ls

# Show all containers
docker container ls -a

# Stop container. <First 3 digit of id are enough>
docker container stop <id>
docker container stop <name>
docker container start <id>

# Run vs Start
Run will spin up a new container while start will start a stopped container.

# To remove stopped containers. Not for running container
docker container rm <id1> <id2> <id3>
docker container rm -f <id1> <id2> <id3>    # Force stop a running container

# Configurable parameters
docker container run --publish <8080>:80 --name webhost -d nginx:<1.11> <nginx -T>

change host listening port, change version of image, change CMD run on start

# Assignment
docker container run --publish 80:80 --detach --name webhost nginx
docker container run --publish 3306:3306 --detach --name db -e MYSQL_RANDOM_VAR=yes nginx
docker container run -p 3306:3306 -d --name db -e MYSQL_RANDOM_ROOT_PASSWORD=yes nginx

docker container run -p 8080:80 -d --name webhost httpd
docker ps

curl localhost              # For nginx
curl localhost:8080            # For Apache

-e : --env

mysql will print random password on `docker logs`

# Show all images on your local machine
docker image ls



# Whats inside container
docker container top        # process details
docker container inspect    # config details
docker container stats      # performance stats for all containers

docker container top mysql
docker container inspect mysql
docker container stats 

# Getting inside containers
docker container run -it    # Start new container interactively
docker container exec -it   # run additional command in existing container


docker container run -it --name proxy nginx bash
docker container start -ai <container_name>     # To enter into a stopped container
docker container exec -it mysql bash        # To enter into a running container. Exiting this will not stop container

docker pull alpine

docker container run -it alpine sh
apk # To install bash



# Docker Networks

docker container run -p 80:80 -name webhost -d nginx
docker container port webhost       # Display open port of running container.

Get IP of the docker container:
docker container inspect --format '{{ .NetworkSettings.IPAddress }} webhost

##  Docker Network: CLI Management
docker network ls
docker network inspect
docker network create --driver
docker network network connect 
docker network network disconnect


docker network create my_app_net
docker container run -d --name new_nginx --network my_app_net nginx

# Shows containers running on respective networks
docker network inspect bridge
docker network inspect my_app_net

docker network --help

docker network connect <new_network> <different_Container_id/name>


# DNS
Containers within same network can talk to each other.
docker container exec -it my_nginx ping new_nginx

# Assignment : Curl version check
docker container run --rm -it centos:7 bash
yum update curl

docker container run --rm -it ubuntu:14.04 bash
apt-get update && apt-get install -y curl

curl --version


## DNS Round Robin test : Assignment
docker network create dude
docker container run -d --net dude --net-alias search elasticsearch:2
docker container run -d --net dude --net-alias search elasticsearch:2
docker container run --rm --net dude alpine nslookup search
docker container run --rm --net dude centos curl -s search:9200

docker container --rm
--net-alias : an alias to call that container with



## Images
docker image ls
docker image histroy nginx
docker history nginx:latest
docker image inspect <image_name>        # return JSON metadata about the image

## Tags
docker image tag --help

docker image tag <source_image> <target_image>
docker image tag nginx arpit/nginx
docker image push arpit/nginx

docker login
cat .docker/config.json
For mac -> Stores in Keychain

## Prune
docker image prune - clean up dangling images
docker system prune - clean up everything
docker image prune -a : remove images not in use
docker system df : see space usage
docker volume prune - remove unused volumes

# Volumes
Volumes remains ever after deleting the containers. Need to be deleted manually.
docker volume ls - get list of all volumes
docker volume inspect <volume_id> : Get more details

volume is like attached volume in docker system. 
Bind mount is simply soft link to a folder in host system.


# Docker Registeries

docker tag hello-world 127.0.0.1:5000/hello-world
docker push 127.0.0.1:5000/hello-world

docker remove image <name>




# Dockerfiles


docker build -f <some-Dockerfile>

docker image build --tag customnginx .
docker image build --tag customnginx <some-dockerfile>

<Github>/dockerfile-sample-1
<Github>/dockerfile-sample-2


Assignment 1: 
https://github.com/BretFisher/udemy-docker-mastery/tree/main/dockerfile-assignment-1


# Volumes

Data Volumes
- Need to be cleaned up manually and doesn't clean up when image is deleted

docker image inspect mysql
Look for Volumes and Mounts
It actually creates a Bind Mount as well which is hosted on our local machine and does the mapping internally


docker volume ls
docker volume inspect 213

Above works only on linux machines
Limitation on Mac and Windows as they create a VM in which these services are running

create named volume for user friendly names
-v mysql-db:/var/lib/mysql
-v <name>:<volume_location>

docker volume create
required to do this before "docker run" to use custom drivers and labels

Bind Mounts
mounting looks very similar to data volume

docker container run -d --name nginx -p 80:80 -v $(pwd):/usr/share/nginx/html nginx

# For reference of Dockerfiles
Go to any docker hub image and check out their dockerfiles.







