from model.prediction import Prediction
import joblib
from os import path
from sklearn.metrics import classification_report

current_dir = path.dirname(path.abspath(__file__))

def test_model_integrity():
    persisted_X_test = joblib.load(f'{current_dir}/X-test.pkl')
    persisted_y_test = joblib.load(f'{current_dir}/y-test.pkl')
    text_file = open(f'{current_dir}/accuracy-report.txt', "r")
    persisted_accuracy_report = text_file.read()
    text_file.close()
    y_pred = Prediction().to(persisted_X_test)
    print(len(y_pred))
    print(len(persisted_X_test))
    accuracy_report = classification_report(persisted_y_test, y_pred)
    assert(accuracy_report == persisted_accuracy_report)
