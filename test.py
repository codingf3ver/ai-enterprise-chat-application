from app.config import settings


print(settings().bedrock_embed_model)


from app.aws import embed, answer

# Test embedding
text = "What is flood risk assessment?"

vector = embed(text)

print("Embedding dimension:", len(vector))
print("First five values:", vector[:5])


# Test chat completion
response = answer(
    question="What is flood risk assessment?",
    evidence="""
    [1] Flood risk assessment evaluates the probability
    and potential impact of flooding on an asset.
    """,
    history=[]
)

print("\nAI Answer:")
print(response)
