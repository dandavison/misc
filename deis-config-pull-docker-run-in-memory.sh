set -e
cd $(mktemp -d)
mkfifo .env
deis config:pull -o -a $app_name &
docker run -it --env-file=.env $image bash
