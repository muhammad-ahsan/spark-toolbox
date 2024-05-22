import os
import logging.config
import shutil
import requests

from pyspark import SparkContext
from pyspark.rdd import RDD

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(module)s:%(funcName)s %(lineno)d: %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def _download_file() -> str:
    url = "https://raw.githubusercontent.com/muhammad-ahsan/spark-toolbox/main/data/sample.txt"
    local_file_path = "input.txt"

    response = requests.get(url)
    if response.status_code == 200:
        with open(local_file_path, 'wb') as f:
            f.write(response.content)
    else:
        print("Failed to download file.")
        raise IOError("Failed to download file.")

    return local_file_path


def main() -> None:
    # Initiate setup
    input_path: str = _download_file()
    output_path: str = "outputs/word-count/"

    # Remove the output directory if it exists
    if os.path.exists(output_path):
        shutil.rmtree(output_path)

    # Initialize Spark Context
    sc: SparkContext = SparkContext(appName="Word Count")
    # Read and process the file
    words: RDD = sc.textFile(input_path).flatMap(lambda line: line.split(" "))
    word_counts: RDD = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)
    # Save the statistics
    word_counts.saveAsTextFile(output_path)
    logger.info("Word counts saved to file...")
    sample_data = word_counts.take(5)  # Take the first 5 elements as a sample
    logger.info(f"Sample words: {sample_data}")


if __name__ == "__main__":
    main()
