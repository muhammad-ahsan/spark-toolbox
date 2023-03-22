from pyspark import SparkContext
from pyspark import HiveContext


def get_spark_context(app_name: str = "Spark Application",
                      with_hive_context: bool = True) -> (SparkContext, HiveContext):
    sc = SparkContext(appName=app_name)
    if with_hive_context:
        sql_context = HiveContext(sc)
        return sc, sql_context
    else:
        return sc, None
