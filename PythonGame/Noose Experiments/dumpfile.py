
    for event in pg.event.get():
        if event.type==pg.QUIT:
            sys.exit()

        accel = 0.01
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                if P1.speed[0] < 1:
                    P1.speed[0]+=accel
            if event.key == pg.K_LEFT:
                if P1.speed[0] > -1:
                    P1.speed[0]-=accel
            if event.key == pg.K_UP: 
                if P1.speed[1] > -1:
                    P1.speed[1]-=accel
            if event.key == pg.K_DOWN:
                if P1.speed[1] < 1:
                    P1.speed[1]+=accel

    pressed = pg.key.get_pressed()
        if pressed