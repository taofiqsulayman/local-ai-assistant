
# Local AI Assistant

## Unlock the Power of Conversational AI

Imagine having a personal AI assistant at your fingertips, ready to answer your questions, provide information, and even entertain you. Welcome to Local AI Assistant, a Streamlit app that harnesses the power of Ollama (for serving LLMs locally) and LangChain to bring conversational AI to your local machine.

## Table of Contents
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Installation and Setup

### Step 1: Install Ollama

To use this project, you need to install Ollama on your system. Follow these steps:

1.  Install the Ollama CLI by running the following command in your terminal:

    ```bash
    pip install ollama
    ```

2. Verify the installation by running:

    ```bash
    ollama --version
    ```

### Step 2: Pull Models

Pull the required models for the project by running:

```bash
ollama pull ${modelName}
```

### Step 3: Clone the Repository

Clone this repository using Git:

```bash
git clone git@github.com:taofiqsulayman/local-ai-assistant.git
```

### Step 4: Create and Activate a Virtual Environment

Create a new virtual environment for the project:

```bash
python -m venv venv
```

Activate the virtual environment:

- On Windows:

    ```bash
    venv\Scripts\activate
    ```

- On macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

### Step 5: Install Requirements

Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### Step 6: Run the App

Run the Streamlit app by executing:

```bash
streamlit run app.py
```

## Usage

1. Select a model from the dropdown list.
2. Type your message in the chat input field.
3. Press Enter to send the message and receive a response from the AI assistant.

## Troubleshooting

- If you encounter any issues with Ollama, refer to the [Ollama documentation](https://ollama.com).
- For Streamlit-related issues, check the [Streamlit documentation](https://docs.streamlit.io/).

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make changes, and submit a pull request.
