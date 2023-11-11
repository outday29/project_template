.PHONY: format lint test

format:
	black .
	ruff --select I --select E --select F --fix .

lint:
	black . --check
	ruff .

test:
	pytest --durations=0.1 ./tests