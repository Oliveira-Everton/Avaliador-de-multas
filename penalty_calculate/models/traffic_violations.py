class TrafficViolations:

    def __init__(self, traffic_violations=[]):
        self._traffic_violations = traffic_violations

    @property
    def violations(self):
        return self._traffic_violations
