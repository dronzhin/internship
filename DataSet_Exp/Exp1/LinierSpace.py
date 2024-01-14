import torch
from My_functions import timex, show_images_list_torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
from MySaveLoad import load_pkl

with timex():
    train = load_pkl('../data10.pkl')
train = torch.from_numpy(train.transpose(0, 3, 1, 2))
autoencoder = torch.load('autoencoder_exp1.pkl')
autoencoder.eval()
list_dist = []
our_image = autoencoder.encode(train[310].unsqueeze(0).to(device)).to('cpu')
with timex():
    with torch.no_grad():
        for i in range(train.shape[0]):
            if i != 310:
                output = autoencoder.encode(train[i].unsqueeze(0).to(device)).to('cpu')
                torch.cuda.empty_cache()
                distance = torch.dist(our_image, output, p=2)
                list_dist.append(distance)

list_dist_per5 = []
percent5 = min(list_dist) + (max(list_dist) - min(list_dist)) * 0.15
for i in range(len(list_dist)):
  if list_dist[i] <= percent5:
        list_dist_per5.append(train[i])

print(len(list_dist_per5))
show_images_list_torch(list_dist_per5)

