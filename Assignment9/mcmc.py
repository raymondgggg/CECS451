import random
tMatrix = [
            [0.9321, 0.0069, 0.0061, 0.0000],
            [0.4993, 0.1620, 0.0000, 0.3448],
            [0.4395, 0.4701, 0.0909, 0.0000],
            [0.0000, 0.1552, 0.4091, 0.4357] 
                                                ]

states = [
            [True, False, True, True],
            [True, False, False, True],
            [False, False, True, True],
            [False, False, False, True]
                                        ]

def partB():
    print("Part B. The transition probability matrix")
    print(f"     S1     S2     S3     S4")
    for row in tMatrix:
        print(f"S{tMatrix.index(row) + 1}", end = " ")
        for col in tMatrix[tMatrix.index(row)]:
            print(f"{col:.4f}", end = " ")
        print()
    print()

def partA():
    print("Part A. The sampling probabilities")
    print("P(C|-s,r) = <0.8780, 0.1220>")
    print("P(C|-s,-r) = <0.3103, 0.6897>")
    print("P(R|c,-s,w) = <0.9863, 0.0137>")
    print("P(R|-c,-s,w) = <0.8182, 0.1818>")
    print()


def partC():
    state0 = states[random.randint(0,3)]
    stateN = state0
    statesCounts = [0] * 4
    for n in range(1_000_000):
        selectionVal = random.uniform(0,1)
        if selectionVal < tMatrix[states.index(stateN)][0]:
            stateN = states[0]
            statesCounts[0] += 1
        elif selectionVal < sum(tMatrix[states.index(stateN)][:2]):
            stateN = states[1]
            statesCounts[1] += 1
        elif selectionVal < sum(tMatrix[states.index(stateN)][:4]):
            stateN = states[2]
            statesCounts[2] += 1
        else:
            stateN = states[3]
            statesCounts[3] += 1

    c = (statesCounts[0] + statesCounts[1]) / 1_000_000
    c_not = (statesCounts[2] + statesCounts[3]) / 1_000_000
    print(statesCounts)
    print("Part C. The probability for the query")
    print(f"P(C|-s,w) = <{c:.4f},{c_not:.4f}>")

        
    





if __name__ == "__main__":
    partA()
    partB()
    partC()





