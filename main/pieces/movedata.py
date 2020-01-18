class MoveData():

    def __init__(self, destination, changes):
        self.destination = destination
        self.changes = changes

    def __str__(self):
        return f'Destination : {self.destination}\n' \
               f'Changes : {self.changes}'

    def as_destination(self):  # used for method referencing
        return self.changes
