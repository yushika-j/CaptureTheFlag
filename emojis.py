import requests
from bs4 import BeautifulSoup

def find_pattern(data):
    # Split the data into parts
    parts = data.split("=")
    symbols = parts[0].strip()  # Get the symbols
    number = int(parts[1].strip())  # Get the corresponding number

    # Calculate the value of each symbol
    total = len(symbols)
    print("Total Symbols:", total)
    print("Number:", number)
    value = number / len(symbols)
    return int(value)

# URL of the website
url = "https://emojis.chals.hackin.ca/1"

while True:
    # Send GET request
    response = requests.get(url)

    # Parse the response
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the input box and submit button
    input_box = soup.find("input", {"id": "answer"})
    submit_button = soup.find("input", {"type": "submit"})

    # Check if input box and submit button exist
    if input_box and submit_button:
        # Find the div tag
        div_tag = soup.find("div")

        # Check if <div> tag exists
        if div_tag:
            # Find the <p> tag inside the <div>
            p_tag = div_tag.find("p")

            # Check if <p> tag exists inside <div>
            if p_tag:
                # Extract the data
                data = p_tag.text.strip()

                # Find the pattern
                pattern = find_pattern(data)

                # Input the pattern value into the input box
                input_box["value"] = str(pattern)

                # Submit the form

                response = requests.post(url, data={"answer": pattern})

                # Print the pattern
                print("Pattern:", pattern)
            else:
                print("Error: <p> tag not found inside <div>.")
        else:
            print("Error: <div> tag not found.")

        # Update the URL for the next iteration if needed
        # Example: url = response.url
    else:
        print("No input box or submit button found. Exiting loop.")
        break
