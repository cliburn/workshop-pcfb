import turtle
import sys
import Image

def get_artist(width=600, height=400, startx=0, starty=0,
               color='forest green', thickness=2, speed='fastest'):
    """Set up for drawing to screen."""
    turtle.setup(width, height)
    artist = turtle.getturtle()
    artist.penup()
    artist.setpos(startx, starty)
    artist.pendown()
    artist.color(color)
    artist.width(thickness)
    artist.speed(speed)
    return artist

def generate(rules, start, levels):
    """Generate L-system drawing instructions based on given rewrite rules."""
    olds = start
    news = []
    for i in range(levels):
        for symbol in olds:
            news.append(rules.get(symbol, symbol))
        olds = ''.join(news)
        news = []

    return olds

def get_actions(forward, left, right, step, angle):
    """Return a dictionary of decoded actions."""
    actions = {}
    forward = list(forward)
    for f in forward:
        actions[f] = ('forward', step)
    actions[left] = ('left', angle)
    actions[right] = ('right', angle)
    return actions

def draw(artist, instructions, actions):
    """Draw the picture given by coded instructions."""
    stack = []
    for s in instructions:
        if s=='[':
            stack.append((artist.pos(), artist.heading()))
        elif s==']':
            pos, heading = stack.pop()
            artist.penup()
            artist.setpos(pos)
            artist.setheading(heading)
            artist.pendown()
        else:
            action, arg = actions.get(s, (None, 0))
            if action:
                fn = getattr(artist, action)
                fn(arg)

if __name__ == '__main__':
    # preset examples
    plant_rules = {
        'X' : 'F-[[X]+X]+F[+FX]-X',
        'F' : 'FF'
        }
    plant_actions = get_actions('F', '-', '+', 3, 25)

    koch_rules = {
        'F' : 'F+F-F-F+F'
        }
    koch_actions = get_actions('F', '+', '-', 5, 90)

    triangle_rules = {
        'F' : 'F-G+F+G-F',
        'G' : 'GG'
        }
    triangle_actions = get_actions(['F', 'G'], '-', '+', 6, 120)

    pictures = {
        'koch' : (koch_rules, koch_actions, 'F', 4),
        'plant' : (plant_rules, plant_actions, 'X', 6),
        'triangle' : (triangle_rules, triangle_actions, 'F-G-G', 6)
        }

    # get user input
    # e.g. python lsys.py triangle -250 -150
    # e.g. python lsys.py koch -200 -100
    # e.g. python lsys.py plant -275, 50
    picture = sys.argv[1]
    startx = int(sys.argv[2])
    starty = int(sys.argv[3])

    # draw!
    artist = get_artist(startx=startx, starty=starty)
    rules, actions, start, levels = pictures[picture]
    instructions = generate(rules, start, levels)
    draw(artist, instructions, actions)

    # ts = turtle.getscreen()
    # ts.getcanvas().postscript(file=picture + '.eps')
    # Image.open(picture + '.eps').save(picture + '.pdf')
    turtle.mainloop()
