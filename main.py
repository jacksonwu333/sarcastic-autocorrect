import tkinter as tk
"""
-------------List of phrases for testing-----------
lemme slide into ur dms -> Allow me to slip into thy private chamber
Bro, you acting like an NPC rn --> Pookie, yn actin like an unskippable cutscene 
"omg bruh wtf" → "By golly, pookie, oh great heavens! Are my eyes deceiving me?"
"dm me btw" → "Slide softly into me, side quest unlocked."
"gtg ttyl" → "Gotta go walk my goldfish, I shall depart now, like a ninja in the night. Until next time!"
"""

# dictionary & sarcastic replacements
sarcasm_dict = {
    "okay": "Sure, because that always works out well.",
    "ok": "Sure, because that always works out well.",
    "kk": "Ah, verily, it is most satisfactory!",
    "k": "By my decree, it is permitted.",
    "yes" : "As the sun rises in the east, so too do I say YES",
    "yea" : "Oh yes, absolutely! No flaws in that plan.",
    "yeah" : "YAS QUEEN",
    "yup" : "Oh yes, absolutely! No flaws in that plan.",
    "thanks": "Oh wow, thank you SO much. I’ll treasure this moment forever.",
    "sorry": "soooooo regretful, totally",
    "nah": "I'd rather eat a bowl of uncooked rice",
    "shush": "sybau",
    "shut": "shut your giggly ahh",
    "goat": "LEBRON",
    "sunshine": "MY GLORIOUS KING LEBRON",
    "hmu": "summon me like a legendary Pokemon",
    "idk": "je ne sais pas",
    "gtg": "gotta go walk my goldfish",
    "lol": "I'm rolling on the floor metaphorically",
    "omg": "by golly",
    "what": "what in the walmart version of reality",
    "ttyl": "I shall depart now, like a ninja in the night. Until next time!",
    "ttytm": "I’m ghosting you until tomorrow, but I’ll return!",
    "good": "skibidi",
    "wth": "what the sigma!",
    "wtf": "oh great heavens! are my eyes deceiving me? ",
    "u": "cutie patootie",   
    "you": "yn",
    "lebron": "lePookie",
    "ik": "Yeah, my last brain cell told me",
    "ikr": "Not a single original thought made",
    "lmao": "imagine me laughing my poop chute off",
    "smh": "vigorously vibrating my noggin",
    "tbh": "allow me a moment of honesty...",
    "rn": "at this very second", 
    "irl": "In roblox language",
    "fyi": "unskippable ad: just in case",
    "btw": "side quest unlocked,",
    "dms": "private chamber",
    "dm": "slide softly into",
    "npc": "unskippable cutscene",
    "short": "vertically challenged",
    "ur": "thy",
    "ngl": "no cap",
    "your": "thine",
    "slide": "slip softly into",
    "lemme": "allow me to",
    "?": "in this economy",
    "is": "is nothing but",
    "block": "vanish into the void",
    "bro": "pookie",

  }

def apply_sarcasm(event=None):
    text = text_input.get("1.0", tk.END)  # Get text from input box
    words = text.split()
    sarcastic_text = " ".join([sarcasm_dict.get(word.lower(), word) for word in words])
    output_text.config(state=tk.NORMAL)  # Enable editing
    output_text.delete("1.0", tk.END)  # Clear previous text
    output_text.insert(tk.END, sarcastic_text)  # Insert new text
    output_text.config(state=tk.DISABLED)  # Disable editing

# GUI Setup
root = tk.Tk()
root.title("Uselss Autocorrect")
root.geometry("1080x600")

# Input field
tk.Label(root, text="Type Here:").pack()
text_input = tk.Text(root, height=10, width=100)
text_input.pack()
text_input.bind("<KeyRelease>", apply_sarcasm)  # Apply sarcasm on every key release

# Output field (Read-only)
tk.Label(root, text="Useless Version:").pack(pady=10)
output_text = tk.Text(root, height=10, width=100, state=tk.DISABLED)
output_text.pack()

# Run the app
root.mainloop()
