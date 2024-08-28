

# Function with global variable

public_toilet = "PB"


def home():
    private_toilet = "PT"
    print(public_toilet)   #PB
    print(private_toilet)  #PT

#home()
def strange():
    print(public_toilet)   #PB
    #print(private_toilet)   # private_toilet is undefined within a function/globally

strange()

print(public_toilet)
#print(private_toilet)    # we can't call outside the function bcoz its defined within the func