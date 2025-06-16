
# Ask the user for the name of the file: For test cases, use 'test.txt'
fileName = input("Please enter the name of your file: ")


try:
    
    # open the file for reading only
    file = open(fileName,"r")
    
    # read the words and split the text by spaces, and convert it to lower case
    text = file.read().lower()
    words = text.split()
    
    # dict to hold frequencies
    frequency = {}

    # For each word, take out the punctuation and either add it to the dict if it doesn't exist, 
    # or increment its frequency if the word appears again
    for word in words:
        word = word.strip('.,/;:{[]}()!?')
        if word:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
    
    # sort the words in descending frequency to print it easily
    sorted_words = sorted(frequency, key=frequency.get, reverse=True)
    
    # open a new file to write the output too
    fileWrite = open("output.txt",'w')
    
    fileWrite.write("\nWord Frequency Count:\n")
    fileWrite.write("---------------------\n")
    
    # print each word and its frequency to the file, adding a new line character everytime
    # as it does not happen automatically
    for word in sorted_words:
        fileWrite.write(f"{word}: {frequency[word]}\n")

# some exception blocks to catch file reading errors, or other exceptions
except FileNotFoundError:
     print(f"Error: The file '{fileName}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

