import replicate

# Set your API token
replicate.api_token = "r8_IP95V68uLZOhgTAtlAIs6GS4M9s8Ile4g79xZ"

def generate_response(input_params):
    try:
        for event in replicate.stream(
            "meta/meta-llama-3-70b-instruct",
            input=input_params
        ):
            print(event, end="")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_params = {
        "top_p": 0.9,
        "prompt": "Write a joke about birds.",
        "min_tokens": 0,
        "temperature": 0.6,
        "prompt_template": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nYou are a helpful assistant<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
        "presence_penalty": 1.15
    }
    generate_response(input_params)