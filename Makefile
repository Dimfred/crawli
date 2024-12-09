.ONESHELL:

build:
	uv build

install:
	pip3 install --break-system-packages dist/*.whl
