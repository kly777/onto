# Basic Formal Ontology: Case Studies

**J. Neil Otte<sup>1</sup>, John Beverley<sup>2</sup>, and Alan Ruttenberg<sup>3</sup>**

<sup>1</sup>Johns Hopkins University Applied Physics Laboratory
<sup>2</sup>Northwestern University
<sup>3</sup>University at Buffalo

August 11, 2021

## Abstract

Basic Formal Ontology (BFO) is a top-level ontology consisting of thirty-eight classes, designed to support information integration, retrieval, and analysis across all domains of scientific investigation, presently employed in over 350 ontology projects around the world. BFO is a genuine top-level ontology, containing no terms particular to material domains, such as physics, medicine, or psychology. In this paper, we demonstrate how a series of cases illustrating common types of change may be represented by universals, defined classes, and relations employing the BFO framework. We provide discussion of these cases to provide a template for other ontologists using BFO, as well as to facilitate comparison with the strategies proposed by ontologists using different top-level ontologies.

Keywords: BFO, top-level ontology, ontological analysis, formal ontology

## 1. Introduction

In this paper, we demonstrate how Basic Formal Ontology (BFO) may be used to represent seven cases involving change. These cases, their goals, and their accompanying focus statements are discussed in order to provide a template for other ontologists using BFO, as well as to facilitate comparison with the strategies proposed by ontologists using different top-level ontologies.

Basic Formal Ontology is a top-level ontology designed to support information integration, retrieval, and analysis across all domains of scientific investigation. Containing only general terms common across disciplines, BFO serves as the top-level ontology of the Open Biomedical and Bioinformatic Ontology (OBO) Foundry [1] and the Industrial Ontology Foundry (IOF) [2].

Moreover, BFO provides a starting point for over 350 known ontology extensions covering more specific domains, such as infectious disease [3], plant development [4], and processed materials [5]. BFO has been designated an ISO standard [6] and BFO’s ISO 21838-2 specification has been axiomatized in First-Order Logic, OWL 2, and CLIF [7].

BFO is committed to the following principles [8], which distinguish it from other top-level ontologies:

-   **Ontological Realism** – The goal of an ontology is to describe reality. Scientific investigation is concerned with general features of reality and relations among them. Consequently, BFO consists fundamentally of representations of reality rather than merely language, concepts, or mental representations about reality.
-   **Fallibilism** – Whereas universals themselves do not change, our understanding of them must in light of new discoveries. While present scientific theories are assumed to be our best sources of accurate statements about reality, BFO recognizes that present scientific theories may be incorrect. Consequently, BFO is committed to tracking scientific developments over time, and updating ontologies in accordance with scientific developments.
-   **Adequatism** – Entities in a domain should not be assumed to be reducible to other kinds of entities. All scientific disciplines are worthy of representation in their own terms, and it is not necessary to paraphrase talk of these entities in terms of a privileged set of entities (e.g., those described by physics).

## 2. Principles and Structure of BFO

BFO adopts the following fundamental categories:

-   **Universal and Particular** – Particulars are individual denizens of reality restricted to specific times and places, which instantiate universals, but which cannot be instantiated. Universals are repeatable across time and space and may have an indefinite number of instantiated particulars.
-   **Continuant and Occurrent** – BFO is largely bifurcated into disjoint universals, distinguished by how particulars relate to time. Continuants endure through time maintaining identity, have no temporal parts, and are fully-present at any time they exist. Examples include house cats, the color of an apple, the function of mitochondria. By contrast, occurrent entities unfold over time or have temporal parts. Examples include: the history of Japan, drinking a cup of coffee, the temporal interval on which a mitotic division occurs.
-   **Relations** – BFO adopts three basic relation types: universal-universal, universal-particular, and particular-particular, the latter two of which may be time indexed. Universal-universal relations in BFO relate subtypes to parent types, whereas the sole universal-particular relation is the instance of relation, which holds between particulars and the universals under which they fall.

We discuss here only those classes necessary for the comprehension of the cases. In what follows, definitions are indicated with the use of “=def”, and those entries regarding classes that lack this symbol are elucidations. First, subclasses of continuant:

-   **a is an independent continuant =def** a is a continuant which is such that there is no b such that a specifically depends on b and no b such that a generically depends on b.
    -   **Material entity** – an independent continuant that at all times at which it exists has some portion of matter as continuant part.
        -   **Object** – a material entity that manifests causal unity and is of a type instances of which are maximal relative to the sort of causal unity manifested.
        -   **Object aggregate** – a material entity consisting exactly of (≥1) object(s) as member(s).
-   **a is an immaterial entity =def** a is an independent continuant which is such that there is no time t when it has a material entity as continuant part.
    -   **Site** – a three-dimensional immaterial entity whose boundaries either (partially or wholly) coincide with the boundaries of one or more material entities or have locations determined in relation to some material entity.

An independent continuant may bear dependent continuants, including:

-   **Generically dependent continuant** – an entity that exists in virtue of the fact that there is at least one of what may be multiple copies; it is the content or the pattern that the multiple copies share.
-   **b is a specifically dependent continuant =def** b is a continuant and there is some independent continuant c which is not a spatial region and which is such that b specifically depends on c.
    -   **Quality** – a specifically dependent continuant that, in contrast to roles and dispositions, does not require any further process in order to be realized.
    -   **Realizable entity** – a specifically dependent continuant that inheres in some independent continuant which is not a spatial region and is of a type some instances of which are realized in processes of a correlated type.
        -   **Role** – a realizable entity that exists because there is some single bearer that is in some special physical, social, or institutional set of circumstances in which this bearer does not have to be and which is not such that, if it ceases to exist, then the physical make-up of the bearer is thereby changed.
        -   **Disposition** – a realizable entity such that if it ceases to exist, then its bearer is physically changed, and whose realization occurs when and because its bearer is in some special physical circumstances, and this realization occurs in virtue of the bearer’s physical make-up.
        -   **Function** – a disposition that exists in virtue of the bearer’s physical make-up and this physical make-up is something the bearer possesses because it came into being either through evolution (in the case of natural biological entities) or through intentional design (in the case of artifacts), in order to realize processes of a certain sort.

From the occurrent portion of the hierarchy, we include the following:

-   **p is a process =def** p is an occurrent that has some temporal proper part and for some time has some material entity as participant.
-   **Temporal region** – an occurrent over which processes can unfold.
    -   **Temporal instant** – a zero-dimensional temporal region that has no proper temporal part.
    -   **Temporal interval** – a one-dimensional temporal region that is continuous, thus without gaps or breaks.

There is often a practical need to accommodate terms in scientific discourse that do not correspond to universals. Examples of such terms include ‘medical doctor’ and disjunctions such as ‘dog or cat’. Such classes are called ‘defined classes’, and are represented as equivalent to any member satisfying a set of assertions whose non-logical symbols are satisfied by models consisting only of relations, universals, or instances of universals. In this way, we hold that ‘medical doctor’ is only a short-hand way of referring to instances of persons who bear a medical doctor role, and to be a ‘dog or cat’ is nothing over and above being an instance of dog or an instance of cat. As with the familiar notion of ‘defined class’ in the OWL2 specification, every defined class is represented with an equivalency axiom however, the ontological interpretation of the notion of asserted class as corresponding to a universal and ‘defined class’ as picking out a mere term is unique to BFO.

## References

1. [Open Biomedical and Bioinformatic Ontology (OBO) Foundry](https://obofoundry.org/)
2. [Industrial Ontology Foundry (IOF)](https://www.iofoundry.org/)
3. Infectious Disease Ontology
4. Plant Ontology
5. Processed Materials Ontology
6. [ISO Standard No. 21838-2:2020](https://www.iso.org/standard/74572.html)
7. [BFO-2020 GitHub Repository](https://github.com/BFO-ontology/BFO-2020/tree/21838-2/21838-2)
8. Other relevant references
