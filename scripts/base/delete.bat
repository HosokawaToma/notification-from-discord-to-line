@echo off
setlocal

echo [1;95mStopping and removing all containers, networks, volumes, and images...[0m
docker-compose down -v --rmi local

echo [1;95mPruning unused Docker data...[0m
docker system prune -af

echo Cleanup complete.
endlocal
