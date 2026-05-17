from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from PIL import Image
import torch

model_name = "nlpconnect/vit-gpt2-image-captioning"

caption_model = VisionEncoderDecoderModel.from_pretrained(model_name)
feature_extractor = ViTImageProcessor.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
caption_model.to(device)

sum_model_name = "sshleifer/distilbart-cnn-12-6"
sum_tokenizer = AutoTokenizer.from_pretrained(sum_model_name)
sum_model = AutoModelForSeq2SeqLM.from_pretrained(sum_model_name)
sum_model.to(device)

def analyze_image(image_path):
    image = Image.open(image_path).convert("RGB")
    pixel_values = feature_extractor(images=[image], return_tensors="pt").pixel_values.to(device)

    output_ids = caption_model.generate(pixel_values, max_length=16, num_beams=4)
    caption = tokenizer.batch_decode(output_ids, skip_special_tokens=True)[0].strip()

    inputs = sum_tokenizer(caption, return_tensors="pt", 
                           max_length=512, truncation=True)
    output = sum_model.generate(inputs["input_ids"], 
                                max_length=50, min_length=10)
    summary = sum_tokenizer.decode(output[0], skip_special_tokens=True)

    return {
        "caption": caption,
        "summary": summary
    }

if __name__ == "__main__":
    result = analyze_image("test.jpg")
    print("Caption:", result["caption"])
    print("Summary:", result["summary"])