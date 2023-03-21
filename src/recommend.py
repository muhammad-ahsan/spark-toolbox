from __future__ import print_function
from pyspark import SparkContext
from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating


def get_spark_context():
    sc = SparkContext(appName="Pyspark mllib Example")
    return sc


def prepare_data(sc):
    data = sc.textFile("test.data")
    ratings = data.map(lambda l: l.split(',')) \
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


def save_model(model, sc):
    # Save and load model
    model.save(sc, "target/tmp/myCollaborativeFilter")
    # Load model from disk
    model_from_disk = MatrixFactorizationModel.load(sc, "target/tmp/myCollaborativeFilter")
    return model_from_disk


def main():
    sc = get_spark_context()
    ratings = prepare_data(sc)
    model = train_model(ratings)
    test_evaluate_model(model, ratings)
    save_model(model, sc)


if __name__ == "__main__":
    main()
