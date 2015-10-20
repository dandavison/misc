FROM ubuntu
RUN apt-get install -y python
RUN mkdir /srv/pypi/
WORKDIR /srv/pypi/
ADD . /srv/pypi/
EXPOSE 8000
CMD ["python", "-m", "SimpleHTTPServer"]
