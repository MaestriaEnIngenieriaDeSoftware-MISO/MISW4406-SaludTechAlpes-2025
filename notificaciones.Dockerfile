FROM python:3.10

COPY notificacion-requirements.txt ./
RUN pip install --no-cache-dir -r notificacion-requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

CMD [ "python", "./src/notificaciones/main.py" ]