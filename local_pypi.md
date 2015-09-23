This document describes how to install python packages from a local pypi-like
server. This is helpful when network bandwidth is limited or expensive, e.g. on
a plane or when tethered to a phone. First you need to download `.tgz` package
files when you do have a good network connection. Then you can run a server
locally. Suggested steps are:

- Populate a directory with .tgz python package files. Use python package
  `pip2pi`, which installs additional executables `pip2tgz`, `dir2pi`:

  ```
  pip install pip2pi
  pip2tgz $LOCAL_PACKAGE_DIR --no-use-wheel $SOME_PACKAGE_NAME
  ```
  
  `pip2tgz` takes the same arguments as `pip` so useful variants include:
  - `-r requirements.txt`
  - `--index-url $MY_COMPANYS_PYPI_INDEX_URL`
  
- Run `dir2pi` to create an index directory named `simple/` with the structure pip expects:

  ```
  dir2pi $LOCAL_PACKAGE_DIR
  ```

- Run a web server serving files out of the `simple/` directory:

  ```
  cd $LOCAL_PACKAGE_DIR
  python -m SimpleHTTPServer
  ```
  
- test that it works:

  ```
  virtualenv /tmp/venv
  /tmp/venv/bin/pip install -i 'http://localhost:8000/simple/' $SOME_PACKAGE_NAME
  ```

##### Docker

- With docker on OS X, if docker containers need to install packages from the
  local pypi server, then run the pypi server in another docker container, e.g.:

  ```
  FROM ubuntu
  RUN apt-get install -y python
  RUN mkdir /srv/pypi/
  WORKDIR /srv/pypi/
  ADD . /srv/pypi/
  EXPOSE 8000
  CMD ["python", "-m", "SimpleHTTPServer"]
  ```

  There are a few ways to contact that server from other containers. You could
  `build` and `run` it with basic options:

  ```
  docker build -t local-pypi .
  docker run -itP local-pypi
  ```
  
  And then simply use `docker-machine ip` to find the VM's IP, and use `docker
  port` or `docker ps` to find out which port on the VM is mapped to 8000 in
  the server container. Then other docker containers can do

  ```
  pip install --index-url "http://$DOCKER_MACHINE_IP:$MAPPED_VM_PORT/simple" $SOME_PACKAGE_NAME
  ```
  
  Alternatively you could run the pypi server container with an explicit name:

  ```
  docker run -itP --name pypi local-pypi
  ```

  and then use `--link pypi:pypi` when running your other container. Then the other container can do

  ```
  pip install --index-url "http://pypi:8000/simple" $SOME_PACKAGE_NAME
  ```
