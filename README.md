# Summary_web_pages_GenAi

This is a kind of Web browser: Give it some URLs, and it will respond with a summary. The Reader's Digest of the internet!

## Description

This project uses generative AI to create summaries of web pages. It extracts content from provided URLs, processes it, and generates concise summaries using an advanced language model.

## Features

- Web content extraction from URLs
- Cleaning and preparation of extracted text
- Summary generation using the OpenAI API
- Support for multiple input URLs

## Installation

1. Clone this repository:
   ```
   git clone git@github.com:davidanthony-ai/Summary_web_pages_GenAi.git
   ```

2. Create the conda environment using the provided `environment.yml` file:
   ```
   conda env create -f environment.yml
   ```

3. Activate the conda environment:
   ```
   conda activate llms
   ```

4. Set up your environment variables by creating a `.env` file in the project root with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage
1. You can change the URLs in the `summary.py` file. for your specific use case.
2. Run the main script by providing one or more URLs:
   ```
   python summary.py
   ```

3. The program will extract the web page content, generate summaries, and display them in the console.

## Main Dependencies

- python-dotenv
- requests
- beautifulsoup4
- openai
- ipython

For a complete list of dependencies, refer to the `environment.yml` file.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
