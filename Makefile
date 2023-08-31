SHELL := /usr/bin/fish
all: push

push:
	git add --all && git commit -m (date) && git push

