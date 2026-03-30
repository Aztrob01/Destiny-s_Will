import pygame, json, os

# ------------------------------------------------------------

def json_read(self, path):
        path = f'./src/{path}.json'

        if os.path.exists(path) is False:
            raise FileNotFoundError(f'File {path} not found.')
        
        with open(path, 'r') as catch:
            data = json.load(catch)
            return data

def json_gets(path, args, all=False):
    if isinstance(args, str):
        args = [args]


    with open(path, 'r') as catch:      
        
        data = json.load(catch)
        
        if all is True:
            return data
        
        if isinstance(args, list): 
                if isinstance(args, str):
                    try:
                        x = data[args]
                    except KeyError:
                        raise KeyError(f'Key {args} not found in data.')
                else:
                    x = {}
                    for nums, items in enumerate(args):
                        if isinstance(items, list):
                                f = items[0]
                                if f not in data:
                                    raise KeyError(f'Father Key ({f}) not found ind data')
                                c = items[1]
                                if c not in data[f]:
                                    raise KeyError(f'Child Key ({c}) not found in data[{f}]')
                                x[c] = data[f][c]
                        else:
                            if items not in data:
                                raise KeyError(f'Key {items} not found in data.')
                            x[items] = data[items]
        return x
                        

                                

                        
# ------------------------------------------------------------
# Sprite Updater, to load and scale Entity Sprites based on their state and size

def update_sprite(state, char): #! 
    for mstate in char.job.sprites:
        if mstate == state[0]:
            for sstate in char.job.sprites[mstate]:
                if sstate == state[1]:
                    char.image = pygame.image.load(char.job.sprites[mstate][sstate])
        elif state[0] not in char.job.sprites:
            print(f'Erro na renderização de {mstate} / {sstate} de {char.job.data['info']['cavaliere']}')
            char.image = pygame.image.load(char.job.sprites['fight']['idle'])

    char.image = pygame.image.load(char.image, (char.job.sprites['size']['common']))
    char.rect  = char.image.get_rect()

# ------------------------------------------------------------
# Image Loader, to load and scale images based on the given path

def load_image(origin, size):
    image = pygame.image.load(origin)
    image = pygame.transform.scale(image, size)
    
    return image

# ------------------------------------------------------------
# Timer class to create cooldowns and delays in the combat system
# using pygame's time module

class Timer:
    def __init__(self, delay):
        self.delay = delay
        self.ltime = 0

    def wait(self):
        ctime = pygame.time.get_ticks()
        if ctime - self.ltime > self.delay:
            self.ltime = ctime
            return True
        return False

# ------------------------------------------------------------
