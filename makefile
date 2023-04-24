run: venv/bin/activate
	python3 ./src/init.py
	python3 ./src/main.py

venv/bin/activate: requirements.txt
	python3 -m venv venv
	. ./venv/bin/activate
	pip install -U -r requirements.txt

config: venv/bin/activate
	python3 ./src/config.py	

docker:
	docker-compose up --force-recreate --build && docker image prune -f

clean: 
	rm -rf ./src/__pycache__
	rm -rf ./src/tests/__pycache__
	rm .coverage

test: venv/bin/activate
	pip install -U pytest
	pip install -U pytest-asyncio
	pip install -U coverage
	coverage run -m pytest ./src/tests/.
	coverage report -m
