#M代表是矩陣鏈乘法的function
#m先代表乘法所需次數的maximum
import sys
import time
import matplotlib.pyplot as plt

def M(p, i, j, split_points):
    if i == j:
        return 0
    
    m = sys.maxsize
    optimal_split = None
    
    for k in range(i, j):
        scalar_mult = (M(p, i, k, split_points) +
                       M(p, k+1, j, split_points) +
                       p[i-1] * p[k] * p[j])
                       
        if scalar_mult < m:
            m = scalar_mult
            optimal_split = k
    
    split_points[i][j] = optimal_split
    
    return m

#split_points[i][j]代表的是從第i個矩陣道第j個矩陣的最佳切分點
def optimal_parenthesis(split_points, i, j):
    if i == j:
        print("A" + str(i), end="")
        return
    
    print("(", end="")
    optimal_parenthesis(split_points, i, split_points[i][j])
    optimal_parenthesis(split_points, split_points[i][j] + 1, j)
    print(")", end="")




def optimal_matrix_chain_mult(p):
    n = len(p) - 1 
    
    split_points = [[0] * (n+1) for _ in range(n+1)]
    
    min_scalar_mult = M(p, 1, n, split_points)
    
    print("Min multiplications:", min_scalar_mult)
    print("Optimal Parenthesis:", end=" ")
    optimal_parenthesis(split_points, 1, n)
    print()



def optimal_mult(p):
    n = len(p) - 1
    
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]
    
    for i in range(n):
        m[i][i] = 0
    
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = sys.maxsize
            
            for k in range(i, j):
                temp_cost = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                
                if temp_cost < m[i][j]:
                    m[i][j] = temp_cost
                    s[i][j] = k
    
    min_scalar_mult = m[0][n - 1]
    
    print("Minimum scalar multiplications:", min_scalar_mult)
    print("Optimal Parenthesis:", end=" ")
    print_optimal_parenthesis(s, 0, n - 1)
    print()




def print_optimal_parenthesis(s, i, j):
    if i == j:
        print("A" + str(i + 1), end="")
        return
    
    print("(", end="")
    print_optimal_parenthesis(s, i, s[i][j])
    print_optimal_parenthesis(s, s[i][j] + 1, j)
    print(")", end="")


time1 = []
print("==============brute_force=================")
matrix_chain = [5,10,3,12]
for i in range(13):
    matrix_chain.append(5)
    start = time.time()
    optimal_matrix_chain_mult(matrix_chain)
    end = time.time()
    execution_time = end - start
    print("Execution time:", execution_time)
    time1.append(execution_time)

time2 = []
print("==============dynamic=================")
matrix_chain = [5,10,3,12]
for i in range(13):
    start = time.time()
    matrix_chain.append(5)
    optimal_mult(matrix_chain)
    end = time.time()
    execution_time = end-start
    print("Execution time:", execution_time)
    time2.append(execution_time)
# print(time1)
# print(time2)
plt.plot(time1, label="Brute-Force",marker = "o",linewidth = 1,color = 'r')
plt.plot(time2, label="Dynamic",marker = "o",linewidth = 1,color = 'b')
plt.title("Algorithm assignment graphs")
plt.xlabel("Input Size")
plt.ylabel("Exec Time (seconds)")
plt.legend()
plt.show()






