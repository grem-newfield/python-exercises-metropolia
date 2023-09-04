SHELL := /usr/bin/fish
all: push

push:
	black ./exercises/
	git add --all 
	git commit -m (date)
	git push

