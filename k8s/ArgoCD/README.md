Install ArgoCD:
```bash
kubctl apply -f install-ArgoCD.yaml -n ci-cd
```
Add Ingress:
```bash
kubectl apply -f ingress-argocd.yaml -n ci-cd
```
Or, use port-foward:
```bash
kubectl port-forward svc/argocd-server -n ci-cd 8080:443
```

Get ArgoCD Admin password: 

```bash
kubectl get secret argocd-initial-admin-secret -n ci-cd -o jsonpath="{.data.password}" | base64 -d
```
Install ArgoCD CLI: 

```bash
curl -sSL -o argocd-linux-amd64 https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64

sudo install -m 555 argocd-linux-amd64 /usr/local/bin/argocd

rm argocd-linux-amd64
```


Login in ArgoCD CLI:

```bash
argocd login localhost:8080 or address
```