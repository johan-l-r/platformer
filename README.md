# Platformer Game

This project is a simple 2D platformer built with **Pygame**. While most of my repositories focus on frontend or full-stack development, I also enjoy building games because they expose me to a completely different set of programming challenges. That's why you'll also find a few non-web projects on this GitHub profile. I enjoy experimenting with different areas of software development, and game development is a great way to learn by building.

The goal of this project is to create a simple platformer featuring:
- Three levels
- Physics
- Collision detection
- Level loading
- Lives counter

As I continue learning, I'll keep expanding the game with new mechanics and improvements.

***

## Development Log

This section serves as a journal of my progress throughout the project. Rather than only documenting what I build, I also want to record what I learn, the mistakes I make, and the reasoning behind important implementation decisions.

***

## 07/19/2026

Yesterday, I worked on the project's foundation: creating the game window, implementing the basic game loop, rendering the player, and adding simple movement. Although these tasks may sound complex, Pygame abstracts away much of the boilerplate for creating the window and managing the game loop. The part I found most interesting was improving how the player moves.

### Basic Movement

```python
self.x += self.movement_speed * self.direction[0] * delta
```

This implementation simply updates the player's horizontal position every frame by multiplying the movement speed by the input direction (`-1` or `1`) and `delta`, which keeps movement consistent regardless of the frame rate. It's simple, predictable, and works perfectly for basic movement.

However, I wanted the controls to feel smoother and more natural, so I started looking into **vector-based movement**.

### Vector Movement

The difference was immediately noticeable. Instead of starting and stopping instantly, the player gradually accelerates and decelerates, making the movement feel much more responsive and enjoyable.

I won't try to explain exactly how the code works because, honestly, I don't fully understand it myself. I understand the individual concepts—speed, velocity, and acceleration—but how they all interact in this implementation is still something I'm learning. Rather than pretending I understand something I don't, I've started studying the underlying physics so that I can eventually explain the logic behind this system instead of simply copying it from a tutorial.

For now, I'm comfortable admitting that this is an area I still need to learn, and that's part of the reason I wanted to build this project in the first place.
