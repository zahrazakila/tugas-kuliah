print("Nama\t: Zahra Zakila Aninda Rahmanti \nNIM\t: 23106050019\nProdi\t : Informatika")
def seidel(a, x ,b):        
    n = len(a)                    
    for j in range(0, n):         
        # temp variable d to store b[j] 
        d = b[j]                   

        # to calculate respective xi, yi, zi 
        for i in range(0, n):      
            if(j != i): 
                d-=a[j][i] * x[i] 
        # updating the value of our solution         
        x[j] = d / a[j][j]

    # returning our updated solution            
    return x
n = 3                              

x = [0, 0, 0]                         
a = [[4, 1, 2],[3, 5, 1],[1, 1, 3]] 
b = [4,7,3]

print("Persamaan A = ",a)
print("Hasil B = ",b)
print("x = ",x)

for i in range(0, 25):             
    x = seidel(a, x, b) 
    #print each time the updated solution 
    print("Current x = ",x) 
print("x1, x2, x3 = ",x)