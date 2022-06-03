check:
	black --check ./ && isort --check-only ./ && flake8 ./	