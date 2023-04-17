FROM python:3.8-alpine

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "sh", "entrypoint.sh" ]

# docker-compose down --volumes --rmi all
# docker-compose up -d --force-recreate --build