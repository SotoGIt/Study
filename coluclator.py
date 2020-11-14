from tkinter import *
from tkinter import ttk


LAYOUT = [
	["1", "2", "4", "/"],
	["4", "5", "6", "*"],
	["7", "8", "9", "-"],
	["0", "C", "=", "+"],
]



class CalcApp(ttk.Frame):
	"""電卓アプリ."""

	def __init__(self, master=None):
		super().__init__(master)
		self.create_widgets()

	def create_widgets(self):
		button = ttk.Button(self, text="押して", command=self.push)
		button.grid(column=0, row=0, sticky=(N, S, E, W))
		self.grid(column=0, row=0, sticky=(N, S, E, W))

	def push(self):
		print("押された")




def main():
	root = Tk()
	root.title("簡易電卓")
	CalcApp(root)
	root.mainloop()


if __name__ == "__main__":
	main()
















