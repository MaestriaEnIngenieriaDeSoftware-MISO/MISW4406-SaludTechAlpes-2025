docker build . -f notificaciones.Dockerfile -t notificaciones/flask --no-cache
docker build . -f exportacionsta.Dockerfile -t exportacionsta/flask --no-cache
docker build . -f bff.Dockerfile -t bff_sta/flask --no-cache
docker build . -f saludtechalpes.Dockerfile -t saludtechalpes/flask --no-cache
docker-compose up --build