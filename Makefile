.PHONY: deploy

dev: pubs
	hugo server -w

deploy: pubs db github

db:
	hugo --config db.science.uoit.ca.toml -d ../db.science.uoit.ca
	cd ../db.science.uoit.ca; git add --all .; git commit -m 'new'; git push -f origin master

github:
	hugo --config kenpuca.github.io.toml -d ../kenpuca.github.io
	cd ../kenpuca.github.io; git add --all .; git commit -m 'new'; git push -f origin master

pubs:
	mkdir -p ./public
	python compile-pubs.py > data/publications.json
