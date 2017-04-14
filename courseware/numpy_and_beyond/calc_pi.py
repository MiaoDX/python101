# calc PI

def get_two_num(ran_g):
    return ran_g.uniform(-1, 1), ran_g.uniform(-1, 1)

def get_two_num_generator(ran_g, itr_num):
    for i in range(itr_num):
        yield ran_g.uniform(-1, 1), ran_g.uniform(-1, 1)


def in_circle(x,y):
    return x*x + y*y <= 1

def calc_pi():
    import random
    
    ran_g = random
    ran_g.seed(42)

    play_time = int(1e4)
    
    in_circle_time = 0

    for i in range(play_time):
        x,y = get_two_num(ran_g)
        #print(x,y)
        if in_circle(x,y):
            in_circle_time += 1
    
    # rg = get_two_num_generator(ran_g, play_time)
    # for x,y in rg:
    #     if in_circle(x,y):
    #         in_circle_time += 1



    return in_circle_time/play_time*4


def test_g():
    import random

    ran_g = random
    ran_g.seed(42)
    rg = get_two_num_generator(ran_g, 10)

    for x,y in rg:
        print(x,y)

if __name__ == '__main__':
    import datetime
    start = datetime.datetime.now()
    ans =  calc_pi()
    print(ans)
    end = datetime.datetime.now()
    print('total time: ', (end - start).total_seconds() )

    #test_g()