import pickle as pkl
import torch
from My_functions import show_orig_pred
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open(f'../data10.pkl', "rb") as f:
    train = pkl.load(f)
train = torch.from_numpy(train.transpose(0, 3, 1, 2))
autoencoder = torch.load('autoencoder_exp1.pkl')
autoencoder.eval()
pred = autoencoder(train[350].unsqueeze(0).to(device))
show_orig_pred(train[350], pred)