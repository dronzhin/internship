from torchsummary import summary
import My_Models
import torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Создаем модель, устанавливаем ошибку и оптимизатор
autoencoder = My_Models.Model_autoencoder_Conv().to(device)
summary(autoencoder, (3, 560, 640))
torch.save(autoencoder, 'autoencoder.pkl')