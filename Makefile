.PHONY: validate check

validate:
	python3 scripts/validate_repo.py

check: validate
