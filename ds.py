import mii
client = mii.serve(
    "mistralai/Mistral-7B-Instruct-v0.2",
    deployment_name="generate",
    enable_restful_api=True,
    restful_api_port=5555,
    tensor_parallel=4,
)