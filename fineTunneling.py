from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer
from datasets import load_dataset

# Load your dataset
data = load_dataset("json", data_files={"train": "converted_training_data3.jsonl"})


# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("./", trust_remote_code=True)


model = AutoModelForCausalLM.from_pretrained("./", trust_remote_code=True)

def preprocess_function(examples):
    full_text = f"{examples['instruction']}\n\nInput: {examples['input']}\n\nOutput: {examples['output']}"
    
    tokens = tokenizer(full_text, padding='max_length', truncation=True,max_length=512)
    
    print(f"Tokenized length: {len(tokens['input_ids'])}")  # Debug the tokenized length
    
    tokens["labels"] = tokens["input_ids"]
    
    return tokens


tokenized_data = data["train"].map(preprocess_function)

# Training arguments
training_args = TrainingArguments(
    output_dir="./fine_tuned_llama",
    evaluation_strategy="no",
    save_strategy="steps",  
    save_steps=500,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=8,
    num_train_epochs=3,
    logging_dir="./logs",
    logging_steps=100,
    save_total_limit=2,
    learning_rate=2e-5,
    weight_decay=0.01,
    fp16=True,  # Mixed precision training
    push_to_hub=False,
)

# Define the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_data,
    tokenizer=tokenizer,
)

# Train the model
trainer.train()

# Save the fine-tuned model
trainer.save_model("./fine_tuned_llama")
tokenizer.save_pretrained("./fine_tuned_llama")
