import torch
import os
def run():
    print("cuda enabled:",torch.cuda.is_available())
    print("number of cores:",os.cpu_count())
if __name__ == "__main__":
    run()