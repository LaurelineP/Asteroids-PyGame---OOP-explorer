# Asteroids clone game
A project for OOP deepening and diving into [pygame](https://www.pygame.org/docs/)

![My Skills](https://skillicons.dev/icons?i=python)

<div align="center">
  <img height=300 src="https://github.com/user-attachments/assets/9b739c81-4364-4700-a70f-38c6b9af71e6" />
</div>





## Pygame and usage review
- vectors: creating a direction
  ```py
  pygame.Vector2(<x>,<y>).rotate(<value>)
  ```
- shapes: drawing a shape
  ```py
  pygame.draw<shape>(<options>)

  # <options - positional arg>
  #  - surface (ex: Surface, screen / defined window - what onto )
  #  - center: (<x>,<y>)  of the element / position to draw
  #  - stroke color
  #  - stroke size
  ```
- pygame methods on shapes
  - `.init()` - init game
  - `.display.set_mode(<width>, <height>` - a surface for the window of the game to open
  - `.sprite` - an object providing hips of methods to use for a game ( ex collision, kill )
  - `.sprite.Group()` - an instance of a container for multipple sprites
    will allows for an entity to hold containers on which to apply affecting changes / events
  - `.event.get()` - allows to list the events of the game,
    could be used to hook into one of the event and apply 
  - `.flip()` - updates Surface display
  - `.kill()` - destroy an object
  - `.time.Clock()` - helper to track time
    (could help to handle FPS for instance, to deduct delta time using the events )

  

