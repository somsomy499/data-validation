# Data Validation ✅

Automated data quality validation with schema drift detection and anomaly alerts.

## Features

- **Schema Validation**: Type checking, null constraints
- **Statistical Tests**: Distribution drift, correlation changes
- **Great Expectations**: Full integration
- **Alerts**: Slack, email, webhook on failures

## Quick Start

```python
from data_validation import Validator

validator = Validator(schema=expected_schema)
results = validator.validate(train_df)
if results.has_failures:
    alert.send(f"Data quality issues: {results.summary}")
```

## License

MIT