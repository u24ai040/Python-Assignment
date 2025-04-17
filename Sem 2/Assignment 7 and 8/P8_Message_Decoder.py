# QUESTION 8

def decode_message(encoded_message):
    decoded_messages = []
    
    stack = [(0, "")]

    while stack:
        index, path = stack.pop()

        if index == len(encoded_message):
            decoded_messages.append(path)
            continue


        if '1' <= encoded_message[index] <= '9':
            char = chr(ord('A') + int(encoded_message[index]) - 1)
            stack.append((index + 1, path + char))

        if index + 1 < len(encoded_message):
            num = int(encoded_message[index]) * 10 + int(encoded_message[index + 1])
            if 10 <= num <= 26:
                char = chr(ord('A') + num - 1)
                stack.append((index + 2, path + char))

    return decoded_messages

encoded_message = input("Enter the encoded message: ")
result = decode_message(encoded_message)
print("Possible decoded messages:")
for message in result:
    print(message)
