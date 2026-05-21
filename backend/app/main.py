from fastapi import FastAPI
app= FastAPI(title="SemanticOps AI")

@app.get("/")
def root():
   return {"message:" "SemanticOps AI Backend is running"}