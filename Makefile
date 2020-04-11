lint:
	isort -y
	black .

install:
	pip install -r requirements.txt