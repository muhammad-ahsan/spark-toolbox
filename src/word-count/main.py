import os
import logging.config
import shutil

from pyspark import SparkContext

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(module)s:%(funcName)s %(lineno)d: %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    # Initiate setup
    input_path = "data/sample.txt"
    output_path = "outputs/word-count/"

    # Remove the output directory if it exists
    if os.path.exists(output_path):
        shutil.rmtree(output_path)

    # Initialize Spark Context
    sc = SparkContext(appName="Word Count")
    # Read and process the file
    words = sc.textFile(input_path).flatMap(lambda line: line.split(" "))
    word_counts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
    # Save the statistics
    word_counts.saveAsTextFile(output_path)
    logger.info("Word counts saved to file...")


if __name__ == "__main__":
    main()
