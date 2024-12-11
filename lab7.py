import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def run_simulation(N, p, i, initial_infected_ratio, time_steps):
    G = nx.fast_gnp_random_graph(N, p)
    S = np.ones(N, dtype=bool)
    I = np.zeros(N, dtype=bool)
    
    initial_infected = np.random.choice(N, int(N * initial_infected_ratio), replace=False)
    S[initial_infected] = False
    I[initial_infected] = True
    
    prevalence = np.zeros(time_steps)
    
    for t in range(time_steps):
        prevalence[t] = np.sum(I) / N
        
        new_infected = []
        for node in range(N):
            if S[node]:
                neighbors = list(G.neighbors(node))
                infected_neighbors = I[neighbors]
                if np.any(np.random.rand(len(infected_neighbors)) < i):
                    new_infected.append(node)
        
        S[new_infected] = False
        I[new_infected] = True
    
    return prevalence

def average_simulations(N, p, i, initial_infected_ratio, time_steps, num_simulations):
    all_prevalences = np.zeros((num_simulations, time_steps))
    
    for sim in range(num_simulations):
        all_prevalences[sim, :] = run_simulation(N, p, i, initial_infected_ratio, time_steps)
    
    mean_prevalence = np.mean(all_prevalences, axis=0)
    std_prevalence = np.std(all_prevalences, axis=0)
    
    return mean_prevalence, std_prevalence

# Parameters
N = 10**5
initial_infected_ratio = 0.1
time_steps = 100
num_simulations = 10

# Case (i)
p_i = 5.0 / N
i_i = 0.01
mean_prevalence_i, std_prevalence_i = average_simulations(N, p_i, i_i, initial_infected_ratio, time_steps, num_simulations)

# Case (ii)
p_ii = 0.8 / N
i_ii = 0.1
mean_prevalence_ii, std_prevalence_ii = average_simulations(N, p_ii, i_ii, initial_infected_ratio, time_steps, num_simulations)

# Plotting case (i)
time = np.arange(time_steps)
plt.figure(figsize=(12, 6))
plt.errorbar(time, mean_prevalence_i, yerr=std_prevalence_i, label='N=10^5, i=0.01, <k>=5.0', fmt='-o')

# Plotting Case (ii)
plt.errorbar(time, mean_prevalence_ii, yerr=std_prevalence_ii, label='N=10^5, i=0.1, <k>=0.8', fmt='-o')

# finish and show plot 
plt.xlabel('Time Steps')
plt.ylabel('Normalized Prevalence (I/N)')
plt.title('Evolution of Normalized Prevalence (I/N) Over Time')
plt.legend()
plt.show()