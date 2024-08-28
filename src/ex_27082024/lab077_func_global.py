


public_toilet = "PB"

# local variables have more preference as compare to public variables

def home():
    private_toilet = "PT"
    print(private_toilet)
    public_toilet = "LPB"       # we can change the global variable value within the function
    print(public_toilet)


home()


def strange():
   print(public_toilet)
    # print(private_toilet)

strange()
print(public_toilet)
#print(private_toilet)