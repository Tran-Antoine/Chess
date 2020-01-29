import inputparser
import util.vector as vector


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

    def __init__(self):
        super().__init__()

    def wait_for_input(self):
        pass