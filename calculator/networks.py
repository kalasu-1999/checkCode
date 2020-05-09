# -*- coding: UTF-8 -*-
import numpy
from calculator import calculatorPublic
import tensorflow as tf

numpy.seterr(divide='ignore', invalid='ignore')


def training(dirPosition, answer, gcov):
    tf.keras.callbacks.LearningRateScheduler(0.001)
    model1 = tf.keras.Sequential()
    model1.add(tf.keras.layers.Dense(len(gcov[0]) / 2, input_shape=(len(gcov[0]),), activation='sigmoid'))
    model1.add(tf.keras.layers.Dense(len(gcov[0]) / 2, activation='sigmoid',
                                     kernel_regularizer=tf.keras.regularizers.l2(0.001)))
    model1.add(tf.keras.layers.Dense(1, activation='sigmoid'))
    model1.summary()
    model1.compile(optimizer='adam',
                   loss='binary_crossentropy',
                   metrics=['acc'])
    model1.fit(gcov, answer, epochs=1700)
    model1.save(dirPosition + '/numpyDataDir/myModel.h5')


def networks(dirPosition, times):
    answerList = calculatorPublic.getAnswer(dirPosition)
    gcovList = calculatorPublic.getGcov(dirPosition, times)
    training(dirPosition, answerList, gcovList)
    model = tf.keras.models.load_model(dirPosition + '/numpyDataDir/myModel.h5')
    testList = numpy.identity(len(gcovList[0]))
    return model.predict(testList)


def networksMain(dirPosition, times):
    resultList = calculatorPublic.getResultList(networks(dirPosition, times))
    numpy.save(dirPosition + '/numpyDataDir/networks' + str(times) + '.npy', resultList)
