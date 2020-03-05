import numpy as np
import keras 

from keras.models       import Sequential, Model
from keras.layers       import Dense, Activation, Flatten
from keras.optimizers   import Adam
from keras.layers       import Dense, MaxPooling2D, AveragePooling2D, GlobalAveragePooling2D, Input, Flatten, Dropout


from rl.agents.dqn  import DQNAgent
from rl.policy      import BoltzmannQPolicy
from rl.memory      import SequentialMemory


def get_model(width: int,height: int,channel: int,nb_classes: int):

    model = keras.applications.mobilenet_v2.MobileNetV2(input_shape=(width,height,channel),
                                                        include_top=False, 
                                                        weights='imagenet')
    x = model.output
    x = AveragePooling2D((10,10), padding='valid')(x) 
    x = Flatten()(x) 
    x = Dense(2048,activation='relu')(x)
    x = Activation('linear')
    new_model = Model(inputs=model.input, outputs=x)
    return new_model

def get_agent(model,nb_actions,learning_rate):
    memory = SequentialMemory(limit=50000, window_length=1)
    policy = BoltzmannQPolicy()
    dqn = DQNAgent(model=model, nb_actions=nb_actions, memory=memory, nb_steps_warmup=10,
                target_model_update=1e-2, policy=policy)
    dqn.compile(Adam(lr=learning_rate), metrics=['mae'])

    return dqn


