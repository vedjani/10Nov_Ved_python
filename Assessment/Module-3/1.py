from tkinter import *
from tkinter import messagebox
import os

posts = []

def save_post():
    username = username_box.get().strip()
    title = post_title_box.get().strip()
    content = post_Content_box.get("1.0", END).strip()

    if username == "" or title == "" or content == "":
        messagebox.showerror(
            "Error",
            "All fields are required!\nPlease fill Username, Post Title and Content."
        )
        return

    filename = (f"{username} {title}.txt")
    try:
        f=open(filename,"w")
        f.write(f"Username : {username}\n")
        f.write(f"Post Title : {title}\n\n")
        f.write("Post Content:\n")
        f.write(content)
        f.close()

        saved_posts_box.insert(END, filename)

        messagebox.showinfo(
            "Success",
            "Post saved successfully!"
        )

        post_Content_box.delete("1.0", END)

    except Exception as e:
        messagebox.showerror("Error", f"File not saved!\n{e}")




def view_post():
    selected = saved_posts_box.curselection()
    if not selected:
        messagebox.showerror(
            "Error",
            "Please select a post to view!"
        )
        return

    filename = saved_posts_box.get(selected[0])

    
    if not os.path.exists(filename):
        messagebox.showerror(
            "File Error",
            f"File not found:\n{filename}"
        )
        return

    try:
        f=open(filename,"r")
        data = f.read()
        f.close()
        
        
        post_output_box.delete("1.0", END)
        post_output_box.insert(END, data)

    except Exception as e:
        messagebox.showerror("Error", f"Unable to open file!\n{e}")

#-----------------------------------------------------------------------------------------------
root=Tk()
root.geometry("900x1100")
root.title("MiniBlog by Ved")
MiniBlog=Label(text="MiniBlog",font=("",20,"bold"))     
MiniBlog.pack()

user_frame = Frame(root)
user_frame.pack(anchor="w", padx=20, pady=10)

# -------- Username Label --------------------------------------------------
Label(user_frame, text="Username", font=("", 14, "bold")).pack(side="left")

# --------------TextBox (Entry)------------username_box ma chhe entry username ni 
username_box = Entry(user_frame, font=("", 14), width=25)
username_box.pack(side="left", padx=10)


# --------------------------------POST TITLE --------------------------------------------------
post_frame = Frame(root)
post_frame.pack(anchor="w", padx=20, pady=11)   # ← yahi space aa rahi hai

Label(post_frame, text="Post Title", font=("", 14, "bold")).pack(side="left")

post_title_box = Entry(post_frame, font=("", 14), width=25)
post_title_box.pack(side="left", padx=12)

# ------------------------------POST CONTENT + SAVE BUTTON ------------------------------------------------
content_frame = Frame(root)
content_frame.pack(anchor="w", padx=20, pady=(20, 10))

# Label
Label(content_frame, text="Post Content", font=("", 14, "bold"))\
    .pack(anchor="w", pady=(0, 5))

# Text box
post_Content_box = Text(content_frame, font=("", 13), width=70, height=10)
post_Content_box.pack()

# Button frame (same width as text box)
btn_frame = Frame(content_frame)
btn_frame.pack(fill="x", pady=8)

save_btn = Button(
    btn_frame,
    text="Save Post",
    font=("", 12, "bold"),
    width=12,
    command=save_post
)
save_btn.pack(side="right")

# ----------------------------------SAVED POSTS ---------------------------------------------------------------
saved_frame = Frame(root)
saved_frame.pack(anchor="w", padx=20, pady=20)

# Label
Label(saved_frame, text="Saved Posts", font=("", 14, "bold"))\
    .pack(anchor="w", pady=(0, 5))

# Saved posts box (Text ya Listbox)
saved_posts_box = Listbox(saved_frame, font=("", 12), width=70, height=6)
saved_posts_box.pack()

# Button frame (textbox ke niche)
saved_btn_frame = Frame(saved_frame)
saved_btn_frame.pack(fill="x", pady=8)

view_btn = Button(
    saved_btn_frame,
    text="View Post",
    font=("", 12, "bold"),
    width=12,
    command=view_post
)
view_btn.pack(side="right")


# ------------------------------------------POST OUTPUT ----------------------------------------------------------
output_frame = Frame(root)
output_frame.pack(anchor="w", padx=20, pady=(5, 25))

Label(
    output_frame,
    text="Post Output",
    font=("", 14, "bold")
).pack(anchor="w", pady=(0, 5))

post_output_box = Text(
    output_frame,
    font=("", 13),
    width=70,
    height=8
)
post_output_box.pack()



root.mainloop()