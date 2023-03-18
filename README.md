# KnightsBoard

## Classes

-   Board: Symbolized the game board and has methods for various board actions:
    -   get_square
    -   add_knight
    -   sort_items
    -   add_item
    -   find_square_by_knight_symbol
    -   getNextMoveCoordinates
    -   changeKnightStatus
    -   move
    -   output
-   Knight
    -   get_name
    -   total_attack_score
    -   total_defend_score
    -   attack
    -   change_coordinates
    -   get_coordinates
    -   get_coordinates_str
    -   output
-   Item
    -   get_name
    -   get_coordinates
    -   get_coordinates_str
    -   output

## Index File Flow

-   Creates Board 8x8 square "Arena"
-   Creates Knights and add them to board in their initial position
    -   RED (R) => R (0,0) (top left)
    -   BLUE (B) => (7,0) (bottom left)
    -   GREEN (G) => G (7,7) (bottom right)
    -   YELLOW (Y) => Y (0,7) (top right)
-   Creates Items and add them to board in their initial position

    -   Axe (A): +2 Attack => (2,2)
    -   Dagger (D): +1 Attack => (2,5)
    -   Helmet (H): +1 Defence => (5,5)
    -   MagicStaff (M): +1 Attack, +1 Defence => (5,2)

-   Print verbose print all actions taking places

    -   adding
    -   movements
    -   fighting
    -   earn items
    -   status changes

-   Generates output file (final_state.json)

## INSTALLATION

-   Install Python https://www.python.org/downloads/ (Used 3)
-   Install Pip+ https://pip.pypa.io/en/stable/installation/

```
    (https://nodejs.org/en/download/ (Used v16.0.0+))
```

### TESTING AND OBSERVE OUTPUT

```
python3 index.js
```

    or

```
python index.js
```

### Readable file format(moves.txt):

GAME-START
<Knight>:<Direction>
<Knight>:<Direction>
<Knight>:<Direction>
.
.
.
GAME-END
For example:
GAME-START
R:S
R:S
B:E
G:N
Y:N
GAME-END

## Author

[@maxahirwe](https://max.rw)
