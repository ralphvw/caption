from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
from langchain import PromptTemplate, LLMChain, OpenAI

load_dotenv(find_dotenv())

# Image to text
def image_to_text(url):
    image_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    text = image_text(url)[0]["generated_text"]

    print(text)
    return text

text = image_to_text("stock-photo-142984111.jpeg")

# GPT Prompt
def generate_caption(scenario):
    template = """
    generate a cool instagram caption with Drake lyrics with this description
    ```{scenario}```
    """

    prompt = PromptTemplate(template=template, input_variables=["scenario"])

    caption_llm = LLMChain(llm=OpenAI(
        model_name="gpt-3.5-turbo", temperature=1
    ), prompt=prompt, verbose=False)

    caption = caption_llm.predict(scenario=scenario)

    print(caption)

    return caption

generate_caption(text)