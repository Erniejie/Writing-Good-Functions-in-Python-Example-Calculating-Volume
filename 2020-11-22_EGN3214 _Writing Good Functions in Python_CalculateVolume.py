# WRITING PYTHON CODE EFFICIENTLY

# 1. Functions Ought to have a clear purpose
# 2. Input should be clearly and concisely Defined
# 3. Output should be clearly and concised Defined

#CASE 1- General Case

def CalculateVolume(P_atm,n_moles,T_kelvin):

    # Returns Volume in Litres
    # P_atm : atmospheric Pressure in atmospheres
    # n_moles : Moles of Gas
    # T_kelvin: Temperature in Kelvin

    result = 0.0821*n_moles*T_kelvin/P_atm
    return result

T = 273
n = 1
P = [0.5,1,1.5]
V = []

for p in P:
    V.append(CalculateVolume(p,n,T))

print("Pressures: ", P)
print("Volumes: ", V)




#CASE 2: ASSIGNING DEFAULT VALUES:


"""
def CalculateVolume(P_atm=1,n_moles=1,T_kelvin=273):

    # Returns Volume in Litres
    # P_atm : atmospheric Pressure in atmospheres
    # n_moles : Moles of Gas
    # T_kelvin: Temperature in Kelvin

    result = 0.0821*n_moles*T_kelvin/P_atm
    return result

T = 273
n = 1
P = [0.5,1,1.5]
V = []

for p in P:
    V.append(CalculateVolume(p,n,T))

print("Pressures: ", P)
print("Volumes: ", V)

print(CalculateVolume())          #   Prints out default values

# FLEXIBILITY OF A FUNCTION:Example of modifying default Values: setting a new Temperature Value..
#... this operation overrides the default value of temperature of 273K.
print(CalculateVolume(T_kelvin=350))
"""


    

    
