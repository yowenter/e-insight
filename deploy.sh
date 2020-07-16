set -ex
rsync -r /Users/wenter/iProjects/e-insight root@161.35.201.232:/root/
ssh do "cd e-insight && docker-compose -f insight.yml build "
ssh do "cd e-insight && docker-compose -f insight.yml up -d "

