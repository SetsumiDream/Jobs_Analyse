from django.shortcuts import render
from django.http import HttpResponse
from lib.http import render_json

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
import os
import math


# Create your views here.
def test(request):
    n = np.random.randint(0, 10, size=10)
    plt.plot(np.arange(0, 10), n)
    plt.savefig('./static/img/analyse/123.png')
    plt.close()
    with open('./static/img/analyse/123.png', 'rb') as f:
        image_data = f.read()
    return HttpResponse(image_data, content_type="image/png")