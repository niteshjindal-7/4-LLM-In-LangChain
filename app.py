from llm_factory import get_llm

def main():
    print("Langchain LLM component demo🧠")

    llm = get_llm()

    prompt = "Explain langchain in simple terms suitable for a 12-year old."

    print(f"Sending prompt to {type(llm).__name__}...\n")
    response = llm.invoke(prompt)

    print("Model's Response:\n")
    print(response.content)


if __name__=="__main__":
    main()