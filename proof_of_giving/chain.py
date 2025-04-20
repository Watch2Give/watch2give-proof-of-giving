def send_proof_to_chain(wallet, file_hash):
    # Simulate on-chain submission (can be replaced later with real Polkadot call)
    print(f"✅ Simulated on-chain submit: {file_hash} from {wallet}")
    return {
        "status": "submitted",
        "wallet": wallet,
        "hash": file_hash
    }
