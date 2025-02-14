import numpy as np
import matplotlib.pyplot as plt

def simulate_clt(sample_size=10, num_samples=1000, distribution='uniform'):
    """
    Simulates the Central Limit Theorem (CLT) by taking multiple samples from a chosen distribution,
    computing their means, and visualizing how the distribution of sample means approaches a normal distribution.

    Parameters:
    - sample_size: Number of values in each sample.
    - num_samples: Number of samples taken.
    - distribution: Type of distribution to sample from ('uniform', 'exponential', or 'poisson').
    """
    
    # Generate samples based on the selected distribution
    if distribution == 'uniform':
        data = np.random.uniform(low=0, high=10, size=(num_samples, sample_size))
    elif distribution == 'exponential':
        data = np.random.exponential(scale=2, size=(num_samples, sample_size))
    elif distribution == 'poisson':
        data = np.random.poisson(lam=5, size=(num_samples, sample_size))
    else:
        raise ValueError("Unsupported distribution. Choose from 'uniform', 'exponential', or 'poisson'.")
    
    # Compute sample means
    sample_means = np.mean(data, axis=1)
    
    # Plot histogram of sample means
    plt.figure(figsize=(10, 6))
    plt.hist(sample_means, bins=30, density=True, alpha=0.7, color='blue', edgecolor='black')
    plt.title(f'Distribution of Sample Means (N={sample_size}, {distribution.capitalize()} Dist.)')
    plt.xlabel('Sample Mean')
    plt.ylabel('Density')
    plt.grid()
    plt.show()

# Run simulation for different distributions
simulate_clt(sample_size=5, num_samples=1000, distribution='uniform')
simulate_clt(sample_size=5, num_samples=1000, distribution='exponential')
simulate_clt(sample_size=5, num_samples=1000, distribution='poisson')
