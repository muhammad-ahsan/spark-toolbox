from pyspark.sql import SparkSession


def main():

    custom_metastore_path = "outputs/test/metastore_db"
    custom_warehouse_path = "outputs/test/warehouse"

    # Create SparkSession with Hive support
    spark = SparkSession.builder \
        .appName("CustomHiveConfig") \
        .config("spark.sql.warehouse.dir", custom_warehouse_path) \
        .config("javax.jdo.option.ConnectionURL", f"jdbc:derby:;databaseName={custom_metastore_path};create=true") \
        .enableHiveSupport() \
        .getOrCreate()

    create_table_query: str = "CREATE TABLE IF NOT EXISTS src (key INT, value STRING)"  # noqa
    spark.sql(create_table_query)

    load_table_query: str = "LOAD DATA LOCAL INPATH 'kv1.txt' INTO TABLE src"
    # hive_context.sql(load_table_query)
    spark.sql(load_table_query)
    select_query: str = "FROM src SELECT key, value"
    # hive_context.sql(select_query).collect()
    spark.sql(select_query).collect()


if __name__ == '__main__':
    main()
