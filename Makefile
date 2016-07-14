dev: pubs
	mkdir -p ./public
	hugo server -w

pubs:
	python compile-pubs.py > data/publications.json
