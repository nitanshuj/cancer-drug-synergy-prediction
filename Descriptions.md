# Basic Descriptions of Terms


### About Drug Synergy
There are two drugs that have specific responses individually on the cell lines. 
Let's say they are drug A and drug B. 
The combined responses of drug A and drug B can have an additive or an inhibitive response on the cell lines.

### **`Synergy Scores`**
**What is a synergy score?**<br>
- A synergy score is a quantitative measure that assesses the `combined effect of two or more drugs` or compounds when used together, compared to the sum of their individual effects. <br>
- It quantifies the degree of synergy or enhancement of therapeutic outcomes achieved through drug interactions. <br>
- A higher synergy score indicates a greater-than-expected positive interaction between the drugs, suggesting that their combined effect is stronger than what would be predicted based on their individual effects.
- It aids in predicting potential synergistic effects in untested drug combinations for patients.
- It also identifies new biomarkers that could uncover mechanisms of drug synergy 
- It also Helps to predict whether a known drug combination will be effective for a specific patient.



### Cancer Cell Lines

- Cancer cell lines are cultured cells derived from cancerous tumors.
- These cell lines serve as models for studying: 
    - various aspects of cancer biology
    - validating cancer targets
    - defining drug efficacy 
    - drug development
    - therapeutic interventions. 
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