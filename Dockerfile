FROM centos:latest

RUN yum update -y
RUN yum install python3 -y

RUN pip3 install numpy

RUN pip3 install joblib

RUN pip3 install scikit-learn

COPY marks_model.pkl /

COPY runmodel.py /

CMD python3 runmodel.py 
