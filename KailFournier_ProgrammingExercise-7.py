import re

def count(paragraph):
    # Pattern to match sentences starting with an uppercase letter or digits
    pattern = r'(?:[A-Z]|\d+).*?[.!?](?=\s+[A-Z\d]|\s*$|$)'
    matches = re.findall(pattern, paragraph, flags=re.DOTALL) # Find all matches
    return len(matches) # Return the count of sentences

def main():
    retry = 'yes'
    while retry == 'yes': #loops program until user declines
        paragraph = input("Enter a paragraph: ").strip() # Get paragraph input from the user
        sentence_count = count(paragraph) # Count sentences and display the result
        print(f"\nThe paragraph contains {sentence_count} sentence(s).")
        # Asks user if they want to process more data
        retry = input('Do you want to process another input? (yes/no) ')
main()