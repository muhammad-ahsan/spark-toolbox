# Spark Toolbox

Welcome to the Spark Toolbox! This mono repository is designed to house a collection of Spark-based applications that can be executed on both local and remote Spark clusters. Each application within this repository is independently dockerized, making it easy to deploy and manage across different environments. This repository is intended for use within our organization, providing a centralized location for all spark jobs.




# Deployment Infrastructure

* Intended to run on AWS EMR serverless
* Should be able to test on local as well as remote cluster


# Local Execution
```
spark-submit --master local src/<APP>/main.py
```

# Local Docker Execution 
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

## Build Dockers 
```
docker build --build-arg job_name=<APP_NAME> -f src/Dockerfile  -t <OPTIONAL_REPO_NAME>/<APP_NAME> .
```

## Run Dockers

```
docker run --rm <OPTIONAL_REPO_NAME>/<APP_NAME>
```
