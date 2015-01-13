import cv2, time, pygame, easygui
pygame.init()


img,t_rang,x,y = easygui.multenterbox("add carpet information",
                              "carpet information",
                              ["wich image(address or name)???",
                               "how many color???",
                               "how many gere???",
                               "how many rach???"])
yarn_colors = [[0, 0, 0] ,
                [11, 11, 11] ,
                [22, 22, 22] ,
                [33, 33, 33] ,
                [44, 44, 44] ,
                [55, 55, 55] ,
                [66, 66, 66] ,
                [77, 77, 77] ,
                [88, 88, 88] ,
                [99, 99, 99] ,
                [110, 110, 110] ,
                [121, 121, 121] ,
                [132, 132, 132] ,
                [143, 143, 143] ,
                [154, 154, 154] ,
                [165, 165, 165] ,
                [176, 176, 176] ,
                [187, 187, 187] ,
                [198, 198, 198] ,
                [209, 209, 209] ,
                [220, 220, 220] ,
                [231, 231, 231] ,
                [242, 242, 242] ,
                [253, 253, 253]]
colors = []
gere_ha = []
carpet_map = open("map.txt","w")
img = cv2.imread(img, cv2.CV_LOAD_IMAGE_COLOR)
r,c,t = img.shape


def draw_main(r,c,yarn_colors,img,x,y,t_rang):
        global gere_ha
        c_jump = c/x
        r_jump = r/y
        t_colors = 0
        colors = []        
        screen = pygame.display.set_mode([int(c/c_jump)*2,int(r/r_jump)*2])
        screen.fill([255,255,255])
        for i in range(r-1,-1,-r_jump):
                for u in range(0,c,c_jump):
                        ###############
                        pixel_color = [img[i,u,2], img[i,u,1], img[i,u,0]]
                        choiced_color = yarn_colors[0]
                        differencer = abs(pixel_color[0]-yarn_colors[0][0])+abs(pixel_color[1]-yarn_colors[0][1])+abs(pixel_color[2]-yarn_colors[0][2])
                        pixel_difference = differencer
                        for color in range(0,len(yarn_colors),1):
                                difference = abs(pixel_color[0]-yarn_colors[color][0])+abs(pixel_color[1]-yarn_colors[color][1])+abs(pixel_color[2]-yarn_colors[color][2])
                                if difference < pixel_difference:
                                        choiced_color = yarn_colors[color]
                                        pixel_difference = difference
                                        if choiced_color not in colors and choiced_color in yarn_colors:
                                                t_colors += 1
                                                colors.append(choiced_color)
                        ###############
                        pygame.draw.rect(screen,choiced_color,[u/c_jump*2,i/r_jump*2,2,2])
                        gere_ha.append(yarn_colors.index(choiced_color))
                        
                        pygame.display.flip()
                pygame.display.update()
        return [r_jump, c_jump]


colors = draw_main(r,c,yarn_colors,img,int(x),int(y),int(t_rang))
z = []
for i in range(int(y)):
    #print int(y)*int(x)    
    y1 = []
    for u in range(int(x)):
        y1.append(gere_ha[i*int(x)+u])
        #carpet_map.write(str(gere_ha[i*int(x)+u])+',')
    #carpet_map.write(" line"+str(i)+"\n")
    z.append(y1)

y2 = []
y3 = []
x = []
for i in range(len(yarn_colors)):
        y2.append([])
        y3.append([])

carpet_map = open('map.txt','w')        
for i in range(len(z)):
        y2 = []
        for u in range(len(yarn_colors)):
                y2.append([])
        carpet_map = open('map.txt','a')
        for u in range(len(z[i])):
                y2[z[i][u]].append(u)
        for u in range(len(y2)):
                carpet_map.write('\"'+str(u)+'\" ')
                carpet_map.write(str(y2[u])+', ')
        carpet_map.write(" line"+str(i)+"\n")
        carpet_map.close()
        x.append(y2)

t = [0]*len(yarn_colors)
for i in range(len(z)):
        for u in range(len(z[i])):
                t[z[i][u]] += 1

carpet_map = open('map.txt','a')
carpet_map.write(str(t))
carpet_map.close()
        
                
pygame.quit()
