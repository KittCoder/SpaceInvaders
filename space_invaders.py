import pygame
import random
import math

pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Set the Background
background = pygame.image.load('./Resources/background.png')
# Set the Background Sound
backgroundsound = pygame.mixer.Sound('./Resources/background.wav')
backgroundsound.play(-1)
# Set the caption and the icon
pygame.display.set_caption('Space Invaders')
# I can go to Flaticon.com for more icons
icon = pygame.image.load('./Resources/ufo.png')
pygame.display.set_icon(icon)

# Set up player
playerimg = pygame.image.load('./Resources/player.png')
playerx = 400
playery = 480
playerx_change = 0

# Set up bullet
bulletIMG = pygame.image.load('./Resources/bullet.png')
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 10
bullet_state = 'ready'
# Set up the enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('./resources/enemy.png'))
    enemyX.append(random.randint(0, 740))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)
# Set the Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Draw the Game Over Screen
over_font = pygame.font.Font('freesansbold.ttf', 64)
# Draw the player
def player(x,y):
    screen.blit(playerimg,(x,y))
# Draw the enemy
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
# Draw the bullet
def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletIMG,(x+15,y+10))
# Define a collision function for bullet/enemy collisions
def isCollision(enemyX, enemyY, bulletx, bullety):
    distance = math.sqrt(math.pow(enemyX-bulletx, 2) + math.pow(enemyY - bullety, 2))
    if distance < 25:
        return True
    return False
def show_score(tx,ty):
    score = font.render(f'Score: {score_value}', True, (255,255,255))
    screen.blit(score,(tx, ty))

def game_over_text():
    over_text = over_font.render('GAME OVER', True, (255,255,255))
    screen.blit(over_text, (200,250))
# Setup game loop
running = True
while running:
    # Set the default background
    screen.fill((0, 0, 0))
     # Set the Background Image
    screen.blit(background,(0,0))
    # Manage events
    for event in pygame.event.get():
        # Process the quit event
        if event.type == pygame.QUIT:
            running = False
        # Process right and left movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -2
            elif event.key == pygame.K_RIGHT:
                playerx_change = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
                playerx_change = 0
        # Process bullet
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bulletsound = pygame.mixer.Sound('./Resources/laser.wav')
                    bulletsound.play()
                    bulletx = playerx
                    fire_bullet(bulletx, bullety)
                    

    # player movement
    playerx += playerx_change
    if playerx <=0:
        playerx = 0
    elif playerx >= 740:
        playerx = 740
    # bullet movement 
    if bullety <= 0:
        bullety = 480
        bullet_state = 'ready'
    
    if bullet_state == 'fire':
        bullety -= bullety_change
        fire_bullet(bulletx, bullety)
    
    if bullet_state == 'fire':
        bullety -= bullety_change    
        fire_bullet(bulletx, bullety)
    # enemy movement
    for i in range(num_of_enemies):
        
        # Process Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        
        enemyX[i] += enemyX_change[i]
        
        if enemyX[i] <= 0:
            enemyX_change[i] = 4 
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 740:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]
        collision = isCollision(enemyX[i], enemyY[i], bulletx, bullety)
        if collision:
            explosionsound = pygame.mixer.Sound('./Resources/explosion.wav')
            explosionsound.play()
            bullet_state = 'ready'
            bullety = 480
            
            enemyX[i] = random.randint(0,740)
            enemyY[i] = random.randint(50,150)
            
            score_value += 1
        # draw the enemy
        enemy(enemyX[i], enemyY[i], i)
        
    player(playerx,playery) 
    show_score(textX, textY)       
    # Update Screen
    pygame.display.update()
    

pygame.quit()