# Kubernetes Deployment

This directory contains Kubernetes manifests for deploying the Log Generator application to a Kubernetes cluster.

## Prerequisites

- Kubernetes cluster
- kubectl configured to access the cluster
- Docker image built and available in the cluster's registry

## Files

- `deployment.yaml`: Deployment configuration for the log generator
- `configmap.yaml`: Configuration for log messages and levels

## Deployment Steps

1. Build and push the Docker image:
```bash
docker build -t your-registry/log-generator:latest .
docker push your-registry/log-generator:latest
```

2. Update the image in deployment.yaml if using a different registry:
```bash
sed -i 's|log-generator:latest|your-registry/log-generator:latest|g' deployment.yaml
```

3. Apply the manifests:
```bash
kubectl apply -f configmap.yaml
kubectl apply -f deployment.yaml
```

4. Verify the deployment:
```bash
kubectl get pods -l app=log-generator
kubectl logs -f deployment/log-generator
```

## Configuration

The deployment can be configured using environment variables in the `deployment.yaml` file:

- `LOG_INTERVAL_MIN`: Minimum interval between logs (default: 0.5)
- `LOG_INTERVAL_MAX`: Maximum interval between logs (default: 3.5)
- `LOG_FORMAT_JSON`: Use JSON format (default: false)
- `LOG_LEVEL`: Minimum log level (default: INFO)

## Updating Log Configuration

To update the log messages:

1. Edit the `configmap.yaml` file
2. Apply the changes:
```bash
kubectl apply -f configmap.yaml
```
3. Restart the pods to apply the changes:
```bash
kubectl rollout restart deployment log-generator
```

## Scaling

To scale the deployment:
```bash
kubectl scale deployment log-generator --replicas=3
```

## Cleanup

To remove the deployment:
```bash
kubectl delete -f deployment.yaml
kubectl delete -f configmap.yaml
``` 