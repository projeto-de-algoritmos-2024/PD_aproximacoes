"""
    Written by BCl0c, whose aproximation will take you most probably nowhere.

    1. Introduction - the problem
        Given some max-weight and some items,
        what items should one take to optimize the
        value one holds in his backpack/knapsack?

        Items are stored as uniques, so there's no
        way to indicate there should be n of x item
        without further processing to create the n new
        lines in the matrix we would need if we added
        these new lines. Optimum has this limitation,
        but greed generally does not care.

    2. Algorithms
        2.1. The optimum I - iterative
            This version aims to fill a weight_interval X items
            matrix from bottom to top.
        
        2.2. The optimum II - purely recursive
            This goes along trying to fill only the squares needed for the algorithm 
            to work. May also be done with a pure recursion, but the pure recursion version
            will use much of the machine's stack. Beware of this.

        2.3 T_O III - recursion memo
            Will take a look at the memo matrix as much as possible.
            Will try to reach matrix borders very fast, so it gets answers
            fast too.
        
        2.3. Aproximation I - Greediest of rats
        
"""

import random

class item:

    def __init__(self, w, v):
        self.weight = w
        self.value  = v
    
    def item_to_list(self):
        """
            returns item values as a dictionary
        """

        return { 'weight': self.weight , 'value':self.value }
    
    def get_item_rate(self):
        """
            returns a value/weight rate;
            useful for greedy aproximation.
        """

        return int(self.value/self.weight)


def problemGenerator(n: int, max_weight, max_value, as_list = False, s = 123 ):
    """
        input: 
            n -> the number of items we plan to generate
            max_weight -> the max weight an item may have
            max_value -> the maximum value an item may have

            KEYWORD ARGUMENTS:
                as_list
                    if False [DEFAULT]:
                        creates a list of item objects and returns 
                        as such.
                    if True:
                        creates a list of items following the structure
                            ITEMS[
                                ITEM0 [ITEM0_WEIGHT , ITEM0_VALUE],
                                ITEM1 [ITEM1_WEIGHT, ITEM1_VALUE],
                                ETC.
                            ]
                        In other words, this kind of structure:
                            [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]]
                        a 2d [n][2] matrix describing the items.
            
                s
                    "s" stands for seed, of course.

                    A number used for the generator function.
                    [DEFAULT]s to 123.

        output: 
            Some list of items, unordered and with the n items specified.
            Items will be returned as objects by default.

        Common and very predictable FOXTROTUNIFORMS (bad usage):
            1. passing a max_weight greater than the available
                weight in the knapsack.
                    The item will never be picked.

            !List will be expanded when I think of more
            MIKEFOXTROTUNIFORMS to put here!
            

    """

    #1. INIT
    items = []
    generator = random()
    #initializes with passed seed
    generator.seed(s)

    if as_list == True:
        for _ in range(n):
            items.append([generator.randint(0, max_weight) , generator.randint(0, max_value)])
    else:
        for _ in range(n):
            items.append(item(generator.randint(0, max_weight), generator.randint(0, max_value)))

def knapsackGR(items):
    """
        knapsack algorithm GREED RAT version.
        
        aproximates the algorithm using the
        coveted value per weight rate.

        should run very violently fast compared
        to dynamic, as it is a true linear
        version. Not optimal in the very least,
        though.

    """
    

def knapsackDI(items):
    """
        Dynamic Iterative version.
        Creates the 2d matrix, initializes it,
        and runs. 
    """
    pass



