# Game of Life Kata (Python)

## Usage
### Initial state
- First, you need to define the initial state
- Create a file, named input.txt (as an example) formatted in this exact way

```
Generation 3:
4 8
........
....*...
...**...
........
```

Thus, you have:

- first line: the string "Generation " followed by the number of the generation the file is describing, followed by a ":"
- second line: the grid size, in term of rows and cols, separated by a simple space
- other lines: the actual grid, with a dot to mark a dead cell and an asterisk to mark a live cell. 

### Run
`python main.py './input.txt'`