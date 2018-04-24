import math as m

home_angs = [0, 0, 0]
default_angs = [0, m.pi/4, m.pi/4]
camera_angs = [0, m.pi/4, m.pi/4]

HOME_POS={'pts':[0.374, 0, 0.630],'angs':home_angs}

HOME_LASER_POS={'pts':[0.0, 0.255, 0.650],'angs':default_angs}

TEST_LINE={'pts':[[0.48,0.0,0.1],[0.53,0.0,0.1],[0.48,0.0,0.1],[0.53,0.0,0.1]],'angs':default_angs}

TEST_SQUARE={'pts':[[0.5,0.0,0.1],[0.5,0.04,0.1],[0.46,0.04,0.1],[0.46,0.0,0.1],[0.5,0.0,0.1],[0.5,0.04,0.1],[0.46,0.04,0.1],[0.46,0.0,0.1]],'angs':default_angs}