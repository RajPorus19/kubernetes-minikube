# backend api
minikube kubectl -- apply -f kubernetes/schoodle-api/deployment.yml
minikube kubectl -- apply -f kubernetes/schoodle-api/service.yml
minikube kubectl -- apply -f kubernetes/schoodle-api/ingress.yml

# health-check
minikube kubectl -- apply -f kubernetes/health-check/deployment.yml
minikube kubectl -- apply -f kubernetes/health-check/service.yml