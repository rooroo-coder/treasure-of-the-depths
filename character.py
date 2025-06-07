def handle_movement(keys, playerX, playerY, rows, cols):
    
    dx, dy = 0, 0

    
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        dy = -1
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        dy = 1
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        dx = -1
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        dx = 1

    # Update player position with boundary checks
    newX = max(0, min(cols - 1, playerX + dx))
    newY = max(0, min(rows - 1, playerY + dy))

    return newX, newY