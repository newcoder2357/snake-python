from pygame import font
import pygame
import pygame.display 
import graphic
import random
import setting 
import login
import radio
import display_number
from functions import Rect, Circle, line
from time import sleep
from collections import defaultdict


pygame.init()

fhead = defaultdict(lambda: None)
ftail = defaultdict(lambda: None)
fbody = defaultdict(int)

fhead[(0, -1)], fhead[(0, 1)], fhead[(-1, 0)], fhead[(1, 0)] = 0, 1, 2, 3
ftail[(0, -1)], ftail[(0, 1)], ftail[(-1, 0)], ftail[(1, 0)] = 0, 1, 2, 3
fbody[(1, 0, 0, 1)], fbody[(0, 1, 1, 0)], fbody[(0, 1, -1, 0)], fbody[(-1, 0, 0, 1)], fbody[(1, 0, 0, -1)], fbody[(0, -1, 1, 0)], fbody[(-1, 0, 0, -1)], fbody[(0, -1, -1, 0)], fbody[(1, 0, -1, 0)], fbody[(-1, 0, 1,0)], fbody[(0, -1, 0, 1)], fbody[(0, 1, 0, -1)] = 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5

# Màu sắc
blue = (30,144,255)
red = (255,0,0)
slate_gray = (112,128,144)
saddle = (139,69,19)
black = (0, 0, 0)
white = (255, 255, 255)
tomato = (255,99,71)
aqua = (0,255,255)

delta = [[0, -1], [0, 1], [-1, 0], [1, 0]]
cell = 20

init_snakes = [ [[1, 33], [1, 32], [1, 31]], [[58, 33], [58, 32], [58, 31]]]

Font_name = pygame.font.Font(None, 80)

# Khởi tạo các biến global
snakes = init_snakes[0][:]
snakes2 = init_snakes[1][:]
apple_x, apple_y = 0, 0
direc = [-1, -1]
save = []
mark = defaultdict(bool)
point = [0, 0]
cube_point = None
cube_time = None
img_name = None 
img_name2 = None # [ADDED] Thêm biến hình ảnh cho tên Player 2

# ======================================================================
# CÁC HÀM CƠ CHẾ
# ======================================================================

def prepare_nickname(Name1, Name2):
    global img_name, img_name2
    # Render cả 2 tên
    img_name = Font_name.render(Name1, True, (255, 255, 255))
    img_name2 = Font_name.render(Name2, True, (255, 255, 255))

def draw_snake(dis, snakes, HeadSet, TailSet, BodySet):
    # HÀM ĐÃ ĐƯỢC CẬP NHẬT ĐỂ NHẬN BỘ HÌNH ẢNH LÀM THAM SỐ
    cell = 20
    global fhead, ftail, fbody
    
    for i in range(len(snakes)):
        snake = snakes[i]
        
        # Chỉ vẽ nếu độ dài rắn > 1
        if len(snakes) > 1:
            if i == 0: # Vẽ Tail
                dx, dy = snakes[1][0] - snake[0], snakes[1][1] - snake[1]
                dis.blit(TailSet[ftail[(dx, dy)]], (snake[0] * cell, snake[1] * cell))
            elif i == len(snakes) - 1: # Vẽ Head
                tmp_id = len(snakes) - 2
                dx, dy = snake[0] - snakes[tmp_id][0], snake[1] - snakes[tmp_id][1]
                dis.blit(HeadSet[fhead[(dx, dy)]], (snake[0] * cell, snake[1] * cell))
            elif 0 < i < len(snakes) - 1: # Vẽ Body
                last, nxt = i - 1, i + 1
                d1x, d1y, d2x, d2y = snake[0] - snakes[last][0], snake[1] - snakes[last][1], snake[0] - snakes[nxt][0], snake[1] - snakes[nxt][1]
                
                key = (d1x, d1y, d2x, d2y)
                if key in fbody:
                    dis.blit(BodySet[fbody[key]], (snake[0] * cell, snake[1] * cell))
                elif (-d1x, -d1y, -d2x, -d2y) in fbody:
                    dis.blit(BodySet[fbody[(-d1x, -d1y, -d2x, -d2y)]], (snake[0] * cell, snake[1] * cell))
        else: # Vẽ rắn có độ dài <= 1
            dis.blit(HeadSet[0], (snake[0] * cell, snake[1] * cell))


def draw_point(dis):
    global point, cube_point
    
    # [EDITED] Chỉnh sửa tọa độ để đối xứng qua trung tâm (x=600)
    # P1 nằm bên trái, P2 nằm bên phải, cách trung tâm một khoảng đều nhau
    
    # Hiển thị điểm Người chơi 1 (P1) - Tọa độ khoảng x=445 và x=500
    display_number.draw_num(dis, (445, 5), point[0] // 10, 15, cube_point)
    display_number.draw_num(dis, (500, 5), point[0] % 10, 15, cube_point)
    
    # Hiển thị điểm Người chơi 2 (P2) - Tọa độ khoảng x=700 và x=755
    display_number.draw_num(dis, (700, 5), point[1] // 10, 15, cube_point)
    display_number.draw_num(dis, (755, 5), point[1] % 10, 15, cube_point)
    
    # Cập nhật vùng hiển thị điểm (Update lại rect theo tọa độ mới)
    pygame.display.update([445, 5, 100, 75])
    pygame.display.update([700, 5, 100, 75]) 


def reset(snakes, Id):
    minx, maxx, miny, maxy = 1200, 0, 750, 0
    for snake in snakes:
        maxx = max(maxx, snake[0])
        maxy = max(maxy, snake[1])
        minx = min(minx, snake[0])
        miny = min(miny, snake[1])
    snakes[:] = init_snakes[Id]
    
    save.append([minx * cell, miny * cell, (maxx - minx + 1) * cell, (maxy - miny + 1) * cell])
    #save.append([snakes[-1][0] * cell, snakes[-1][1] * cell, 40, 80])

    

def move_snake(dis, snakes, other_snakes, point, Id):
    save.append([(snakes[0][0] - 1) * cell, (snakes[0][1] - 1) * cell, cell * 3, cell * 3])
    save.append([(snakes[-1][0] - 1) * cell, (snakes[-1][1] - 1) * cell, cell * 3, cell * 3])
    global apple_x, apple_y, direc
    
    if direc[Id] == -1:
        return
    
    # Vị trí đầu mới
    new_head = [snakes[-1][0] + delta[direc[Id]][0], snakes[-1][1] + delta[direc[Id]][1]]
    snakes.append(new_head)
    
    # 1. Va chạm với Tường/Vật cản HOẶC Va chạm với thân mình
    if mark[(new_head[0], new_head[1])] == True:
        radio.touchfence.play()
        reset(snakes, Id)
        direc[Id] = -1
        point[Id] = max(0, point[Id] - 1)
        draw_point(dis)
        return

    # 2. Va chạm với Rắn khác
    if (new_head in other_snakes):
        radio.touchfence.play()
        reset(snakes, Id)
        direc[Id] = -1
        point[Id] = max(0, point[Id] - 1)
        draw_point(dis)
        return

    # ĂN MỒI
    if apple_x == new_head[0] and apple_y == new_head[1]:
        point[Id] += 1
        radio.farm[random.randint(0, 4)].play()
        
        # Tạo táo mới
        while True:
            apple_x = random.randint(1, 58)
            apple_y = random.randint(6, 33)
            if (mark[(apple_x, apple_y)] == False and 
                [apple_x, apple_y] not in snakes and 
                [apple_x, apple_y] not in other_snakes):
                break
        
        draw_point(dis)
    else:
        # Nếu không ăn, pop đuôi
        snakes.pop(0)


# ======================================================================
# VÒNG LẶP CHÍNH (Hàm play)
# ======================================================================

def play(dis, Fence, Name, Name2):
    radio.playing.play()
    graphic.load_image() # Cần đảm bảo load_image() đã load cả các hình ảnh có đuôi '2'
    
    DECLINE = 90
    prepare_nickname(Name, Name2) # [EDITED] Truyền cả 2 tên vào
    
    # KHỞI TẠO BỘ HÌNH ẢNH RẮN 1 (P1)
    Head1 = [graphic.head_up, graphic.head_down, graphic.head_left, graphic.head_right]
    Tail1 = [graphic.tail_down, graphic.tail_up, graphic.tail_right, graphic.tail_left]
    Body1 = [graphic.body_topleft, graphic.body_topright, graphic.body_bottomleft, graphic.body_bottomright, graphic.body_horizontal, graphic.body_vertical]

    # KHỞI TẠO BỘ HÌNH ẢNH RẮN 2 (P2)
    Head2 = [graphic.head_up2, graphic.head_down2, graphic.head_left2, graphic.head_right2]
    Tail2 = [graphic.tail_down2, graphic.tail_up2, graphic.tail_right2, graphic.tail_left2]
    Body2 = [graphic.body_topleft2, graphic.body_topright2, graphic.body_bottomleft2, graphic.body_bottomright2, graphic.body_horizontal2, graphic.body_vertical2]

    global cube, cube_time, cube_point
    cube = pygame.transform.scale(graphic.cube, (20, 20))
    cube_point = pygame.transform.scale(graphic.cube, (15, 15))
    cube_time = pygame.transform.scale(graphic.cube, (8, 8))

    clock = pygame.time.Clock()
    clock.tick(60)
    SNAKE_MOVE = pygame.USEREVENT + 1
    DEC_TIME = pygame.USEREVENT + 2
    pygame.time.set_timer(SNAKE_MOVE, 120)
    pygame.time.set_timer(DEC_TIME, 1000)
    
    
    # Khởi tạo dữ liệu
    global snakes, snakes2, apple_x, apple_y, delta, direc, cell, save, mark, point
    snakes = init_snakes[0][:]
    snakes2 = init_snakes[1][:]

    save = []
    direc = [-1, -1]
    point = [0, 0]

    mark = defaultdict(bool)
    for [x, y] in Fence:
        mark[(x, y)] = True

    # Tạo táo ban đầu
    while True:
        apple_x = random.randint(1, 58)
        apple_y = random.randint(6, 33)
        if (mark[(apple_x, apple_y)] == False and 
            [apple_x, apple_y] not in snakes and 
            [apple_x, apple_y] not in snakes2):
            break
    
    runing = True    
    load_map = False
    pygame.event.set_allowed(None) 
    
    while runing:
        dis.fill(black)
        
        # VẼ MAP
        for pos in Fence:
            dis.blit(cube, (pos[0] * cell, pos[1] * cell))
        for i in range(61):
            line(dis, aqua, (i * cell, 100), (i * cell, 700), 1)
        for i in range(31):
            line(dis, aqua, (0, i * cell + 100), (1200, i * cell + 100), 1)
        
        # VẼ VIỀN
        line(dis, aqua, (0, 1), (1200, 1), 2)
        line(dis, aqua, (0, 1), (0, 100), 2)
        line(dis, aqua, (1200, 1), (1200, 100), 2)
        line(dis, aqua, (0, 700), (0, 800), 2)
        line(dis, aqua, (1200, 650), (1200, 750), 2)
        line(dis, aqua, (0, 750), (1200, 750), 2)
        line(dis, aqua, (400, 700), (500, 750), 2)
        line(dis, aqua, (800, 700), (700, 750), 2)
        line(dis, aqua, (500, 750), (700, 750), 2)
        
        # [EDITED] HIỂN THỊ TÊN NGƯỜI CHƠI ĐỐI XỨNG
        # Tên P1 ở bên trái
        dis.blit(img_name, (20, 10)) 
        
        # Tên P2 ở bên phải (Tính tọa độ x = Chiều rộng màn hình - độ dài chữ - lề phải)
        name2_width = img_name2.get_width()
        dis.blit(img_name2, (1200 - name2_width - 20, 10))

        draw_point(dis)
        
        if load_map == False:
            pygame.display.flip()
            load_map = True
        
        # VẼ APPLE VÀ RẮN
        dis.blit(graphic.apple, (apple_x * cell, apple_y * cell))
        save.append([apple_x * cell, apple_y * cell, cell, cell])
        
        # GỌI HÀM VẼ VỚI BỘ HÌNH ẢNH ĐẶC TRƯNG
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            if not runing:
                break
                
            if event.type == pygame.KEYDOWN:
                # Điều khiển Người chơi 1 (A, W, S, D)
                if event.key == pygame.K_w and direc[0] != 1:
                    direc[0] = 0
                if event.key == pygame.K_s and direc[0] != 0 and direc[0] != -1:
                    direc[0] = 1
                if event.key == pygame.K_a and direc[0] != 3:
                    direc[0] = 2
                if event.key == pygame.K_d and direc[0] != 2:
                    direc[0] = 3

                # Điều khiển Người chơi 2 (Mũi tên)
                if event.key == pygame.K_UP and direc[1] != 1:
                    direc[1] = 0
                if event.key == pygame.K_DOWN and direc[1] != 0 and direc[1] != -1:
                    direc[1] = 1
                if event.key == pygame.K_LEFT and direc[1] != 3:
                    direc[1] = 2
                if event.key == pygame.K_RIGHT and direc[1] != 2:
                    direc[1] = 3

            # Logic di chuyển
            if event.type == SNAKE_MOVE:
                move_snake(dis, snakes, snakes2, point, 0)
                draw_snake(dis, snakes, Head1, Tail1, Body1)
                move_snake(dis, snakes2, snakes, point, 1)
                draw_snake(dis, snakes2, Head2, Tail2, Body2)
            
            # Logic đếm ngược thời gian
            if event.type == DEC_TIME and DECLINE > 0:
                DECLINE -= 1
                display_number.draw_num(dis, (570, 705), DECLINE // 10, 8, cube_time)
                display_number.draw_num(dis, (606, 705), DECLINE % 10, 8, cube_time)
                pygame.display.update([570, 705, 70, 40])
                if DECLINE == 0:
                    runing = False
                    
        # Cập nhật màn hình
        while len(save):
            pygame.display.update(save[-1])
            save.pop()
            
    pygame.time.set_timer(SNAKE_MOVE, 0)
    pygame.time.set_timer(DEC_TIME, 0)
    radio.playing.stop()
    
    return point[0] 

# ======================================================================
# KHỐI LỆNH CHÍNH (ĐỂ CHẠY GAME)
# ======================================================================

if __name__ == "__main__":
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800
    dis = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game - 2 Players") 

    # Thiết lập Tường/Vật cản
    Fence = []
    for i in range(61): 
        Fence.append([i, 5])
        Fence.append([i, 35])
    for i in range(6, 35): 
        Fence.append([0, i])
        Fence.append([60, i])

    name1 = "Player 1" 
    name2 = "Player 2"
    final_score = play(dis, Fence, name1, name2)
    print(f"Game Over. P1 Score: {point[0]}, P2 Score: {point[1]}") 
    
    pygame.quit()