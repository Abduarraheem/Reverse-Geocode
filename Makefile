default: rebuild

install: rebuild

rebuild: env 

run:
	(source env/bin/activate; gunicorn app:app)

env:    requirements.txt
	python3 -mvenv env
	pip3 install -r requirements.txt

env-test: 
	requirements-test.txt
	python3 -mvenv env
	pip3 install -r requirements-test.txt


clean:
	rm -rf env
