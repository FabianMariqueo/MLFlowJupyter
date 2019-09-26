FROM python

RUN pip3 install flask
RUN pip3 install flask-cors
RUN pip3 install requests

RUN mkdir /proxy/
WORKDIR /proxy
COPY proxy-mlflow.py /proxy
