# **Concepts and Terminologies**


### Why Gene-expression and PPIs are important?

Analyzing gene expression levels and the biological pathways associated with the genes involved in cancer leads to studying the difference between a normal cell and cancerous cell pathways to determine the genetic origin of the faulty pathway and thereby identifying potential targets for treating cancer.

Protein-protein interactions (PPIs) participate in all important biological processes in living organisms, such as catalyzing metabolic reactions, DNA replication, DNA transcription, responding to stimuli, and transporting molecules from one location to another
Understanding the molecular mechanisms of PPIs is crucial for developing accurate methods for the prevention, diagnosis, and treatment of cancers. 

The contact interface between two proteins is the structural foundation of their interaction. Understanding the contact region between proteins will help to elucidate their functions in interaction networks.

The cancer-related proteins are abnormally expressed (overexpressed, low expressed, or mutant) in cancer cells compared to normal cells.
Deeper investigations of protein-protein interfaces relevant to human oncogenesis and cancer-associated protein-protein interaction networks have shown that cancer-related proteins are smaller, more planar, more charged, and have less hydrophobic binding sites than non-cancer-related proteins and they tend to show lower affinity and higher specificity for cancer-associated PPI networks. Moreover, cancer-related proteins often interface with their binding partners using distinct surfaces, corresponding typically to the multi-interface hub.



## **Drug Synergy**
- There are two drugs that have specific responses individually on the cell lines. 
- Let's say they are drug A and drug B. 
- The combined responses of drug A and drug B can have an additive or an inhibitive response on the cell lines.
- This is measured with something we call as synergy scores.


### **`Synergy Scores`**
- A synergy score is a quantitative measure that assesses the `combined effect of two or more drugs` or compounds when used together, compared to the sum of their individual effects.
- It quantifies the degree of synergy or enhancement of therapeutic outcomes achieved through drug interactions.
- A higher synergy score indicates a greater-than-expected positive interaction between the drugs, suggesting that their combined effect is stronger than what would be predicted based on their individual effects.
- It aids in predicting potential synergistic effects in untested drug combinations for patients.
- It also identifies new biomarkers that could uncover mechanisms of drug synergy 
- It also Helps to predict whether a known drug combination will be effective for a specific patient.

### **`Why Drug Synergy scores are important??`**
Drug synergy is of paramount importance due to its role in optimizing treatment effectiveness and addressing the challenge of treatment resistance, particularly in the context of intricate and multifaceted diseases like cancer. 

When multiple drugs interact synergistically, their combined effect becomes greater than the sum of their individual effects. This phenomenon can lead to more potent therapeutic outcomes, enabling lower individual drug doses, reducing the risk of adverse reactions, and potentially overcoming mechanisms that contribute to treatment resistance. 

By harnessing the power of drug synergy, medical interventions can achieve enhanced results and provide a more comprehensive approach to managing complex diseases.



### **Cancer Cell Lines**

- Cancer cell lines are cultured cells derived from cancerous tumors.
- These cell lines serve as models for studying: 
    - various aspects of cancer biology
    - validating cancer targets
    - defining drug efficacy 
    - drug development
    - therapeutic interventions
- Cancer cell lines are the most commonly used models for studying cancer biology. 
- They are widely used in research laboratories and pharmaceutical companies to investigate the mechanisms underlying cancer growth, metastasis, and drug responses.


<br><br><br><br>

 **What is a Fingerprint?**

Deep learning models almost always take arrays of numbers as their inputs. If we want to process molecules with them, we somehow need to represent each molecule as one or more arrays of numbers.

Many (but not all) types of models require their inputs to have a fixed size. This can be a challenge for molecules, since different molecules have different numbers of atoms. If we want to use these types of models, we somehow need to represent variable sized molecules with fixed sized arrays.

Fingerprints are designed to address these problems. A fingerprint is a fixed length array, where different elements indicate the presence of different features in the molecule. If two molecules have similar fingerprints, that indicates they contain many of the same features, and therefore will likely have similar chemistry.

DeepChem supports a particular type of fingerprint called an "Extended Connectivity Fingerprint", or "ECFP" for short. They also are sometimes called "circular fingerprints". The ECFP algorithm begins by classifying atoms based only on their direct properties and bonds. Each unique pattern is a feature. For example, "carbon atom bonded to two hydrogens and two heavy atoms" would be a feature, and a particular element of the fingerprint is set to 1 for any molecule that contains that feature. It then iteratively identifies new features by looking at larger circular neighborhoods. One specific feature bonded to two other specific features becomes a higher level feature, and the corresponding element is set for any molecule that contains it. This continues for a fixed number of iterations, most often two.




## References
[1] https://sites.broadinstitute.org/ccle/#:~:text=Cancer%20cell%20lines%20are%20the,lines%20of%20the%20NCI60%20panel.

[2]