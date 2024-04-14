import tkinter as tk
import pathlib
import os
import shutil
import platform
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog, font
import tkinter.messagebox as messagebox
from collections import defaultdict

BASE_DIR = Path(__file__).parent
ASSETS_PATH = BASE_DIR / "assets" / "frame0"

output1_path = None
output2_path = None

def is_font_exist(font_name):
    available_fonts = font.families()
    return font_name in available_fonts

def browse_file_output1():
    global output1_path
    output1_path = filedialog.askopenfilename(initialdir="/", title="Select output1.txt", filetypes=(("Original Output", "output1.txt"), ("All files", "*.*")))
    if output1_path:
        entry_1.delete(0, tk.END)
        entry_1.insert(0, output1_path)

def browse_file_output2():
    global output2_path
    output2_path = filedialog.askopenfilename(initialdir="/", title="Select output2.txt", filetypes=(("Modified Output", "output2.txt"), ("All files", "*.*")))
    if output2_path:
        entry_2.delete(0, tk.END)
        entry_2.insert(0, output2_path)

def differed_galaxy(output1_path, output2_path):
    if output1_path is None or output2_path is None:
        canvas.itemconfig(handler_text, text="Error: Please select both output files.", fill="red")
        messagebox.showerror("Oops! An Error Occurred!", "Please select both output files.")
        return

    try:
        with open(output1_path, 'r') as file1, open(output2_path, 'r') as file2:
            hashes1 = defaultdict(list)
            for line in file1:
                if 'diff_galaxy_og' not in line and 'diff_galaxy_modded' not in line:
                    path, hash = line.split(' - ')[0], line.split(' - ')[1].strip()
                    hashes1[hash].append(path)

            hashes2 = defaultdict(list)
            for line in file2:
                if 'diff_galaxy_og' not in line and 'diff_galaxy_modded' not in line:
                    path, hash = line.split(' - ')[0], line.split(' - ')[1].strip()
                    hashes2[hash].append(path)

        diff_hashes = set(hashes2.keys()).difference(hashes1.keys())

        with open('differed.txt', 'w') as outfile:
            for hash in diff_hashes:
                for path in hashes2[hash]:
                    outfile.write(path + ' - ' + hash + '\n\n')

        canvas.itemconfig(handler_text, text="Differed Successfully!", fill="green")
    except FileNotFoundError:
        canvas.itemconfig(handler_text, text="Error: One or both output files not found.", fill="red")
        messagebox.showerror("Oops! An Error Occurred!", "One or both output files not found.")
    except PermissionError:
        canvas.itemconfig(handler_text, text="Error: No permission", fill="red")
        messagebox.showerror("Oops! An Error Occurred!", "No permission to access file. Check your permissions.")
    except Exception as e:
        canvas.itemconfig(handler_text, text="Differ Error", fill="red")
        messagebox.showerror("Oops! A Rare Error Occurred!", str(e))

def copy_files():
    canvas.itemconfig(handler_text, text="Generating... Please wait.", fill="black")
    root.update_idletasks()

    try:
        with open('differed.txt', 'r') as file:
            paths = [line.split(' - ')[0] for line in file if line.strip()]

        for path in paths:
            abs_path = os.path.abspath(path)
            _, rel_path = os.path.splitdrive(abs_path)
            dest_path = os.path.join('GENERATED', rel_path.lstrip('\\'))
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy2(path, dest_path)

        canvas.itemconfig(handler_text, text="Generated Successfully! Thanks for using Pygafi.", fill="green")

    except Exception as e:
        canvas.itemconfig(handler_text, text="Generate Error", fill="red")
        messagebox.showerror("Oops! An Error Occurred!", str(e))

def copy_files_linux():
    canvas.itemconfig(handler_text, text="Generating... Please wait.", fill="black")
    root.update_idletasks()

    try:
        with open('differed.txt', 'r') as file:
            paths = [line.split(' - ')[0] for line in file if line.strip()]

        for path in paths:
            if os.path.isabs(path):
                abs_path = path
            else:
                abs_path = os.path.abspath(path)
            dest_path = os.path.join('GENERATED', abs_path.lstrip('/'))
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy2(abs_path, dest_path)

        canvas.itemconfig(handler_text, text="Generated Successfully! Thanks for using Pygafi.", fill="green")

    except Exception as e:
        canvas.itemconfig(handler_text, text="Generate Error", fill="red")
        messagebox.showerror("Oops! An Error Occurred!", str(e))


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



root = tk.Tk()
root.title("Pygafi v0.4 -- A Filesystem tool for Super Mario Galaxy")
root.geometry("660x470")
root.configure(bg = "#F1EAFF")
root.resizable(False, False)

if platform.system() == "Windows":
    root.iconbitmap(relative_to_assets("icon.ico"))

if is_font_exist("Delfino"):
    font_name = "Delfino"
else:
    font_name = "Arial"

canvas = Canvas(
    root,
    bg = "#F1EAFF",
    height = 470,
    width = 660,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
title_image = PhotoImage(
    file=relative_to_assets("title.png"))
title = canvas.create_image(
    329.0,
    44.0,
    image=title_image
)

image_bg = PhotoImage(
    file=relative_to_assets("image_bg.png"))
bg_image = canvas.create_image(
    328.0,
    270.0,
    image=image_bg
)

output_text = PhotoImage(
    file=relative_to_assets("text_outputsel.png"))
outputtxt = canvas.create_image(
    168.0,
    120.0,
    image=output_text
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    247.5,
    166.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#E4E4E4",
    fg="#000716",
    highlightthickness=0,
    text="Selected file (output1.txt): "
)
entry_1.place(
    x=62.0,
    y=147.0,
    width=371.0,
    height=36.0
)


browse1_button = PhotoImage(
    file=relative_to_assets("browse1.png"))
browse1 = Button(
    image=browse1_button,
    borderwidth=0,
    highlightthickness=0,
    command=browse_file_output1,
    relief="flat",
    bg="white",
    activebackground="white"
)
browse1.place(
    x=469.0,
    y=146.0,
    width=150.0,
    height=47.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    247.5,
    228.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#E4E4E4",
    fg="#000716",
    highlightthickness=0,
    text="Selected file (output2.txt): "
)
entry_2.place(
    x=62.0,
    y=209.0,
    width=371.0,
    height=36.0
)

browse2_button = PhotoImage(
    file=relative_to_assets("browse2.png"))
browse2 = Button(
    image=browse2_button,
    borderwidth=0,
    highlightthickness=0,
    command=browse_file_output2,
    relief="flat",
    bg="white",
    activebackground="white"
)
browse2.place(
    x=469.0,
    y=208.0,
    width=150.0,
    height=47.0
)

differ_button = PhotoImage(
    file=relative_to_assets("differ.png"))
differ = Button(
    image=differ_button,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: differed_galaxy(output1_path, output2_path),
    relief="flat",
    bg="white",
    activebackground="white"
)
differ.place(
    x=250.0,
    y=265.0,
    width=167.0,
    height=47.0
)

filesystem_text = PhotoImage(
    file=relative_to_assets("text_filesystem.png"))
filesystemtxt = canvas.create_image(
    168.0,
    330.0,
    image=filesystem_text
)

generate_windows_button = PhotoImage(
    file=relative_to_assets("generate_windows.png"))
generate_windows = Button(
    image=generate_windows_button,
    borderwidth=0,
    highlightthickness=0,
    command=copy_files,
    relief="flat",
    bg="white",
    activebackground="white"
)
generate_windows.place(
    x=41.0,
    y=357.0,
    width=287.0,
    height=47.0
)

generate_linux_button = PhotoImage(
    file=relative_to_assets("generate_linux.png"))
generate_linux = Button(
    image=generate_linux_button,
    borderwidth=0,
    highlightthickness=0,
    command=copy_files_linux,
    relief="flat",
    bg="white",
    activebackground="white"
)
generate_linux.place(
    x=332.0,
    y=357.0,
    width=287.0,
    height=47.0
)



handler_text = canvas.create_text(
    45.0, 409.0,
    anchor="nw",
    text="Pygafi by LariVille",
    fill="#000000",
    font=(font_name, 24 * -1),
    )



root.mainloop()
