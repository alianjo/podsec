# PodSec
## A simple security warner for Kubernetes Pods
### PodSec helps Kubernetes administrator to detect security vulnerabilities in Pods.

## how it works:
#### this project will check the the below security parameters:
1. Privileged Container
2. hostNetwork
3. hostPID
4. hostIPC

#### if any of above parameter is set true during Pod creation all over the cluster, the operator will notify the user with adding a warning notify in Pod's event object.


## installation

### Install the operator
```shell
kubectl apply -f https://github.com/alianjo/podsec/releases/download/v1/components.yaml
```
