#### Useful Tutorials
[Docker Tutorial for Beginners - A Full DevOps Course on How to Run Applications in Containers](https://youtu.be/fqMOX6JJhGo)

[Practice Labs](https://kodekloud.com/p/docker-labs) - Practiice docker commands

### **Commands**
1. `docker run image_name`
   - Run docker image 
   - If not present locally, it will go to docker hub and pull the image
2. `docker ps`
   - List running containers and their basic information
3. `docker ps -a`
   - List all containers including all running and previously stopped containers
4. `docker stop container_name/container_id`
   - To stop a running container
5. `docker rm container_name`
   - Remove a container (remove from cache for exited containers)
   - Returns container name if successful
6. `docker images`
   - List the available images and their information
7. `docker rmi image_name`
   - Delete the image
   - **Important**: Delete all dependent containers to remove image
8. `docker pull image_name`
   - Pull docker image from docker hub for later use
9. #### Append a command
   - Docker container will exit if it has no processes running. 
   - The container only lives as long as the process inside it is alive. 
   - for example `docker run ubuntu` will open and exit because it don't have any running processes. 
   - `docker run ubuntu sleep 5`  here command sleep for 5 seconds is executed after initializing docker container and after executing sleep, the container will exit. This is executing command with run command.
10. `docker exec container_name <command>` 
    - This will execute the specified command on a already running docker container
11. `docker inspect container_name/container_id`
    - This will give detailed info about container.
12. `docker logs container_id/container_name`
    - To see the logs
13. `docker history image_name`
    - Shows history of building the specified docker image and their information


### Run - attach and detach 

- When running a docker image, it runs in a foreground or in an attached mode.
- This means the console will be attached to the standard out of the container and you will see the output from the container. 
- You won't be able do anything on that console other than view the output until the container stops. 
- Also, it won't respond to your inputs. 
- Either you can press `CTRL+C` to stop the container and application hosted on the container exits and you get back to your prompt. 
- Otherwise you can use the docker container in **Detach** mode by giving `-d` flag. 
- `docker run -d image_name` - This will run the docker container in background mode and you will get back to your promt immediately. 
- `docker attach container_name/container_id` - To attach back to the running container by its name or id. 

### Detailed `docker run`
1. Tag
   - You can specify tag of run command.
   - `docker run redis:4.0` this will use image containing redis version 4.0.
   - If tag is not specified, it will consider the latest tag associated with the latest version of software. 

2. Run - STDIN
   -  Upon running a docker container, it does not listen to standard input and will not accept any inputs if you have specified in the program.
   -  `-i` flag specifies interactive mode. The console goes in interactive mode and accepts inputs. for example `docker run -i simple-prompt-docker`
   -  `-it` flag specifies that the console will be attached to docker's terminal. It will then promt for input and will accept input as well.
3. Run - PORT Mapping
   - `-p` flag will map the internal port of docker container to global port of the host. 
   - for example `docker run -p 80:5000 simple-webapp`
4. Run - Volume mapping
   - Every container has its own isolated filesystem. Any changes to the file is done inside the filesystem. 
   - When you remove any container, all the data inside it will be deleted.
   - For example if you do `docker run mysql` and then `docker stop mysql` and `docker rm mysql` then all the data will get deleted.
   - If you want to persist the data, you would want to map a directory outside the container on the host to the directory inside the container.
   - `docker run -v /directory/of/host:/directory/of/container image_name`

### Environment Variables
1. Set an environment variable while running docker container:
   - `docker run -e variable_name=VALUE image_name`
2. Check all environment variables
   - `docker inspect container_name/id` and under Config->ENV.

### **Create your own docker image**
Steps to follow:
1. Choose OS
2. Updatet apt repo
3. Install dependencies using apt
4. Install Python dependencies using pip
5. Copy source code to /opt folder

For example, for a simple web page, create this docker file named `Dockerfile` without giving extension. 
```
FROM Ubuntu

RUN apt-get update
RUN apt-get install python

RUN pip install flask
RUN pip install flask-mysql

COPY . /opt/source-code

ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run
```

Now build the docker image using `docker build` command and specify the dockerfile as input as well as tag name for the image.
This will create the image locally on your system.

To make it available to public docker hub registry, run the `docker push` command and specify name of the image you created. 

For example: `docker push account_name/image_name`

### Dockerfile
format: `INSTRUCTION ARGUMENT`

Basic commands:
1. FROM - Defines what the base OS Should be. Every docker image is based on another image. Either an OS or image build previously based on an OS. 
2. RUN - instructs docker to run particular command on the container
3. COPY - copies files from local system to docker image
4. ENTRYPOINT - Allows us to specify a command that will run when image will run as a container.
   - Whatever you will pass in `docker run` command will appended to ENTRYPOINT and that command will get executed.
   - To set a default argument (if in case `docker run` command doesn't specify entrypoint argument) write `CMD` and default param after using ENTRYPOINT. 
5. CMD - Run a command
   - format: `CMD <command> <param1>`
   - JSON array format: `CMD ["command","param1"]`