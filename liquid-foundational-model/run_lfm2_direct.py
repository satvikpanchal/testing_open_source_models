#!/usr/bin/env python3
import subprocess
import time
import os

def run_lfm2_direct():
    print("Running LFM2 using local GGUF file...")
    
    # Path to the local GGUF file
    gguf_path = "/Users/satvikpanchal/.cache/huggingface/hub/models--LiquidAI--LFM2-1.2B-GGUF/snapshots/d23656b943d691ca6a7f146e46feac7b0024061d/LFM2-1.2B-Q4_K_M.gguf"
    
    if not os.path.exists(gguf_path):
        print(f"GGUF file not found at: {gguf_path}")
        return
    
    def ask_lfm2(prompt: str) -> str:
        # Use llama-cpp-python or llama.cpp directly
        try:
            # Try using llama-cpp-python if available
            import llama_cpp
            model = llama_cpp.Llama(
                model_path=gguf_path,
                n_ctx=2048,
                n_threads=8
            )
            response = model(prompt, max_tokens=100, temperature=0.7)
            return response['choices'][0]['text']
        except ImportError:
            # Fallback to llama.cpp binary if available
            try:
                cmd = [
                    "llama-cpp",  # or "main" depending on your build
                    "-m", gguf_path,
                    "-n", "100",
                    "-t", "8",
                    "-p", prompt,
                    "--temp", "0.7"
                ]
                
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                if result.returncode == 0:
                    return result.stdout.strip()
                else:
                    return f"Error: {result.stderr}"
            except FileNotFoundError:
                return "Error: llama.cpp not found. Install llama-cpp-python or llama.cpp"
    
    # Test questions
    questions = [
        "Who are you?",
        "What is your architecture?",
        "Are you a transformer model?"
    ]
    
    for question in questions:
        print(f"\n>>> {question}")
        start = time.time()
        answer = ask_lfm2(question)
        inference_time = time.time() - start
        print(f"Response ({inference_time:.2f}s): {answer}")

if __name__ == "__main__":
    run_lfm2_direct()
