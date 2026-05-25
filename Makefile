.PHONY: validate grade security check

validate:
	python3 scripts/validate_repo.py

grade:
	python3 scripts/grade_skills.py --min-score 90

security:
	python3 scripts/security_scan.py

check: validate grade security
