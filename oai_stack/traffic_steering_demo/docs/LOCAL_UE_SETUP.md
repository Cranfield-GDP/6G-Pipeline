Since we are using the OAI's NR UE image, we will build our UE image from it:

```bash
cd build
docker build -t oai-nr-ue:local -f Dockerfile.oai_nr_ue_ai .
```