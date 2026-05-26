PYTHON ?= python3

.PHONY: validate grade security lint test check

validate:
	$(PYTHON) scripts/validate_repo.py
	$(PYTHON) scripts/validate_skills.py

grade:
	$(PYTHON) scripts/grade_skills.py --min-score 90

security:
	$(PYTHON) scripts/security_scan.py

lint:
	$(PYTHON) -m ruff check .

test:
	$(PYTHON) -m pytest

check: validate grade lint security test
