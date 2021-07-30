from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""
qualities = []
select = ''


# file location
def open_location():
    global Folder_Name
    Folder_Name = filedialog.askdirectory(initialdir="C:\\Users\\hp\\Desktop")
    if len(Folder_Name) > 1:
        path_error.config(text=Folder_Name, fg='green')
    else:
        path_error.config(text='Please Choose Folder', fg='red')


def download_video():
    global select
    choice = youtube_choice.get()
    url = youtube_entry_box.get()
    if len(url) > 1:
        youtube_error.config(text='')
        yt = YouTube(url)
        for q in qualities:
            if choice == q:
                select = yt.streams.get_by_resolution(str(choice))
        else:
            youtube_error.config(text='paste link again!', fg='red')
        select.download(Folder_Name)
        complete_message = 'Download Completed!!' + str(yt.title)[0:10]
        youtube_error.config(text=complete_message)
        qualities.clear()


def check():
    url = youtube_entry_box.get()
    yt = YouTube(url)
    global qualities
    for q in yt.streams.filter(progressive=True):
        qualities.append(q.resolution)
    youtube_choice.config(values=qualities)
    youtube_choice.current(0)
    youtube_error.config(text='Video available', fg='green')
    video_title.config(text=yt.title, fg='black')


root = Tk()
root.title("Youtube Video Breaker")
root.iconbitmap('youtube_socialnetwork_19998.ico')
# root.geometry("600x400")
# Youtube Video Link Url
youtube_url_link_label = Label(root, text="Enter Youtube Video URL", font=('jost', 15))
youtube_url_link_label.grid(row=0, column=0, pady=(10, 10))
# Entry BOX
youtube_entry_box_var = StringVar()
youtube_entry_box = Entry(root, width=50, textvariable=youtube_entry_box_var)
youtube_entry_box.grid(row=1, column=0, pady=(10, 10), padx=(10, 10))
# check button
check_button = Button(root, width=20, bg='blue', fg='white', text='Check', command=check)
check_button.grid(row=1, column=1, pady=(10, 10), padx=(10, 10))
# error msg
youtube_error = Label(root, fg='red', font=('jost', 12))
youtube_error.grid(row=0, column=1, pady=(10, 10))

# video_title
video_title = Label(root, font=('jost', 12), wraplength=300, justify="center")
video_title.grid(row=2, column=0, rowspan=3, pady=(10, 10))

# choose path
save_entry = Button(root, width=20, bg='blue', fg='white', text='Choose Path', command=open_location)
save_entry.grid(row=3, column=1, pady=(10, 10))
# path error msg
path_error = Label(root, text='', fg='red', font=('jost', 12))
path_error.grid()

# dropbox
youtube_choice = ttk.Combobox(root)
youtube_choice.grid(row=2, column=1, pady=(10, 10))

# download button
download_button = Button(root, width=20, text="Download Now", bg='red', fg='white', command=download_video)
download_button.grid(row=4, column=1, pady=(10, 10))

# This button will initialize
# the progress bar
# Button(root, text='Start', command=bar).grid(pady=10)
# developer label
developer_label = Label(root, text='©WebGroundBreaker', fg='Black', font=('jost', 8))
developer_label.grid(row=6, column=0, columnspan=3, pady=(10, 10))
root.mainloop()
