set -ex
rsync --exclude venv -r ../e-insight root@ty-1:/root/
ssh ty-1 "cd e-insight && docker-compose -f insight.yml build "
#ssh ty-1 "cd e-insight && docker-compose -f insight.yml up -d "

