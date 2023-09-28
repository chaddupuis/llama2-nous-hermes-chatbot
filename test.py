from ctransformers import AutoModelForCausalLM

# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
llm = AutoModelForCausalLM.from_pretrained("resources/Nous-Hermes-Llama2-GGUF", model_file="nous-hermes-llama2-13b.Q4_K_M.gguf", model_type="llama", local_files_only=True, gpu_layers=25)

print(llm("What is Traditional Chinese Medicine?"))
