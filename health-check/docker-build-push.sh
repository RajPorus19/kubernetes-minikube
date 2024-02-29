docker build -t health-check .
docker tag health-check esiee79798987/health-check:latest
docker push esiee79798987/health-check:latest