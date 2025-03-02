FROM python:3.10

EXPOSE 5000/tcp

COPY bff-requirements.txt ./
RUN pip install --no-cache-dir -r bff-requirements.txt

COPY . .

WORKDIR "/src"

CMD [ "uvicorn", "bff_sta.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]