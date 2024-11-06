# this program reads a txt file that contains a text in english (mainly song lyrics and poems but it works with any text)
# and prints some stats like word amount, repeated and unique words, word diversity ratio, and top ten repeated words.

import string

def main():
    print("Text Analytics")
    print("------------------------------------------------------------------------")
    print("Welcome to Text Analytics, make sure the txt file you want to analyze is in the same")
    print("directory as this program.")

    another = True
    while another:
        try:
            file_name = input("\nEnter file name (excluding the .txt): ")
            print("\n------------------------------------------------------------------------")
            print(f"Stats for {file_name}")
            file_name = file_name + ".txt"
            text_string = read_file(file_name)
        except FileNotFoundError:
            print("Couldn't open txt file because it doesn't exist. Try again with the correct filename.")
            print("Make sure your txt file is in the same directory as this program.\n")
        except PermissionError:
            print("Permission denied for accessing file or directory. Try again with adequate permission.")
   
        clean_string = format_string(text_string)
        word_list = string_to_list(clean_string)
        total_words = len(word_list)
        content_word_list = remove_stopwords(word_list)
        word_amount_list = list_to_word_amount_list(content_word_list)
        unique_words = unique_word_counter(word_amount_list)
        sorted_list = sort_word_amount_list(word_amount_list)

        repeated_words = total_words - unique_words
        word_diversity = unique_words/total_words

        print(f"\nThe total amount of words is: {total_words}")
        print(f"The amount of unique words is: {unique_words}")
        print(f"The amount of repeated words is: {repeated_words}")
        print(f"The word diversity ratio is: {word_diversity:.2f}")
        print("\nThe top ten repeated words are:")
        print("WORD                AMOUNT                PERCENTAGE")
        i = 0
        while i < 10:
            word = sorted_list[i][0]
            amount = sorted_list[i][1]
            percentage = amount / total_words * 100

            txt = "{:<12}{:>12}{:>24.1f}%"
            print(txt.format(word, amount, percentage))
            i += 1

        print("\n------------------------------------------------------------------------")
        print("Thank you for using Text Analytics")
        yes_no = input("Would you like to try another text? (yes/no) ")
        if yes_no.lower() == "yes":
            another = True
        else:
            another = False

def read_file(filename):
    # reads file into a string
    try:
        with open(filename, "r", encoding="utf8") as file:
            text_string = file.read()
    except FileNotFoundError:
        print("Couldn't open txt file because it doesn't exist. Try again with the correct filename.")
        print("Make sure your txt file is in the same directory as this program.\n")
    except PermissionError:
        print("Permission denied for accessing file or directory. Try again with adequate permission.")
            
    return text_string

def format_string(text_string):
    # cleans string by removing spaces, newlines, and various special characters
    clean_string = text_string.lower()

    clean_string = clean_string.replace("\n", " ")
    clean_string = clean_string.replace("’", "")     #these are extra weird characters that string.punctuation doesn't handle correctly
    clean_string = clean_string.replace("‘", "")
    clean_string = clean_string.replace("¡", "")
    clean_string = clean_string.replace("¿", "")
    clean_string = clean_string.replace("-", " ")
    clean_string = clean_string.replace("_", " ")
    clean_string = clean_string.replace("—", " ")
    clean_string = clean_string.replace("â€", " ")
    clean_string = clean_string.replace("”", "")
    clean_string = clean_string.replace("“", "")
    clean_string = clean_string.replace("´´", "")
    clean_string = clean_string.replace("\\", " ")
    clean_string = clean_string.replace("°", "")

    clean_string = clean_string.translate(str.maketrans('', '', string.punctuation))

    clean_string = clean_string.replace("0", "")
    clean_string = clean_string.replace("1", "")
    clean_string = clean_string.replace("2", "")
    clean_string = clean_string.replace("3", "")
    clean_string = clean_string.replace("4", "")
    clean_string = clean_string.replace("5", "")
    clean_string = clean_string.replace("6", "")
    clean_string = clean_string.replace("7", "")
    clean_string = clean_string.replace("8", "")
    clean_string = clean_string.replace("9", "")
    clean_string = clean_string.replace("     ", " ")
    clean_string = clean_string.replace("    ", " ")
    clean_string = clean_string.replace("   ", " ")
    clean_string = clean_string.replace("  ", " ")

    clean_string = clean_string.strip()
    return clean_string

def string_to_list(clean_string):
    # saves each word of the string into a list by splitting at the spaces and
    # sorts list into alphabetical order to put all the same words together
    word_list = clean_string.split(" ")
    word_list.sort()
    return word_list

def list_to_word_amount_list(word_list):
    # counts amount of repeated words and saves into a compound list with the word
    # as the 0 index and amount of repetitions as the 1 index in the mini_list
    word_amount_list = []
    
    while len(word_list) != 0:
        word = word_list[0]
        amount = word_list.count(word)
        mini_list = []
        mini_list.append(word)
        mini_list.append(amount)
        word_amount_list.append(mini_list)

        i = 0
        while i < amount:
            word_list.pop(0)
            i += 1
    return word_amount_list

def remove_stopwords(word_list):
    # removes common words with little meaning from the list and leaves only
    # the words that represent the content better
    stopwords = ["a", "an", "the", "and", "but", "or", "so", "yet", "for",
                 "this", "that", "there", "here", "of", "in", "to", "with",
                 "on", "at", "by", "from", "about", "be", "am", "is", "are",
                 "was", "were", "been", "being", "have", "had", "than", "im",
                 "your", "has", "it", "its", "my"]
    word_list = [word for word in word_list if word not in stopwords]
    return word_list

def sort_word_amount_list(word_list):
    # sorts list in descending order according to the amount of times each word
    # is repeated
    sorted_list = sorted(word_list, key=lambda x: x[1], reverse=True)
    return sorted_list

def unique_word_counter(word_amount_list):
    #returns amount of words that only appear once in the text.
    count = 0
    for element in word_amount_list:
        if element[1]:
            count += 1
    return count

if __name__ == "__main__":
    main()