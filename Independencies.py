import numpy as np
import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
bay=BayesianNetwork()
bay.add_node("B")
bay.add_node("E")
bay.add_node("A")
bay.add_node("J")
bay.add_node("M")
bay.add_edge("B","A")
bay.add_edge("E","A")
bay.add_edge("A","J")
bay.add_edge("A","M")
cpd_B=TabularCPD('B',2,values=[[0.999],[0.001]])
cpd_E=TabularCPD('E',2,values=[[0.998],[0.002]])
cpd_A=TabularCPD('A',2,values=[[0.999,0.71,0.06,0.05],[0.001,0.29,0.94,0.95]],evidence=['B','E'],evidence_card=[2,2])
cpd_J=TabularCPD('J',2,values=[[0.95,0.1],[0.05,0.9]],evidence=['A'],evidence_card=[2])
cpd_M=TabularCPD('M',2,values=[[0.95,0.1],[0.05,0.9]],evidence=['A'],evidence_card=[2])
bay.add_cpds(cpd_B,cpd_E,cpd_A,cpd_J,cpd_M)
if(bay.check_model()):
    print("Model is Correct")
else:
    print("Model is Not Correct")
print(bay.get_independencies())
print("Completed.")

