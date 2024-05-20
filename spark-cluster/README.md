# Setup the Spark Cluster
Run the spark cluster in via docker. A docker compose file will spin up spark master and worker nodes. 

```
mkdir spark-cluster
cd spark-cluster
# Use the pre-built bitnami/spark images
touch docker-compose.yml
```

# Start the Spark Cluster
```
docker-compose up -d
```
# Teardown the Spark Cluster
```
docker-compose down
```
cd .. 
# Copy Files
```
docker cp -L <LOCAL PATH>/main.py spark-master:/opt/bitnami/spark/main.py
```
# See the Logs

```
docker logs spark-master
```

cd spark-cluster

# Submit the spark program
```
docker-compose exec spark-master spark-submit --master spark://172.23.0.2:7077 main.py
```

# Reference

https://medium.com/@mehmood9501/using-apache-spark-docker-containers-to-run-pyspark-programs-using-spark-submit-afd6da480e0f