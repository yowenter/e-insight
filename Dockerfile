FROM python:3.6-alpine3.6 

RUN apk add --no-cache gcc python-dev musl-dev


RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app



COPY ./requirements.txt /usr/src/app/
# RUN pip install  -r /usr/src/app/requirements.txt -i http://pypi.douban.com/simple/  --trusted-host pypi.douban.com

RUN pip install  -r /usr/src/app/requirements.txt

COPY . /usr/src/app


EXPOSE 8000

CMD [ "gunicorn","-k","sync","-w","5","--max-requests","50000", \
        "--max-requests-jitter","50000","--access-logfile","-", "--error-logfile","-","-b", \
        "0.0.0.0:8000","e_insight.app:app"  ]



