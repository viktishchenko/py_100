# Настройки экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = 'black'
TITLE = 'PONG Game'

# Настройки ракеток
PADDLE_COLOR = 'white'
PADDLE_SHAPE = 'square'
PADDLE_STRETCH_LEN = 1
PADDLE_STRETCH_WID = 5
PADDLE_SPEED = 20
PADDLE_LIMIT = 250  # Макс. высота движения ракетки

# Настройки мяча
BALL_COLOR = 'white'
BALL_SHAPE = 'circle'
BALL_SPEED = 0.1
BALL_SPEED_INCREMENT = 0.9  # Коэфф. ускорения
BALL_X_MOVE = 10
BALL_Y_MOVE = 10

# Настройки счета
SCORE_FONT = ('Courier', 40, 'bold')
GAME_OVER_FONT = ('Courier', 26, 'bold')
ALIGNMENT = 'center'
SCORE_POSITION = (0, 220)
GAME_OVER_POSITION = (0, 0)
WIN_SCORE = 5