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

def pong_game():
    game_components = setup_game()
    screen = game_components[0]
    ball = game_components[1]
    l_paddle = game_components[2]
    r_paddle = game_components[3]
    l_score = 0
    r_score = 0

    def l_paddle_up():
        l_paddle.sety(l_paddle.ycor() + 20)

    def l_paddle_down():
        l_paddle.sety(l_paddle.ycor() - 20)

    def r_paddle_up():
        r_paddle.sety(r_paddle.ycor() + 20)

    def r_paddle_down():
        r_paddle.sety(r_paddle.ycor() - 20)

    screen.listen()
    screen.onkeypress(l_paddle_up, 'w')
    screen.onkeypress(l_paddle_down, 's')
    screen.onkeypress(r_paddle_up, 'Up')
    screen.onkeypress(r_paddle_down, 'Down')
