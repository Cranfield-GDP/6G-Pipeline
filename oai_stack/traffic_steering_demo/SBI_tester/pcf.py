import httpx
import os
import json

PCF_IP_ADDRESS = os.getenv("PCF_IP_ADDR", "localhost")
PCF_SBI_PORT = os.getenv("PCF_SBI_PORT", 13980)

sm_policies_url = f"http://{PCF_IP_ADDRESS}:{PCF_SBI_PORT}/npcf-smpolicycontrol/v1/sm-policies"

print(sm_policies_url)
# Sending an HTTP/2 GET request
with httpx.Client(http2=True, http1=False) as client:
    response = client.get(sm_policies_url)
    print("Status Code:", response.status_code)
    print("Headers:", response.headers)
    # print("Response Data:", response.text)

    print(json.dumps(json.loads(response.text), indent=4))


# # Sending an HTTP/2 POST request
# data = {"message": "Hello, HTTP/2!"}
# response = client.post(sm_policies_url + "/api", json=data)
# print("POST Status Code:", response.status_code)
# print("POST Response:", response.text)