import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import numpy as np
from torch.utils.data import DataLoader, TensorDataset

#%%
import pandas as pd
import pyreadstat

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd


import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import numpy as np
from torch.utils.data import DataLoader, TensorDataset


#%%
input_file = "RT Brainstem.sav"  # مسیر فایل sav

# df, meta = pyreadstat.read_sav(input_file)
df = pd.read_csv("./RT.csv")

df = df[["coppre", "voxelpre", "zpre","BSCpre", "group"]]

df[["group"]] = df[["group"]].applymap(lambda x: 1 if x == 1 else 2)

df1 = df[df['group'] == 1]
df2 = df[df['group'] == 2]


df1 = df1.drop(columns=['group'])     

print(df1)


#%%
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

df = df1
# Normalize data for training the GAN
data_min = df.min()
data_max = df.max()
norm_data = (df - data_min) / (data_max - data_min)

# Convert normalized data to torch tensor
norm_data_tensor = torch.tensor(norm_data.values, dtype=torch.float32)

# Generator
class Generator(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(Generator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, 32),
            nn.LeakyReLU(0.2),
            nn.BatchNorm1d(32),
            nn.Linear(32, 64),
            nn.LeakyReLU(0.2),
            nn.BatchNorm1d(64),
            nn.Linear(64, output_dim),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.model(x)

# Discriminator
class Discriminator(nn.Module):
    def __init__(self, input_dim):
        super(Discriminator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_dim, 64),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.3),
            nn.Linear(64, 32),
            nn.LeakyReLU(0.2),
            nn.Dropout(0.3),
            nn.Linear(32, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        return self.model(x)

# Parameters
input_dim = 4  # Number of features in your dataset
latent_dim = 8  # Latent space dimension

generator = Generator(latent_dim, input_dim)
discriminator = Discriminator(input_dim)

# Optimizers
g_optimizer = optim.Adam(generator.parameters(), lr=0.0001, betas=(0.5, 0.999))
d_optimizer = optim.Adam(discriminator.parameters(), lr=0.0001, betas=(0.5, 0.999))

# Loss function
criterion = nn.BCELoss()

# Training the GAN
def train_gan(data, epochs, batch_size):
    d_losses = []
    g_losses = []

    for epoch in range(epochs):
        for _ in range(len(data) // batch_size):
            # Train Discriminator
            idx = np.random.randint(0, data.shape[0], batch_size)
            real_data = data[idx]

            noise = torch.randn(batch_size, latent_dim)
            fake_data = generator(noise).detach()

            real_labels = torch.ones((batch_size, 1)) * 0.9  # Label smoothing
            fake_labels = torch.zeros((batch_size, 1))

            d_loss_real = criterion(discriminator(real_data), real_labels)
            d_loss_fake = criterion(discriminator(fake_data), fake_labels)
            d_loss = d_loss_real + d_loss_fake

            d_optimizer.zero_grad()
            d_loss.backward()
            d_optimizer.step()

            # Train Generator
            noise = torch.randn(batch_size, latent_dim)
            valid_labels = torch.ones((batch_size, 1))
            g_loss = criterion(discriminator(generator(noise)), valid_labels)

            g_optimizer.zero_grad()
            g_loss.backward()
            g_optimizer.step()

        # Store losses
        d_losses.append(d_loss.item())
        g_losses.append(g_loss.item())

        # Print losses every 100 epochs
        if epoch % 100 == 0:
            print(f"Epoch {epoch}/{epochs} | D Loss: {d_loss.item()} | G Loss: {g_loss.item()}")

    return d_losses, g_losses

# Train the GAN
d_losses, g_losses = train_gan(norm_data_tensor, epochs=1000, batch_size=4)

# Plot the learning curves
plt.figure(figsize=(10, 5))
plt.plot(d_losses, label="Discriminator Loss")
plt.plot(g_losses, label="Generator Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("GAN Training Losses")
plt.legend()
plt.show()

# Generate synthetic data
noise = torch.randn(30, latent_dim)
synthetic_data = generator(noise).detach().numpy()

# Rescale synthetic data back to original scale
synthetic_data_rescaled = synthetic_data * (data_max - data_min).values + data_min.values
synthetic_df = pd.DataFrame(synthetic_data_rescaled, columns=df.columns)

# Combine original and synthetic data
combined_df = pd.concat([df, synthetic_df], ignore_index=True)

combined_df['coppre'] = combined_df['coppre'].round(2)
combined_df['voxelpre'] = combined_df['voxelpre'].round(0)
combined_df['zpre'] = combined_df['zpre'].round(3)
combined_df['BSCpre'] = combined_df['BSCpre'].round(3)
combined_df["group"] = 1

print(combined_df)

combined_df.to_csv("G1RT-A.csv")



