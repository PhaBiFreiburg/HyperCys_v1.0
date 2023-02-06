# HyperCys: A Structure- and Sequence-Based Predictor of Hyper-Reactive Druggable Cysteines

**Contact:**
	 * mingjie.gao@pharmazie.uni-freiburg.de * 
	 * stefan.guenther@pharmazie.uni-freiburg.de * 

Keyword: `machine learning` `structure- and sequence-based` `druggable cysteine` `reactivity prediction`

![image](https://github.com/mingjie-tech/HyperCys/blob/master/data/flowchart.png)

## Features Collection
* Feature Collection from 3D structures (34 features)
    * Pocket profile (PP)
        * Fpocket
            * Fpocket(https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-10-168) was used to determine whether or not amino acids are located in detectable binding pockets, and only those cysteines located in pockets were retained. Druggability, hydrophobicity, and polarity were collected.
       * Depth 
            * Depth (https://academic.oup.com/nar/article/41/W1/W314/1111943?login=false) was used to calculate the depth of cysteine burial.
    * SASA-PKA profile (SPP)
        * The pKa and SASA values for each cysteine and its surrounding amino acids within 4, 6, 8, and 10 Å of cysteine were calculated using PROPKA 3 (https://pubmed.ncbi.nlm.nih.gov/26596171/) and freeSASA (https://freesasa.github.io/), respectively.
    * Amino Acid Composition (AAC)
            * Total number of surrounding amino acid residues within 4, 6, 8, and 10 Å of cysteine was calculated, and also the respective number of polar and hydrophobic amino acids according to the hydrophobic/polar (H/P) classification by Kamtekar et al. (https://pubmed.ncbi.nlm.nih.gov/8259512/).
             Canonical H/P patterning: ADEGHKNPQRST-CFILMVWY
* Feature Collection from sequences (46 features)
HyperCys utilizes DisPredict2 to extract sequence features.
DisPredict_v2.0 (http://cs.uno.edu/~tamjid/Software.html).
Sumaiya Iqbal and Md Tamjidul Hoque, 2016
Contact:
	thoque@uno.edu
	siqbal1@my.uno.edu (anni.are@gmail.com)
1) Column 10 - 29: 20 PSSMs

					- generate with PSI-BLAST and normalize using 9.0 -	
										
2) Column 30 - 32: 3 secondary structure (helix, strand and coil) probabilities

					- generate using SPINE X -
					
3) Column 33: 1 accessible surface area

					- generate using SPINE X -
				

4) Column 36 - 56: 1 monogram and 20 bigrams

				- generate using source code provided with DisPredict supplementary materials

				- available at SuppMaterial_DisPredict/Software/Source Codes

				- guidelines to execute it is described in "Steps to prediction" below

				- normalize the values with exponent (6.0)


5) Column 57
				- 1 Position Specific Estimated Energy (PSEE)
    * Totally collected:
    * 20 PSSMs
    * 1 monogram
    * 20 bigrams
    * 1 PSEE
    * 1 Helix probability
    * 1 Beta-Strand probability
    * 1 Coil probability
    * 1 ASA
    
# Folders
 * Data Folder
    * Storing bechmark data for training the machine learning models.
 * Code Folder
    * code_for_sequence_based_features_collection

    * code_for_3d_structure_features_collection

    * code_for_prediction
* Model Folder
    * binding_pocket.model

    * not_in_detected_pocket.model

    * sequence_based.model

    * strucutre_based.model
## Cite Us
