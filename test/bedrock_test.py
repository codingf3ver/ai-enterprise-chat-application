
import os
import json
import boto3
from dotenv import load_dotenv

load_dotenv()

import boto3

client = boto3.client(
    "bedrock-runtime",
    region_name=os.environ.get("AWS_REGION"),
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
)

try:
    embedding_response = client.invoke_model(
        modelId=os.environ.get("BEDROCK_EMBED_MODEL"),
        body=json.dumps({
            "inputText": "Hello Amazon Bedrock",
            "dimensions": 1024,
            "normalize": True
        }),
        contentType="application/json",
        accept="application/json"
    )

    embedding_data = json.loads(
        embedding_response["body"].read()
    )

    print("Embedding dimension:", len(embedding_data["embedding"]))
except Exception as err:
    print('error occurred while invoking embed model ',err)


try:
    chat_response = client.converse(
        modelId=os.environ.get("BEDROCK_CHAT_MODEL"),
        messages=[
            {
                "role": "user",
                "content": [
                    {"text": "Explain RAG in one sentence."}
                ]
            }
        ],
        inferenceConfig={"maxTokens": 200}
    )

    print(
        "Nova Response:",
        chat_response["output"]["message"]["content"][0]["text"]
    )
except Exception as err:
    print('error occurred while invoking chat model ',err)


