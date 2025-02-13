import httpx
import os
import json

PCF_IP_ADDRESS = os.getenv("PCF_IP_ADDR", "localhost")
PCF_SBI_PORT = os.getenv("PCF_SBI_PORT", 13980)

provisioning_base_url = f"http://{PCF_IP_ADDRESS}:{PCF_SBI_PORT}/npcf-provisioning/v1"

def http2_get_json(url):
    with httpx.Client(http2=True, http1=False) as client:
        response = client.get(url)
        # print(response.text)
        print(response)
        if response is None or response.status_code != 200:
            return None
        if response is not None and response.text is not None and response.text.strip() != "":
            return json.loads(response.text.strip())
        else:
            return None

def http2_put_json(url, data):
    with httpx.Client(http2=True, http1=False) as client:
        response = client.put(url, json=data)
        # print(response.text)
        print(response)
        print(response.status_code)
        if response is None or response.status_code != 200:
            return None
        if response is not None and response.text is not None and response.text.strip() != "":
            return json.loads(response.text.strip())
        else:
            return None

UE_supi = "imsi-208950000000032"
url = f"{provisioning_base_url}/supiPolicyDecision/{UE_supi}"

print("\n---------- GET supiPolicyDecision for UE2 ------------")
print(url)
res = http2_get_json(url)
print(res)

print("\n---------- PUT supiPolicyDecision for UE2 ------------")
data = {
    "supi": UE_supi,
    "pccRuleIds": ["edge-rule", "internet-rule"]
}
print(url)
print(json.dumps(data))
res = http2_put_json(url, data)
print(res)