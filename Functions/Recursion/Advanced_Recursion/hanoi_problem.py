# 4. Create a recursive function to solve the Towers of Hanoi problem for three pegs.

def TOH(numbers, start, aux, end):
    if numbers == 1:
        print(f"Move disk 1 from {start} to {end}")
        return
    TOH(numbers-1, start, end, aux)
    print("Move disk", numbers, "from", start, "to", end)
    TOH(numbers-1, aux, start, end)

disc = 3
TOH(disc, "A", "B", "C")