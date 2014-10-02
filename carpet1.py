import cv2, test, time, pygame, easygui
pygame.init()


img,t_rang,x,y = easygui.multenterbox("add carpet information",
                              "carpet information",
                              ["wich image(address or name)???",
                               "how many color???",
                               "how many gere???",
                               "how many rach???"])
yarn_colors = [[255,255,255],
               [250,250,250],
               [200,200,200],
               [150,150,150],
               [100,100,100],
               [012,99,234],
               [000,000,000]]
colors = []
carpet_map = file("map.txt","w")
img = cv2.imread(img, cv2.CV_LOAD_IMAGE_COLOR)
r,c,t = img.shape


def draw_main(r,c,yarn_colors,img,x,y,t_rang):
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
                        
                        pygame.display.flip()
                pygame.display.update()
        return colors


colors = draw_main(r,c,yarn_colors,img,int(x),int(y),int(t_rang))
print colors
while True:
        pass
