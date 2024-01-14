import torch.nn as nn

class Model_autoencoder_Conv(nn.Module):
  def __init__(self):
    super(Model_autoencoder_Conv, self).__init__()
    self.En1 = nn.Sequential(
      nn.Conv2d(3, 8, kernel_size=3, padding=1),
      nn.BatchNorm2d(8),
      nn.ELU())
    self.En2 = nn.Sequential(
      nn.Conv2d(8, 16, kernel_size=4, padding=1, stride=2),
      nn.BatchNorm2d(16),
      nn.ELU())
    self.En3 = nn.Sequential(
      nn.Conv2d(16, 32, kernel_size=4, padding=1, stride=2),
      nn.BatchNorm2d(32),
      nn.ELU())
    self.En4 = nn.Sequential(
      nn.Conv2d(32, 64, kernel_size=3, padding=1),
      nn.BatchNorm2d(64),
      nn.ELU())

    self.Dec1 = nn.Sequential(
      nn.Conv2d(64, 32, kernel_size=3, padding='same'),
      nn.BatchNorm2d(32),
      nn.ELU())
    self.Dec2 = nn.Sequential(
      nn.ConvTranspose2d(32, 16, kernel_size=4, stride=2, padding=1),
      nn.BatchNorm2d(16),
      nn.ELU())
    self.Dec3 = nn.Sequential(
      nn.ConvTranspose2d(16, 8, kernel_size=4, stride=2, padding=1),
      nn.BatchNorm2d(8),
      nn.ELU())
    self.Dec4 = nn.Sequential(
      nn.Conv2d(8, 3, kernel_size=3, padding='same'),
      nn.Sigmoid())

  def encode(self, x):
    x = self.En1(x)
    x = self.En2(x)
    x = self.En3(x)
    x = self.En4(x)
    return x

  def decode(self, z):
    z = self.Dec1(z)
    z = self.Dec2(z)
    z = self.Dec3(z)
    z = self.Dec4(z)
    return z

  def forward(self, x):
    encoder = self.encode(x)
    decoder = self.decode(encoder)
    return decoder