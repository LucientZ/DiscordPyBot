run: setup
	python3 ./src/main.py

setup: requirements.txt
	pip install -r requirements.txt

config:
	python3 ./src/config.py

clean: 
	rm -rf __pycache__
