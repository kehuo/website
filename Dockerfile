FROM python:3.7
WORKDIR /data/project
ENV PYTHONIOENCODING utf-8
ENV LANG en_US.UTF-8

COPY . .
VOLUME [ "/data/project/website/instance" ]
RUN pip install -r requirements.txt
CMD [ "gunicorn", "website:create_app()", "-c", "./website/instance/gunicorn.conf.py" ]
