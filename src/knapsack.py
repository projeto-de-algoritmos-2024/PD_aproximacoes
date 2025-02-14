"""
    Written by BCl0c, whose aproximation will take you most probably nowhere.

    0. first steps
        https://en.wikipedia.org/wiki/Knapsack_problem -> read this, pretty please.
            Most of this algorithm approach is based on this wiki article.

        next, take a look at the chapter 6 in the Tardos' algorithm design.
        That's that. 

        The book is not very didatic, but at least it provides some initial 
        guiding light to constructing the algorithm.

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
            takes as much as possible of the most value per weight unit
            rate and goes along like that. 
        
"""

import random
SEED = 123

TESTING_RANGE = 10000
TESTING_STEP = 100


def problemGenerator(n: int, max_weight, max_value, s = SEED ):
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
                    [DEFAULT]s to 123 or, more specifically, the 
                    SEED constant. 

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
    generator = random
    #initializes with passed seed
    generator.seed(s)

    for _ in range(n):
        items.append([generator.randint(1, max_weight) , generator.randint(1, max_value)])
   
    return items

def knapsackGR(items: list, weight):
    """
        knapsack algorithm GREED RAT version.
        
        aproximates the algorithm using the
        coveted value per weight rate.

        should run very violently fast compared
        to dynamic, as it is a true linear
        version. Not optimal in the very least,
        though.

        That said, algorithm is as simple as it gets with the correct
        data structures and methods.

    """

    items.sort( key = lambda x : x[1]/x[0]) #this should sort the items by value/weight rate
    items.reverse()
    #print(items)
    took = []

    #very retarded, very simple.
    #its greed, after all, depends on the sorting you do.
    for item in items:
        if weight - item[0] < 0:
            continue
        took.append(item)
        weight -= item[0]
    
    return took
            
    

    

def knapsackDI(items, weight):
    """
        Dynamic Iterative version.
        Creates the 2d matrix, initializes it,
        and runs. 

        Much harder to implement compared to greed.
        Greed also returns the set of items much faster, too.

        In general, not useful for real time application. Very 
        precise though.

        Input:
            items -> the list of items available
            weight -> the max weight of the theoretical backpack

        Output:
            the set of items used.
    """

    # sort this sucker by value.
    items.sort(key = lambda x: x[0])
    # initialize our matrix
    matrix = []
    for _ in range(len(items) + 1):
        matrix.append([0 for _ in range(weight + 1)]) #initialize matrix as all 0
    vec = []
    #then, we process, ignoring the first line and column.
    for i in range(1, len(matrix)):
        this_item = items[i - 1]
        for j in range(1, len(matrix[0])):
            #don't take value is always top.
            dt = matrix[i-1][j]
            #can take needs further processing...

            #if the remaining weight j - 1 is greater than 1, then
            w_offset = j - this_item[0]
            if  w_offset >= 0:
                ct = this_item[1] + matrix[i-1][w_offset]
            else:
                ct = 0
            matrix[i][j] = max([dt, ct])
    # DEBUG
    #for line in matrix:
    #    print(line)

    i = len(matrix) - 1
    j = len(matrix[0]) - 1
    res = []
    while matrix[i][j] != 0:
        #meaning it took the item
        if matrix[i][j] > matrix[i-1][j]:
            #then, append it to res, 
            res.append(items[i - 1])
            #go to next item
            i -= 1 
            #and subtract available weight
            j -= items[i][0]
        else:
            #else we go up.
            i -= 1 
    return res

def run_comparison(n: int) -> list:
    """
        tests greedy and optimum algorithm. Do not pass
        a very big n if you don't plan on testing the TLE of
        the optimum. It will alocate pretty much all memory available
        and it will crash the script.

        input:
            n -> the number of items to generate
        output:
            a list containing:
                time of execution for the Greedy
                time of execution for the Optimal
                aproximation rate
            IN THIS ORDER.
    
    """
    import timeit
    import random

    print(f'running comparison for n = {n}')

    try:
        a = int(n)
    except ValueError:
        print("not int. quiting")
        quit()
    b = a
    #print("generating items")
    items = problemGenerator(a, a, a, b)
    #print("generation done.")
    #print("---------------------------")
    #print("starting knapsack greedyrat version!")
    start = timeit.default_timer()
    res_aprox = knapsackGR(items, a)
    stop = timeit.default_timer()
    time_greed = stop-start
    #print(f'GREEDY TOOK {time} SECONDS.')
    #print("---------------------------")
    #print("starting knapsack iterative optimal version!")
    start = timeit.default_timer()
    res_opt = knapsackDI(items, a)
    stop = timeit.default_timer()
    time_opt = stop-start
    #print(f'ITERATIVE OPTIMAL TOOK {time} SECONDS.')
    sum_aprox = 0
    sum_opt = 0
    for i in res_aprox:
        sum_aprox += i[1]
    for i in res_opt:
        sum_opt += i[1]

    #print(f'ITERATIVE RESULT -> {sum_opt}')
    #print(f'GREEDY RESULT -> {sum_aprox}')
    #print(f'GREEDY APROXIMATION RATE: {sum_aprox/sum_opt}')
    aprox_rate = sum_aprox/sum_opt

    return [time_greed, time_opt, aprox_rate]

if __name__ == "__main__":
    """ TESTBATCH!
    print("TEST 1: PROBLEM GENERATOR AND ITS CONSEQUENCES TO HUMANITY")
    
    print(problemGenerator(20, 20, 20, as_list=True))
    print(problemGenerator(10, 10, 10))
    """
    """
    print("TEST 2: KNAPSACK DI")
    wares = problemGenerator(20,20,20)
    wares.sort(key = lambda x: x[0])
    print(wares)
    print(knapsackDI(wares, 20))

    print("TEST 3: KNAPSACK GR")
    print(knapsackGR(wares, 20))
    """
    import matplotlib.pyplot as plt
    import gc
    print("STARTING EXECUTION OF THE COMPARISON ROUTINE!")
    number_of_items = []
    greed_times = []
    opt_times = []
    aprox_rates = []
    zetta: list
    for i in range(10, TESTING_RANGE, TESTING_STEP):
        number_of_items.append(i)
        zetta =  run_comparison(i)
        greed_times.append(zetta[0])
        opt_times.append(zetta[1])
        aprox_rates.append(zetta[2])

    fig, ax = plt.subplots(ncols=2, figsize = (10,10), layout = "constrained")
    curve_greed = ax[0].plot(number_of_items, greed_times, label = "Greed Time Curve")
    curve_opt   = ax[0].plot(number_of_items, opt_times, label = "Dynamic Time Curve")
    curve_rate  = ax[1].plot(number_of_items, aprox_rates, label =  "Aproximation rate Greed/Optimal")


    ax[0].set_xlabel('Number of Items')
    ax[0].set_ylabel('Time')
    ax[0].set_title('Time Curve Comparison')

    ax[1].set_ylim([0, 1.5])
    ax[1].set_xlabel('Number of Items')
    ax[1].set_ylabel('Aproximation Rate')
    ax[1].set_title('Aproximation Rates')

    ax[0].legend()
    ax[1].legend()
    plt.show()

    print("finished...")











