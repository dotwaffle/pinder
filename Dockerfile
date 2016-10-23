# docker build -f Dockerfile . -t pinder:0.1
# sudo docker run -p 8000:8000 pinder:0.1 runserver 0.0.0.0:8000

FROM python:3
ENV PYTHONUNBUFFERED 1
COPY pinder /pinder
EXPOSE 8000
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt;\
    python /pinder/manage.py migrate;\
    python /pinder/manage.py loaddata /pinder/users/fixtures/initial_data.json

ENTRYPOINT ["python", "/pinder/manage.py"]
