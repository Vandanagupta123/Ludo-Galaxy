from tkinter import *
from PIL import ImageTk, Image
from stopwatch import Stopwatch
from duplicateGALAXYY import Ludo
from tkinter import messagebox
class MainApp:
    def __init__(self, root):
        self.root = root
        
        self.create_initial_window()


    def create_initial_window(self):
        self.root.geometry("500x150")
        self.root.config(bg="sky blue")

        head = Label(self.root, text="Total number of players:- ", font=("Arial", 14, "bold"), bg="sky blue", fg="chocolate")
        head.place(x=40, y=30)
        take_entry = Entry(self.root, font=("Arial", 10, "bold", "italic"), bd=7, width=18)
        take_entry.place(x=280, y=30)
        take_entry.focus()

        def filtering():
            num_players = take_entry.get()
            if num_players.isdigit() and 2 <= int(num_players) <= 4:
                root.withdraw()  # Hide the initial window
                app.create_stopwatch_and_ludo()  # Create the game window
            else:
                messagebox.showerror("Input Error", "Please input a valid number of players between 2 and 4")

        submit_btn = Button(self.root, text="Submit", bg="orange", fg="black", font=("Arial", 13, "bold"), relief=RAISED, bd=8, command=filtering)
        submit_btn.place(x=180, y=100)

    def input_filtering(self, input_value):
        return True  # Placeholder for input validation logic

    def create_stopwatch_and_ludo(self):
        self.game_window = Toplevel(self.root)
        self.game_window.geometry("1000x700")
        self.game_window.title("Game Window")

        # Create a label for the background image
        background_label = Label(self.game_window)
        background_label.place(relwidth=1, relheight=1)

        # Load and set the background image
        bg_image_path = "C:/Users/Anurag/Downloads/bg.png"
        bg_image = Image.open(bg_image_path)
        bg_image = bg_image.resize((1000, 700), Image.BILINEAR)
        self.background_image = ImageTk.PhotoImage(bg_image)
        background_label.config(image=self.background_image)

        # Create and pack the stopwatch
        self.stopwatch_frame = Frame(self.game_window)
        self.stopwatch_frame.pack(side=LEFT, padx=5, pady=5)
        self.stopwatch = Stopwatch(self.game_window)  # Pass game_window as the master widget

        # Create the Ludo game
        self.ludo_frame = Frame(self.game_window)
        self.ludo_frame.pack(side=LEFT, padx=10, pady=10)

        # Explicitly update the game window
        self.game_window.update()

        # Create and pack the Ludo game
        self.create_ludo()

    def create_ludo(self):
        # Load and resize images for Ludo
        six_side_block = ImageTk.PhotoImage(Image.open("C:/Users/Anurag/Downloads/ludoimages/Images/6_block.png").resize((50, 50)))
        five_side_block = ImageTk.PhotoImage(Image.open("C:/Users/Anurag/Downloads/ludoimages/Images/5_block.png").resize((50, 50)))
        four_side_block = ImageTk.PhotoImage(Image.open("C:/Users/Anurag/Downloads/ludoimages/Images/4_block.png").resize((50, 50)))
        three_side_block = ImageTk.PhotoImage(Image.open("C:/Users/Anurag/Downloads/ludoimages/Images/3_block.png").resize((50, 50)))
        two_side_block = ImageTk.PhotoImage(Image.open("C:/Users/Anurag/Downloads/ludoimages/Images/2_block.png").resize((50, 50)))
        one_side_block = ImageTk.PhotoImage(Image.open("C:/Users/Anurag/Downloads/ludoimages/Images/1_block.png").resize((50, 50)))

        # Create Ludo instance with block images
        self.ludo_game = Ludo(self.ludo_frame, six_side_block, five_side_block, four_side_block, three_side_block, two_side_block, one_side_block)

if __name__ == "__main__":
    root = Tk()
    app = MainApp(root)
    root.mainloop()
