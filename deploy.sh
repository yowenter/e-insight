set -ex
rsync --exclude venv --exclude grafana-storage  --exclude prometheus-data -r ../e-insight root@centos-1:/smb/share
#ssh ty-1 "cd e-insight && docker-compose -f insight.yml up -d  "
#ssh ty-1 "cd e-insight && docker-compose -f insight.yml up -d "
#ssh centos-1 "supervisorctl restart e-insight"

ssh centos-1 "cd /smb/share/e-insight && docker-compose -f insight.yml build && docker-compose -f insight.yml up -d "