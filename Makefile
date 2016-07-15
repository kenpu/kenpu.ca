TARGET = kenpuca.github.io

dev: pubs
	hugo server -w

deploy: pubs
	hugo
	cp -R ./public/* ../$(TARGET)/
	cd ../$(TARGET)/; git add --all .; git commit -m 'new'; git push


pubs:
	mkdir -p ./public
	python compile-pubs.py > data/publications.json
