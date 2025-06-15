Clone the FlexRIC repo (forked by Yun) and build the image:

```bash
# clone the repo somewhere outside of this project folder.
git clone https://gitlab.eurecom.fr/yuntang/flexric.git

# checkout the docker_fix branch
# this branch fixes some issue in the develop branch.
cd flexric
git checkout docker_fix

# build the image
docker build -t flexric:local -f ./docker/Dockerfile.flexric.ubuntu . 
```

Make sure the RAN is using the local FlexRIC image. Check `docker-compose-ran-ue.yaml` file and confirm that:

```yaml
...
    flexric:
        image: flexric:local
        container_name: flexric
...
```