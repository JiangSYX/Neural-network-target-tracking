# Neural-network-target-tracking
The neural network calculates the moving direction by obtaining the target coordinates and its own coordinates to track the target. The neural network structure is a simple three-layer neural network, which has been used in another project of mine (pyGame - the basic content of a game)

### ai.py
You can run this file to see the tracking function of neural network
> python ai.py

The first iteration will be carried out after the program is started, and the window is black at this time.

- Number of iterations: 10
- Number of nerves in input layer: 4
- Number of hidden layer nerves: 200
- Number of nerves in output layer: 8
- Learning rate: 0.01
- Activation function: sigmoid function

The operation result of neural network has a little problem, but the problem is not big.

- 4 nerves in the input layer: Target X coordinate, Target Y coordinate, AI X coordinates, AI Y coordinates
- 8 nerves in the output layer: Up, down, left and right, upper left, lower left, upper right and lower right
