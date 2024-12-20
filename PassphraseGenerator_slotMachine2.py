#!/usr/bin/python3.2.3

'''
This is an updated version of my 3 word passphrase generator.
Version 2 of this program has added 150 more words to the original
20 words of version 1.
This update has come out roughly an hour after the original was created,
as I felt there needed to be more than 20 word options for security purposes
and to help throw some additional odd words into the mix that you might not
typically see.

This script was written by Alayna Ferdarko (AlaynaVendetta on GitHub.)
Written on 20 December, 2024.
Please do not edit without my permission, please!
'''

import tkinter as tk
from tkinter import messagebox
import random

# Sample words for passphrase generation
WORDS = [
    "sunset", "mountain", "ocean", "forest", "river", "cloud", "storm",
    "whisper", "shadow", "echo", "flame", "dream", "spark", "breeze",
    "stone", "meadow", "wave", "sky", "fire", "light", "galaxy", "comet", "nebula", "planet", "star", "orbit", "cosmos",
    "meteor", "asteroid", "eclipse", "quasar", "horizon", "dawn",
    "twilight", "glimmer", "prism", "crystal", "vortex", "void",
    "cascade", "tempest", "frost", "ember", "blaze", "aurora", "chasm",
    "abyss", "rapids", "delta", "peak", "ridge", "valley", "summit",
    "grove", "thicket", "canopy", "brook", "canyon", "dune", "lagoon",
    "reef", "glacier", "cavern", "tundra", "savanna", "desert", "mesa",
    "plateau", "arch", "spire", "crown", "bluff", "haven", "oasis",
    "sanctuary", "enclave", "bastion", "citadel", "fortress", "stronghold",
    "citadel", "realm", "kingdom", "empire", "province", "village",
    "hamlet", "settlement", "outpost", "camp", "pavilion", "tent",
    "shack", "cottage", "lodge", "villa", "manor", "palace", "castle",
    "tower", "keep", "dungeon", "crypt", "labyrinth", "maze", "portal",
    "gate", "passage", "corridor", "hall", "chamber", "sanctum",
    "temple", "shrine", "monument", "obelisk", "statue", "idol",
    "relic", "artifact", "tome", "scroll", "manuscript", "map",
    "compass", "beacon", "signal", "flare", "lantern", "torch",
    "candle", "lamp", "spark", "glow", "radiance", "luster", "gleam",
    "shine", "beam", "ray", "arc", "ring", "circle", "sphere",
    "orb", "disk", "plate", "fragment", "shard", "sliver", "chip",
    "pebble", "boulder", "rock", "stone", "gem", "jewel", "crystal",
    "diamond", "ruby", "sapphire", "emerald", "topaz", "amber"
]

class PassphraseGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Passphrase Generator")
        
        # Locks for keeping parts of the passphrase
        self.locks = [False, False, False]

        # Current passphrase parts
        self.passphrase_parts = ["", "", ""]

        # Saved passphrases
        self.saved_passphrases = []

        # Frame for the slot machine display
        self.display_frame = tk.Frame(self.root)
        self.display_frame.pack(pady=20)

        self.labels = []
        self.lock_buttons = []
        
        # Create display labels and lock buttons
        for i in range(3):
            frame = tk.Frame(self.display_frame)
            frame.pack(side=tk.LEFT, padx=10)

            label = tk.Label(frame, text="", font=("Helvetica", 24), width=10, relief="solid")
            label.pack()
            self.labels.append(label)

            lock_button = tk.Button(frame, text="Unlock", command=lambda idx=i: self.toggle_lock(idx))
            lock_button.pack(pady=5)
            self.lock_buttons.append(lock_button)

        # Spin button
        self.spin_button = tk.Button(self.root, text="Spin", font=("Helvetica", 16), command=self.spin)
        self.spin_button.pack(pady=20)

        # Like button
        self.like_button = tk.Button(self.root, text="Like", font=("Helvetica", 16), command=self.like)
        self.like_button.pack(pady=10)

        # Saved passphrases button
        self.show_saved_button = tk.Button(self.root, text="Show Saved", font=("Helvetica", 16), command=self.show_saved)
        self.show_saved_button.pack(pady=10)

    def spin(self):
        """Generates a new passphrase."""
        for i in range(3):
            if not self.locks[i]:
                self.passphrase_parts[i] = random.choice(WORDS)
                self.labels[i].config(text=self.passphrase_parts[i])

    def toggle_lock(self, idx):
        """Toggles the lock for a specific part of the passphrase."""
        self.locks[idx] = not self.locks[idx]
        self.lock_buttons[idx].config(text="Lock" if self.locks[idx] else "Unlock")

    def like(self):
        """Saves the current passphrase."""
        passphrase = " ".join(self.passphrase_parts)
        if passphrase not in self.saved_passphrases:
            self.saved_passphrases.append(passphrase)
            messagebox.showinfo("Saved", "Passphrase saved: " + passphrase)
        else:
            messagebox.showinfo("Info", "Passphrase already saved!")

    def show_saved(self):
        """Displays the saved passphrases."""
        if self.saved_passphrases:
            saved = "\n".join(self.saved_passphrases)
            messagebox.showinfo("Saved Passphrases", saved)
        else:
            messagebox.showinfo("Saved Passphrases", "No passphrases saved yet.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PassphraseGenerator(root)
    root.mainloop()

