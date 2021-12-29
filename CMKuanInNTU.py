import CMKuan_game, CMKuan_player, CMKuan_event
import pygame

def game_loop(gameName):
    game_exit = False
    allsprite = pygame.sprite.Group()
    player = CMKuan_player.Player()
    allsprite.add(player)

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
            if event.type == pygame.QUIT:
                game_exit = True
        
        # game flow
        gameName.display_background()
        gameName.display_status()
        gameName.display_player()
        # gameName.display_event()
                
        pygame.display.update()

if __name__ == '__main__':
    CMKGame = CMKuan_game.Game()
    # display cover page
    """
    CMKGame.init_screen()
    CMKGame.display_cover()
    pygame.display.update()
    """
    # display game page
    CMKGame.init_screen()
    CMKGame.init_clock()
    game_loop(CMKGame)
