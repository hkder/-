# 구름은 흘러 어디로 가는가 Go Goorm

<p align=center>
  <img src="./weather.gif" alt="weather" width=300px height=300px>
</p>

------

## Keras How To

In the keras_env directory, there are different directories for different models.
In each model, there are codes needed to use different models.

#### Step 1. Generating Dataset

    $ python data_gen.py

When you run above script, you will get 4 different npy files. 

<ul>
  <li> train_set.npy
  <li> train_label.npy
  <li> test_set.npy
  <li> test_label.npy
</ul>

Those are the files you need. You can check the data by running the following script.

    $ python check_data.py
    
#### Step 2. Training

    $ python train.py
    
Run the above script, and the model will start training based on your npy data. 
The result will be saved in .h5 format.

#### Step 3. Testing
You can easily check the result of the model by running

    $ python test_model.py
    
