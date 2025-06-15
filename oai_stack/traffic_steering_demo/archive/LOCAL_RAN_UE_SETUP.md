Since we are using the gnbsim image, which simulates both RAN (gNodeB) and UE, we will build our RAN/UE image from it:

```bash
cd build
docker build -t gnbsim:local -f Dockerfile.gnbsim_ai .
```