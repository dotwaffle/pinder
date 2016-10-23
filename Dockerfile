FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
CMD [ "python", "/code/pinder/manage.py", "migrate" ]
CMD [ "python", "/code/pinder/manage.py", "loaddata", "/code/pinder/users/fixtures/initial_data.json" ]
CMD [ "python", "/code/pinder/manage.py", "loaddata", "/code/pinder/peering_requests/fixtures/initial_data.json" ]
