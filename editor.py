formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'new-line', 'ordered-list', 'unordered-list']
special_commands = ["!help", "!done"]

modified_text = ''


def printer():
    print(modified_text)


def plain():
    global modified_text
    text = input("Text:")
    modified_text = modified_text + text
    printer()


def bold():
    global modified_text
    text = input("Text:")
    modified_text = modified_text + f"**{text}**"
    printer()


def italic():
    global modified_text
    text = input("Text:")
    modified_text = modified_text + f"*{text}*"
    printer()


def header_():
    global modified_text
    while True:
        level = int(input("Level:"))
        if 1 <= level <= 6:
            text = input("Text:")
            modified_text = modified_text + f"{level * '#'} {text}\n"
            printer()
            break
        else:
            print("The level should be within the range of 1 to 6")
            continue


def link__():
    global modified_text
    label = input("Label:")
    url = input("URL:")
    modified_text = modified_text + f"[{label}]({url})"
    printer()


def inline_code_():
    global modified_text
    text = input("Text:")
    modified_text = modified_text + f"`{text}`"
    printer()


def newline_():
    global modified_text
    modified_text = modified_text + '\n'
    # modified_text = modified_text + '<br>'
    printer()


def ordered_unordered(list_type):
    global modified_text
    list1 = []
    while True:
        number_of_rows = int(input("Number of rows:"))
        if number_of_rows > 1:
            break
        else:
            print("The number of rows should be greater than zero")

    for i in range(number_of_rows):
        if list_type == 'ordered-list':
            list1.append(f"{i + 1}. {input(f'Row #{i + 1}:')}\n")
        elif list_type == 'unordered-list':
            list1.append(f"* {input(f'Row #{i + 1}:')}\n")

    list1_str = ''.join(list1)
    modified_text = modified_text + list1_str

    printer()


def save_to_file():
    with open('output.md', 'w') as file_w:
        file_w.write(modified_text)


while True:
    answer = input("Choose a formatter:")

    if answer == '!help':
        print("""Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done""")

    elif answer == '!done':
        save_to_file()
        break

    elif answer not in formatters and answer not in special_commands:
        print('Unknown formatting type or command')

    elif answer in formatters:
        if answer == 'plain':
            plain()
        elif answer == 'bold':
            bold()
        elif answer == 'italic':
            italic()
        elif answer == 'header':
            header_()
        elif answer == 'link':
            link__()
        elif answer == 'inline-code':
            inline_code_()
        elif answer == 'new-line':
            newline_()
        elif answer == 'ordered-list':
            ordered_unordered('ordered-list')
        elif answer == 'unordered-list':
            ordered_unordered('unordered-list')
