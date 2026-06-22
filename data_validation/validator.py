"""Data quality validator."""
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class ValidationResult:
    passed: int
    failed: int
    failures: List[Dict]
    
    @property
    def has_failures(self):
        return self.failed > 0
        
    def summary(self):
        return f"{self.passed} passed, {self.failed} failed"

class Validator:
    def __init__(self, schema=None):
        self.schema = schema or {}
        
    def validate(self, df):
        return ValidationResult(passed=0, failed=0, failures=[])
