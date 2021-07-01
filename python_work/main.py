from os import read
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from tabulate import tabulate
from django.http import HttpResponse
import csv
#import sys

# protein = ""

def protein(req) :

    X = ProteinAnalysis(req) #% sys.argv[1]

    sum = (X.count_amino_acids()['A']) + (X.count_amino_acids()['V']) + (X.count_amino_acids()['Y']) + (X.count_amino_acids()['W']) + (X.count_amino_acids()['T']) + (X.count_amino_acids()['S']) + (X.count_amino_acids()['P']) + (X.count_amino_acids()['F']) + (X.count_amino_acids()['M']) + (X.count_amino_acids()['K']) + (X.count_amino_acids()['L']) + (X.count_amino_acids()['I']) + (X.count_amino_acids()['H']) + (X.count_amino_acids()['G']) + (X.count_amino_acids()['E']) + (X.count_amino_acids()['Q']) + (X.count_amino_acids()['C']) + (X.count_amino_acids()['D']) + (X.count_amino_acids()['N']) + (X.count_amino_acids()['R'])

    prt = "Total Number of Amino Acids : ", str(sum)

    return prt
    
def protein2(req2) :

    X = ProteinAnalysis(req2)

    abc = "The molecular weight :",str("%0.2f" % X.molecular_weight())


    field  = ['Amino_acid', 'Number_in_seq', 'Percentage']

    tabel =[ 
    [('alanine (A) :'), (X.count_amino_acids()['A']),(str (float("%0.2f" % X.get_amino_acids_percent()['A']) * 100)) + "%"],
    [("arginine (R) :"),
    (X.count_amino_acids()['R']),
    str(float("%0.2f" % X.get_amino_acids_percent()['R']) * 100) +"%"],
    [("asparagine (N) :"),
    (X.count_amino_acids()['N']),
    str(float("%0.2f" % X.get_amino_acids_percent()['N']) * 100) +"%"],
    [("aspartic acid (D) :"),
    (X.count_amino_acids()['D']),
    str(float("%0.2f" % X.get_amino_acids_percent()['D']) * 100) + "%"],
    [("cysteine (C) :"),
    (X.count_amino_acids()['C']),
    str(float("%0.2f" % X.get_amino_acids_percent()['C']) * 100) + "%"],
    [("glutamine (Q) :"),
    (X.count_amino_acids()['Q']),
    str(float("%0.2f" % X.get_amino_acids_percent()['Q']) * 100) + "%"],
    [("glutamic acid (E) :"),
    (X.count_amino_acids()['E']),
    str(round(float("%0.2f" % X.get_amino_acids_percent()['E']) * 100, 2)) + "%"],
    [("glycine (G) :"),
    (X.count_amino_acids()['G']),
    str(float("%0.2f" % X.get_amino_acids_percent()['G']) * 100) + "%"],
    [("histidine (H) :"),
    (X.count_amino_acids()['H']),
    str(float("%0.2f" % X.get_amino_acids_percent()['H']) * 100) + "%"],
    [("isoleucine (I) :"),
    (X.count_amino_acids()['I']),
    str(float("%0.2f" % X.get_amino_acids_percent()['I']) * 100) + "%"],
    [("leucine (L) :"),
    (X.count_amino_acids()['L']),
    str(float("%0.2f" % X.get_amino_acids_percent()['L']) * 100) + "%"],
    [("lysine (K) :"),
    (X.count_amino_acids()['K']),
    str(float("%0.2f" % X.get_amino_acids_percent()['K']) * 100) + "%"],
    [("methionine (M) :"),
    (X.count_amino_acids()['M']),
    str(float("%0.2f" % X.get_amino_acids_percent()['M']) * 100) + "%"],
    [("phenylalanine (F) :"),
    (X.count_amino_acids()['F']),
    str(float("%0.2f" % X.get_amino_acids_percent()['F']) * 100) + "%"],
    [("proline (P) :"),
    (X.count_amino_acids()['P']),
    str(float("%0.2f" % X.get_amino_acids_percent()['P']) * 100) + "%"],
    [("serine (S) :"),
    (X.count_amino_acids()['S']),
    str(float("%0.2f" % X.get_amino_acids_percent()['S']) * 100) + "%"],
    [("threonine (T) :"),
    (X.count_amino_acids()['T']),
    str(float("%0.2f" % X.get_amino_acids_percent()['T']) * 100) + "%"],
    [("tryptophan (W) :"),
    (X.count_amino_acids()['W']),
    str(float("%0.2f" % X.get_amino_acids_percent()['W']) * 100) + "%"],
    [("tyrosine (Y) :"),
    (X.count_amino_acids()['Y']),
    str(float("%0.2f" % X.get_amino_acids_percent()['Y']) * 100) + "%"],
    [("valine (V) :"),
    (X.count_amino_acids()['V']),
    str(float("%0.2f" % X.get_amino_acids_percent()['V']) * 100) + "%"],
    ]

    #name of csv file 
    filename = "protein_seq.csv"
    
# writing to csv file 
    with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
        csvwriter.writerow(field) 
        
    # writing the data rows 
        csvwriter.writerows(tabel)

    abc4 =  tabulate(tabel)

    return abc

def protein3(req3) :

    X = ProteinAnalysis(req3)
   
    abc2 = "The Theoretical pI value :", str("%0.2f" % X.isoelectric_point())

    return abc2

# def protein4(req4) :

#     X = ProteinAnalysis(req4)
   
#     abc5 = "Grand average of hydropathicity :", str("%0.2f" % X.gravy())
    
#     return abc5
    # abc = "The molecular weight :",str("%0.2f" % X.molecular_weight())
    # abc2 = "The Theoretical pI value :", str("%0.2f" % X.isoelectric_point()) 
    # abc3 = "Amino_Acid Composition : " 
    

    # print(prt)
    # print(abc)
    # print(abc2)
    # print(abc3)
    # print(abc4)

    # file = open("index.html","w")
    # file.write(abc4)
    # file.write(abc3)
    # file.close()

    ##prt.save("index.html")

     
 
    # print(str(sum), str(X.molecular_weight()), str(X.isoelectric_point()), str(tabulate(tabel)))

# protein3("MLPGLALLLLAAWTARALEVPTDGNAGLLAEPQIAMFCGRLNMHMNVQNGKWDSDPSGTKTCIDTKEGILQYCQEVYPELQITNVVEANQPVTIQNWCKRGRKQCKTHPHFVIPYRCLVG")
#name of csv file 
# filename = "protein_seq.csv"
    
# # writing to csv file 
# with open(filename, 'w') as csvfile: 
#     # creating a csv writer object 
#     csvwriter = csv.writer(csvfile) 
        
#     # writing the fields 
#     csvwriter.writerow(field) 
        
#     # writing the data rows 
#     csvwriter.writerows(tabel)

# output = "i am %s current time is " % sys.argv[1]