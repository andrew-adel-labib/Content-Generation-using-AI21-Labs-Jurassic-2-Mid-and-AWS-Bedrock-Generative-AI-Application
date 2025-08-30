import json 
import boto3

prompt = """
Act like Shakespeare and compose a poem about Generative AI.
"""

bedrock = boto3.client(service_name="bedrock-runtime")

payload = {
    "prompt": prompt,
    "maxTokens": 512,
    "temperature": 0.8,
    "topP": 0.8
}

body = json.dumps(payload)
model_id = "ai21.j2-mid-v1"

response = bedrock.invoke_model(
    modelId=model_id,
    contentType="application/json",
    accept="application/json",
    body=body
)

response_body = json.loads(response.get("body").read())
response_text = response_body.get("completions")[0].get("data").get("text")
print(response_text)