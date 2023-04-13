import unittest

from main_penalty_calculate.models import (
    ViolatorAvaliation,
    IdentityCard,
    LicensePlate
)


class TestViolatorAvaliation(unittest.TestCase):
    def test_violator_avaliation_identity_card(self):
        violator = ViolatorAvaliation(
            identity_card=IdentityCard("29.441.369-8", "Aoki"),
            license_plate=LicensePlate("UCH-6237"),
            demerit_points=4,
            penalty_amount=78.10,
            status_driver_license = "Ativa"
        )

        identity_card = (
            violator.identity_card_name, violator.identity_card_number
        )
    
        self.assertEqual(
            identity_card, ("Aoki", "29.441.369-8")
        )

    def test_violator_avaliation_license_plate(self):
        violator = ViolatorAvaliation(
            identity_card=IdentityCard("19.632.142-6", "Takashi"),
            license_plate=LicensePlate("IDE-3516"),
            demerit_points=7,
            penalty_amount=00.00,
            status_driver_license = "Ativa"
        )

        license_plate_number = violator.license_plate_number

        self.assertEqual(
            license_plate_number, "IDE-3516"
        )

    def test_violator_avaliation_demerit_points(self):
        violator = ViolatorAvaliation(
            identity_card=IdentityCard("29.441.369-8", "Aoki"),
            license_plate=LicensePlate("UCH-6237"),
            demerit_points=4,
            penalty_amount=78.10,
            status_driver_license = "Ativa"
        )

        demerit_points = violator.demerit_points
    
        self.assertEqual(
            demerit_points, 4
        )

    def test_violator_avaliation_penalty_amount(self):
        violator = ViolatorAvaliation(
            identity_card=IdentityCard("29.441.369-8", "Aoki"),
            license_plate=LicensePlate("UCH-6237"),
            demerit_points=4,
            penalty_amount=78.10,
            status_driver_license = "Ativa"
        )

        penalty_amount = violator.penalty_amount
    
        self.assertEqual(
            penalty_amount, 78.10
        )

    def test_violator_avaliation_status_driver_license(self):
        violator = ViolatorAvaliation(
            identity_card=IdentityCard("29.441.369-8", "Aoki"),
            license_plate=LicensePlate("UCH-6237"),
            demerit_points=4,
            penalty_amount=78.10,
            status_driver_license = "Ativa"
        )

        status_driver_license = violator.status_driver_license
    
        self.assertEqual(
            status_driver_license, "Ativa"
        )