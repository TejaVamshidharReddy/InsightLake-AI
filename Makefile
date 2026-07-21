install:
	python -m pip install -r requirements.txt

test:
	pytest -q

lint:
	ruff check .

run-api:
	uvicorn api.main:app --reload
