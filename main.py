from fastapi import FastAPI
import os
import subprocess
from pydantic import BaseModel
from typing import List, Dict, Any
from utils import LLM
# import dotenv
# dotenv.load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

for var_name, value in {
    "API_KEY": API_KEY
}.items():
    if not value:
        raise EnvironmentError(f"Missing environment variable: {var_name}")



app = FastAPI(
    title="📘 Nutrition Guide API",
    description="""
> Use the `/docs` endpoint for interactive Swagger UI or `/redoc` for alternative documentation.
"""
)

llm = LLM()

class Health(BaseModel):
    health_status: str

class Products(BaseModel):
    products: List[Dict[str, Any]]

class QueryRequest(BaseModel):
    query: str


@app.post("/health")
def set_health_status(request: Health):
    try:
        llm.health_status = request.health_status
        return {"status": "success", "message": "Heath status set"}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}
    
@app.post("/products")
def set_product_nutririon(request: Products):
    try:
        llm.food_products = request.products
        return {"status": "success", "message": "Products set"}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}
    

@app.post("/query")
def query_rag(request: QueryRequest):
    """Run a RAG query using Vector or Hybrid mode."""
    query = request.query
    response = llm.query(query)
    return {
        "query": query,
        "response": response
    }

