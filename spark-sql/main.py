#  sc is an existing SparkContext.

from utils import get_spark_context


def main():
    sc, sql_context = get_spark_context("Spark SQL Application", True)
    sql_context.sql("CREATE TABLE IF NOT EXISTS src (key INT, value STRING)")
    sql_context.sql("LOAD DATA LOCAL INPATH 'kv1.txt' INTO TABLE src")
    # Queries are expressed in HiveQL
    sql_context.sql("FROM src SELECT key, value").collect()


if __name__ == '__main__':
    main()