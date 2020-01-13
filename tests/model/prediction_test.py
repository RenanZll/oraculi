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

    y_pred = Prediction().validate(persisted_X_test)

    accuracy_report = classification_report(persisted_y_test, y_pred)
    assert(accuracy_report == persisted_accuracy_report)


def test_prediction_return_class(mocker):
    pipeline = mocker.Mock()
    pipeline.predict.return_value = ['class1']

    subject = Prediction(pipeline=pipeline)

    assert subject.to('document1') == 'class1'

def test_prediction_receive_document_in_a_list(mocker):
    pipeline = mocker.Mock()
    pipeline.predict.return_value = ['class1']

    prediction = Prediction(pipeline=pipeline)
    prediction.to('document1')

    pipeline.predict.assert_called_once_with(['document1'])
