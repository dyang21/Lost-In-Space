#dy
from pygame import Rect


#takes rect object and list of other rects. returns which tile it collides with
def rectTest(player_rect,tiles,testVertRect): #side,displacement; divide it by the side and add it by the displacement
    """
    parameters: rect, list, bool
    gives a list of rects colliding with the player
    returns list of rects that collided witht the user rect
    """
    col_List = []
    if testVertRect == False:
        for tile in tiles:
            if player_rect.colliderect(tile):
                col_List.append(tile)

                
    else:

        preciseRect = Rect(player_rect.x,player_rect.y + 2  ,42,player_rect.height)
        
        for tile in tiles:
            
            if preciseRect.colliderect(tile):
                
                col_List.append(tile) #second tile would be the time it has been stepped on, and to include Rect collision
                #if player_rect.y < tile.y - 66:
                    #player_rect.bottom = tile.top
                
    return col_List



#char obj,how much being moved, objects to be collided with
def col(player_rect,movement,tiles): #(rect,[ints,],[rects,])
    """
    parameters: rect, list of ints, list of rects
    Determines the collision type based on the player movement
    returns dictionary of the collision types.
    """
    #print(movement)
    col_types = {'top':False,'bottom':False,'right':False,'left':False}
    #seperated because the collision list is reassigned
    player_rect.x += movement[0]
    hit_list = rectTest(player_rect,tiles,False)
    for tile in hit_list:
        if movement[0] > 0:
            #prevents border collision 
            player_rect.right = tile.left
            col_types['right'] = True

        elif movement[0] < 0:
            player_rect.left = tile.right
            col_types['left'] = True
            
    player_rect.y += movement[1]
    hit_list = rectTest(player_rect,tiles,False)
    #enables stopping at collisions for left and right. 
    for tile in hit_list:
        #move left or right
        if movement[1] > 0:
            player_rect.bottom = tile.top
            col_types['bottom'] = True
        elif movement[1] < 0:
            player_rect.top = tile.bottom
            col_types['top'] = True

    #return collision types and location of rect obj
    #print(col_types)
    return col_types
