FROM python:3.10

EXPOSE 5000/tcp

COPY exportacionsta-requirements.txt ./
RUN pip install --upgrade --no-cache-dir "pip<24.1" setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r exportacionsta-requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

CMD [ "flask", "--app", "./src/exportacionsta/api", "run", "--host=0.0.0.0"]
