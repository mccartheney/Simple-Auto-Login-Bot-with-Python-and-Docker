build :
	docker build -t auto-login -f Dockerfile .


run :
	docker run -it -v ${PWD}/src:/app auto-login sh

build-run : build run