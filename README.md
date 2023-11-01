# Flask App for Image Caption Generation

This Flask application integrates with the LangChain and OpenAI APIs to generate captions for images. It provides a simple and intuitive interface to upload images and receive automated descriptive captions using AI-powered technologies.

## Setup and Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/your-username/flask-image-captioning.git
    ```

2. **Install Dependencies**

    Navigate to the project directory and install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up API Keys**

    Obtain API keys for LangChain and OpenAI. Update the configuration with your API keys in `config.py`:

    ```python
    HUGGINGFACEHUB_API_TOKEN= 'your huggingface token'
    OPENAI_API_KEY= 'your openai api key'
    ```

4. **Run the Application**

    Start the Flask application:

    ```bash
    python app.py
    ```

    Access the application in your web browser at `http://localhost:5000`.

## Usage

1. **Upload Images**

    Use the provided interface to upload images for caption generation.
   You can check out my own frontend @ https://github.com/ralphvw/caption-frontend
   Hosted @ caption-frontend-pied.vercel.app

3. **Generate Captions**

    Click the "Generate Caption" button to utilize LangChain and OpenAI for automated caption generation.


## Credits

- [LangChain API](https://langchain.org) - Powered by LangChain for language processing.
- [OpenAI API](https://openai.com) - OpenAI for advanced AI capabilities.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify it according to your needs.

_For detailed documentation and examples, refer to the project's wiki or documentation section._

Please make sure to update the necessary API keys and configurations before running the application. Adjust the paths and configurations as needed based on your project's structure and requirements.
