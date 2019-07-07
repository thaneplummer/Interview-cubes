"""

interview-cubes.py

--tkp

From the book "How to crack the coding interview".

Problem: find all the positive integer solutions less than 1,000 for a^3 + b^3 = c^3 + d^3

"""


cubes = [i**3 for i in range(1, 1001)]
solutions = []
pairmap = {}

def get_pairs(nums):
    for a in nums:
        for b in nums:
            pairsum = a + b
            ab = (a,b) if a < b else (b,a)
            if pairsum in pairmap.keys():
                (c,d) = pairmap[pairsum]
                if c != a and c != b:
                    solution = (ab, (c,d))
                    if solution not in solutions:
                        solutions.append(solution)
            else:
                pairmap[pairsum] = (a,b)
    return solutions


if __name__ == "__main__":
    pairs = get_pairs(cubes)
    print(len(pairs))
    for pair in pairs:
        print(pair)
    print(len(pairs))
