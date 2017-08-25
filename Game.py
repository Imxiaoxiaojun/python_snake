# -*- coding: utf-8 -*-
from Board import Board
from Snake import Snake
from Food import Food
import pygame
import copy
from Utils import Utils


class Game(object):
    board = Board()
    snake = Snake()
    food = Food()
    direction_flag = 'R'

    def __init__(self):
        pass
        # self.new_food()
        # self.board.clear()
        # self.board.put_snake(self.snake.getPoints())
        # self.board.put_food(self.food)

    def run(self):
        while True:
            frame_rate = pygame.time.Clock().tick(20)
            self.board = Board()
            # 检测例如按键等pygame事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.direction_flag = 'R'
                    elif event.key == pygame.K_LEFT:
                        self.direction_flag = 'L'
                    elif event.key == pygame.K_UP:
                        self.direction_flag = 'U'
                    elif event.key == pygame.K_DOWN:
                        self.direction_flag = 'D'

            food_position = copy.deepcopy(self.food.food_list())
            # food_position[0] += 20
            # food_position[1] += 20
            food_image = Utils.load_image('food.png').convert()
            self.board.screen.blit(food_image, (food_position[0], food_position[1]))

            snake_position = self.snake.pos_list
            for pos in snake_position:
                snake_head = Utils.load_image('snake_head.png').convert()
                self.board.screen.blit(snake_head, (pos[0], pos[1]))
                if len(snake_position) > 1:
                    snake_image = Utils.load_image('snake_head.png').convert()
                    self.board.screen.blit(snake_image, (pos[0], pos[1]))


                # pygame.draw.rect(self.self.board.screen, (255, 0, 0), temp_rect)
            pygame.display.update()
            snake_head = snake_position[0]

            if self.direction_flag == 'R':
                if snake_head[0] < 560:
                    self.snake.change_direction(self.direction_flag)
                    self.snake.move_direction()
                else:
                    self.direction_flag = 'D'
            elif self.direction_flag == 'D':
                if snake_head[1] < 400:
                    self.snake.change_direction(self.direction_flag)
                    self.snake.move_direction()
                else:
                    self.direction_flag = 'L'
            elif self.direction_flag == 'L':
                if snake_head[0] > 20:
                    self.snake.change_direction(self.direction_flag)
                    self.snake.move_direction()
                else:
                    self.direction_flag = 'U'
            elif self.direction_flag == 'U':
                if snake_head[1] > 20:
                    self.snake.change_direction(self.direction_flag)
                    self.snake.move_direction()
                else:
                    self.direction_flag = 'R'

            if snake_head == food_position:
                self.snake.eat_food(food_position)
                self.food.update_food()
            # if x < 5:
            #     x += 1
            # else:
            #     x = 0

if __name__ == '__main__':
    Game().run()
