from datetime import date
from unittest import TestCase, main

from pay_by_square import generate


class TestPayBySquare(TestCase):
    def test_amount_iban(self):
        self.assertEqual(
            generate(amount=1, iban='SK7700000000000000000000', date=date(2020, 7, 5)),
            '000440007S3VT0DFSETNDU5J8KF4EI1MT7B3BBH3P91D830QDBA6IRPF97451V4U'
            '11PHMI423IDK7VVU5P800',
        )

    def test_amount_iban_swift(self):
        self.assertEqual(
            generate(
                amount=1,
                iban='SK7700000000000000000000',
                swift='FIOZSKBAXXX',
                date=date(2020, 7, 5),
            ),
            '0004Q000DS03UHKLF59M2IK7FUCM3SBUK5FM62CCKLR4QOKAJSBPPL4ND4R66LSI'
            '1K92GURM0FH5E3DASNBTNAKASV94PB5VVU1BRO00',
        )

    def test_amount_iban_symbols(self):
        self.assertEqual(
            generate(
                amount=1,
                iban='SK7700000000000000000000',
                date=date(2020, 7, 5),
                variable_symbol='11',
                constant_symbol='22',
                specific_symbol='33',
            ),
            '0004G000EIUCQ7TO82O7GRAEMT06773UPLKOEC76BV3NBBNP7HPVSSJHUNVFBD7G'
            '6DAAMTDL4B8ND4D06QCNS7PHMPBVVVROGU000',
        )

    def test_amount_iban_symbols_beneficiary_name(self):
        self.assertEqual(
            generate(
                amount=1,
                iban='SK7700000000000000000000',
                date=date(2020, 7, 5),
                variable_symbol='11',
                constant_symbol='22',
                specific_symbol='33',
                beneficiary_name='Foo',
            ),
            '0004M0006MISSBD0SBV1135OEDE05KA7IM2GBI0U0M5LHD5LIEP7D9CJO6T8GQDF'
            'UKCL7TOEGN8TDOVAJ2GL85IOEA8OV3O1AQOFVU3JKS00',
        )

    def test_pass_all_arguments(self):
        self.assertEqual(
            generate(
                amount=1,
                iban='SK7700000000000000000000',
                swift='FIOZSKBAXXX',
                date=date(2020, 7, 5),
                variable_symbol='11',
                constant_symbol='22',
                specific_symbol='33',
                beneficiary_name='Foo',
                beneficiary_address_1='address 1',
                beneficiary_address_2='address 2',
                note='money',
            ),
            '0006Q0006GO7VIPNP2PPLDV1MO04PTB6C4OSM4KU3JKSDNJLJ0GBAT9GTI9DD7MF'
            'QKGMLI4RD7996S1K78MKT8S0F46HK5TF6A6GP881BBMM66JVFMBBSM9KQRM2TN2V'
            'RABUV7KFD22BFFIVVTFKO000',
        )


if __name__ == "__main__":
    main()
