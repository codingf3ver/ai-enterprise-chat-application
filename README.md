# ai-enterprise-chat-application

## Implementation steps

• Phase 1 — Infrastructure: Environment PostgreSQL, AWS, and Pinecone.
• Phase 2 — Al Engineering : RAG, memory, guardrails, observability, HITL, and LangGraph.
• Phase 3 - Full-Stack Application: API, HTML, CSS, and JavaScript.
• Phase 4 — Integration and Testing: S3 CORS, tests, documentation, and end-to-end demonstration.


### phase 1 Instrtcution 

1. conda create -n chat-env python=3.12 -y

2. conda activate chat-env

3. pip install -r requirements.txt

4. create_structure.py

5. create an IAM user --> provide admin access

6. select model from aws bedrock
7. create s3 bucket and add [
                {
                    "AllowedHeaders": ["*"],
                    "AllowedMethods": ["PUT"],
                    "AllowedOrigins": [
                    "http://127.0.0.1:8000",
                    "http://localhost:8000"
                    ],
                    "ExposeHeaders": ["ETag"],
                    "MaxAgeSeconds": 3000
                }
                ] 
    into the permission section

8. set pinecone api key and its comnfiguration
9. Go to render cloud to setup postgresql
    Install extension SQLTOOLs and other for accessing the DB

10. create glassflow rius api key

### • Phase 2 — Al Engineering : RAG, memory, guardrails, observability, HITL, and LangGraph.




