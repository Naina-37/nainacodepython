messages = [
    {
        "sender": "99155 71177",
        "receiver": "99999 11111",
        "conversation":[
            "Hello",
            "How are you", 
            "Its Friday",
            "Lets Party. No Code today"
        ]
    },
    {
        "sender": "99155 71177",
        "receiver": "99999 22222",
        "conversation":[
            "Hello",
            "Kaisa hai bhai", 
            "Aj Friday hai",
            "lets party."
        ]
    },
    {
        "sender": "98765 12345",
        "receiver": "99155 71177",
        "conversation":[
            "Beta",
            "Bahut Kaam Hai", 
            "Sabji leni hai",
            "jaldio aa jana. mummy here"
        ]
    }
]

# Get the keyword to search from the user
search_keyword = input("Enter Word to Search: ").lower()

# Search logic
def search_conversations(messages, search_keyword):
    results = []
    for message in messages:
        idx = 0
        for line in message["conversation"]:
            if search_keyword in line.lower():
                results.append((message, idx))
            idx += 1
    return results

# Search for the keyword in the conversations
matched_conversations = search_conversations(messages, search_keyword)

# Display the results
if matched_conversations:
    print("Conversations containing the keyword '{}':".format(search_keyword))
    for message, idx in matched_conversations:
        print("\nSender: {}".format(message["sender"]))
        print("Receiver: {}".format(message["receiver"]))
        print("Conversation:")
        for line in message["conversation"]:
            print(" - {}".format(line))
        print("Keyword found at index: {}".format(idx))
else:
    print("No conversations contain the keyword '{}'.".format(search_keyword))
