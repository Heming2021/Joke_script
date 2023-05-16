import rotatescreen
import time

time.sleep(2)

screen = rotatescreen.get_primary_display()
start_pos = screen.current_orientation

for i in range(1,257):
    pos = abs((start_pos - i*90) % 360)
    screen.rotate_to(pos)
    time.sleep(0.01)