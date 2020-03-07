FROM python:3.7.5
WORKDIR /data/project
ENV PYTHONIOENCODING utf-8
ENV LANG en_US.UTF-8

EXPOSE 8000

COPY . .
VOLUME [ "/data/project/website/instance", "/data/project/website/static" ]
RUN pip install -r requirements.txt
CMD [ "gunicorn", "website:create_app()", "-c", "./website/instance/gunicorn.conf.py" ]
