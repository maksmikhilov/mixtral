import mii
client = mii.serve(
    "mistralai/Mistral-7B-Instruct-v0.2",
    deployment_name="generate",
    enable_restful_api=True,
    tensor_parallel=2,
)