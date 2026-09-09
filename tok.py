##TOKENIZER AND LAST RESP RETRIVER CODE##

def last_response_retriever(conversation):
    """
    Retrieves the last response from a conversation.

    Args:
        conversation (list): A list of messages in the conversation.

    Returns:
        str: The last response in the conversation.
    """
    if not conversation:
        return None
    return conversation[-1]['response'] if 'response' in conversation[-1] else None

def token(convo) :
    """
    Tokenizes the conversation into a list of tokens.

    Args:
        convo (list): A list of messages in the conversation.

    Returns:
        list: A list of tokens representing the conversation.
    """
    tokens = []
    for message in convo:
        if 'response' in message:
            tokens.append(message['response'])
        if 'user' in message:
            tokens.append(message['user'])
    return tokens