FROM tiangolo/uwsgi-nginx-flask:python3.8
WORKDIR /app
COPY ./app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app  .
ENV FLASK_APP=main.py
# EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]

