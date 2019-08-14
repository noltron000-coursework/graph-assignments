# IMPORTANT NOTE: PLEASE READ THE WRITEUP AT
# https://github.com/noltron000/graph-assignments/blob/master/source/challenges/README.md
# writeup credit should be covered with this readme.


def prepare_knapsack(items, capacity):
    '''
    "capacity" is a numeric value representing a max weight.
    this capacity will be modified as items are added.
    ---
    "storage" is a list (usually a set) of item tuples.
    the tuples inside store an item's name, value, and weight.
    this variable represents all possible items available.
    ---
    "knapsack" is a list (usually a set) of item tuples.
    the tuples inside store an item's name, value, and weight.
    this variable represents desireable items to pack up.
    '''
    # storage is full of items with unknown desireabilities.
    storage = items.copy()
    # knapsack holds desireable items & starts empty.
    knapsack = set()
    # as our knapsack fills up, its capacity will decrease.
    return pack_bag(storage, knapsack, capacity)


def pack_bag(storage, knapsack, capacity):
    # needed to keep things in check
    storage = storage.copy()
    knapsack = knapsack.copy()

    # base case - knapsack is full or storage is empty.
    if capacity == 0 or len(storage) == 0:
        return knapsack

    # extract a random current item from storage
    item = storage.pop()
    # create semantic names
    item_weight = item[2]

    if item_weight > capacity:
        # item's weight is too heavy to fit in knapsack.
        return pack_bag(storage, knapsack, capacity)

    else:
        # imagine a reality where the current item is kept in.
        kept_bag = knapsack.copy()
        kept_bag.add(item)
        kept_bag = pack_bag(
            storage, kept_bag, capacity - item_weight)
        # imagine a reality where the current item is left out.
        left_bag = pack_bag(
            storage, knapsack, capacity)

        # calculate total values of both knapsack.
        # == FIXME ==
        # here is a helper function to determine the total.
        # its O(n), but can be easily improved with refactor.
        def get_value(backpack):
            '''
            used word backpack to avoid confusion with knapsack.
            '''
            result = 0
            for column in (row[1] for row in backpack):
                result += column
            return result

        # use function call to calculate sums.
        kept_in_value = get_value(kept_bag)
        left_out_value = get_value(left_bag)

        # this is where we decide whether to add the item in.
        if kept_in_value >= left_out_value:
            # the knapsack is better with the item kept in!
            return kept_bag
        elif kept_in_value < left_out_value:
            # the knapsack is better with the item left out...
            return left_bag


if __name__ == '__main__':

    # a given capacity of the knapsack
    capacity = 50

    # a list of items w/properties, in no particular order
    # properties are: name, value, weight -- in order.
    items = {
        ('boot', 60, 10),
        ('tent', 100, 20),
        ('water', 120, 30),
        ('first aid', 70, 15),
    }

    knapsack = prepare_knapsack(items, capacity)

    # get value
    value = 0
    for column in (row[1] for row in knapsack):
        value += column

    # get weight
    weight = 0
    for column in (row[2] for row in knapsack):
        weight += column

    terminal_text = (
        'For this input of items (name, value, weight):\n'
        f'\t{items}\n\n'
        'The optimal solution is:\n'
        f'\t{knapsack}\n\n'
        'The total weight is:\n'
        f'\t{weight} / {capacity}\n\n'
        'The total value is:\n'
        f'\t{value}\n'
    )

    print(terminal_text)
