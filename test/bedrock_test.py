
import os
import json
import boto3
from dotenv import load_dotenv

load_dotenv()

import boto3

# sts = boto3.client(
#     "sts",
#     region_name="us-east-1"
# )

# print(sts.get_caller_identity())





client = boto3.client(
    "bedrock-runtime",
    region_name=os.environ.get("AWS_REGION"),
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
)

# try:
#     embedding_response = client.invoke_model(
#         modelId=os.environ.get("BEDROCK_EMBED_MODEL"),
#         body=json.dumps({
#             "inputText": "Hello Amazon Bedrock",
#             "dimensions": 1024,
#             "normalize": True
#         }),
#         contentType="application/json",
#         accept="application/json"
#     )

#     embedding_data = json.loads(
#         embedding_response["body"].read()
#     )

#     print("Embedding dimension:", len(embedding_data["embedding"]))
# except Exception as err:
#     print('error occurred while invoking embed model ',err)


# try:
#     chat_response = client.converse(
#         modelId=os.environ.get("BEDROCK_CHAT_MODEL"),
#         messages=[
#             {
#                 "role": "user",
#                 "content": [
#                     {"text": "Explain RAG in one sentence."}
#                 ]
#             }
#         ],
#         inferenceConfig={"maxTokens": 200}
#     )

#     print(
#         "Nova Response:",
#         chat_response["output"]["message"]["content"][0]["text"]
#     )
# except Exception as err:
#     print('error occurred while invoking chat model ',err)



import boto3
import json

client = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"
)

try:
    response = client.invoke_model(
        modelId="amazon.titan-embed-text-v2:0",
        body=json.dumps({
            "inputText": "Hello Amazon Bedrock",
            "dimensions": 1024,
            "normalize": True
        }),
        contentType="application/json",
        accept="application/json"
    )

    result = json.loads(response["body"].read())

    print("SUCCESS!")
    print("Embedding dimension:", len(result["embedding"]))

except Exception as e:
    print("ERROR:", repr(e))


sts = boto3.client("sts")

identity = sts.get_caller_identity()

print("Account:", identity["Account"])
print("ARN:", identity["Arn"])