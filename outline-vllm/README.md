For React Agent --> https://dottxt-ai.github.io/outlines/latest/cookbook/react_agent/

vLLM Installation --> https://docs.vllm.ai/en/v0.6.0/getting_started/installation.html#installation

serving with vLLM,
```
docker run -p 8000:8000 outlinesdev/outlines --model="microsoft/Phi-3-mini-4k-instruct"
```

Then inference can be performed using,
```
curl http://127.0.0.1:8000/generate \
    -d '{
        "prompt": "What is the capital of France?",
        "schema": {"type": "string", "maxLength": 5}
        }'
```

or via python requests using,
```
import requests

url = "http://127.0.0.1:8000/generate"

# Define the data to be sent as a JSON payload
data = {
    "prompt": "What is the capital of France?",
    "schema": {"type": "string", "maxLength": 5}
}

# Send the POST request
response = requests.post(url, json=data)

# Print the response
print(response.text)
```
