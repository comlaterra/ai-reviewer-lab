.PHONY: run test lint

run:
	FLASK_ENV=development python -m src.app

test:
	python -m pytest tests/ -v

lint:
	python -m flake8 src/ --max-line-length=100
