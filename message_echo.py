def main():
    print("Welcome to the Echo Console (type 'exit' to quit):")
    while True:
        message = input("You: ")
        if message.lower() == 'exit':
            print("Session ended.")
            break
        print(f"Echo: {message}")

if __name__ == "__main__":
    main()