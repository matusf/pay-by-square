# PAY by square

Generate codes for [by square](https://bysquare.com/) payments.

## Installation

Note: `pay-by-square` generates string that can be passes to QR code generator to create
image. To run example below, you need to install
[qrcode module](https://github.com/lincolnloop/python-qrcode) as well.

```sh
pip install pay-by-square
```

## Usage

### API

```text
pay_by_square.generate(
    *,
    amount: float,
    iban: str,
    swift: str = '',
    date: Optional[date] = None,
    beneficiary_name: str = '',
    currency: str = 'EUR',
    variable_symbol: str = '',
    constant_symbol: str = '',
    specific_symbol: str = '',
    note: str = '',
    beneficiary_address_1: str = '',
    beneficiary_address_2: str = '',
) -> str:
    Generate pay-by-square code that can by used to create QR code for banking apps

    When date is not provided current date will be used.
```

### Example

```python
import qrcode
import pay_by_square


code = pay_by_square.generate(
    amount=10,
    iban='SK7283300000009111111118',
    swift='FIOZSKBAXXX',
    variable_symbol='47',
)

print(code)
img = qrcode.make(code)
img.show()
```

## Testing

```sh
python -m unittest tests.py
```

---

Kudos to [guys from devel.cz](https://devel.cz/otazka/qr-kod-pay-by-square)
