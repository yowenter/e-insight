set -ex
rsync --exclude venv --exclude grafana-storage  --exclude prometheus-data -r ../e-insight root@ali-dev:/root/
#ssh ty-1 "cd e-insight && docker-compose -f insight.yml up -d  "
#ssh ty-1 "cd e-insight && docker-compose -f insight.yml up -d "
ssh ali-dev "supervisorctl restart e-insight"
