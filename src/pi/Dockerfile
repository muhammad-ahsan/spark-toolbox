FROM bitnami/spark:3.1.2

ENV PYSPARK_PYTHON=python3
ENV SPARK_HOME=/opt/bitnami/spark
ENV PATH=$SPARK_HOME/bin:$PATH

USER root
RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /opt/bitnami/spark/app/pi/

COPY src/pi/* .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["spark-submit", "/opt/bitnami/spark/app/pi/main.py"]