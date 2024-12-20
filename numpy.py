'''
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.transpose(a)
print(b)
reshape=np.reshape(a,(3,2))
print(reshape)
'''
o/p:
[[1 4]
 [2 5]
 [3 6]]
[[1 2]
 [3 4]
 [5 6]]
'''
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
resize=np.resize(a,(3,3))
print(resize)
'''
o/p:
[[1 2 3]
 [4 5 6]
 [1 2 3]]
'''
import numpy as np
a=np.arange(12)
b=np.reshape(a,(3,4))
print(b)
'''
o/p:
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
import numpy as np
array=np.array([[1,2,3],[4,5,6]])
col_mean=np.mean(array,axis=1)
print(col_mean)
'''
o/p:
[2. 5.]
'''
import numpy as np
array=np.random.rand(6)
print(array)
'''
o/p:
[0.6557627  0.10279066 0.57765896 0.22213781 0.13803875 0.73296955]

