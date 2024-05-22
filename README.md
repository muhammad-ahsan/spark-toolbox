# Spark Toolbox

Welcome to the Spark Toolbox! This mono repository is designed to house a collection of Spark-based applications that can be executed on both local and remote Spark clusters. Each application within this repository is independently dockerized, making it easy to deploy and manage across different environments. This repository is intended for use within our organization, providing a centralized location for all Spark jobs.




# Deployment Infrastructure

* Intended to run on AWS EMR serverless
* Should be able to test on local as well as remote cluster


# Local Execution
```
spark-submit --master local[*] src/<APP>/main.py
```

# Local Execution via Docker
```
./script/build-image.sh
```


# Execution over Spark Cluster

```
```

# Miscellaneous
## Running using Hive support

```
spark-submit --packages org.apache.spark:spark-hive_2.12:3.1.2 your_script.py
```

## Dockerized Apps
```
docker build -f src/<APP_DIR>/Dockerfile  -t <APP_NAME> .
```