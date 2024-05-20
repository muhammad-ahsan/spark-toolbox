import argparse
import logging
from operator import add
from random import random

from pyspark.sql import SparkSession

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(module)s:%(funcName)s %(lineno)d: %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def calculate_pi(partitions, output_uri):
    def calculate_hit(_):
        x = random() * 2 - 1
        y = random() * 2 - 1
        return 1 if x ** 2 + y ** 2 < 1 else 0

    tries = 100000 * partitions
    logger.info(f"Calculating pi with a total of {tries} tries in {partitions}")

    with SparkSession.builder.appName("spark-pi").getOrCreate() as spark:
        hits = spark.sparkContext.parallelize(range(tries), partitions) \
            .map(calculate_hit) \
            .reduce(add)
        pi = 4.0 * hits / tries
        logger.info(f"tries = {tries} - hits = {hits}  -> pi = {pi}")
        if output_uri is not None:
            df = spark.createDataFrame(
                [(tries, hits, pi)], ['tries', 'hits', 'pi'])
            df.write.mode('overwrite').json(output_uri)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--partitions',
                        default=2,
                        type=int,
                        help="No. of parallel partitions to use")
    parser.add_argument('--output_uri',
                        help="URI where output is saved")
    args = parser.parse_args()

    calculate_pi(args.partitions, args.output_uri)
