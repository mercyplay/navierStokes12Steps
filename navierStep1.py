#Rafael Orozco may 2017
#Step 1 of 12 step Navier Stokes
#1-d linear Convection.

stepsTime = []
stepsSpace = []

numStepsSim = 100
c           = 0.1
deltaTime   = 
deltaSpace  = 

uForwardTime = uCurrTime - c * (deltaTime / deltaSpace) * (uCurrTime - uPrevSpace) 
