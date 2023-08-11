from dotenv import find_dotenv, load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline
from langchain import PromptTemplate, LLMChain, OpenAI
import os

app = Flask(__name__)
CORS(app)
load_dotenv(find_dotenv())


# Image to text
def image_to_text(url):
    image_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    text = image_text(url)[0]["generated_text"]

    print(text)
    return text

# GPT Prompt
def generate_caption(scenario):
    template = """
    generate a cool instagram caption with JAY Z lyrics with this description
    ```{scenario}```
    """

    prompt = PromptTemplate(template=template, input_variables=["scenario"])

    caption_llm = LLMChain(llm=OpenAI(
        model_name="gpt-3.5-turbo", temperature=1
    ), prompt=prompt, verbose=False)

    caption = caption_llm.predict(scenario=scenario)

    print(caption)

    return caption

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part'})
    
    image = request.files['image']
    if image.filename == '':
        return jsonify({'error': 'No selected image'})
    
    image_path = 'temp_image.jpg'
    image.save(image_path)

    text = image_to_text('temp_image.jpg')
    caption = generate_caption(text)

    os.remove(image_path)

    return jsonify({'caption': caption})

if __name__ == '__main__':
   app.run(debug=True)