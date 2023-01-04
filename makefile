run: setup
	python3 ./src/init.py && python3 ./src/main.py

setup: requirements.txt
	pip install -r requirements.txt

config:
	python3 ./src/config.py	

docker:
	docker-compose up --force-recreate --build && docker image prune -f

clean: 
	rm -rf ./src/__pycache__
