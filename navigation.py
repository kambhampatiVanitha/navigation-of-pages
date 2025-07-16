import tkinter as tk
from tkinter import messagebox

class HomepageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Homepage with Navigation")
        self.root.geometry("400x300")
        
        # List of page options
        self.pages = ["Google", "ChatGPT", "Firefox", "Microsoft Edge"]
        
        # Create the homepage content
        self.create_homepage()

    def create_homepage(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Heading for the homepage
        heading = tk.Label(self.root, text="Homepage: Select Any One Option", font=("Arial", 16))
        heading.pack(pady=20)

        # Create the page options as buttons
        for idx, page in enumerate(self.pages, 1):
            option_button = tk.Button(self.root, text=f"{idx}. {page}", command=lambda p=page: self.open_page(p))
            option_button.pack(pady=5)

        # Create Previous Button
        prev_button = tk.Button(self.root, text="Previous", command=self.previous_page)
        prev_button.pack(pady=20)

    def open_page(self, page_name):
        # Open a new window with the selected page's content
        page_window = tk.Toplevel(self.root)
        page_window.title(f"{page_name} Page")
        page_window.geometry("400x300")

        # Create a label to show the page content
        label = tk.Label(page_window, text=f"This is the {page_name} page", font=("Arial", 14))
        label.pack(pady=50)

        # Navigation buttons (Previous, Next, Close)
        prev_button = tk.Button(page_window, text="Previous", command=lambda: self.navigate_page(page_window, "previous"))
        prev_button.pack(side="left", padx=20, pady=20)

        next_button = tk.Button(page_window, text="Next", command=lambda: self.navigate_page(page_window, "next"))
        next_button.pack(side="right", padx=20, pady=20)

        close_button = tk.Button(page_window, text="Close", command=page_window.destroy)
        close_button.pack(pady=20)

    def navigate_page(self, page_window, direction):
        # Get the title of the current page
        current_page = page_window.title().replace(" Page", "")
        
        # Get the current index of the page
        current_idx = self.pages.index(current_page)

        if direction == "next":
            # If the current page is Microsoft Edge, show the "No next page" message
            if current_page == "Microsoft Edge":
                messagebox.showinfo("No Next Page", "There is no next page.")
                return  # Prevent navigation
            
            next_idx = (current_idx + 1) % len(self.pages)  # Go forward in the list

        elif direction == "previous":
            if current_page == "Google":
                # If it's Google, go back to the homepage
                self.return_to_homepage()
                return
            else:
                next_idx = (current_idx - 1) % len(self.pages)  # Go backward in the list

        # Close the current page window
        page_window.destroy()

        # Open the next page
        self.open_page(self.pages[next_idx])

    def previous_page(self):
        # Show a message if Previous is clicked before the homepage
        messagebox.showinfo("No Page Before", "There is no page before the homepage")

    def return_to_homepage(self):
        # Destroy the current page window and return to the homepage
        self.create_homepage()

# Set up the Tkinter window
root = tk.Tk()
app = HomepageApp(root)

# Start the Tkinter event loop
root.mainloop()
