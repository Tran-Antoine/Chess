import inputparser
import util.vector as vector
import threading
import tkinter


class ConsoleInputParser(inputparser.InputParser):
    
    def __init__(self):
        super().__init__()
        
    def wait_for_input(self):
        move = input("Enter your next move, 'stop' to interrupt the program\n")    
        try:
            target, destination = move.upper().split()
            conversion = lambda letter: 'ABCDEFGH'.index(letter)
            initial_position = vector.Vector2f(conversion(target[0]), int(target[1])-1)
            final_position = vector.Vector2f(conversion(destination[0]), int(destination[1])-1)
            return (initial_position, final_position)
        except ValueError:
            if move == 'stop':
                return None, None
            print("Invalid input, try again")
            return self.wait_for_input()
          
    def wait_for_extra_piece(self):
        return input("Entrez l'ID de la pièce: ")
          

class TkinterInputParser(inputparser.InputParser):

    def __init__(self, renderer):
        super().__init__()
        self.renderer = renderer
        self.piece_on_tile_chosen = None
        self.initial_position = None
        self.final_position = None
        self.continue_game = True

        # Bind the button to quit the app and to move the pieces
        self.renderer.canvas.master.bind("<Control-q>", lambda _: self.stop_game())
        self.renderer.canvas.bind("<ButtonPress>", self.get_piece_by_mouse_position)
        lock = threading.Lock()
        self.wait_for_canvas_input = threading.Condition(lock)
        lock.acquire()

        self.renderer.menu.add_cascade(label="quit", command=self.stop_game)

    def wait_for_input(self):
        self.wait = True
        # So the program waits for a proper input
        self.wait_for_canvas_input.acquire()
        if not self.continue_game:
            return None, None
        # Put the piece at his initial position, in case the move is invalid
        self.renderer.canvas.move(self.piece_on_tile_chosen, self.initial_position[0] - self.final_position[0],
                                  self.initial_position[1] - self.final_position[1])

        real_initial_position = self.convert_to_chess_coords(self.initial_position)
        real_final_position = self.convert_to_chess_coords(self.final_position)
        return real_initial_position, real_final_position

    def convert_to_chess_coords(self, position):
        for i in range(8):
            if self.renderer.CANVAS_SIZE/8 * i <= position[0] < self.renderer.CANVAS_SIZE/8 * (i + 1):
                position_x = i

            if self.renderer.CANVAS_SIZE/8 * i <= position[1] < self.renderer.CANVAS_SIZE/8 * (i + 1):
                position_y = 7 - i
        return vector.Vector2f(position_x, position_y)

    def stop_game(self):
        self.wait_for_canvas_input.release()
        self.continue_game = False
        self.renderer.canvas.master.destroy()

    def get_piece_by_mouse_position(self, event):
        for position in self.renderer.cases_position:
            # To know in which tile the mouse is.
            if position[0] < event.x < position[2] and position[1] < event.y < position[3]:
                # To know whether there are 2 objects on the canvas --> if there are 2, it means that
                # there is a piece on the tile.
                widgets_at_position = self.renderer.canvas.find_overlapping(position[0] + 1,
                                                                            position[1] + 1,
                                                                            position[2] - 1,
                                                                            position[3] - 1)
                self.piece_on_tile_chosen = widgets_at_position[-1] if len(widgets_at_position) == 2 else None
                break

        if self.piece_on_tile_chosen is not None:
            self.initial_position = self.renderer.canvas.coords(self.piece_on_tile_chosen)
            self.renderer.canvas.bind("<Motion>", self.move_piece_with_mouse)
            self.renderer.canvas.bind("<ButtonRelease>", lambda _: self.release_piece_at_mouse_position())

    def move_piece_with_mouse(self, event):
        """
        When the piece is selected and the user moves the mouse, it moves the piece.
        """
        piece_coords = self.renderer.canvas.coords(self.piece_on_tile_chosen)
        self.renderer.canvas.move(self.piece_on_tile_chosen, event.x - piece_coords[0], event.y - piece_coords[1])

    def release_piece_at_mouse_position(self):
        self.renderer.canvas.unbind("<ButtonRelease>")
        self.renderer.canvas.unbind("<Motion>")

        self.final_position = self.renderer.canvas.coords(self.piece_on_tile_chosen)
        self.wait_for_canvas_input.release()            
    
    def wait_for_extra_piece(self):
        return input("Entrez l'ID de la pièce: ")
