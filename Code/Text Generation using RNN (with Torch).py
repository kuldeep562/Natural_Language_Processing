import torch
import torch.nn as nn
import random
import string

# Simple char-level RNN
class CharRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(CharRNN, self).__init__()
        self.hidden_size = hidden_size
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x, h=None):
        out, h = self.rnn(x, h)
        out = self.fc(out)
        return out, h

def char_tensor(text):
    tensor = torch.zeros(len(text), 1, len(all_chars))
    for c in range(len(text)):
        tensor[c][0][char_to_idx[text[c]]] = 1
    return tensor

all_chars = string.ascii_lowercase + " .,;'-"
char_to_idx = {ch: i for i, ch in enumerate(all_chars)}
idx_to_char = {i: ch for ch, i in char_to_idx.items()}

def generate_text(prompt, model, length=100):
    input_tensor = char_tensor(prompt.lower())
    output = prompt
    h = None
    for _ in range(length):
        out, h = model(input_tensor, h)
        last_char_logits = out[-1][0]
        predicted_idx = torch.argmax(last_char_logits).item()
        next_char = idx_to_char[predicted_idx]
        output += next_char
        input_tensor = char_tensor(next_char)
    print(output)

if __name__ == "__main__":
    model = CharRNN(input_size=len(all_chars), hidden_size=128, output_size=len(all_chars))
    prompt = "Once upon a time"
    generate_text(prompt, model)
