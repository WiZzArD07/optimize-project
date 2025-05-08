# src/defense/adversarial_training.py

from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import Dataset

def prepare_adversarial_dataset(prompts, model_tokenizer):
    data = []
    for entry in prompts:
        prompt = entry['prompt']
        # Teach the model to refuse unsafe requests
        response = "I'm sorry, but I can't help with that request."
        text = f"User: {prompt}\nAssistant: {response}"
        data.append({"text": text})
    return Dataset.from_list(data).map(lambda x: model_tokenizer(x["text"], truncation=True), batched=True)

def run_adversarial_training(model_name="gpt2", prompts=[], output_dir="./models/adversarial"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    dataset = prepare_adversarial_dataset(prompts, tokenizer)
    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    training_args = TrainingArguments(
        output_dir=output_dir,
        per_device_train_batch_size=4,
        num_train_epochs=3,
        save_steps=10,
        logging_steps=5,
        save_total_limit=2,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        tokenizer=tokenizer,
        data_collator=data_collator,
    )

    trainer.train()
    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)
