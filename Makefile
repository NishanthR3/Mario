build:
	@echo "Building game."
	docker build -t mario-bash:latest .

run:
	@echo "Running game."
	docker run -it mario-bash:latest

clean:
	@echo "Clean docker images."
	docker rmi -f mario-bash:latest