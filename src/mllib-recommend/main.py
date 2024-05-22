import os
import shutil

from pyspark import SparkContext
from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating

from common_utils.utils import download_file


def prepare_data(input_data: str, sc: SparkContext):
    data = sc.textFile(input_data)
    ratings = data.map(lambda line: line.split(',')) \
        .map(lambda l: Rating(int(l[0]), int(l[1]), float(l[2])))
    return ratings


def train_model(ratings):
    # Build the recommendation model using Alternating Least Squares
    rank = 10
    num_iterations = 10
    model = ALS.train(ratings, rank, num_iterations)
    return model


def test_evaluate_model(model, ratings):
    # Evaluate the model on training data
    testdata = ratings.map(lambda p: (p[0], p[1]))
    predictions = model.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))
    rates_and_predictions = ratings.map(lambda r: ((r[0], r[1]), r[2])).join(predictions)
    mse = rates_and_predictions.map(lambda r: (r[1][0] - r[1][1]) ** 2).mean()
    print("Mean Squared Error = " + str(mse))


def save_model(output_path: str, model, sc: SparkContext):
    # Save and load model
    model.save(sc, output_path + "collaborative-filter")
    # Load model from disk
    model_from_disk = MatrixFactorizationModel.load(sc, output_path + "collaborative-filter")
    return model_from_disk


def main():
    output_path: str = "outputs/recommend/"
    input_path: str = download_file(
        "https://raw.githubusercontent.com/muhammad-ahsan/spark-toolbox/main/data/sample.csv",
        "csv")

    # Remove the output directory if it exists
    if os.path.exists(output_path):
        shutil.rmtree(output_path)

    sc: SparkContext = SparkContext(appName="spark-mllib-recommender")

    ratings = prepare_data(input_path, sc)
    model = train_model(ratings)
    test_evaluate_model(model, ratings)
    save_model(output_path, model, sc)
    print("Saved model to disk")


if __name__ == '__main__':
    main()
