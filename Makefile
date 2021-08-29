NAME = no-deploy-on-friday-action

all: build run # Build and run container

build: # Build the container
	docker build . -t $(NAME)

dev: build # Get python interepter in the container
	docker run -v "$$(pwd)":/app --entrypoint python --rm -it $(NAME)

run: build # Run the container
	docker run --rm -it --env TZ='MST' $(NAME)

tests: build # Run the unittests
	docker run --rm -it $(NAME) /app/tests.py -vv

lint: # Run the unittests
	black --line-length 100 ./app