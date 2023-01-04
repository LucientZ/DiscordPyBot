run: setup init
	python3 ./src/main.py

setup: requirements.txt
	pip install -r requirements.txt

config:
	python3 ./src/config.py

init:
	python3 ./src/init.py

docker:
	docker-compose up --force-recreate --build && docker image prune -f

clean: 
	rm -rf ./src/__pycache__
