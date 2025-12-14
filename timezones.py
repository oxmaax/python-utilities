
---

### `timezones.py`

```python
from datetime import datetime
import pytz


def convert_timezone(
    dt: datetime,
    from_tz: str = "US/Eastern",
    to_tz: str = "Europe/Zurich",
) -> datetime:
    """
    convert a datetime from one timezone to another.
    """
    source = pytz.timezone(from_tz)
    target = pytz.timezone(to_tz)

    # localize if naive
    if dt.tzinfo is None:
        dt = source.localize(dt)
    else:
        dt = dt.astimezone(source)

    return dt.astimezone(target)


if __name__ == "__main__":
    # example: 2025-01-01 09:00 in ET to CET
    naive = datetime(2025, 1, 1, 9, 0, 0)
    converted = convert_timezone(naive, "US/Eastern", "Europe/Zurich")

    print("original (et):", naive, "(naive)")
    print("converted (zurich):", converted)
