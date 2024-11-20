#pip install pygame
import pygame
import random
import time

# 초기화
pygame.init()

# 상수 정의
BLOCK_SIZE = 30
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
SCREEN_WIDTH = BLOCK_SIZE * BOARD_WIDTH
SCREEN_HEIGHT = BLOCK_SIZE * BOARD_HEIGHT

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (128, 128, 128)

# 화면 설정
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("테트리스")

# 테트리스 블록 모양 정의
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]]  # Z
]

class Tetris:
    def __init__(self):
        self.board = [[0 for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
        self.current_piece = None
        self.current_x = 0
        self.current_y = 0
        self.score = 0
        self.game_over = False
        self.new_piece()

    def new_piece(self):
        self.current_piece = random.choice(SHAPES)
        self.current_x = BOARD_WIDTH // 2 - len(self.current_piece[0]) // 2
        self.current_y = 0

        if self.check_collision():
            self.game_over = True

    def rotate_piece(self):
        rows = len(self.current_piece)
        cols = len(self.current_piece[0])
        rotated = [[self.current_piece[rows-1-j][i] for j in range(rows)] for i in range(cols)]
        
        old_piece = self.current_piece
        self.current_piece = rotated
        
        if self.check_collision():
            self.current_piece = old_piece

    def check_collision(self):
        for y in range(len(self.current_piece)):
            for x in range(len(self.current_piece[y])):
                if self.current_piece[y][x]:
                    new_x = self.current_x + x
                    new_y = self.current_y + y
                    
                    if (new_x < 0 or new_x >= BOARD_WIDTH or 
                        new_y >= BOARD_HEIGHT or 
                        (new_y >= 0 and self.board[new_y][new_x])):
                        return True
        return False

    def merge_piece(self):
        for y in range(len(self.current_piece)):
            for x in range(len(self.current_piece[y])):
                if self.current_piece[y][x]:
                    self.board[self.current_y + y][self.current_x + x] = 1
        self.clear_lines()
        self.new_piece()

    def clear_lines(self):
        lines_cleared = 0
        y = BOARD_HEIGHT - 1
        while y >= 0:
            if all(self.board[y]):
                del self.board[y]
                self.board.insert(0, [0 for _ in range(BOARD_WIDTH)])
                lines_cleared += 1
            else:
                y -= 1
        self.score += lines_cleared * 100

    def draw(self):
        screen.fill(BLACK)
        
        # 보드 그리기
        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                if self.board[y][x]:
                    pygame.draw.rect(screen, GRAY,
                                   [x * BLOCK_SIZE, y * BLOCK_SIZE,
                                    BLOCK_SIZE - 1, BLOCK_SIZE - 1])

        # 현재 조각 그리기
        if self.current_piece:
            for y in range(len(self.current_piece)):
                for x in range(len(self.current_piece[y])):
                    if self.current_piece[y][x]:
                        pygame.draw.rect(screen, RED,
                                       [(self.current_x + x) * BLOCK_SIZE,
                                        (self.current_y + y) * BLOCK_SIZE,
                                        BLOCK_SIZE - 1, BLOCK_SIZE - 1])

        # 점수 표시
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {self.score}', True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

def main():
    game = Tetris()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.5  # 초당 한 칸씩 떨어짐

    while not game.game_over:
        current_time = time.time()
        delta_time = current_time - fall_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.current_x -= 1
                    if game.check_collision():
                        game.current_x += 1
                elif event.key == pygame.K_RIGHT:
                    game.current_x += 1
                    if game.check_collision():
                        game.current_x -= 1
                elif event.key == pygame.K_DOWN:
                    game.current_y += 1
                    if game.check_collision():
                        game.current_y -= 1
                        game.merge_piece()
                elif event.key == pygame.K_UP:
                    game.rotate_piece()

        if delta_time > fall_speed:
            game.current_y += 1
            if game.check_collision():
                game.current_y -= 1
                game.merge_piece()
            fall_time = current_time

        game.draw()
        clock.tick(60)

    # 게임 오버 화면
    font = pygame.font.Font(None, 48)
    game_over_text = font.render('Game Over!', True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2))
    pygame.display.flip()
    pygame.time.wait(2000)

if __name__ == '__main__':
    main()
    pygame.quit()