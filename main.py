import cohere
import os

# https://docs.cohere.com/docs/streaming
co = cohere.Client(os.getenv("COHERE_API_KEY"))
message = "hello"
for event in co.chat_stream(message=message, model="command-r-plus"):
    if event.event_type == "text-generation":
        print(event.text)
    elif event.event_type == "stream-end":
        print("(%s)" % event.finish_reason)
"""
response = co.chat(message=message, model="command-r-plus", temperature=0.3)
answer = response.text
print(answer)
"""
