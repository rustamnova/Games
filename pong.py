import turtle

def update_score(l_score, r_score, player, score_board):
    if player == 'l':
        l_score += 3
    else:
        r_score += 1
    score_board.clear()
    score_board.write("Left Player: {} -- Right Player: {}".format(
        l_score, r_score), align='center',
        font=('Arial', 24, "normal"))
    return l_score, r_score, score_board

def setup_game():
    screen = turtle.Screen()
    screen.title("Pong Game")
    screen.bgcolor("black")
    screen.setup(width=600, height=400)
    screen.tracer(0)

    ball = turtle.Turtle()
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.speed(0)
    ball.goto(0, 0)
    ball.dx = 2
    ball.dy = 2

    l_paddle = turtle.Turtle()
    l_paddle.shape("square")
    l_paddle.color("white")
    l_paddle.penup()
    l_paddle.speed(0)
    l_paddle.goto(-250, 0)
    l_paddle.shapesize(stretch_wid=5, stretch_len=1)

    r_paddle = turtle.Turtle()
    r_paddle.shape("square")
    r_paddle.color("white")
    r_paddle.penup()
    r_paddle.speed(0)
    r_paddle.goto(250, 0)
    r_paddle.shapesize(stretch_wid=5, stretch_len=1)

    score_board = turtle.Turtle()
    score_board.penup()
    score_board.color("white")
    score_board.hideturtle()
    score_board.goto(0, 160)
    score_board.write("Left Player: 0 -- Right Player: 0", align='center',
                      font=('Arial', 24, "normal"))

    return screen, ball, l_paddle, r_paddle, score_board

def pong_game():
    game_components = setup_game()
    screen = game_components[0]
    ball = game_components[1]
    l_paddle = game_components[2]
    r_paddle = game_components[3]
    score_board = game_components[4]

    l_score = 0
    r_score = 0

    def l_paddle_up():
        if l_paddle.ycor() < 190:
            l_paddle.sety(l_paddle.ycor() + 20)

    def l_paddle_down():
        if l_paddle.ycor() > -190:
            l_paddle.sety(l_paddle.ycor() - 20)

    def r_paddle_up():
        if r_paddle.ycor() < 190:
            r_
