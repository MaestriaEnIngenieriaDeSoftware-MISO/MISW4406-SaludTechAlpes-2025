FROM python:3.10

EXPOSE 5000/tcp

COPY notififaciones-requirements.txt ./
RUN pip install --upgrade --no-cache-dir "pip<24.1" setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r notififaciones-requirements.txt

COPY . .

CMD [ "flask", "--app", "./src/notificaciones/main", "run", "--host=0.0.0.0"]