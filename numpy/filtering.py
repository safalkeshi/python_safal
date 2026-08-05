import numpy as np
ages  =np.array([[21,17,19,16,30,18,65],
                  [39,22,15,99,18,20,21]])
teenagers = ages[ages < 18]
print(teenagers)