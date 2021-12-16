def ar_circle(radius):
    a=3.14*radius**2
    p=2*3.14*radius
    return(a,p)

radius=int(input())
out=ar_circle(radius)
print(out)
