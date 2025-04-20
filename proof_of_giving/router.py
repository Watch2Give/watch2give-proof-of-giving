from fastapi import APIRouter, UploadFile, File, Form, Depends
from .hasher import hash_file_bytes
from .file_handler import save_uploaded_file
from .chain import proof_to_chain

router = APIRouter()

# Form wrapper to make wallet_address visible in Swagger
def form_inputs(
    wallet_address: str = Form(...)
):
    return {"wallet_address": wallet_address}

@router.post("/upload-proof")
async def upload_proof(
    file: UploadFile = File(...),
    form_data: dict = Depends(form_inputs)
):
    wallet_address = form_data["wallet_address"]
    file_bytes = await file.read()

    # Save file
    filename, filepath, timestamp = save_uploaded_file(file, file_bytes)

    # Hash contents
    file_hash = hash_file_bytes(file_bytes)

    # Simulated on-chain write
    chain_response = send_proof_to_chain(wallet_address, file_hash)

    return {
        "message": "Proof uploaded successfully",
        "filename": filename,
        "hash": file_hash,
        "timestamp": timestamp,
        "chain_response": chain_response
    }
