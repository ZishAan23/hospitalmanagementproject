from datetime import date
import fileio
import matplotlib.pyplot as plt

def update_population():
    pd = {} 

    day = date.today()
    print(day)

    pts = fileio.read_file("patient_data.txt")

    population = len(pts)+1
    

    pd = dict(fileio.read_file("population_data.txt"))

    pd[str(day)] = population

    fileio.write_file("population_data.txt", pd)

def plot_graph():
    pd = dict(fileio.read_file("population_data.txt"))
    x = []
    y = []
    
    for i,v in pd.items():
        x.append(i)
        y.append(v)
    plt.xlabel("Day")
    plt.ylabel("Patients")
    plt.title("Patient Amount Graph")
    plt.plot(x, y)
    plt.show()