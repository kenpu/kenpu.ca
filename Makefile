TARGET = kenpuca.github.io

dev: pubs
	hugo server -w

deploy: pubs db kenpu github
	hugo
	cp -R ./public/* ../$(TARGET)/
	cd ../$(TARGET)/; git add --all .; git commit -m 'new'; git push

db:
	hugo --config db.science.uoit.ca.toml -d ../db.science.uoit.ca
	cd ../db.science.uoit.ca; git add --all .; git commit -m 'new'; git push

github:
	hugo --config kenpuca.github.io.toml -d ../kenpuca.github.io
	cd ../kenpuca.github.io; git add --all .; git commit -m 'new'; git push

pubs:
	mkdir -p ./public
	python compile-pubs.py > data/publications.json
