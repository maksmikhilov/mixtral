import mii
client = mii.server(
    "TheBloke/Mixtral-8x7B-Instruct-v0.1-GPTQ",
    deployment_name="generate",
    enable_restful_api=True,
    restful_api_port=8000,
)