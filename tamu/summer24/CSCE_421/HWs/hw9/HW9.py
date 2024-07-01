import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import matplotlib.pyplot as plt

# Define the CNN architecture
class SimpleCNN(nn.Module):
    def __init__(self, num_classes=10, num_filters=16, kernel_size=3, padding=1, dropout_rate=0):
        super(SimpleCNN, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(3, num_filters, kernel_size=kernel_size, padding=padding),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        self.layer2 = nn.Sequential(
            nn.Conv2d(num_filters, num_filters*2, kernel_size=kernel_size, padding=padding),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2))
        
        self.feature_size = self._get_feature_size(32, kernel_size, padding)
        self.fc = nn.Linear((num_filters*2) * self.feature_size * self.feature_size, num_classes)
        self.dropout = nn.Dropout(dropout_rate)

    def _get_feature_size(self, input_size, kernel_size, padding):
        conv1_out = (input_size - kernel_size + 2 * padding) + 1
        pool1_out = conv1_out // 2
        conv2_out = (pool1_out - kernel_size + 2 * padding) + 1
        pool2_out = conv2_out // 2
        return pool2_out

    def forward(self, x):
        out = self.layer1(x)
        out = self.layer2(out)
        out = out.view(out.size(0), -1)
        out = self.dropout(out)
        out = self.fc(out)
        return out


# Define transformations for the train set
train_transforms = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])

# Define transformations for the validation set
val_transforms = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
])

# Load datasets
train_dataset = datasets.CIFAR10(root='./data', train=True, download=True, transform=train_transforms)
val_dataset = datasets.CIFAR10(root='./data', train=False, download=True, transform=val_transforms)

# Define data loaders
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32, shuffle=False)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def train(model, train_loader, lr=0.01, momentum=0.9):
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=lr, momentum=momentum)
    
    model.train()
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

def validate(model, val_loader):
    model.eval()
    total = 0
    correct = 0
    with torch.no_grad():
        for images, labels in val_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    accuracy = correct / total
    print('Validation accuracy: {:.2f}%'.format((accuracy) * 100))
    return accuracy

def visulization(accuracies):
    plt.figure(figsize=(10, 5))
    plt.plot(accuracies)
    plt.title('Validation accuracy over epochs')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.show()
    
def task1():
    print('Task 1 with different number of filters')
    num_filters_list = [16, 32]
    for num_filters in num_filters_list:
        print(f"\nTraining with {num_filters} filters")
        model = SimpleCNN(num_filters=num_filters) 
        model = model.to(device)
        accuracies = []
        for epoch in range(10):
            print('Epoch {}/{}'.format(epoch+1, 10))
            train(model, train_loader)
            accuracy = validate(model, val_loader)
            accuracies.append(accuracy)
        visulization(accuracies)

def task2():
    print('Task 2 with different kernel sizes')
    kernel_sizes = [3, 5]
    for kernel_size in kernel_sizes:
        print(f"\nTraining with {kernel_size}x{kernel_size} kernel size")
        model = SimpleCNN(kernel_size=kernel_size) 
        model = model.to(device)
        accuracies = []
        for epoch in range(10):
            print('Epoch {}/{}'.format(epoch+1, 10))
            train(model, train_loader)
            accuracy = validate(model, val_loader)
            accuracies.append(accuracy)
        visulization(accuracies)

def task3():
    print('Task 3 with different padding')
    padding_list = [0, 1]
    for padding in padding_list:
        print(f"\nTraining with padding={padding}")
        model = SimpleCNN(padding=padding) 
        model = model.to(device)
        accuracies = []
        for epoch in range(10):
            print('Epoch {}/{}'.format(epoch+1, 10))
            train(model, train_loader)
            accuracy = validate(model, val_loader)
            accuracies.append(accuracy)
        visulization(accuracies)

def task4(best_num_filters, best_kernel_size, best_padding, dropout_rate=0.3):
    print('Task 4: Train the best model with dropout')
    model = SimpleCNN(num_filters=best_num_filters, 
                      kernel_size=best_kernel_size, 
                      padding=best_padding, 
                      dropout_rate=dropout_rate)
    model = model.to(device)
    accuracies = []
    for epoch in range(10):
        print('Epoch {}/{}'.format(epoch+1, 10))
        train(model, train_loader)
        accuracy = validate(model, val_loader)
        accuracies.append(accuracy)
    visulization(accuracies)

if __name__ == "__main__":
    task1()
    task2()
    task3()
    best_num_filters = 32
    best_kernel_size = 3
    best_padding = 1
    task4(best_num_filters, best_kernel_size, best_padding, dropout_rate=0.3)