import math

input_layer = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
}

new_weight = {
    'A to E': 0.3,
    'B to E': 0.2,
    'C to E': 0.5,
    'D to E': 0.2,

    'A to F': 0.6,
    'B to F': 0.3,
    'C to F': 0.7,
    'D to F': 0.2,

    'E to G': 0.1,
    'F to G': 0.3,
    'E to H': 0.1,
    'F to H': 0.2
}

initial_weight = {
    'A to E': 0,
    'B to E': 0,
    'C to E': 0,
    'D to E': 0,

    'A to F': 0,
    'B to F': 0,
    'C to F': 0,
    'D to F': 0,

    'E to G': 0,
    'F to G': 0,
    'E to H': 0,
    'F to H': 0
}

hidden_layer = {
    'E': 0,
    'F': 0,
}

output_layer = {
    'G':0,
    'H':0
}

# grab binary value from file and turn it into array
def getInput(file):
    inputFile = [line.rstrip('\n') for line in open(file)]

    input_layers = []
    for input_layer in inputFile:
        nodes = []
        for bit in list(input_layer):
            nodes.append(int(bit))
        input_layers.append(nodes)

    return input_layers

# some needed variables for back propogation
learningRate = 0.1
target = 1
notTarget = 0

# sigmoid function
# takes the value of an input layer and multiples it to its weight to a node in the hidden layer
# does this for all input layers for each hidden layers
# take the sigmoid of the sum

# repeats and does the same thing for the output layer
# using the hidden layer instead
def produceSigmoid():
    hidden_layer['E'] = sigmoid((input_layer['A'] * new_weight['A to E']) + (input_layer['B'] * new_weight['B to E']) + (input_layer['C'] * new_weight['C to E']) + (input_layer['D'] * new_weight['D to E']))
    hidden_layer['F'] = sigmoid((input_layer['A'] * new_weight['A to F']) + (input_layer['B'] * new_weight['B to F']) + (input_layer['C'] * new_weight['C to F']) + (input_layer['D'] * new_weight['D to F']))

    output_layer['G'] =  sigmoid((hidden_layer['E'] * new_weight['E to G']) + (hidden_layer['F'] * new_weight['F to G']))
    output_layer['H'] = sigmoid((hidden_layer['E'] * new_weight['E to H']) + (hidden_layer['F'] * new_weight['F to H']))

def sigmoid(s):
    return 1.0/(1.0 + math.exp(-s))

# this uses backpropagation to train the NN
def backPropagation():

    for i, j in new_weight.items():
        initial_weight[i] = j

    pixelSum = 0
    for i, j in input_layer.items():
        pixelSum += j

    #calculate G, H, E and F errors
    # we will need these for back prop

    if pixelSum > 1:
        G_ERROR = output_layer['G'] * (1 - output_layer['G']) * (target - output_layer['G'])
        H_ERROR = output_layer['H'] * (1 - output_layer['H']) * (notTarget - output_layer['H'])

    else:
        G_ERROR = output_layer['G'] * (1 - output_layer['G']) * (notTarget - output_layer['G'])
        H_ERROR = output_layer['H'] * (1 - output_layer['H']) * (target - output_layer['H'])

    E_ERROR = ((new_weight['E to G'] * G_ERROR) + (new_weight['E to H'] * H_ERROR)) * (hidden_layer['E'] * (1 - hidden_layer['E']))
    F_ERROR = ((new_weight['F to G'] * G_ERROR) + (new_weight['F to H'] * H_ERROR)) * (hidden_layer['F'] * (1 - hidden_layer['F']))

    # actual backward propagation
    # takes old weight between each node and adds it to the learning rate times the error to the next node
    # and times the value of the start node
    # do this for every possible weight

    #input layer to E
    new_weight['A to E'] = old_weight['A to E'] + (learningRate * E_ERROR * input_layer['A'])
    new_weight['B to E'] = old_weight['B to E'] + (learningRate * E_ERROR * input_layer['B'])
    new_weight['C to E'] = old_weight['C to E'] + (learningRate * E_ERROR * input_layer['C'])
    new_weight['D to E'] = old_weight['D to E'] + (learningRate * E_ERROR * input_layer['D'])

    #input layer to F
    new_weight['A to F'] = old_weight['A to F'] + (learningRate * F_ERROR * input_layer['A'])
    new_weight['B to F'] = old_weight['B to F'] + (learningRate * F_ERROR * input_layer['B'])
    new_weight['C to F'] = old_weight['C to F'] + (learningRate * F_ERROR * input_layer['C'])
    new_weight['D to F'] = old_weight['D to F'] + (learningRate * F_ERROR * input_layer['D'])

    #hidden layer to G
    new_weight['E to G'] = old_weight['E to G'] + (learningRate * G_ERROR * hidden_layer['E'])
    new_weight['F to G'] = old_weight['F to G'] + (learningRate * G_ERROR * hidden_layer['F'])

    #hidden layer to H
    new_weight['E to H'] = old_weight['E to H'] + (learningRate * H_ERROR * hidden_layer['E'])
    new_weight['F to H'] = old_weight['F to H'] + (learningRate * H_ERROR * hidden_layer['F'])

#input our array. This will be a binary value i.e. 4 = [1,0,0,0]
input = getInput("/Users/echelon/Desktop/input_file.txt")

#this will predict based on the model. If model is confident there are more light panels
#than dark panels, G will be greater than H. Otherwise, they are dark.
def predict():
    if output_layer['G'] > output_layer['H']:
        print("light")
    else:
        print("dark")

# assign input layer to our input binary value
def loadInputLayer(input):
    input_layer['A'] = input[0]
    input_layer['B'] = input[1]
    input_layer['C'] = input[2]
    input_layer['D'] = input[3]

# this will write our new weights to our old weights. We can reuse these
def createWeights(file, oldWeights):
    createWeights = open(file, "w")

    for i, j in oldWeights.items():
        createWeights.write("{}\n".format(j))

# load the stored weights
def loadWeights(file):
    newFile = [line.rstrip('\n') for line in open(file)]
    g = 0
    for i, j in new_weight.items():
        new_weight[i] = float(newFile[g])
        g+=1

# this is the training segment.
# First we load the input, run the sigmoid, and back propogate before writing our new weights
# after we have our initial 1 set up, we train using 1000 iterations
def train():
    for i in range(0, 1):
        for index in range(0, 16):
            loadInputLayer(inputs[index])
            produceSigmoid()
            print(output_neuron, end = " ")

            backward_propagation()
            write_new_weights_to("/Users/echelon/Desktop/new_weights.txt", weight)

    for i in range(0, 1000):
        for index in range(0, 16):
            load_inputs_from(inputs[index])
            loadWeights("/Users/echelon/Desktop/new_weights.txt")
            produceSigmoid()
            print(output_neuron, end = " ")
            predict()
            backward_propagation()
            write_new_weights_to("/Users/echelon/Desktop/new_weights.txt", weight)
        print()


# Testing. If 2,3, or 4 panels are 1 we print light
# If 0 or 1 panel is 0 we print dark
def test(t):
    loadInputLayer(input[t])
    loadWeights("/Users/echelon/Desktop/trained_weights.txt")
    produceSigmoid()
    display(input[t])

# nice display in substitue of UI
def display(input):
    list = input
    print('|===========|')
    print('|     =     |')
    print('|  '+str(list[0])+'  =   '+str(list[1])+' |')
    print('|     =     |')
    print('|========== |')
    print('|     =     |')
    print('|  '+str(list[2])+'  =   '+str(list[3])+' |')
    print('|     =     |')
    print('|===========|')
    print("Prediction: ", end = " ")
    predict()

t = 4
test(int(t))
