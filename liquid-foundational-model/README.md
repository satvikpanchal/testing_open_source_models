## LFM2 Model Setup

### Start the server

Start the `llama-server` with LFM2:

```bash
llama-server -hf LiquidAI/LFM2-1.2B-GGUF:Q4_K_M \
 -t 16 -c 8192 --temp 0.2
```

This will expose an endpoint at `http://localhost:8080`.

### Python client

Use the `lfm2_client.py` script to interact with the LFM2 model:

```bash
python lfm2_client.py
```

The client connects to the local llama-server and can handle chat completions with the LFM2 model.
