def test_plane_wall(plane , wall):
    if plane.getX() - plane.dim <= -wall:
        plane.setX(-wall + plane.dim) 

    if plane.getX() + plane.dim >= wall:
        plane.setX(wall - plane.dim) 

    if plane.y + plane.dim >= wall:
        plane.setY(wall - plane.dim) 

    if plane.y - plane.dim <= -wall:
        plane.setY(-wall + plane.dim) 

def test_plane_bullet(plane , b):
    if b.BulletX <= plane.getX() + plane.dim and b.BulletX >= plane.getX() - plane.dim:
        if b.BulletY <= plane.getY() + plane.dim and b.BulletY >= plane.getY() - plane.dim:
            return True

def test_alien_bullet(alien, b):
     if b.BulletX <= alien.getX() + alien.dim and b.BulletX >= alien.getX() - alien.dim:
        if b.BulletY <= alien.getY() + alien.dim and b.BulletY >= alien.getY() - alien.dim:
            return True

def test_alien_plane(alien , plane):
     if alien.getX() - alien.dim <= plane.getX() + .6 and alien.getX() + alien.dim >= plane.getX() - .6:
        if alien.getY() - alien.dim <= plane.getY() +.6  and alien.getY() + alien.dim >= plane.getY() -.6 :
            return True            