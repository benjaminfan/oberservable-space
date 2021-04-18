app_name=service
build:
	@docker build -t $(app_name) .
run:
	docker run --detach -p 8003:8003 --name observable-space $(app_name)
kill:
	@echo 'Killing container...'
	@docker ps | grep $(app_name) | awk '{print $$1}' | xargs docker stop