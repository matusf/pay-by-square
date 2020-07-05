from unittest import TestCase, main

from pay_by_square import generate


class TestPayBySquare(TestCase):
    def test(self):
        self.assertEqual(
            generate(amount=1, iban='SK7700000000000000000000'),
            '00044000DULVORPA054O3Q3S5TOTRH7S1PGF5J19UGS6EJQA7JEIN75VVFUSNSV3'
            '9T51EA4H07727VVURLU00',
        )
        self.assertEqual(
            generate(amount=1, iban='SK7700000000000000000000', swift='FIOZSKBAXXX'),
            '0004Q000D6VLDPM892PSOAVJ4R1ATTVSV98NUI3DFIPR7D4QQ4KONF90F526KCRO'
            'I8BLQ82MPPSR0USOHGD9NAC1K1N014FVVUMDPG00',
        )
        self.assertEqual(
            generate(
                amount=1,
                iban='SK7700000000000000000000',
                variable_symbol='11',
                constant_symbol='22',
                specific_symbol='33',
            ),
            '0004G0008OV1L1JQP2PSOAVJ4R1ATTVSV98NUI3DFIPR7D7LM1EV7HET0A1P82ES'
            'R1S31L45TSU1KEC8QMSRJDVVHRLVVVS3E5000',
        )
        self.assertEqual(
            generate(
                amount=1,
                iban='SK7700000000000000000000',
                variable_symbol='11',
                constant_symbol='22',
                specific_symbol='33',
                beneficiary_name='Foo',
            ),
            '0004M0009KHOVQ8LKP6SS5PM8L1RE2O72SM9D7B0J1OEIB5IFNPSCAO1QQNHFMAC'
            'KQB05H5SVO5TFHJB0A365357DHD40O3ORU1FVTIPFO00',
        )
        self.assertEqual(
            generate(
                amount=1,
                iban='SK7700000000000000000000',
                swift='FIOZSKBAXXX',
                variable_symbol='11',
                constant_symbol='22',
                specific_symbol='33',
                beneficiary_name='Foo',
                beneficiary_address_1='address 1',
                beneficiary_address_2='address 2',
                note='money',
            ),
            '0006Q000AEC7VBLGJROL8RIVGVK02C4MMLA7T6LKCVDOIJFK1QUJ4DS1J52UEIP5'
            'IVSLPQ2MG18S424V3SE9403C9GLRN4QNH6EQV7T0G4M143O82OO87MLAL2K6MFO3'
            '3T7ET83B3IM8AS7VVTIIR000',
        )


if __name__ == "__main__":
    main()
