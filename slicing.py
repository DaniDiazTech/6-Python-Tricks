# Reversing lists
lst = ["Fun", "is", "Programming"]

lst = lst[::-1]

print(lst) # ['Programming', 'is', 'Fun']

# Reversing strings

string = "Dog running on the park"

string = string[::-1]

print(string) # krap eht no gninnur goD

def cutoff(seq, index):
    if not len(seq) > index:
        return "Sorry the index is bigger than the sequence"

    return seq[:index]

long_string = "This is a long description of a blog post about Python and technology"
print(cutoff(long_string, 15))
# This is a long 
print(cutoff(long_string, 70))
# Sorry the index is bigger than the sequence
    