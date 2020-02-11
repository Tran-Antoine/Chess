import inputparser
import util.vector as vector
import time


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


class TkinterInputParser(inputparser.InputParser):

    def __init__(self, renderer):
        super().__init__()
        self.renderer = renderer
        self.piece_on_tile = None
        self.wait = True
        self.initial_position = None
        self.final_position = None

    def wait_for_input(self):
        self.wait = True

        self.renderer.canvas.bind("<ButtonPress>", self.click_position)
        print(self.renderer.canvas.master)
        # So the program waits for a proper input
        answer = 0
        while answer != 1:
            time.sleep(0.1)
            answer = self.still_wait()

        self.renderer.canvas.move(self.piece_on_tile, self.initial_position[0] - self.final_position[0],
                                  self.initial_position[1] - self.final_position[1])

        real_initial_position = self.convert_to_chess_coords(self.initial_position)
        real_final_position = self.convert_to_chess_coords(self.final_position)
        return (real_initial_position, real_final_position)

    def convert_to_chess_coords(self, position):
        for i in range(8):
            if self.renderer.CANVAS_SIZE/8 * i <= position[0] < self.renderer.CANVAS_SIZE/8 * (i + 1):
                position_x = i
            if self.renderer.CANVAS_SIZE/8 * i <= position[1] < self.renderer.CANVAS_SIZE/8 * (i + 1):
                position_y = 7 - i
        return vector.Vector2f(position_x, position_y)

    def still_wait(self):
        """
        Verify if a piece has been moved, so the program can proceed to the next step.
        """
        if not self.wait:
            return 1
        return 0

    def click_position(self, event):
        print(event.x, event.y)
        for position in self.renderer.cases_position:
            if position[0] < event.x < position[2] and position[1] < event.y < position[3]:
                widgets_at_position = self.renderer.canvas.find_overlapping(position[0] + 1,
                                                                            position[1] + 1,
                                                                            position[2] - 1,
                                                                            position[3] - 1)
                self.piece_on_tile = widgets_at_position[-1] if len(widgets_at_position) == 2 else None
                break
        if self.piece_on_tile is not None:
            self.initial_position = self.renderer.canvas.coords(self.piece_on_tile)
            self.renderer.canvas.bind("<Motion>", self.canvas_move)
            self.renderer.canvas.bind("<ButtonRelease>", self.click_release)

    def canvas_move(self, event):
        piece_coords = self.renderer.canvas.coords(self.piece_on_tile)
        self.renderer.canvas.move(self.piece_on_tile, event.x - piece_coords[0] - 20, event.y - piece_coords[1] - 20)

    def click_release(self, event):
        self.renderer.canvas.unbind("<ButtonPress>")
        self.renderer.canvas.unbind("<ButtonRelease>")
        self.renderer.canvas.unbind("<Motion>")

        self.final_position = self.renderer.canvas.coords(self.piece_on_tile)
        self.wait = False
