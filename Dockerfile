FROM tensorflow/tensorflow:latest
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir --ignore-installed -r requirements.txt
RUN pip install flask
EXPOSE 8080
CMD [ "python" , "app.py" ]