def tower_builder(n_floors, block_size):
    tower =[];
    max_size = block_size[0] + (block_size[0] * (n_floors-1) * 2)
    for floor in range(n_floors):
        for _ in range(block_size[1]):
            width = block_size[0] * (floor * 2 + 1)
            tower.append(("*" * width).center(max_size, " "));
    return tower;


print(tower_builder(3, (4, 2)))
print(tower_builder(17, (4, 4)))
