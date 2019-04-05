from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, REGISTRY
from flask import Flask, Response, abort
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

class DummyCollector(object):
    def collect(self):
        dummy_metric = GaugeMetricFamily("dummy_metric", "dummy metric", labels=["dummy_label"])

        dummy_metric.add_metric(["a"], 1)
        dummy_metric.add_metric(["b"], 2)
        dummy_metric.add_metric(["c"], 3)

        yield dummy_metric


REGISTRY.register(DummyCollector())

app = Flask(__name__)

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route("/up")
def up():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, threaded=True)
