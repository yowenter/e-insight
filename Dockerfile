FROM python:3.6-alpine3.6 

RUN apk add --no-cache gcc python-dev musl-dev  libxml2-dev libxslt-dev python3-dev libffi-dev


RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app



COPY ./requirements.txt /usr/src/app/
# RUN pip install  -r /usr/src/app/requirements.txt -i http://pypi.douban.com/simple/  --trusted-host pypi.douban.com
RUN pip install --upgrade pip
RUN pip install  -r /usr/src/app/requirements.txt
RUN pip install gunicorn[gevent]

COPY . /usr/src/app

ENV PYTHONPATH /usr/src/app
EXPOSE 8000

CMD [ "gunicorn","-k","gevent","-w","1","--max-requests","50000","--log-level","debug", \
        "--max-requests-jitter","50000","--access-logfile","-", "--error-logfile","-","-b", \
        "0.0.0.0:8000","e_insight.app:app"  ]

#CMD ["python","e_insight/app.py"]

