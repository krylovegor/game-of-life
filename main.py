import pygame

pygame.init()
gameDisplay = pygame.display.set_mode((1000, 750))
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
gameDisplay.fill(white)
pygame.display.set_caption('Игра Жизнь')
finished = False


def get_next_generation(current_generation):
    def cell_sum(matrix, i, j):
        if i == 0 and j == 0:
            return matrix[0][1] + matrix[1][0] + matrix[1][1]
        elif i == 0 and j == len(matrix[0]) - 1:
            return matrix[0][j - 1] + matrix[1][j] + matrix[1][j - 1]
        elif i == len(matrix) - 1 and j == 0:
            return matrix[i - 1][0] + matrix[i][1] + matrix[i - 1][1]
        elif i == len(matrix) - 1 and j == len(matrix[i]) - 1:
            return matrix[i - 1][j] + matrix[i][j - 1] + matrix[i - 1][j - 1]
        elif i == 0:
            return matrix[0][j + 1] + matrix[0][j - 1] + \
                   matrix[1][j] + matrix[1][j + 1] + matrix[1][j - 1]
        elif j == 0:
            return matrix[i - 1][j] + matrix[i + 1][j] + \
                   matrix[i][j + 1] + matrix[i - 1][j + 1] + matrix[i + 1][j + 1]
        elif i == len(matrix) - 1:
            return matrix[i][j + 1] + matrix[i][j - 1] + \
                   matrix[i - 1][j] + matrix[i - 1][j + 1] + matrix[i - 1][j - 1]
        elif j == len(matrix[i]) - 1:
            return matrix[i - 1][j] + matrix[i + 1][j] + \
                   matrix[i][j - 1] + matrix[i - 1][j - 1] + matrix[i + 1][j - 1]
        else:
            return matrix[i - 1][j - 1] + matrix[i - 1][j] + matrix[i - 1][j + 1] + \
                   matrix[i][j - 1] + matrix[i][j + 1] + matrix[i + 1][j - 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]

    next_generation = [[current_generation[i][j] for j in range(len(current_generation[i]))]
                       for i in range(len(current_generation))]
    for i in range(len(current_generation)):
        for j in range(len(current_generation[i])):
            if current_generation[i][j] == 0 and cell_sum(current_generation, i, j) == 3:
                next_generation[i][j] = 1
            elif current_generation[i][j] == 1 and (cell_sum(current_generation, i, j) > 3 or
                                                    cell_sum(current_generation, i, j) < 2):
                next_generation[i][j] = 0
    return next_generation


def draw_next_generation(generation):
    for i in range(len(generation)):
        for j in range(len(generation[i])):
            if generation[i][j] == 1:
                pygame.draw.rect(gameDisplay, black, [i * 50, j * 50, 50, 50])
            else:
                pygame.draw.rect(gameDisplay, white, [i * 50, j * 50, 50, 50])


generation = [[0 for i in range(20)] for j in range(15)]
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = event.pos
            i = position[0] // 50
            j = position[1] // 50
            if event.button == 1:
                if generation[i][j] == 0:
                    generation[i][j] = 1
                    draw_next_generation(generation)
            elif event.button == 3:
                if generation[i][j] == 1:
                    generation[i][j] = 0
                    draw_next_generation(generation)
        elif event.key == pygame.K_SPACE:
            generation = [[0 for i in range(15)] for j in range(20)]
            draw_next_generation(generation)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                generation = get_next_generation(generation)
                draw_next_generation(generation)
    for x0 in range(0, 1000, 50):
        pygame.draw.line(gameDisplay, blue, (x0, 0), (x0, 750))
    for y0 in range(0, 750, 50):
        pygame.draw.line(gameDisplay, blue, (0, y0), (1000, y0))

    pygame.display.update()

pygame.quit()
