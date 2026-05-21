import tkinter as tk
import pygame

# --- CONFIG ---

prompts = [
    "Stig till: 3 500 fot", # Cue 1
    "Sväng vänster: 240 grader\nBehåll 3 500 fot", # Cue 2
    "Signalstyrka: God", # Cue 3
    "Sväng vänster: 240 grader\nBehåll 3 500 fot", # Cue 4
    "Sjunk till 2 000 fot\nBehåll kurs 240 grader", # Cue 5
    "Sväng höger: 330 grader\nStig till 3 000 fot", # Cue 6
    "Motortemperatur: Normal", # Cue 7
    "Sväng höger: 330 grader\nStig till 3 000 fot",  # Cue 8
    "Vindstyrka: 0 m/s", # Cue 9
    "Sväng höger: 330 grader\nStig till 3 000 fot", # Cue 10
    "Sessionen avslutad\nTack!" # Cue 11

]

audio_files = [
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    None,
    "audio/avslut.wav"
]

# Time after each cue before the next one (milliseconds)
cue_intervals = [
    45000,  # after cue 1
    14000,  # after cue 2
    8000,   # after cue 3
    29000,   # after cue 4
    50000,   # after cue 5
    10000,   # after cue 6
    9000,   # after cue 7
    18000,   # after cue 8
    9000,   # after cue 9
    30000,   # after cue 10
    60000,   # after cue 11
]

# --- INIT AUDIO ---
pygame.mixer.init()

root = tk.Tk()
root.title("UAV Cue Display")
root.geometry("1000x600")
root.configure(bg="black")

display_label = tk.Label(
    root,
    text="Välkommen!\nInstruktioner kommer \nvisas här.",
    font=("Helvetica", 72, "bold"),
    fg="lime",
    bg="black",
    justify="center"
)
display_label.pack(expand=True, fill="both")

running = False
current_index = 0

# --- FLASH ---
def flash_window():
    display_label.config(bg="red")
    root.after(100, lambda: display_label.config(bg="black"))

# --- PLAY AUDIO ---
def play_audio(index):
    if index < len(audio_files) and audio_files[index] is not None:
        pygame.mixer.music.load(audio_files[index])
        pygame.mixer.music.play()

# --- SHOW PROMPT ---
def show_prompt(index):
    display_label.config(text=prompts[index])
    flash_window()
    play_audio(index)

# --- CUE LOOP ---
def cue_loop():
    global current_index

    if not running:
        return

    show_prompt(current_index)

    wait_time = cue_intervals[current_index]

    current_index = (current_index + 1) % len(prompts)

    root.after(wait_time, cue_loop)

# --- START / STOP ---
def toggle_run(event=None):
    global running
    running = not running

    if running:
        cue_loop()

# --- KEY BINDING ---
root.bind("<space>", toggle_run)

root.mainloop()
