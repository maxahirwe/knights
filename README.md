# KnightsBoard

## Installation

-   Go In project root folder
-   Install Python https://www.python.org/downloads/ (Used 3)
-   Install Pip (if you don't have it already installed) with the following commands

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

```
python3 get-pip.py
```

```
pip install numpy
```

## Testing

```
python3 index.py
```

-   Observe console output
-   Inspect generated JSON file ([final_state](/outputs/final_state.json))

## Classes

-   **Board**: Symbolizes the game board and has methods for various board:

    -   `get_square`: get a square based on (X,Y) 2d coordinates.
    -   `add_knight`: add knight to the board at provided coordidates.
    -   `sort_items`: sort items on each board square per priority.
    -   `add_item`: add items to the board at provided coordidates.
    -   `find_square_by_knight_symbol`: searches the first square on the board that contains a knight with a given symbol (ex:R OR B).
    -   `get_next_move_coordinates`: identifies the next move/square/coordinates based on current (X,Y) coordinates and the direction(N,E,S,W).
    -   `change_knight_status`: changes a knight's status to DROWNED OR DEAD.
    -   `move`: moves a knights accross the board.
    -   `output`: output that provides status for all items on board.

-   **Knight**: Symbolises a knight used to play across the board:

    -   `get_name`: get knight name.
    -   `total_attack_score`: get knight's total attack score.
    -   `total_defend_score`: get knight's total defend score.
    -   `attack`: perfoms an attack on a defender knight and evalutates the winer/looser, returns boolean.
    -   `change_coordinates`: change (X,Y) coordinates.
    -   `get_coordinates`: get (X,Y) coordinates.
    -   `get_coordinates_str`: get (X,Y) coordinates in string format.
    -   `output`: generate output for console and file extration.

-   **Item**: Symbolises an Item that knights can earn to boosts their defending/attack score:

    -   `get_name`: get item name.
    -   `get_coordinates`: get (X,Y) coordinates.
    -   `get_coordinates_str`: get (X,Y) coordinates in string format.
    -   `output`: generate output for console and file.

## Index File Process Flow

-   Creates Board 8x8 square "Arena"

-   Creates Knights and adds them to the board in their initial positions

    -   RED (R) => (0,0) (top left)
    -   BLUE (B) => (7,0) (bottom left)
    -   GREEN (G) => (7,7) (bottom right)
    -   YELLOW (Y) => (0,7) (top right)

-   Creates Items and adds them to the board in their initial positions

    -   Axe (A): +2 Attack => (2,2)
    -   Dagger (D): +1 Attack => (2,5)
    -   Helmet (H): +1 Defence => (5,5)
    -   MagicStaff (M): +1 Attack, +1 Defence => (5,2)

-   Reads moves from file (moves.txt):

-   Verbose print all actions taking places

    -   adding
    -   movements
    -   fighting
    -   earned items
    -   status changes

-   Generates output file (/outputs/final_state.json)

## Documentation

-   ![console snapshot](/documentation/consolesnapshot.png)
-   ![json output](/documentation/jsonoutput.png)

## Author

[@maxahirwe](https://max.rw)
