from dotenv import load_dotenv
import os
import sys
from langchain_openai import ChatOpenAI

# Global variables
openai_api_key = None
llm = None

def initialize_api_keys():
    """
    Initialize the API keys for the application.
    This function loads the API keys from the .env file and returns the OpenAI API key and the LLM model.    
    """

    global openai_api_key, llm

    # Load the API keys from the .env file
    load_dotenv()

    # Get the OpenAI API key from the .env file
    openai_api_key = os.getenv("OPENAI_API_KEY")

    # Check if the OpenAI API key is set, if not, request it from the user
    if not openai_api_key:
        print("OPENAI_API_KEY not found in environment variables.")
        print("Please enter your OpenAI API key: ", end='')
        openai_api_key = input().strip()

        if not openai_api_key:
            print("No OpenAI API key provided. Exiting...")
            sys.exit(1)

        else:   
            # Save it in environment for this session
            os.environ["OPENAI_API_KEY"] = openai_api_key
    
    # Initialize the LLM model
    try:
        llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)
        print("✅ Successfully initialized OpenAI API")

    except Exception as e:
        print(f"❌ ERROR initializing ChatOpenAI: {e}")
        sys.exit(1)

    # Return the OpenAI API key and the LLM model
    return openai_api_key, llm
