# see https://www.youtube.com/watch?v=QEaBAZQCtwE

from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")

res = generator(
    "The latest book written by Stephen King has the title",
    max_length=30,
    num_return_sequences=2,
)

print(res)
