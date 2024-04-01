
#Use Python 3.8.5!!
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM, set_seed
import torch

model_id = "roberta-base"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, is_decoder=True
)
model.to_bettertransformer()

set_seed(0)
messages = [
    {
        "role": "system",
        "content": "You are a friendly chatbot who always responds in the style of a thug",
    },
    {"role": "user", "content": "How many helicopters can a human eat in one sitting?"},
]
model_inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt")
input_length = model_inputs.shape[1]
print("Generating result...")
generated_ids = model.generate(model_inputs, do_sample=True, max_new_tokens=20, max_time=60)
print("Done generating")
print(tokenizer.batch_decode(generated_ids[:, input_length:], skip_special_tokens=True)[0])
#'None, you thug. How bout you try to focus on more useful questions?'
# As we can see, it followed a proper thug style 😎


print("Hello World!")