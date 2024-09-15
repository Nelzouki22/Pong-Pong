import pygame
import sys

# إعدادات اللعبة
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 7
PADDLE_SPEED = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# تهيئة pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()

# تعريف الكائنات
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
ball_dx, ball_dy = BALL_SPEED, BALL_SPEED
paddle_width, paddle_height = 20, 100
left_paddle = pygame.Rect(20, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
right_paddle = pygame.Rect(WIDTH - 20 - paddle_width, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)

def draw_objects():
    screen.fill(BLACK)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.rect(screen, RED, left_paddle)
    pygame.draw.rect(screen, BLUE, right_paddle)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

def move_ball():
    global ball_dx, ball_dy
    ball.x += ball_dx
    ball.y += ball_dy

    # تصادم مع الحواف
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    # تصادم مع الألواح
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_dx *= -1

    # كرة خارج الشاشة
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.x = WIDTH // 2 - 15
        ball.y = HEIGHT // 2 - 15
        ball_dx *= -1

def move_paddles(keys):
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED

# حلقة اللعبة الرئيسية
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    move_paddles(keys)
    move_ball()
    draw_objects()
    pygame.display.flip()
    clock.tick(60)

