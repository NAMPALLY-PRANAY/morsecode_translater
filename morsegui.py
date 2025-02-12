import tkinter as tk
from tkinter import ttk, messagebox

# Dictionary mapping English to Morse code
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', 
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', ',': '--..--', '.': '.-.-.-', '?': '..--..', 
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', '&': '.-...', 
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '_': '..--.-', 
    '"': '.-..-.', '$': '...-..-', '!': '-.-.--', '@': '.--.-.', ' ': '/'
}

# Reverse the Morse code dictionary for decoding
REVERSE_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    text = text.upper()
    morse_code = []
    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append('?')
    return ' '.join(morse_code)

def morse_to_text(morse):
    words = morse.split(' / ')
    decoded_text = []
    for word in words:
        decoded_word = []
        for code in word.split():
            if code in REVERSE_MORSE_CODE_DICT:
                decoded_word.append(REVERSE_MORSE_CODE_DICT[code])
            else:
                decoded_word.append('?')
        decoded_text.append(''.join(decoded_word))
    return ' '.join(decoded_text)

def convert():
    conversion_type = conversion_type_var.get()
    input_text = input_text_box.get("1.0", tk.END).strip()
    if conversion_type == "English to Morse Code":
        result = text_to_morse(input_text)
    else:
        result = morse_to_text(input_text)
    output_text_box.config(state=tk.NORMAL)
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, result)
    output_text_box.config(state=tk.DISABLED)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(output_text_box.get("1.0", tk.END).strip())
    messagebox.showinfo("Copied", "Text copied to clipboard!")

# Create main window
root = tk.Tk()
root.title("Morse Code Converter")
root.geometry("400x400")
root.config(bg="#282c34")

# Dropdown for conversion type
conversion_type_var = tk.StringVar(value="English to Morse Code")
conversion_type_dropdown = ttk.Combobox(root, textvariable=conversion_type_var, state="readonly")
conversion_type_dropdown['values'] = ("English to Morse Code", "Morse Code to English")
conversion_type_dropdown.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Input text box
input_text_label = tk.Label(root, text="Input Text:", bg="#282c34", fg="#ffffff")
input_text_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
input_text_box = tk.Text(root, height=5, width=40)
input_text_box.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert, bg="#98c379", fg="#282c34")
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Output text box
output_text_label = tk.Label(root, text="Output Text:", bg="#282c34", fg="#ffffff")
output_text_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
output_text_box = tk.Text(root, height=5, width=40, state=tk.DISABLED)
output_text_box.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Copy button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#61afef", fg="#282c34")
copy_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()
