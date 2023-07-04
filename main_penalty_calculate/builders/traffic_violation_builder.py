from ..models import TrafficViolation, IdentityCard, LicensePlate


class TrafficViolationBuilder:
    _IDENTITY_CARD_NAME = 'identity_card_name'
    _IDENTITY_CARD_NUMBER = 'identity_card_number'
    _LICENSE_PLATE_NUMBER = 'license_plate_number'
    _TYPE_INFRACTION = 'type_infraction'
    _INFRACTION_DATE = 'infraction_date'
    _NOTIFICATION_DATE = 'notification_date'

    def __init__(self, pre_traffic_violations):
        self._pre_traffic_violations = pre_traffic_violations

    def build_traffic_violations(self):
        traffic_violations = []
        for pre_traffic_violation in self._pre_traffic_violations:
            traffic_violations.append(
                TrafficViolation(
                    identity_card=IdentityCard(
                        name=pre_traffic_violation[
                            self._IDENTITY_CARD_NAME
                        ],
                        number=pre_traffic_violation[
                            self._IDENTITY_CARD_NUMBER
                        ]
                    ),
                    license_plate=LicensePlate(
                        number=pre_traffic_violation[
                            self._LICENSE_PLATE_NUMBER
                        ]
                    ),
                    type_infraction=pre_traffic_violation[
                        self._TYPE_INFRACTION
                    ],
                    infraction_date=pre_traffic_violation[
                        self._INFRACTION_DATE
                    ],
                    notification_date=pre_traffic_violation[
                        self._NOTIFICATION_DATE
                    ]
                )
            )
        return traffic_violations
