def show_messages(unsent_messages):
    """Prints out messages sent to the function."""
    for message in unsent_messages:
        print(f"{message}")

def send_messages(unsent_messages, sent_messages):
    while unsent_messages:
        current_message = unsent_messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

unsent_messages = ['Hi!', 'Hey!', 'Hello!']
sent_messages = []
show_messages(unsent_messages)
send_messages(unsent_messages[:], sent_messages)
print(unsent_messages)
print(sent_messages)