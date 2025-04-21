# Proof of Giving – Watch2Give

The **Proof of Giving** module is a backend component of the Watch2Give platform that enables vendors to submit verifiable photo-based proof of donations or product giveaways. It securely processes, hashes, and stores these proofs for validation and leaderboard updates.

---

## Project Structure

```
proof-of-giving/
│
├── proof_of_giving/
│   ├── __init__.py
│   ├── chain.py           # Handles interaction with the Polkadot blockchain
│   ├── file_handler.py    # Saves uploaded images to local storage
│   ├── hasher.py          # Computes SHA256 hashes of images
│   ├── proof_main.py      # FastAPI entry point
│   └── router.py          # Manages API routes and logic
│
├── proofs/                # Directory where proof images are saved
├── proof_registry.json    # JSON file storing proof hashes and metadata
└── __pycache__/           # Compiled Python cache files
```

---

## How It Works

1. **Upload Image**: Vendors submit an image proof via API.
2. **Hashing**: The image is hashed using SHA256.
3. **Registry**: The image hash is stored in `proof_registry.json` and saved in the `proofs/` folder.
4. **Chain Link (Optional)**: Hashes can later be pushed to Polkadot via ink! smart contracts for tamper-proof verification.

---

## How to Run

### 1. Install Requirements

```bash
pip install fastapi uvicorn python-multipart
```

### 2. Run the FastAPI Server

```bash
cd proof-of-giving/proof_of_giving
uvicorn proof_main:app --reload
```

### 3. Test with Swagger UI

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## API Endpoints

### `POST /upload`
Upload a photo and receive a hash.

### `GET /proofs`
Returns all registered proofs with metadata.

---

## Future Enhancements

- Push hashes on-chain via smart contracts
- Add vendor authentication and signature verification
- Integrate IPFS or decentralized file storage
- QR code generation from proof hashes

---

## Technologies Used

- **FastAPI** – Web framework
- **Python** – Core logic
- **SHA256** – Hashing engine
- **JSON** – Local proof registry
- **Polkadot / ink!** – Future chain integration

---
