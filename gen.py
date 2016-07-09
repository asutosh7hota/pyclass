import numpy as np
from StringIO import StringIO
data = "1 2 3/n 4 5 67/n 890123 4"

print np.genfromtxt(StringIO(data), delimiter='/n')

