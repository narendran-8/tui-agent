import os
import re
import dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# Load environment variables from .env file
dotenv.load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    print("API key not found in .env file. Please set OPENROUTER_API_KEY.")
    exit()

def get_os_choice():
    print("Choose your Operating System:")
    print("1. Windows")
    print("2. Linux")
    print("3. macOS")
    choice = input("Enter option number: ").strip()
    os_map = {"1": "Windows", "2": "Linux", "3": "macOS"}
    return os_map.get(choice, "Linux")

def main():
    os_type = get_os_choice()

    # Initialize LLM using OpenRouter and DeepSeek/Qwen
    try:
        llm = ChatOpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
            model="deepseek/deepseek-r1-0528:freey"  # or use "qwen:8b" if preferred
        )
    except Exception as e:
        print("❌ Error initializing OpenRouter LLM:", e)
        return

    # Prompt to generate system command
    prompt = PromptTemplate(
        input_variables=["os_type", "instruction"],
        template="""
You are an expert system assistant.

Convert the user's instruction into a SINGLE system command for the specified OS.

OS: {os_type}
Instruction: {instruction}

Respond with only the command — no explanation, no backticks, no quotes.
"""
    )

    chain = prompt | llm

    while True:
        instruction = input("\nEnter instruction (or 'exit' to quit): ").strip()
        if instruction.lower() in ["exit", "quit"]:
            break

        try:
            result = chain.invoke({"os_type": os_type, "instruction": instruction})
            command = re.sub(r"[`\"']", "", result.content.strip())
            print(f"\nSuggested Command:\n{command}")
        except Exception as e:
            print("❌ Failed to generate command:", e)
            continue

        confirm = input("\nExecute this command? (y/n): ").strip().lower()
        if confirm == "y":
            print("⏳ Running...\n")
            os.system(command)
        else:
            print("Skipped execution.")

if __name__ == "__main__":
    main()
