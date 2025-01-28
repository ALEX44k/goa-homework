# Training on isograms.
def is_isogram(string):
    return len(set(list(string.lower()))) == len(string)

#


#Training on exes and ohs
def xo(s):
      return s.lower().count('o') == s.lower().count('x')


