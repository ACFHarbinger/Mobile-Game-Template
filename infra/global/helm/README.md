# helm/

> **Optional.** Only relevant for the optional leaderboards/cloud-save backend.
> Packages (mostly) the same resources as `infra/global/k8s/base/`, for teams that
> prefer `helm install` over `kubectl apply -k`. Pick one, don't run both
> against the same cluster/namespace.

```bash
helm lint infra/global/helm/mobile-game-template
helm install mobile-game-template infra/global/helm/mobile-game-template -f infra/global/helm/mobile-game-template/values.yaml
```
