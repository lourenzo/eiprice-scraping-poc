all:
		@echo "Options: \n   * build"
clean:
		docker-compose down --rmi local
		docker volume prune -f

build: clean
		pip freeze > src/app/requirements.txt
		docker-compose build
		docker-compose up -d
