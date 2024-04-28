# genetic algorithm search of the one max optimization problem
import numpy as np
import os


def main():
    if os.path.exists("GA3.txt"):
        os.remove("GA3.txt")

    print("Generating Population ...")
    pop = [np.random.randint(1, 31, 4).tolist() for _ in range(6)]
    print(f" Population of the first Generation : {pop}")

    print("Objective function : abs(sum([a,b,c,d]) - 30)")
    print("Fitness Function : 1/(1+abs(sum([a,b,c,d]) - 30))")
    def objective(x): return abs(sum(x) - 30)

    for iter in range(1, 10):
        print(f"Generation {iter} :")
        Fitness_Fn = []
        for i, p in enumerate(pop):
            print(f"Fitness Function [{i+1}] : {1/(1+objective(p))}")
            Fitness_Fn.append(1/(1+objective(p)))

        if max(Fitness_Fn) == 1:
            with open("GA3.txt", "a") as f:

                f.write(f"Generation {iter} : \n")
                f.write(f"Population (Last Children) : {pop} \n")
                f.write(f"Fitness Function : {Fitness_Fn} \n")
                f.write("\n")

            print("Done !")
            break

        proba = [i/sum(Fitness_Fn) for i in Fitness_Fn]

        cum_sum = np.cumsum(proba)
        del proba

        random_proba = np.random.rand(6)

        # random selection , not tournament selection
        selected = []
        for r in random_proba:
            for i, csum in enumerate(cum_sum):
                if r < csum:
                    selected.append(pop[i])
                    break

        children = []
        for i in range(0, 6, 2):
            p1, p2 = selected[i], selected[i+1]
            pt = np.random.randint(1, 3)
            c1 = p1[:pt] + p2[pt:]
            c2 = p2[:pt] + p1[pt:]
            children.append(c1)
            children.append(c2)

        print(f"Children : {children}")
        # mutation probability  = 1/4
        print("Mutation ...")
        for c in children:
            for i in range(4):
                if np.random.rand() < 0.25:
                    c[i] = np.random.randint(1, 31)
        print(f"Mutated Children : {children}")

        # write each population and fitness function to a file
        with open("GA3.txt", "a") as f:
            f.write(f"Generation {iter} : \n")
            f.write(f"Population : {pop} \n")
            f.write(f"Fitness Function : {Fitness_Fn} \n")
            f.write(f"Children : {children} \n")
            f.write("\n")

        pop = children


main()
