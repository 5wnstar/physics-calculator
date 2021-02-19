#EQUATION OF MOTION

import math

def velocity():
    u=float(input("Enter value for U:"))
    a=float(input("Enter value for A:"))
    t=float(input("Enter value for T:"))
    vel= (u + a*t)
    print ("Velocity is =", vel)
    return vel

def initial_velocity():
    u=float(input("Enter value for U:"))
    a=float(input("Enter value for A:"))
    s=float(input("Enter value for s:"))
    v= (math.sqrt(u*u + 2*a*s))
    print("initial velocity is =", v)
    return v

def distance():
    u=float(input("Enter value for U:"))
    a=float(input("Enter value for A:"))
    t=float(input("Enter value for T:"))
    s= (u*t  + (1/2)*a* pow(t, 2))
    print("Distance is =", s)
    return s

#PROJECTILE MOTION

def maximum_height():
    u=float(input("Enter value for u:"))
    g=float(input("Enter value for g:"))
    a=float(input("Enter the angle:"))
    m= math.sin(a)
    h=(u*m/g)
    print("maximum height is =", h)
    return h
    
def time_of_flight():
    u=float(input("Enter value for u:"))
    g=(9.8)
    a=float(input("Enter the angle:"))
    t=( (2*u)*(math.sin(a))/g)
    print("time of flight is =", t)
    return t

def Range():
    u=float(input("Enter value for u:"))
    g=(9.8)
    a=float(input("Enter the angle:"))
    m= math.sin(a)
    r=(  pow(u,2)*m/g)
    print("Range is =", r)
    return r

#CIRCULAR MOTION

def centripetal_acceleration():
    v=float(input("Enter velocity:"))
    r=float(input("Enter radius:"))
    c=( pow(v, 2)/r)
    print("centripetal acceleration is =", c)
    return c


def centripetal_force():
    m=float(input("Enter mass:"))
    v=float(input("Enter velocity:"))
    r=float(input("Enter radius:"))
    c=( m*pow(v, 2)/r)
    print("centripetal force is =", c)
    return c

def velocity_in_circular_motion():
    p=3.14
    r=float(input("Enter radius:"))
    t=float(input("Enter period:"))
    v=( 2*p*r)/t
    print("velocity in circular motion is =", v)
    return v

def frequency():
    t=float(input("Enter radius:"))
    f=( 1/t)
    print("frequency is =", f)
    return f

#WORK ENERGY AND POWER  

def workdone():
    f=float(input("Enter force:"))
    d=float(input("Enter distance:"))
    w=( f*d )
    print("workdone is =", w)
    return w

def workdone_with_angle():
    f=float(input("Enter force:"))
    d=float(input("Enter distance:"))
    a=float(input("Enter angle:"))
    w=( f*d*(math.cos(a)))
    print("workdone is =", w)
    return w

def potential_energy():
    m=float(input("Enter mass:"))
    g=(9.8)
    h=float(input("Enter height:"))
    p=( m*g*h)
    print("potential energy is =", p)
    return p

def kinetic_energy():
    m=float(input("Enter mass:"))
    v=float(input("Enter velocity:"))
    k=((1/2)*m*(pow(v,2)))
    print("kinectic energy is =", k)
    return k

def power():
    w=float(input("Enter workdone:"))
    t=float(input("Enter time:"))
    p=( w/t )
    print("power is =", p)
    return p


def energy():
    k=float(input("Enter value for kinetic energy:"))
    p=float(input("Enter value for potential energy:"))
    e=( k + p )
    print("energy is =", e)
    return e

# TORQUES AND ANGULAR MOMENTUM

def torque():
    r=float(input("Enter radius:"))
    f=float(input("Enter friction force:"))
    t=( r*f )
    print("torque is =", t)
    return t

def torque_with_angle():
    r=float(input("Enter radius:"))
    f=float(input("Enter friction force:"))
    a=float(input("Enter angle:"))
    t=( r*f *(math.sin(a) ))
    print("torque is =", t)

def angular_velocity():
    m=float(input("Enter mass:"))
    v=float(input("Enter velocity:"))
    r=float(input("Enter radius:"))
    a=( m*v*r )
    print("angular velocity is =", a)
    return a

def S_M_H():
    p=3.14
    l=float(input("Enter length:"))
    g=9.8
    s=( 2*p*(math.sqrt(l/g)))
    print("simple harmonic motion is =", s)
    return s
    


#ELECTRICITY AND MAGNETISM

def electric_field():
    f=float(input("Enter electric force:"))
    q=float(input("Enter external charge (q):"))
    e=( f/q )
    print("electric field is =", e)
    return e

    
def electric_potential():
    u=float(input("Enter electric potential energy:"))
    q=float(input("Enter external charge (q):"))
    e=( u/q )
    print("electric potential is =", e)
    return e


def electric_field_strength():
    k=float(input("Enter value for K:"))
    Q=float(input("Enter charge(Q):"))
    r=float(input("Enter distance charge:"))
    e=( k*Q/pow(r, 2) )
    print("electric field strength is =", e)
    return e

def electric_potential_energy():
    k=float(input("Enter value for K:"))
    Q=float(input("Enter charge(Q):"))
    q=float(input("Enter external charge(q):"))
    r=float(input("Enter distance charge:"))
    e= (k*Q*q/r )
    print("electric potential energy is =", e)
    return e

def electric_force():
    k=float(input("Enter value for K:"))
    Q=float(input("Enter charge(Q):"))
    q=float(input("Enter external charge(q):"))
    r=float(input("Enter distance charge:"))
    e=( k*Q*q/pow(r, 2) )
    print("electric force is =", e)
    return e

def potential_difference():
    r=float(input("Enter resistance:"))
    i=float(input("Enter current:"))
    p=( r*i )
    print("potential difference is =", p)
    return p

def power_in_electric():
    i=float(input("Enter current:"))
    v=float(input("Enter potential difference:"))
    p=( i*v )
    print("power in electric is =", p)
    return p

def current():
    q=float(input("Enter charge (q):"))
    t=float(input("Enter time :"))
    c=( q/t )
    print("current is =", c)
    return c

def resistance():
    p=float(input("Enter resistivity:"))
    l=float(input("Enter length:"))
    a=float(input("Enter Area:"))
    r=( p*l/a )
    print("resistance is =", r)
    return r

while True:
    

    print("""
            KIMATICS
        
1 : velocity
2 : initial velocity
3 : distance

        PROJETILE
        
4 : maximum height
5 : time of flight
6 : range

    CIRCULAR MOTION
    
7 : centripetal acceleration
8 : centripetal force
9 : velocity in circular motion
10: frequency

     WORK ENERGY AND POWER
     
11: workdone
12: workdone with angle
13: potential energy
14: kinectic energy
15: power
16: enrgy

        TORQUE AND ANGULAR MOMENTUM
17: torque
18: torque with angle
19: angular velocity
20: simple harmonic motion

    ELECTRICITY AND MAGNETISM

21: electric field
22: electric potential
23: electric field strength
24: electric force
25: potential difference
26: power in electric
27: current
28: resistance
29 : Quit
""")
    option=int(input("Enter your choice : "))
    if option ==1:
        velocity()   
        
    elif option ==2:
        initial_velocity()
        
    elif option ==3:
        distance()
        
    elif option ==4:
        maximum_height()

    elif option ==5:
        time_of_flight()
        
    elif option ==6:
        Range()

    elif option==7:
        centripetal_acceleration()
        
    elif option==8:
        centripetal_force()

    elif option==9:
        velocity_in_circular_motion()

    elif option==10:
        frequency()

    elif option==11:
        workdone()

    elif option==12:
        workdone_with_angle()

    elif option==13:
        potential_energy()

    elif option==14:
        kinectic_energy()

    elif option==15:
        power()

    elif option==16:
        energy()

    elif option==17:
        torque()

    elif option==18:
        torque_with_angle()

    elif option==19:
        angular_velocity()

    elif option==20:
        s.m.h()

    elif option==21:
        electric_field()

    elif option==22:
        electric_potential()

    elif option==23:
        electric_field_strength()

    elif option==24:
        electric_force()

    elif option==25:
        potential_difference()

    elif option==26:
        power_in_electric()

    elif option==27:
        current()

    elif option==28:
        resistance()
        
    elif option==29:
        break
    
    else:
        print("wrong option")

