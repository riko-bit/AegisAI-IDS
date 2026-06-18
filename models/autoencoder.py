import torch
import torch.nn as nn

# Define the Autoencoder neural network model
# Autoencoders learn how to reconstruct normal input data
class Autoencoder(nn.Module):

    def __init__(self,input_dim):

        # Initialize parent PyTorch module
        super().__init__()

        # Encoder part of the network
        # Compresses input features into a smaller representation
        self.encoder=nn.Sequential(
            nn.Linear(input_dim,128),   # Reduce input features to 128 neurons
            nn.ReLU(),                  # Activation function
            nn.Linear(128,64),          # Further compression
            nn.ReLU(),
            nn.Linear(64,32)            # Final encoded representation (latent space)
        )

        # Decoder part of the network
        # Reconstructs the original input from the compressed representation
        self.decoder=nn.Sequential(
            nn.Linear(32,64),           # Expand latent space back to higher dimension
            nn.ReLU(),
            nn.Linear(64,128),
            nn.ReLU(),
            nn.Linear(128,input_dim)    # Reconstruct original number of input features
        )

    # Forward pass through the network
    def forward(self,x):

        # Encode the input into compressed latent features
        encoded=self.encoder(x)

        # Decode the compressed features back to original size
        decoded=self.decoder(encoded)

        # Return reconstructed output
        return decoded