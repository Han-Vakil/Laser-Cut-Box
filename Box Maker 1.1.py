import svgwrite
import os
#How this is gonna work:
#Input interior length, width, height, the program first makes the inner box, then the bottom, then the top

def inner(inner_length,inner_width,inner_height,wood,cerf,nameo):
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

    dwg = svgwrite.Drawing(nameo+'_Inner.svg', profile='tiny',height="450mm",width="650mm")
    for x in range(2):
        current_x=x*(inner_length+(wood*4)+(cerf*2))
        #Length*height
        dwg.add(dwg.line((current_x,current_y),(current_x+inner_length,current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_x=current_x+inner_length
        for x in range((int(height_number)//2)):
            #Right Dent
            dwg.add(dwg.line((current_x,current_y),(current_x+(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(wood+cerf)
            #Down tab out
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+(cerf+height_tab_make)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+cerf+height_tab_make
            #Left Dent
            dwg.add(dwg.line((current_x,current_y),(current_x-(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(wood+cerf)
            #Down Tab in
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-cerf+height_tab_make),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-cerf+height_tab_make
        for x in range(int(len_number)//2):
            #Down dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+cerf+wood),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+cerf+wood
            #Left Tab Out
            dwg.add(dwg.line((current_x,current_y),(current_x-(length_tab_make+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(length_tab_make+cerf)
            #Up Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+wood)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-(cerf+wood)
            #Left Tab In
            dwg.add(dwg.line((current_x,current_y),(current_x-(length_tab_make-cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(length_tab_make-cerf)
        for x in range(int(height_number)//2):
            #Left Dent
            dwg.add(dwg.line((current_x,current_y),(current_x-(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(wood+cerf)
            #Up Tab Out
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-cerf-height_tab_make),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-cerf-height_tab_make
            #Right Dent
            dwg.add(dwg.line((current_x,current_y),(current_x+(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(wood+cerf)
            #Up Tab In
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+cerf-height_tab_make),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+cerf-height_tab_make

    #Width*height
    for x in range(2):
        current_x=x*(inner_height+wood*2+cerf*2)
        current_y=-1*(inner_width+wood*3+cerf*2)
        #Right
        for x in range(int(height_number)//2):
            #Up Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+wood)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-(cerf+wood)
            #Right Out
            dwg.add(dwg.line((current_x,current_y),(current_x+(height_tab_make+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(height_tab_make+cerf)
            #Down Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+cerf+wood),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+cerf+wood
             #Right In
            dwg.add(dwg.line((current_x,current_y),(current_x+(height_tab_make-cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(height_tab_make-cerf)
        #Long Down
        #Doooooooooooooooooown
        dwg.add(dwg.line((current_x,current_y),(current_x,current_y+inner_width),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_y=current_y+inner_width
        for x in range(int(height_number)//2):
            #Left
            #Down Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+cerf+wood),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+cerf+wood
            #Left Out
            dwg.add(dwg.line((current_x,current_y),(current_x-(height_tab_make+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(height_tab_make+cerf)
             #Up Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+wood)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-(cerf+wood)
            #Left In
            dwg.add(dwg.line((current_x,current_y),(current_x-(height_tab_make-cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(height_tab_make-cerf)
        for x in range(int(wid_number)//2):
            #Up
            #Left Dent
            dwg.add(dwg.line((current_x,current_y),(current_x-(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(wood+cerf)
            #Up Out
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+width_tab_make)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-(cerf+width_tab_make)
            #Right Dent
            dwg.add(dwg.line((current_x,current_y),(current_x+(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(wood+cerf)
            #Up In
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+(cerf-width_tab_make)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+(cerf-width_tab_make)
        

    #Length*width
    for x in range(1):
        current_x=2*(inner_length+(wood*4)+(cerf*2))
        current_y=(wood+cerf)
        #Top Left Corner
        #Up Dent
        dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+wood)),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_y=current_y-(cerf+wood)
        #Right Dent
        dwg.add(dwg.line((current_x,current_y),(current_x+(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_x=current_x+(wood+cerf)
        #Top
        for x in range(int(len_number)//2):
            #Right Tab Out
            dwg.add(dwg.line((current_x,current_y),(current_x+(length_tab_make+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(length_tab_make+cerf)
            #Down Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+cerf+wood),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+cerf+wood
            #Right Tab In
            dwg.add(dwg.line((current_x,current_y),(current_x+(length_tab_make-cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(length_tab_make-cerf)
            #Up Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+wood)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-(cerf+wood)
        #Top Right Corner
        #Right Dent
        dwg.add(dwg.line((current_x,current_y),(current_x+(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_x=current_x+(wood+cerf)
        #Down Dent
        dwg.add(dwg.line((current_x,current_y),(current_x,current_y+cerf+wood),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_y=current_y+cerf+wood
        #Right
        for x in range(int(wid_number)//2):
            #Down Tab Out
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+(cerf+width_tab_make)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+cerf+width_tab_make
            #Left Dent
            dwg.add(dwg.line((current_x,current_y),(current_x-(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(wood+cerf)
            #Down Tab In
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+(width_tab_make-cerf)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+(width_tab_make-cerf)
            #Right Dent
            dwg.add(dwg.line((current_x,current_y),(current_x+(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(wood+cerf)
        #Bottom Right Corner
        #Down Dent
        dwg.add(dwg.line((current_x,current_y),(current_x,current_y+cerf+wood),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_y=current_y+cerf+wood
        #Left Dent
        dwg.add(dwg.line((current_x,current_y),(current_x-(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_x=current_x-(wood+cerf)
        #Bottom
        for x in range(int(len_number)//2):
            #Left Tab Out
            dwg.add(dwg.line((current_x,current_y),(current_x-(length_tab_make+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(length_tab_make+cerf)
            #Up Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+wood)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-(cerf+wood)
            #Left Tab In
            dwg.add(dwg.line((current_x,current_y),(current_x-(length_tab_make-cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(length_tab_make-cerf)
            #Down Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+cerf+wood),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+cerf+wood
        #Bottom Left Corner
        #Left Dent
        dwg.add(dwg.line((current_x,current_y),(current_x-(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_x=current_x-(wood+cerf)
        #Up Dent
        dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+wood)),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_y=current_y-(cerf+wood)
        #Left
        for x in range(int(wid_number)//2):
            #Up Tab In
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(width_tab_make-cerf)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-(width_tab_make-cerf)
            #Right Dent
            dwg.add(dwg.line((current_x,current_y),(current_x+(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(wood+cerf)
            #Up Tab Out
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+width_tab_make)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-(cerf+width_tab_make)
            #Left Dent
            dwg.add(dwg.line((current_x,current_y),(current_x-(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(wood+cerf)
        dwg.add(dwg.line((-100,-300),(-100,300),stroke=svgwrite.rgb(10, 10, 16, '%')))
        dwg.add(dwg.line((-100,300),(500,300),stroke=svgwrite.rgb(10, 10, 16, '%')))
        dwg.add(dwg.line((500,300),(500,-300),stroke=svgwrite.rgb(10, 10, 16, '%')))
        dwg.add(dwg.line((500,-300),(-100,-300),stroke=svgwrite.rgb(10, 10, 16, '%')))    
        dwg.save()
    


def bottom(bottom_length,bottom_width,bottom_height,wood,cerf,nameo):
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
    global current_x
    global current_y
    current_x=wood+cerf
    current_y=0

    dwg = svgwrite.Drawing(nameo+'_Bottom.svg', profile='tiny')
    for x in range(2):
        current_x=x*(bottom_length+(wood*4)+(cerf*2))
        #Length*height
        dwg.add(dwg.line((current_x,current_y),(current_x+bottom_length,current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_x=current_x+bottom_length
        for x in range((int(height_number)//2)):
            #Right Dent
            dwg.add(dwg.line((current_x,current_y),(current_x+(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(wood+cerf)
            #Down tab out
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+(cerf+height_tab_make)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+cerf+height_tab_make
            #Left Dent
            dwg.add(dwg.line((current_x,current_y),(current_x-(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(wood+cerf)
            #Down Tab in
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-cerf+height_tab_make),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-cerf+height_tab_make
        for x in range(int(len_number)//2):
            #Down dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+cerf+wood),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+cerf+wood
            #Left Tab Out
            dwg.add(dwg.line((current_x,current_y),(current_x-(length_tab_make+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(length_tab_make+cerf)
            #Up Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+wood)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-(cerf+wood)
            #Left Tab In
            dwg.add(dwg.line((current_x,current_y),(current_x-(length_tab_make-cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(length_tab_make-cerf)
        for x in range(int(height_number)//2):
            #Left Dent
            dwg.add(dwg.line((current_x,current_y),(current_x-(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(wood+cerf)
            #Up Tab Out
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-cerf-height_tab_make),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-cerf-height_tab_make
            #Right Dent
            dwg.add(dwg.line((current_x,current_y),(current_x+(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(wood+cerf)
            #Up Tab In
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+cerf-height_tab_make),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+cerf-height_tab_make

    #Width*height
    for x in range(2):
        current_x=x*(bottom_height+wood*2+cerf*2)
        current_y=-1*(bottom_width+wood*3+cerf*2)
        #Right
        for x in range(int(height_number)//2):
            #Up Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+wood)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-(cerf+wood)
            #Right Out
            dwg.add(dwg.line((current_x,current_y),(current_x+(height_tab_make+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(height_tab_make+cerf)
            #Down Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+cerf+wood),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+cerf+wood
             #Right In
            dwg.add(dwg.line((current_x,current_y),(current_x+(height_tab_make-cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(height_tab_make-cerf)
        #Long Down
        #Doooooooooooooooooown
        dwg.add(dwg.line((current_x,current_y),(current_x,current_y+bottom_width),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_y=current_y+bottom_width
        for x in range(int(height_number)//2):
            #Left
            #Down Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+cerf+wood),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+cerf+wood
            #Left Out
            dwg.add(dwg.line((current_x,current_y),(current_x-(height_tab_make+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(height_tab_make+cerf)
             #Up Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+wood)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-(cerf+wood)
            #Left In
            dwg.add(dwg.line((current_x,current_y),(current_x-(height_tab_make-cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(height_tab_make-cerf)
        for x in range(int(wid_number)//2):
            #Up
            #Left Dent
            dwg.add(dwg.line((current_x,current_y),(current_x-(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(wood+cerf)
            #Up Out
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+height_tab_make)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-(cerf+height_tab_make)
            #Right Dent
            dwg.add(dwg.line((current_x,current_y),(current_x+(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(wood+cerf)
            #Up In
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+(cerf-height_tab_make)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+(cerf-height_tab_make)
        

    #Length*width
    for x in range(1):
        current_x=2*(bottom_length+(wood*4)+(cerf*2))
        current_y=(wood+cerf)
        #Top Left Corner
        #Up Dent
        dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+wood)),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_y=current_y-(cerf+wood)
        #Right Dent
        dwg.add(dwg.line((current_x,current_y),(current_x+(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_x=current_x+(wood+cerf)
        #Top
        for x in range(int(len_number)//2):
            #Right Tab Out
            dwg.add(dwg.line((current_x,current_y),(current_x+(length_tab_make+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(length_tab_make+cerf)
            #Down Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+cerf+wood),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+cerf+wood
            #Right Tab In
            dwg.add(dwg.line((current_x,current_y),(current_x+(length_tab_make-cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(length_tab_make-cerf)
            #Up Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+wood)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-(cerf+wood)
        #Top Right Corner
        #Right Dent
        dwg.add(dwg.line((current_x,current_y),(current_x+(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_x=current_x+(wood+cerf)
        #Down Dent
        dwg.add(dwg.line((current_x,current_y),(current_x,current_y+cerf+wood),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_y=current_y+cerf+wood
        #Right
        for x in range(int(wid_number)//2):
            #Down Tab Out
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+(cerf+width_tab_make)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+cerf+width_tab_make
            #Left Dent
            dwg.add(dwg.line((current_x,current_y),(current_x-(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(wood+cerf)
            #Down Tab In
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+(width_tab_make-cerf)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+(width_tab_make-cerf)
            #Right Dent
            dwg.add(dwg.line((current_x,current_y),(current_x+(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(wood+cerf)
        #Bottom Right Corner
        #Down Dent
        dwg.add(dwg.line((current_x,current_y),(current_x,current_y+cerf+wood),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_y=current_y+cerf+wood
        #Left Dent
        dwg.add(dwg.line((current_x,current_y),(current_x-(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_x=current_x-(wood+cerf)
        #Bottom
        for x in range(int(len_number)//2):
            #Left Tab Out
            dwg.add(dwg.line((current_x,current_y),(current_x-(length_tab_make+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(length_tab_make+cerf)
            #Up Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+wood)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-(cerf+wood)
            #Left Tab In
            dwg.add(dwg.line((current_x,current_y),(current_x-(length_tab_make-cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(length_tab_make-cerf)
            #Down Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+cerf+wood),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+cerf+wood
        #Bottom Left Corner
        #Left Dent
        dwg.add(dwg.line((current_x,current_y),(current_x-(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_x=current_x-(wood+cerf)
        #Up Dent
        dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+wood)),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_y=current_y-(cerf+wood)
        #Left
        for x in range(int(wid_number)//2):
            #Up Tab In
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(width_tab_make-cerf)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-(width_tab_make-cerf)
            #Right Dent
            dwg.add(dwg.line((current_x,current_y),(current_x+(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(wood+cerf)
            #Up Tab Out
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+width_tab_make)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-(cerf+width_tab_make)
            #Left Dent
            dwg.add(dwg.line((current_x,current_y),(current_x-(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(wood+cerf)
        dwg.add(dwg.line((-100,-300),(-100,300),stroke=svgwrite.rgb(10, 10, 16, '%')))
        dwg.add(dwg.line((-100,300),(500,300),stroke=svgwrite.rgb(10, 10, 16, '%')))
        dwg.add(dwg.line((500,300),(500,-300),stroke=svgwrite.rgb(10, 10, 16, '%')))
        dwg.add(dwg.line((500,-300),(-100,-300),stroke=svgwrite.rgb(10, 10, 16, '%')))    
        dwg.save()


def top(top_length,top_width,top_height,wood,cerf,nameo):
    #Makes the top box
    length_tab_make=top_length
    length_tab_done=False
    while length_tab_done==False:
        if length_tab_make>6:
            length_tab_make=length_tab_make/4
        elif length_tab_make<3:
            length_tab_make=length_tab_make*2
        if 3<=length_tab_make<=6:
            length_tab_done=True
    len_number=top_length/length_tab_make
    width_tab_make=top_width
    width_tab_done=False
    while width_tab_done==False:
        if width_tab_make>6:
            width_tab_make=width_tab_make/4
        elif width_tab_make<3:
            width_tab_make=width_tab_make*2
        if 3<=width_tab_make<=6:
            width_tab_done=True
    wid_number=top_width/width_tab_make
    height_tab_make=top_height
    height_tab_done=False
    while height_tab_done==False:
        if height_tab_make>6:
            height_tab_make=height_tab_make/4
        elif height_tab_make<3:
            height_tab_make=height_tab_make*2
        if 3<=height_tab_make<=6:
            height_tab_done=True
    height_number=top_height/height_tab_make
    global current_x
    global current_y
    current_x=wood+cerf
    current_y=0

    dwg = svgwrite.Drawing(nameo+'_Top.svg', profile='tiny')
    for x in range(2):
        current_x=x*(top_length+(wood*4)+(cerf*2))
        #Length*height
        dwg.add(dwg.line((current_x,current_y),(current_x+top_length,current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_x=current_x+top_length
        for x in range((int(height_number)//2)):
            #Right Dent
            dwg.add(dwg.line((current_x,current_y),(current_x+(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(wood+cerf)
            #Down tab out
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+(cerf+height_tab_make)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+cerf+height_tab_make
            #Left Dent
            dwg.add(dwg.line((current_x,current_y),(current_x-(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(wood+cerf)
            #Down Tab in
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-cerf+height_tab_make),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-cerf+height_tab_make
        for x in range(int(len_number)//2):
            #Down dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+cerf+wood),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+cerf+wood
            #Left Tab Out
            dwg.add(dwg.line((current_x,current_y),(current_x-(length_tab_make+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(length_tab_make+cerf)
            #Up Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+wood)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-(cerf+wood)
            #Left Tab In
            dwg.add(dwg.line((current_x,current_y),(current_x-(length_tab_make-cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(length_tab_make-cerf)
        for x in range(int(height_number)//2):
            #Left Dent
            dwg.add(dwg.line((current_x,current_y),(current_x-(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(wood+cerf)
            #Up Tab Out
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-cerf-height_tab_make),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-cerf-height_tab_make
            #Right Dent
            dwg.add(dwg.line((current_x,current_y),(current_x+(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(wood+cerf)
            #Up Tab In
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+cerf-height_tab_make),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+cerf-height_tab_make

    #Width*height
    for x in range(2):
        current_x=x*(top_height+wood*2+cerf*2)
        current_y=-1*(top_width+wood*3+cerf*2)
        #Right
        for x in range(int(height_number)//2):
            #Up Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+wood)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-(cerf+wood)
            #Right Out
            dwg.add(dwg.line((current_x,current_y),(current_x+(height_tab_make+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(height_tab_make+cerf)
            #Down Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+cerf+wood),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+cerf+wood
             #Right In
            dwg.add(dwg.line((current_x,current_y),(current_x+(height_tab_make-cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(height_tab_make-cerf)
        #Long Down
        #Doooooooooooooooooown
        dwg.add(dwg.line((current_x,current_y),(current_x,current_y+top_width),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_y=current_y+top_width
        for x in range(int(height_number)//2):
            #Left
            #Down Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+cerf+wood),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+cerf+wood
            #Left Out
            dwg.add(dwg.line((current_x,current_y),(current_x-(height_tab_make+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(height_tab_make+cerf)
             #Up Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+wood)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-(cerf+wood)
            #Left In
            dwg.add(dwg.line((current_x,current_y),(current_x-(height_tab_make-cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(height_tab_make-cerf)
        for x in range(int(wid_number)//2):
            #Up
            #Left Dent
            dwg.add(dwg.line((current_x,current_y),(current_x-(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(wood+cerf)
            #Up Out
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+width_tab_make)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-(cerf+width_tab_make)
            #Right Dent
            dwg.add(dwg.line((current_x,current_y),(current_x+(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(wood+cerf)
            #Up In
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+(cerf-width_tab_make)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+(cerf-width_tab_make)
        dwg.save()
        

    #Length*width
    for x in range(1):
        current_x=2*(top_length+(wood*4)+(cerf*2))
        current_y=(wood+cerf)
        #Top Left Corner
        #Up Dent
        dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+wood)),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_y=current_y-(cerf+wood)
        #Right Dent
        dwg.add(dwg.line((current_x,current_y),(current_x+(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_x=current_x+(wood+cerf)
        #Top
        for x in range(int(len_number)//2):
            #Right Tab Out
            dwg.add(dwg.line((current_x,current_y),(current_x+(length_tab_make+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(length_tab_make+cerf)
            #Down Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+cerf+wood),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+cerf+wood
            #Right Tab In
            dwg.add(dwg.line((current_x,current_y),(current_x+(length_tab_make-cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(length_tab_make-cerf)
            #Up Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+wood)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-(cerf+wood)
        #Top Right Corner
        #Right Dent
        dwg.add(dwg.line((current_x,current_y),(current_x+(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_x=current_x+(wood+cerf)
        #Down Dent
        dwg.add(dwg.line((current_x,current_y),(current_x,current_y+cerf+wood),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_y=current_y+cerf+wood
        #Right
        for x in range(int(wid_number)//2):
            #Down Tab Out
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+(cerf+width_tab_make)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+cerf+width_tab_make
            #Left Dent
            dwg.add(dwg.line((current_x,current_y),(current_x-(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(wood+cerf)
            #Down Tab In
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+(width_tab_make-cerf)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+(width_tab_make-cerf)
            #Right Dent
            dwg.add(dwg.line((current_x,current_y),(current_x+(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(wood+cerf)
        #Bottom Right Corner
        #Down Dent
        dwg.add(dwg.line((current_x,current_y),(current_x,current_y+cerf+wood),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_y=current_y+cerf+wood
        #Left Dent
        dwg.add(dwg.line((current_x,current_y),(current_x-(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_x=current_x-(wood+cerf)
        #Bottom
        for x in range(int(len_number)//2):
            #Left Tab Out
            dwg.add(dwg.line((current_x,current_y),(current_x-(length_tab_make+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(length_tab_make+cerf)
            #Up Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+wood)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-(cerf+wood)
            #Left Tab In
            dwg.add(dwg.line((current_x,current_y),(current_x-(length_tab_make-cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(length_tab_make-cerf)
            #Down Dent
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y+cerf+wood),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y+cerf+wood
        #Bottom Left Corner
        #Left Dent
        dwg.add(dwg.line((current_x,current_y),(current_x-(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_x=current_x-(wood+cerf)
        #Up Dent
        dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+wood)),stroke=svgwrite.rgb(10, 10, 16, '%')))
        current_y=current_y-(cerf+wood)
        #Left
        for x in range(int(wid_number)//2):
            #Up Tab In
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(width_tab_make-cerf)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-(width_tab_make-cerf)
            #Right Dent
            dwg.add(dwg.line((current_x,current_y),(current_x+(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x+(wood+cerf)
            #Up Tab Out
            dwg.add(dwg.line((current_x,current_y),(current_x,current_y-(cerf+width_tab_make)),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_y=current_y-(cerf+width_tab_make)
            #Left Dent
            dwg.add(dwg.line((current_x,current_y),(current_x-(wood+cerf),current_y),stroke=svgwrite.rgb(10, 10, 16, '%')))
            current_x=current_x-(wood+cerf)
        dwg.add(dwg.line((-100,-300),(-100,300),stroke=svgwrite.rgb(10, 10, 16, '%')))
        dwg.add(dwg.line((-100,300),(500,300),stroke=svgwrite.rgb(10, 10, 16, '%')))
        dwg.add(dwg.line((500,300),(500,-300),stroke=svgwrite.rgb(10, 10, 16, '%')))
        dwg.add(dwg.line((500,-300),(-100,-300),stroke=svgwrite.rgb(10, 10, 16, '%')))    
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
    inner(length,width,height*3/4,mat_thickness,kerf,Name)
    outer_length=length+mat_thickness*2+0.5
    outer_width=width+mat_thickness*2+5.5
    outer_height=height+mat_thickness*2+0.5
    bottom(outer_length,float(outer_height*4/8),outer_width,mat_thickness,kerf,Name)
    top(outer_length,float(outer_height)*4/8,outer_width,mat_thickness,kerf,Name)
    print("In each resulting svg file, there will be a box around the pieces to cut. Resize this box (highlighting the contents as well) to 600mm by 600mm so the parts are the right size.")

#make_box("Pencil Case 2.0",25,50,160,0.07,3)
#inner(16,89,64,3,0.06,"Card")
make_box("Card Box",16,640,89,0.07,3)
