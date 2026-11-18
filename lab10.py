# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline (write your plan here first):
    #  take a string thats the math operations in polish notation and then give back a number that is just evaluating it
    # i.e 8 2 + 3 2 + /  would be 2 because  8 + 2 = 10 / 3 + 2 = 5
    # use stack because the numbers are used together one
    """
    1. create an empty stack
    2. iterate through every token
    3. if the token is a number convert it to the integer and push it to stack
    4. if the token  operator pop the last two numbers and do operation
    5. push the result back to the stack
    6. return the number
    """

    stack = []

    for token in tokens:
        if token not in ["+", "-", "*", "/"]:
            stack.append(int(token))

        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            elif token == "/":
                result = int(a / b)

            stack.append(result)

    return stack[0]


def decode_string(s):
    # Outline:
    # take a string, and then read it for the symbol at the start for number of time repeat pattern, look at number assosciated with letter and repeat that many times and then keep doing that until no more left
    # 4[b2[c]] would be bccbccbccbcc
    # also use stack for this beecause it one after the other we look for
    """
    1. create an empty stack
    2. iterate through each character
    3. if it is a number build the repetition count
    4. if it is an opening bracket push the current string and repetition count onto the stack
    5. if it is a closing bracket pop the previous string and repetition count then repeat and combine the current string
    6. if it is a letter append it to the current string
    7. return the final decoded string
    """
    # TODO: decode a string written with the rule k[encoded], meaning `encoded` repeated
    #   k times. The brackets can be nested.
    #   Example: "3[a2[c]]"  ->  "accaccacc"
    stack = []
    current_string = ""
    num = 0

    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)

        elif char == "[":
            stack.append((current_string, num))
            current_string = ""
            num = 0

        elif char == "]":
            previous_string, repeat_count = stack.pop()
            current_string = previous_string + current_string * repeat_count

        else:
            current_string += char

    return current_string



def daily_temperatures(temps):
    # Outline:
    #  for each temeprature keep looking consecutivley if theres a higher temperature if not keep track and keep increasing dayas until find one or theres nothing where it would be 0, then do that for each number
    # eg. [1,2,3,4,7,6,8,9,10] would be [1,1,1,3,1,1,1,1,0]
    """
    we can use monotonic stack for this because we just looking one after other each time
    1. create a result list initialized with zeros
    2. create an empty stack to store the indices of days
    3. iterate through the temperatures
    4. while the current temperature is warmer than the temperature at the index on top of the stack push the current day's index onto the stack
    6. return the result list
    """
    # TODO: for each day, return how many days you'd wait for a WARMER temperature.
    #   Put 0 if no warmer day ever comes.
    #   Example: [73,74,75,71,69,72,76,73]  ->  [1,1,4,2,1,1,0,0]
    result = [0] * len(temps)
    stack = []

    for i in range(len(temps)):

        while stack and temps[i] > temps[stack[-1]]:
            previous_day = stack.pop()
            result[previous_day] = i - previous_day

        stack.append(i)

    return result


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    # grid of numbers with 1 and 0 1 being land and 0 being water, sub ararys below given if the same position connect the land together to form multiple isalnds, take paramter find how many islands there are
    # eg. 
    """
    ["10110",
    "10100",
    "00001",
    "11001"]
    Island 1, the two 1s in the first column are connected vertically
    Island 2, the two 1s in the third column are connected vertically
    Island 3, the 1 in the first row, fourth column is connected to Island 2 horizontally
    Island 4, the two 1s in the last column are connected vertically
    Island 5, the two 1s in the last row, first and second columns are connected horizontally
    gives 5
    """
    # use depth first search because we can just go look into each kind of sub array deeper each time to keep finding if there is island or not
    """
    create a counter to keep track of the number of islands
    create a set to keep track of land cells that have already been visited
    loop through every row and column in the grid
    whenever we find a "1" that hasn't been visited:
    while the stack isn't empty:
    - remove a cell from the stack
    - mark it as visited
    - check its four neighbours (up, down, left, right)
    - if a neighbour is land and hasn't been visited, add it to the stack
    continue until all connected land cells have been explored
    once the stack is empty, continue searching the rest of the grid for another island
    return the island counter
    """
    
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    visited = set()
    islands = 0

    for r in range(rows):
        for c in range(cols):

            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1

                stack = [(r, c)]

                while stack:
                    row, col = stack.pop()

                    if (row, col) in visited:
                        continue

                    visited.add((row, col))

                    directions = [
                        (0, 1),   # right
                        (0, -1),  # left
                        (1, 0),   # down
                        (-1, 0)   # up
                    ]

                    for dr, dc in directions:
                        nr = row + dr
                        nc = col + dc

                        if (0 <= nr < rows and
                            0 <= nc < cols and
                            grid[nr][nc] == "1" and
                            (nr, nc) not in visited):

                            stack.append((nr, nc))

    return islands



def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    


if __name__ == "__main__":
    main()
