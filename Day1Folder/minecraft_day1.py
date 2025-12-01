# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################


################## On Chat Commands Section #####################
def move_forward(steps):
    agent.move(FORWARD, steps)
def move_back(steps):
    agent.move(BACK, steps)
def move_up(steps):
    agent.move(UP, steps)

def move_down(steps):
    agent.move(DOWN, steps)

def turn_left():
    agent.turn(TurnDirection.LEFT)

def turn_right():
    agent.turn(TurnDirection.RIGHT)

player.on_chat("mf1",move_forward)
player.on_chat("mb1",move_back)
player.on_chat("mu1",move_up)
player.on_chat("md1",move_down)
player.on_chat("tl",turn_left)
player.on_chat("tr",turn_right)
def teleport():
    agent.teleport_to_player()
player.on_chat("come",teleport)

def obby1():
    agent.move(FORWARD, 4)
    agent.move(LEFT, 4)
    agent.move(FORWARD, 3)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 2)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
player.on_chat("obby",obby1)