FROM bitnami/spark:3.1.2

ENV PYSPARK_PYTHON=python3
ENV SPARK_HOME=/opt/bitnami/spark
ENV PATH=$SPARK_HOME/bin:$PATH

USER root
RUN apt-get update && apt-get install -y python3 python3-pip

ARG job_name

WORKDIR "/opt/bitnami/spark/app/${job_name}/"

COPY "src/${job_name}/*" .

RUN pip3 install --no-cache-dir -r requirements.txt

# In Dockerfile, the RUN instructions are executed during the image
# building process. The $file_path variable set in the RUN instruction is not
# available in the CMD instruction. Fix: Use an environment variable

ENV file_path="/opt/bitnami/spark/app/${job_name}/main.py"
CMD ["sh", "-c", "spark-submit $file_path"]
