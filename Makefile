.PHONY: validate grade check

validate:
	python3 scripts/validate_repo.py

grade:
	python3 scripts/grade_skills.py --min-score 90

check: validate grade
