import torchvision.models as models
import torch.nn as nn
import torch.optim as optim
import Models.Helper.DeviceHelper as Helper
class ResNet34:

    def set_params(self,num_classes):
        resnet_34 = models.resnet34(pretrained=False)
        num_filters = resnet_34.fc.in_features
        num_classes = num_classes
        resnet_34.fc = nn.Linear(num_filters,num_classes)
        device = Helper.set_device()

