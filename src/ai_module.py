import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple neural network model for NPC decision-making
class NPCDecisionModel(nn.Module):
    def __init__(self):
        super(NPCDecisionModel, self).__init__()
        self.fc1 = nn.Linear(10, 20)
        self.fc2 = nn.Linear(20, 5)  # 5 possible actions: idle, move, attack, defend, flee

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.softmax(self.fc2(x), dim=1)
        return x

# Function to train the NPC model with sample data
def train_npc_model():
    model = NPCDecisionModel()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    inputs = torch.randn(100, 10)
    labels = torch.randint(0, 5, (100,))

    for epoch in range(100):
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        if epoch % 10 == 0:
            print(f"Epoch [{epoch}/100], Loss: {loss.item():.4f}")

# Simulate NPC action choice based on the model’s prediction
def npc_behavior(input_data):
    model = NPCDecisionModel()
    model.eval()  # Set model to evaluation mode
    output = model(input_data)
    action = torch.argmax(output, dim=1).item()
    actions = ["idle", "move", "attack", "defend", "flee"]
    print(f"NPC action chosen: {actions[action]}")

# Train the model and run a test
train_npc_model()
npc_behavior(torch.randn(1, 10))
