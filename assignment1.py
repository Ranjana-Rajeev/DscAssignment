thriller=["Dark","Mindhunter","Parasite","Inception","Insidious","Interstellar","Prison Break","Money Heist","War","Jack Ryan"]
comedy=["Friends","3 Idiots","Brooklyn 99","How I Met Your Mother","Rick And Morty","The Big Bang Theory","The Office","Space Force"]
i=0
movie=input("Enter the movie:")
if movie==thriller[i]:
    print("It is a thriller")
elif movie==comedy[i]:
    print("It is a comedy")
else:
    print("It's neither thriller nor comedy")
