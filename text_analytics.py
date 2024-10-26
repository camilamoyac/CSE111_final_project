# remember to save the sources I used to learn for my program
# remember I tried with putting the word amount pairs in a dictionary first but
# it was easier to print them when they were in a compound list so i changed it
# into a list

# 6 hours so far
# I need to find a way to add a python module maybe math and do some stats with
# the words?

def main():
    print("Text Analytics")
    print("------------------------------------------------------------------------")
    print("Welcome to Text Analytics, make sure the txt file you want to analyze is in the same")
    print("directory as this program.")

    another = True
    while another:
        try:
            file_name = input("\nEnter file name (excluding the .txt): ")
            file_name = file_name + ".txt"
            text_string = read_file(file_name)
        except FileNotFoundError:
            print("Couldn't open txt file because it doesn't exist. Try again with the correct filename.")
            print("Make sure your txt file is in the same directory as this program.\n")
        except PermissionError:
            print("Permission denied for accessing file or directory. Try again with adequate permission.")
                
        clean_string = format_string(text_string)
        word_list = string_to_list(clean_string)
        content_word_list = remove_stopwords(word_list)
        word_amount_list = list_to_word_amount_list(content_word_list)
        sorted_list = sort_word_amount_list(word_amount_list)

        print("\nHere are the top ten words repeated in your text:")
        print("WORD          AMOUNT")
        i = 0
        while i < 10:
            word = sorted_list[i][0]
            amount = sorted_list[i][1]

            txt = "{:<10}{:>10}"
            print(txt.format(word, amount))
            i += 1

        print("\n------------------------------------------------------------------------")
        print("Thank you for using Text Analytics")
        yes_no = input("Would you like to try another text? ")
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
    clean_string = clean_string.replace('"', "")
    clean_string = clean_string.replace("'", "")
    clean_string = clean_string.replace("’", "")
    clean_string = clean_string.replace("‘", "")
    clean_string = clean_string.replace(",", "")
    clean_string = clean_string.replace(";", "")
    clean_string = clean_string.replace(".", "")
    clean_string = clean_string.replace("¡", "")
    clean_string = clean_string.replace("!", "")
    clean_string = clean_string.replace("¿", "")
    clean_string = clean_string.replace("?", "")
    clean_string = clean_string.replace("(", "")
    clean_string = clean_string.replace(")", "")
    clean_string = clean_string.replace("{", "")
    clean_string = clean_string.replace("}", "")
    clean_string = clean_string.replace("[", "")
    clean_string = clean_string.replace("]", "")
    clean_string = clean_string.replace("-", " ")
    clean_string = clean_string.replace("_", " ")
    clean_string = clean_string.replace("—", " ")
    clean_string = clean_string.replace("â€", " ")
    clean_string = clean_string.replace("”", "")
    clean_string = clean_string.replace("“", "")
    clean_string = clean_string.replace("#", "")
    clean_string = clean_string.replace("$", "")
    clean_string = clean_string.replace("%", "")
    clean_string = clean_string.replace("&", "")
    clean_string = clean_string.replace("/", " ")
    clean_string = clean_string.replace("+", " ")
    clean_string = clean_string.replace("=", " ")
    clean_string = clean_string.replace("*", "")
    clean_string = clean_string.replace(":", "")
    clean_string = clean_string.replace("@", "")
    clean_string = clean_string.replace("\\", " ")
    clean_string = clean_string.replace("^", "")
    clean_string = clean_string.replace("//", "")
    clean_string = clean_string.replace("|", "")
    clean_string = clean_string.replace("°", "")
    clean_string = clean_string.replace("~", "")
    clean_string = clean_string.replace("π", "")
    clean_string = clean_string.replace("≈", "")
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
                 "your", "has", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                 "10", "0", "it", "its", "my"]
    word_list = [word for word in word_list if word not in stopwords]
    return word_list

def sort_word_amount_list(word_list):
    # sorts list in descending order according to the amount of times each word
    # is repeated
    sorted_list = sorted(word_list, key=lambda x: x[1], reverse=True)
    return sorted_list

if __name__ == "__main__":
    main()