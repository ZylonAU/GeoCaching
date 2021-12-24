test = '''
Notice how roos can hop with no break for great distances?

These amazing wonders of the outback can keep going and going for hours. A good set of big hind legs make the long hops possible.

On the national emblem, they can be controlled by the use of culling.

Balance is via a strong, chunky tail.

Hop speed for a red kangaroo (less slow than you thought) is near eighteen or so MPH, sometimes between the roadside and a car. Wikipedia has extra info.
'''

import re

print(''.join(re.findall('[A-Za-z]+', test))[11::12])
