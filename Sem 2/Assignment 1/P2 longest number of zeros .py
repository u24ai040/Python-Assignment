import random
# Generate 100 random integers (either 0 or 1)
random_integers=[random.randint(0, 1) for _ in range(100)]

Longest_run=0
current_run=0

for num in random_integers:
    if num==0:
        current_run+=1
    else:
        if Longest_run<current_run:
            Longest_run=current_run
       
        current_run=0

if Longest_run<current_run:
    Longest_run=current_run

print("Generated List: ", random_integers)
print("Longest run of zeros: ", Longest_run)