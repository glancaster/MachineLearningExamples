# confusion matrix
# 	predicted
# a	    - 	+
# c  
# t  - 	TN	FP          
# u   
# a  
# l  +  FN	TP
#     
#
# 	predicted           
# a	    cat	dog
# c  c
# t  a 	42	8          
# u  t 
# a  d
# l  o  18	32
#    g 
#
# This means it got 42 cat cases right, 8 wrong. 32 dog cases right, 18 wrong.


# Accuracy = (TP + TN) / (TP + TN + FP + FN)
TP = 42
TN = 32
FP = 8
FN = 18
Accuracy = (TP + TN) / (TP + TN + FP + FN)
print(f"{Accuracy=}")

# Accuracy can still be high even if it selects a lot of one case correctly 
# This is an accuracy paradox

# Precision = TP / ( TP + FP )
TP,TN,FP,FN = 114,12,14,0
Precision = TP / ( TP + FP ) 

print(f"{Precision=}")


# Recall/Sensitivity = TP / ( TP + FP )
Recall = TP / ( TP + FN )
print(f"{Recall=}")


# F1 - Score = 2 * (precision * recall) / (precision + recall)
F1Score = 2 * (Precision * Recall) / (Precision + Recall)
print(f"{F1Score=}")

TF = 7
print("\tFN\tFP\tTP\tPRE\tACC\tREC\tF1")
for FN in range(0,7):
    for FP in range(0,FN+1):
        TP = 100 - FN - FP - TF
        Precision = TP / ( TP + FP ) 
        Accuracy = (TP + TN) / (TP + TN + FP + FN)
        Recall = TP / ( TP + FN )
        F1Score = 2 * (Precision * Recall) / (Precision + Recall)
        print("\t{:2.2f}\t{:2.2f}\t{:2.2f}\t{:2.2f}\t{:2.2f}\t{:2.2f}\t{:2.2f}".format(FN,FP,TP,Precision,Accuracy,Recall,F1Score))



