import svgwrite
import os
#How this is gonna work:
#Input interior length, width, height, the program first makes the inner box, then the bottom, then the top
global current_y
global current_x
current_y=0
current_x=0

def dent(drwing,ceerf,woood,dir):
    global current_x
    global current_y
    if dir=="up":
        drwing.add(drwing.line((current_x,current_y),(current_x,current_y-(ceerf+woood)),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_y=current_y-(woood+ceerf)
    elif dir=="down":
        drwing.add(drwing.line((current_x,current_y),(current_x,current_y+(ceerf+woood)),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_y=current_y+(woood+ceerf)
    elif dir=="left":
        drwing.add(drwing.line((current_x,current_y),(current_x-(woood+ceerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_x=current_x-(woood+ceerf)
    elif dir=="right":
        drwing.add(drwing.line((current_x,current_y),(current_x+(woood+ceerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_x=current_x+(woood+ceerf)
    else:
        print("Error: Invalid Dent Input")
        exit()
def tab(drwing,ceerf,dir,desc,tabb):
    global current_x
    global current_y
    distance=0
    if desc=="in":
        distance=tabb-ceerf
    elif desc=="out":
        distance=tabb+ceerf
    else: 
        print("Error: Invalid Tab In/Out")
    if dir == "up":
        drwing.add(drwing.line((current_x,current_y),(current_x,current_y-distance),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_y=current_y-distance
    elif dir == "down":
        drwing.add(drwing.line((current_x,current_y),(current_x,current_y+distance),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_y=current_y+distance
    elif dir == "left":
        drwing.add(drwing.line((current_x,current_y),(current_x-distance,current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_x=current_x-distance
    elif dir == "right":
        drwing.add(drwing.line((current_x,current_y),(current_x+distance,current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_x=current_x+distance
def corner(drwing,ceerf,woood,dir1,dir2):
    global current_x
    global current_y
    dent(drwing,ceerf,woood,dir1)
    dent(drwing,ceerf,woood,dir2)
def righthand_side(dwg,cerf,wood,num,make):
    for x in range((int(num)//2)):
        dent(dwg,cerf,wood,"right")
        tab(dwg,cerf,"down","out",make)
        dent(dwg,cerf,wood,"left")
        tab(dwg,cerf,"down","in",make)
def lefthand_side(dwg,cerf,wood,num,make):
    for x in range(int(num)//2):
        dent(dwg,cerf,wood,"left")
        tab(dwg,cerf,"up","out",make)
        dent(dwg,cerf,wood,"right")
        tab(dwg,cerf,"up","in",make)
def downhand_side(dwg,cerf,wood,num,make):   
    for x in range(int(num)//2):
        dent(dwg,cerf,wood,"down")
        tab(dwg,cerf,"left","out",make)
        dent(dwg,cerf,wood,"up")
        tab(dwg,cerf,"left","in",make)
def uphand_side(dwg,cerf,wood,num,make):
    for x in range(int(num)//2):
        dent(dwg,cerf,wood,"up")
        tab(dwg,cerf,"right","out",make)
        dent(dwg,cerf,wood,"down")
        tab(dwg,cerf,"right","in",make)
def centre_left(dwg,cerf,wood,num,make):
    for x in range(int(num)//2):
        tab(dwg,cerf,"up","in",make)
        dent(dwg,cerf,wood,"right")
        tab(dwg,cerf,"up","out",make)
        dent(dwg,cerf,wood,"left")
def centre_right(dwg,cerf,wood,num,make):
    for x in range(int(num)//2):
        tab(dwg,cerf,"down","out",make)
        dent(dwg,cerf,wood,"left")
        tab(dwg,cerf,"down","in",make)
        dent(dwg,cerf,wood,"right")
def centre_top(dwg,cerf,wood,num,make):
    for x in range(int(num)//2):
        tab(dwg,cerf,"right","out",make)
        dent(dwg,cerf,wood,"down")
        tab(dwg,cerf,"right","in",make)
        dent(dwg,cerf,wood,"up")
def centre_bottom(dwg,cerf,wood,num,make):
    for x in range(int(num)//2):
        tab(dwg,cerf,"left","out",make)
        dent(dwg,cerf,wood,"up")
        tab(dwg,cerf,"left","in",make)
        dent(dwg,cerf,wood,"down")
def loong(dwg,side,make):
    global current_x
    global current_y
    if side=="uphand":
        dwg.add(dwg.line((current_x,current_y),(current_x+make,current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_x=current_x+make
    elif side=="downhand":
        dwg.add(dwg.line((current_x,current_y),(current_x-make,current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_x=current_x-make
    elif side=="righthand":
        dwg.add(dwg.line((current_x,current_y),(current_x,current_y+make),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_y=current_y+make
    elif side=="lefthand":
        dwg.add(dwg.line((current_x,current_y),(make,current_y-make),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_y=current_y-make
    


def inside(inner_length,inner_width,inner_height,wood,cerf,nameo):
    #Makes the inner box
    length_tab_make=inner_length
    length_tab_done=False
    while length_tab_done==False:
        if length_tab_make>6:
            length_tab_make=length_tab_make/4
        elif length_tab_make<3:
            length_tab_make=length_tab_make*2
        if 3<=length_tab_make<=6:
            length_tab_done=True
    len_number=inner_length/length_tab_make
    
    width_tab_make=inner_width
    width_tab_done=False
    while width_tab_done==False:
        if width_tab_make>6:
            width_tab_make=width_tab_make/4
        elif width_tab_make<3:
            width_tab_make=width_tab_make*2
        if 3<=width_tab_make<=6:
            width_tab_done=True
    wid_number=inner_width/width_tab_make

    height_tab_make=inner_height
    height_tab_done=False
    while height_tab_done==False:
        if height_tab_make>6:
            height_tab_make=height_tab_make/4
        elif height_tab_make<3:
            height_tab_make=height_tab_make*2
        if 3<=height_tab_make<=6:
            height_tab_done=True
    height_number=inner_height/height_tab_make

    global current_x
    global current_y
    current_x=wood+cerf
    current_y=0


    dwg = svgwrite.Drawing(nameo+' Inside.svg', profile='tiny',size=('450mm','600mm'))
    for x in range(2):
        current_x=x*(inner_length+(wood*4)+(cerf*2))
        #Length*height
        loong(dwg,"uphand",inner_length)
        righthand_side(dwg,cerf,wood,height_number,height_tab_make)
        downhand_side(dwg,cerf,wood,len_number,length_tab_make)
        lefthand_side(dwg,cerf,wood,height_number,height_tab_make)

    #Width*height
    for x in range(2):
        current_x=x*(inner_height+wood*2+cerf*2)
        current_y=-1*(inner_width+wood*3+cerf*2)
        uphand_side(dwg,cerf,wood,height_number,height_tab_make)
        loong(dwg,"righthand",inner_width)
        downhand_side(dwg,cerf,wood,height_number,height_tab_make)
        lefthand_side(dwg,cerf,wood,wid_number,width_tab_make)
        

    #Length*width
    for x in range(1):
        current_x=2*(inner_length+(wood*4)+(cerf*2))
        current_y=(wood+cerf)
        corner(dwg,cerf,wood,"up","right")
        centre_top(dwg,cerf,wood,len_number,length_tab_make)
        corner(dwg,cerf,wood,"right","down")
        centre_right(dwg,cerf,wood,wid_number,width_tab_make)
        corner(dwg,cerf,wood,"down","left")
        centre_bottom(dwg,cerf,wood,len_number,length_tab_make)
        corner(dwg,cerf,wood,"left","up")
        centre_left(dwg,cerf,wood,wid_number,width_tab_make)
        dwg.save()
    


def outside(bottom_length,bottom_width,bottom_height,wood,cerf,nameo):
    print(bottom_height)
    length_tab_make=bottom_length
    length_tab_done=False
    while length_tab_done==False:
        if length_tab_make>6:
            length_tab_make=length_tab_make/4
        elif length_tab_make<3:
            length_tab_make=length_tab_make*2
        if 3<=length_tab_make<=6:
            length_tab_done=True
    len_number=bottom_length/length_tab_make

    width_tab_make=bottom_width
    width_tab_done=False
    while width_tab_done==False:
        if width_tab_make>6:
            width_tab_make=width_tab_make/4
        elif width_tab_make<3:
            width_tab_make=width_tab_make*2
        if 3<=width_tab_make<=6:
            width_tab_done=True
    wid_number=bottom_width/width_tab_make
    
    height_tab_make=bottom_height

    height_tab_done=False
    while height_tab_done==False:
        if height_tab_make>6:
            height_tab_make=width_tab_make/4
        elif height_tab_make<3:
            height_tab_make=height_tab_make*2
        if 3<=height_tab_make<=6:
            height_tab_done=True
    height_number=bottom_height/height_tab_make
    height_rounding = round(height_number)
    height_tab_make = height_tab_make * height_number / height_rounding
    height_number = height_rounding
    
    global current_x
    global current_y
    current_x=wood+cerf
    current_y=bottom_height
    dwg = svgwrite.Drawing(nameo+' Outside.svg', profile='tiny',size=('450mm','600mm'))
    for x in range(2):
        current_y=bottom_height+bottom_length+wood*2+cerf*2
        current_x=wood+cerf+x*(wood*10+cerf*4+bottom_width+bottom_length)
        #Height*Width
        loong(dwg,"uphand",bottom_width)
        righthand_side(dwg,cerf,wood,height_number,height_tab_make)
        downhand_side(dwg,cerf,wood,wid_number,width_tab_make)
        lefthand_side(dwg,cerf,wood,height_number,height_tab_make)
        lefthand_side(dwg,cerf,wood,height_number,height_tab_make)
        uphand_side(dwg,cerf,wood,wid_number,width_tab_make)
        righthand_side(dwg,cerf,wood,height_number,height_tab_make)
        current_x=wood+cerf+x*(wood*4+cerf*4+bottom_width+bottom_length)+bottom_width+wood*2+cerf*2
        #Height*Length
        loong(dwg,"uphand",bottom_length)
        righthand_side(dwg,cerf,wood,height_number,height_tab_make)
        downhand_side(dwg,cerf,wood,len_number,length_tab_make)
        lefthand_side(dwg,cerf,wood,height_number,height_tab_make)
        lefthand_side(dwg,cerf,wood,height_number,height_tab_make)
        uphand_side(dwg,cerf,wood,len_number,length_tab_make)
        righthand_side(dwg,cerf,wood,height_number,height_tab_make)
        #Length*Width
        current_x=wood+cerf+x*(wood*4+cerf*4+bottom_width+bottom_length)
        current_y=bottom_length+wood+cerf
        corner(dwg,cerf,wood,"left","up")
        centre_left(dwg,cerf,wood,len_number,length_tab_make)
        corner(dwg,cerf,wood,"up","right")
        centre_top(dwg,cerf,wood,wid_number,width_tab_make)
        corner(dwg,cerf,wood,"right","down")
        centre_right(dwg,cerf,wood,len_number,length_tab_make)
        corner(dwg,cerf,wood,"down","left")
        centre_bottom(dwg,cerf,wood,wid_number,width_tab_make)
        
    dwg.save()


def make_box(Name,length,width,height,kerf,mat_thickness):
    #Makes a box
    if length>200:
        print("Length too large! Please make it less than 200.")
        exit()
    if length<15:
        print("Length too small! Please make it at least than 15.")
        exit()
    if width>200:
        print("Width too large! Please make it less than 200.")
        exit()
    if width<15:
        print("Width too small! Please make it at least than 15.")
        exit()
    if height>200:
        print("Height too large! Please make it less than 200.")
        exit()
    if height<15:
        print("Height too small! Please make it at least than 15.")
        exit()
    inside(length,width,height*3/4,mat_thickness,kerf,Name)
    outer_length=length+mat_thickness*2+0.25
    outer_width=width+mat_thickness*2+0.25
    outer_height=height+mat_thickness*4
    outside(outer_length,outer_width,(float(outer_height*0.5)),mat_thickness,kerf,Name)
    print(outer_height)

make_box("Lindsey Box",20,20,40,0.16,2.9)
