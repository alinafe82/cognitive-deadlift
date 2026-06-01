PYTHON ?= python3

.PHONY: help repo-check skills-check policy-check harness-check context-check docs-check slop-scan grade lint test security doctor check prod-gate validate

help:
	@echo "Targets:"
	@echo "  prod-gate    Run every meaningful check (use before merging)"
	@echo "  repo-check   Validate repo contract (files, manifests, index, doc contract, artifacts)"
	@echo "  skills-check Validate skill structure and content"
	@echo "  policy-check Validate thinking budget policy"
	@echo "  harness-check Validate harness fixtures"
	@echo "  context-check Validate context packs"
	@echo "  docs-check   Validate doc contract only (alias of repo-check)"
	@echo "  slop-scan    Scan for banned filler, placeholders, secret patterns"
	@echo "  grade        Score skills against the rubric (min 90)"
	@echo "  lint         Ruff lint"
	@echo "  test         Pytest"
	@echo "  security     Security hygiene scan"
	@echo "  doctor       Print repo readiness for AI-assisted work"
	@echo "  check        Back-compat alias for prod-gate"

repo-check:
	$(PYTHON) scripts/validate_repo.py

skills-check:
	$(PYTHON) scripts/validate_skills.py

policy-check:
	$(PYTHON) scripts/validate_policies.py

harness-check:
	$(PYTHON) scripts/validate_harnesses.py

context-check:
	$(PYTHON) scripts/validate_context_packs.py

docs-check: repo-check

slop-scan:
	$(PYTHON) scripts/validate_skills.py --slop-only

grade:
	$(PYTHON) scripts/grade_skills.py --min-score 90

security:
	$(PYTHON) scripts/security_scan.py

lint:
	$(PYTHON) -m ruff check .

test:
	$(PYTHON) -m pytest

doctor:
	$(PYTHON) scripts/doctor.py

prod-gate: repo-check skills-check policy-check harness-check context-check slop-scan grade lint security doctor test

check: prod-gate

# Back-compat alias for the previous validate target used in CI.
validate: repo-check skills-check policy-check harness-check context-check
