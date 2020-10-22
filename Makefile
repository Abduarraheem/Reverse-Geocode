default: rebuild

install: rebuild

rebuild: env 

run:
	(source env/bin/activate; gunicorn flask_poll:app)

env:    requirements.txt
	python3 -mvenv env
	pip3 install -r requirements.txt


clean:
	rm -rf env
