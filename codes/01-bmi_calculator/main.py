
print(r'''
ooo        ooooo                  oooooooooo.  ooo        ooooo ooooo
`88.       .888'                  `888'   `Y8b `88.       .888' `888'
 888b     d'888  oooo    ooo       888     888  888b     d'888   888
 8 Y88. .P  888   `88.  .8'        888oooo888'  8 Y88. .P  888   888
 8  `888'   888    `88..8'         888    `88b  8  `888'   888   888
 8    Y     888     `888'          888    .88P  8    Y     888   888
o8o        o888o     .8'          o888bood8P'  o8o        o888o o888o
                 .o..P'
                 `Y8P'
                                                  ''')
                                                  
print(r'''
                                                                             
 __  __   ___                           /|         __  __   ___   .--\ 
|  |/  `.'   `..-.          .-          ||        |  |/  `.'   `. |__| 
|   .-.  .-.   '\ \        / /          ||        |   .-.  .-.   '.--. 
|  |  |  |  |  | \ \      / /           ||  __    |  |  |  |  |  ||  | 
|  |  |  |  |  |  \ \    / /            ||/'__ '. |  |  |  |  |  ||  | 
|  |  |  |  |  |   \ \  / /             |:/`  '. '|  |  |  |  |  ||  | 
|  |  |  |  |  |    \ `  /              ||     | ||  |  |  |  |  ||  | 
|__|  |__|  |__|     \  /               ||\    / '|__|  |__|  |__||__| 
                     / /                |/\'..' /                      
                 |`-' /                 '  `'-'`                       
                  '..'                                                
      ''')

# Daryafte Ghad va Vazne Kaarbar
w = input("Please enter your weight (in kg): ")
h = input("Please enter your height (in cm): ")

# Error handling (check if input is digit)
if w.replace(".", "").isdigit() and h.replace(".", "").isdigit():
    w = float(w)
    h = float(h)
    h /= 100  # h = h/100

    # Mohasebeye BMI
    bmi = w / h**2
    bmi = round(bmi, 1)

    # Gozaresh be karbar
    print(f"Your BMI is: {bmi} kg/m^2 because your weight is {w}",
          f"and your height is {h*100}")

    # Tamrin2: Classhaye chaaghi ra ham be sharthaaye zir ezafe konid
    if bmi<18.5:
        status = 'Underweight'
        color = '\033[33;1m'
    elif bmi<=25:
        status = 'Normal'
        color = '\033[32;1m'
    elif bmi<=30:
        status = 'Overweight'
        color = '\033[35;1m'
    else:
        status = 'Obese'
        color = '\033[31;1m'
    
    print(f'Your bmi is {color}{bmi:.2f}\033[0m and your',
          f'status is: {color}{status} \033[0m')

    # Tamrin3: Meghdaare ezafe ya kamboode vazn ra ham gozaresh dahid

else:
    print("Invalid input: Bayad addad vared konid")
