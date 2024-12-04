
class AnomalyDetector:

    def __init__(self):

        self.data = []


    def add_data(self, data_point):

        self.data.append(data_point)


    def detect_anomalies(self):

        # Placeholder for anomaly detection logic

        anomalies = []

        for data_point in self.data:

            if self.is_anomalous(data_point):

                anomalies.append(data_point)

        return anomalies


    def is_anomalous(self, data_point):

        # Placeholder for actual anomaly detection logic

        # For demonstration, let's assume any data point > 100 is an anomaly

        return data_point > 100


# Example usage

detector = AnomalyDetector()

detector.add_data(10)

detector.add_data(105)

detector.add_data(200)


anomalies = detector.detect_anomalies()

print("Detected anomalies:", anomalies)