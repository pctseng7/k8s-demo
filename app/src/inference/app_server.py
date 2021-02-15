import logging
import json
from flask import Response, Flask
from inference.environment import HostEnvironment
class Server(object):
    def __init__(self, name):
        self.serviceName = name
        self.env = HostEnvironment()
        self.app = self._start_flask_app(name)
        
    def _start_flask_app(self,serviceName):
        app = Flask(serviceName)
        app.add_url_rule('/view-loaded-models', 'listmodel', self._listModel, methods=['GET'])
        app.add_url_rule('/infer', 'invoke', self._invoke, methods=['POST'])
        return app
        
    def _invoke(self):
        # Pending: Python Client API call to Inferencing backend 
        output = {
            'sampleModelName': 'PredictPatientFalling',
            'modelVersion': 1,
            'Description': 'Patient has high risk falling in the next 15 mins',
            'Probability': 0.95678
        }
        logging.debug("k8s-demo: Infer API being hit!")
        return Response(response=json.dumps(output), status=200, content_type="application/json")

    def _listModel(self):
        # Pending: Python Client API call to Inferencing backend 
        output = [
            {
                'sampleModelName': 'PredictPatientFalling',
                'modelVersion': 1,
                'Description': 'Patient has high risk falling in the next 15 mins'
            },
            {
                'sampleModelName': 'PredictPatientFalling',
                'modelVersion': 2,
                'Description': 'Patient has high risk falling in the next 30 mins'
            }
        ]
        logging.debug("k8s-demo: view-loaded-models API being hit!")
        return Response(response=json.dumps(output), status=200, content_type="application/json")

