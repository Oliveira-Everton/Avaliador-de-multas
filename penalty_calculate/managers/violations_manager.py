class ViolationsManager:
    def __init__(self, traffic_violations):
        self._traffic_violations = traffic_violations

    @property
    def traffic_violations(self):
        return self._traffic_violations
