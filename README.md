# Pay by square

Generate codes for [by square](https://bysquare.com/) payments.

## Installation

Note: `pay-by-square` generates string that can be passes to QR code generator to create
image. To run example below, you need to install
[qrcode module](https://github.com/lincolnloop/python-qrcode) as well.

```sh
pip install pay-by-square
```

## Usage

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
