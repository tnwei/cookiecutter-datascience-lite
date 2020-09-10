"""
Functions for loading data, example:

```
import pandas as pd
def load_shopping_bill():
    \"""
    Returns DataFrame of shopping bill.
    \"""
    bill = pd.DataFrame({
        "item": ["apple", "pear", "grapes", "lemon"],
        "unit_price": ["4.00, 2.50, 10.00, 2.00"],
        "count": [2, 2, 1, 1]
    })   
    return bill
```
"""
