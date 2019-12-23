"""
Test de comment faire bouger un objet dans un canvas avec la souris.
"""

import tkinter as tk


class Test():
    def __init__(self, root):
        self.canvas = tk.Canvas(height=500, width=500, bg="blue")
        self.objet1 = self.canvas.create_rectangle(0, 0, 40, 40, fill="white")
        self.objet2 = self.canvas.create_rectangle(50, 50, 90, 90, fill="Green")
        self.objets =[self.objet1, self.objet2]
        self.canvas.pack()
        self.objet = None
        root.bind("<ButtonPress>", self.selectObject)
        root.bind("<ButtonRelease>", self.move)

    def move(self, event):
        if self.objet is not None:
            self.objet_coord = self.canvas.coords(self.objet)
            self.canvas.move(self.objet, event.x - self.objet_coord[0] - 20, event.y - self.objet_coord[1] - 20)
            self.objet = None

    def selectObject(self, event):
        """
        """
        for objet in self.objets:
            objet_coords = self.canvas.coords(objet)
            if objet_coords[0] < event.x < objet_coords[2] and objet_coords[1] < event.y < objet_coords[3]:

                self.objet = objet
root = tk.Tk()
Test(root)
root.mainloop()