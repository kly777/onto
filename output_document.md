# Basic Formal Ontology: Case Studies

**J. Neil Otte**<sup>1</sup>, **John Beverley**<sup>2</sup>, and **Alan Ruttenberg**<sup>3</sup>  
<sup>1</sup>Johns Hopkins University Applied Physics Laboratory  
<sup>2</sup>Northwestern University  
<sup>3</sup>University at Buffalo  

**August 11, 2021**

## Abstract
Basic Formal Ontology (BFO) is a top-level ontology consisting of thirty-eight classes, designed to support information integration, retrieval, and analysis across all domains of scientific investigation, presently employed in over 350 ontology projects around the world. BFO is a genuine top-level ontology, containing no terms particular to material domains, such as physics, medicine, or psychology. In this paper, we demonstrate how a series of cases illustrating common types of change may be represented by universals, defined classes, and relations employing the BFO framework. We provide discussion of these cases to provide a template for other ontologists using BFO, as well as to facilitate comparison with the strategies proposed by ontologists using different top-level ontologies.

### Keywords: BFO, top-level ontology, ontological analysis, formal ontology

## 1. Introduction
In this paper, we demonstrate how **Basic Formal Ontology (BFO)** may be used to represent seven cases involving change. These cases, their goals, and their accompanying focus statements are discussed in order to provide a template for other ontologists using BFO, as well as to facilitate comparison with the strategies proposed by ontologists using different top-level ontologies.

**Basic Formal Ontology** is a top-level ontology designed to support information integration, retrieval, and analysis across all domains of scientific investigation. Containing only general terms common across disciplines, BFO serves as the top-level ontology of the Open Biomedical and Bioinformatic Ontology (OBO) Foundry [1] and the Industrial Ontology Foundry (IOF) [2].

Moreover, BFO provides a starting point for over 350 known ontology extensions covering more specific domains, such as infectious disease [3], plant development [4], and processed materials [5]. BFO has been designated an ISO standard [6] and BFO’s ISO 21838-2 specification has been axiomatized in First-Order Logic, OWL 2, and CLIF.

BFO is committed to the following principles [7], which distinguish it from other top-level ontologies [8]:
- **Ontological Realism** – The goal of an ontology is to describe reality. Scientific investigation is concerned with general features of reality and relations among them. Consequently, BFO consists fundamentally of representations of reality rather than merely language, concepts, or mental representations about reality [9].
- **Fallibilism** – Whereas universals themselves do not change, our understanding of them must in light of new discoveries. While present scientific theories are assumed to be our best sources of accurate statements about reality, BFO recognizes, of course, that present scientific theories may be incorrect. Consequently, BFO is committed to tracking scientific developments over time, and updating ontologies in accordance with scientific developments [2].
- **Adequatism** – Entities in a domain should not be assumed to be reducible to other kinds of entities. All scientific disciplines are worthy of representation in their own terms, and it is not necessary to paraphrase talk of these entities in terms of a privileged set of entities (e.g., those described by physics). This commitment contrasts with reductionism, which seeks to reduce entities described by some domain of science to another deemed more fundamental [9].

## 2. Principles and Structure of BFO
BFO adopts the following fundamental categories [6, 8]:

- **universal and particular** – Particulars are individual denizens of reality restricted to specific times and places, which instantiate universals, but which cannot be instantiated. Universals are repeatable across time and space and may have an indefinite number of instantiated particulars [13, 14].
- **continuant and occurrent** – BFO is largely bifurcated into disjoint universals, distinguished by how particulars relate to time. Continuants endure through time maintaining identity, have no temporal parts, and are fully-present at any time they exist. Examples include house cats, the color of an apple, the function of mitochondria. By contrast, occurrent entities unfold over time or have temporal parts. Examples include the history of Japan, drinking a cup of coffee, the temporal interval on which a mitotic division occurs [15].
- **relations** – BFO adopts three basic relation types: universal-universal, universal-particular, and particular-particular, the latter two of which may be time indexed. Universal-universal relations in BFO relate subtypes to parent types, whereas the sole universal-particular relation is the instance of relation, which holds between particulars and the universals under which they fall [16].

We discuss here only those classes necessary for the comprehension of the cases. In what follows, definitions are indicated with the use of “=def”, and those entries regarding classes that lack this symbol are elucidations. First, subclasses of continuant:

- **a is an independent continuant =def** a is a continuant which is such that there is no b such that a specifically depends on b and no b such that a generically depends on b.
  - **material entity** – an independent continuant that at all times at which it exists has some portion of matter as continuant part.
    - **object** – a material entity that manifests causal unity and is of a type instances of which are maximal relative to the sort of causal unity manifested.
    - **object aggregate** – a material entity consisting exactly of (≥1) object(s) as member(s).
  - **a is an immaterial entity =def** a is an independent continuant which is such that there is no time t when it has a material entity as continuant part.
    - **site** – a three-dimensional immaterial entity whose boundaries either (partially or wholly) coincide with the boundaries of one or more material entities or have locations determined in relation to some material entity.

An independent continuant may bear dependent continuants, including:
- **generically dependent continuant** – an entity that exists in virtue of the fact that there is at least one of what may be multiple copies; it is the content or the pattern that the multiple copies share.

- **b is a specifically dependent continuant =def** b is a continuant and there is some independent continuant c which is not a spatial region and which is such that b specifically depends on c.
  - **quality** – a specifically dependent continuant that, in contrast to roles and dispositions, does not require any further process in order to be realized.
  - **realizable entity** – a specifically dependent continuant that inheres in some independent continuant which is not a spatial region and is of a type some instances of which are realized in processes of a correlated type.
    - **role** – a realizable entity that exists because there is some single bearer that is in some special physical, social, or institutional set of circumstances in which this bearer does not have to be and which is not such that, if it ceases to exist, then the physical make-up of the bearer is thereby changed.
    - **disposition** – a realizable entity such that if it ceases to exist, then its bearer is physically changed, and whose realization occurs when and because its bearer is in some special physical circumstances, and this realization occurs in virtue of the bearer’s physical make-up.
      - **function** – a disposition that exists in virtue of the bearer’s physical make-up and this physical make-up is something the bearer possesses because it came into being either through evolution (in the case of natural biological entities) or through intentional design (in the case of artifacts), in order to realize processes of a certain sort.

From the occurrent portion of the hierarchy, we include the following:
- **p is a process =def** p is an occurrent that has some temporal proper part and for some time has some material entity as participant.
- **temporal region** – an occurrent over which processes can unfold.
  - **temporal instant** – a zero-dimensional temporal region that has no proper temporal part.
  - **temporal interval** – a one-dimensional temporal region that is continuous, thus without gaps or breaks.

There is often a practical need to accommodate terms in scientific discourse that do not correspond to universals. Examples of such terms include ‘medical doctor’ and disjunctions such as ‘dog or cat’. Such classes are called 'defined classes', and are represented as equivalent to any member satisfying a set of assertions whose non-logical symbols are satisfied by models consisting only of relations, universals, or instances of universals. In this way, we hold that

## Formalization and Analysis in BFO

### 3. Formalization of BFO in First-Order Logic

We describe a fragment of the **BFO ISO 21838-2 First-Order Logic (FOL)** axiomatization [6]. The domain is comprised of **particulars** that stand in the primitive instances of relation to **universals** at times. **BFO’s hierarchy of universals** can be represented by defining the relation:

\[ \forall x,t \; is\_a(A, B) =def \; instance\_of(x,A, t) \rightarrow instance\_of(x, B, t) \]

For example, **material entity** is a **independent continuant**. Visual representation of **BFO’s hierarchy** can be found in Figure 1 and Figure 2.

#### Figures

**Figure 1: BFO Continuant Hierarchy**

By **rigid universal** \( Ur \), we mean any entity that is instantiated by \( Ur \), instantiates \( Ur \) for the whole of its existence. All classes in **BFO** are rigid other than the three subclasses of **material entity**: **fiat object part**, **object**, and **object aggregate**. For example, an instance of **object aggregate** at some time may later instantiate **object**.

**BFO’s theory of parts** is modeled after **Minimal Extension Mereology (MEM)** [7]. MEM is described in terms of binary part relations, but is extended to handle the time-indexed relations. The MEM axioms state that a part relation is reflexive, antisymmetric, transitive, weakly supplemented, and exhibits the unique product property. Any time-indexed relation implies that the first two relata exist, and holds at any time the relata exist. For instance, when a time-indexed relation is reflexive, we mean that the self-relationship refers to the first two relata and it must hold at any time the relata exist.

**BFO** has two **part of** relations, one for **continuants**, called **continuant part of**, and one for **occurrents** called **occurrent part of**. **Continuant part of** is time indexed, whereas **occurrent part of** is not. Worth noting is the treatment of the anti-symmetry of **continuant part of** applied to **object aggregates**. If a **continuant part of b** at some \( t \) and \( b \) **continuant part of a** at the same time \( t \), we do not conclude that \( a=b \).

Using these relations, we can define **irreflexive, asymmetric, transitive proper occurrent part of** and **proper continuant part of** relations in the usual way.

#### Starting at the Continuant Side of the BFO Hierarchy

An **independent continuant** is distinguished from other **continuants** in that they neither generically nor specifically depend on other entities. In contrast, a **specifically dependent continuant** specifically depends on an **independent continuant** rigidly. If \( x \) specifically depends on \( y \), then as long as \( x \) exists, the relation holds. If \( y \) ceases to exist, then \( x \) does as well.

A **specifically dependent continuant** is said to **inhere in** – a relation defined in terms of **specifically depends on** – an instance of **independent continuant**. The inverse of **inheres in** is **bearer of**. A **generically dependent continuant** is concretized by a process or **specifically dependent continuant**. When the concretization is a **specifically dependent continuant**, the **generically dependent continuant** generically depends on the **specifically dependent continuant’s bearer**.

All **independent continuants** other than spatial regions occupy a spatial region, and so are extended in space and time. Some may be located in others at some time, as the food you ingest is at some point located in the lumen of your stomach after you have eaten. **Located in** is transitive.

A **material entity** can be **continuant part of** another **material entity** at some time. **Material entities** can have material and immaterial parts. An **object** can be **member part of** an **object aggregate**. **Member part of** is not transitive but implies **continuant part of**. An **object aggregate** always has at least one member, and must, at some time, have more than one.

Any **independent continuant**, **specifically dependent continuant**, or **generically dependent continuant** can participate in a process. In the latter two cases, it is implied that their **bearer** also participates in the process. When a process realizes a **realizable entity**, the **realizable entity’s bearer** also participates in the process. When a **generically dependent continuant** participates in a process \( p \), some concretization of the **generically dependent continuant** participates in \( p \). If that concretization is a process, it is **temporal part of** \( p \).

A **process** occupies a temporal region. **Processes** have at least one **process boundary** as part. The temporal region that a process occupies must have as part a **temporal interval**. A **process boundary** can only occupy a **temporal instant**.

An **occurrent** can be a **temporal part of** some other. **Occurrent parts** can differ from what they are part of both spatially and temporally (e.g., the process which occurs in the left half of a soccer field during the first period of a game). By contrast, **temporal part of an occurrent** differs in that there is no difference in the spatial extent of the part and the whole.

**Temporal regions** provide the indices for all the time-indexed ternary relations in **BFO**. A **temporal region** has a first instant and a last instant, marking its extrema. A first or last instant can be a **temporal part of** the region or not. A **temporal instant** that precedes the last instant of a temporal interval and is preceded by the interval’s first instant are necessarily part of the interval. Using these relations, the familiar and widely used Allen’s interval algebra may be formulated [17].

### 4. Analysis and Formalization in BFO: Examples

In this section, we examine several cases reflecting composition, roles, property and event change, and scientific progress. As **BFO** is a small top-level ontology comprised of domain-neutral terms, the examples use either terms we define in this paper, or wherever possible, existing terms from **BFO-aligned ontologies within the OBO Foundry library** [18] and **The Common Core Ontologies (CCO)** [19].

Since the cases reflect changes over time, **temporal intervals** will be used throughout. We introduce some formalization here to avoid repetitions. In each case, we will use “i” to represent the interval during which the case unfolds. We will use subscripts on “i” to represent proper interval parts of \( i \) ordered by precedence. Formally:

1. \( instance\_of(i, temporal\_interval, i) \)
2. \( \forall 1 \leq k \leq n \; instance\_of (ik, temporal\_interval, ik) \)
3. \( \forall 1 \leq k \leq n \; proper\_temporal\_part (ik, i) \)
4. \( \forall 1 \leq k \leq n \; precedes (ik, ik+1) \)

Many of the cases involve information. An **information content entity** is a **generically dependent continuant** that is about some entity. The term originates in the **Information Artifact Ontology (IAO)**, an ontology that extends **BFO**. Because **information content entity** is a direct subclass of **generically dependent continuant**, an **information content entity** may generically depend on one or more **material entities**. One example is the content of a novel may be concretized by patterns of ink in multiple physical books or may be concretized by the digital patterns in different network servers; when this occurs, the novel (an **information content entity**) then generically depends on the physical books and network servers.

Although it is possible to define a subclass of **information content entity** as always having a unique serialization (e.g., as in the case of an International Standard Book Number ISBN, which would have a unique serialization such as “978-0-393-28857-5”), it is preferable in many cases to track information that can be common across serializations or translations, much as a proposition may be expressed by different sentences. One way to enable this is to treat the serialization as a property of the bearer of the **information content entity**, rather than the **information content entity** itself. To illustrate, **Figure 3** depicts a measurement **information content entity**, its subject (an instance of **process of walking**), a **material entity**, and the measurement unit and string associated with that material entity. If the measurement **information content entity** was converted to kilometers, the instance of **information content entity** would remain the same, but would now also generically depend on a distinct instance of **information bearing entity** that would have text value “3.22 kilometers per hour”.

#### 4.1 Composition/Constitution

**CASE 1:** There is a four-legged table made of wood. Sometime later, a leg of the table is replaced. Even later, the table is demolished so it ceases to exist although the wood is still there after the demolition.

Any “proper” relation \( R(x,y) \) used here should be understood as \( R(x,y) \land x \neq y \).

In figures throughout, we use circular nodes to represent both **universals** and **defined classes**, and diamonds to represent particulars.

![Figure 3: Relationships among Information Content Entities and Bearers](#)

---

This structure maintains the original logic while enhancing readability through Markdown formatting, preserving key terms in bold, and organizing the content into sections and subsections.

## GOAL: Modeling Materials, Objects, and Components

### FOCUS: The Relationship Between Wood and the Table and Its Parts Over Time

**BFO** does not have a constitution relation such as "made of," typically related to an entity described as a mass noun. Instead, our example directly represents the particular portion of wood and its parts which are, when the table exists, part of the table.

### Classes, Particulars, and Relations

#### Class Definitions or Elucidations

- **portion of wood**: A material entity that was formerly part of one or more tree trunks or branches.
- **table function**: A function that inheres in a material entity with a flat surface that has realization as a process during which a material entity is placed on the bearer without it falling off.
- **leg function**: A function that inheres in a stiff object and which has realization as a process of support and elevation of other objects.
- **table destruction process**: A process during which a material entity bearer of a table function loses that table function.

#### Particular Descriptions

- **wood**: The portion of wood that has continuant part leg 1 at i2 and leg 2 at i5.
- **leg 1**: The object that is bearer of leg function 1. Leg 1 is replaced in the example.
- **leg 2**: The object that is bearer of leg function 2. Leg 2 replaces leg 1 in the example.
- **table function**: The table function that inheres in wood.
- **leg function 1**: The leg function that inheres in leg 1.
- **leg function 2**: The leg function that inheres in leg 2.
- **leg replacement process**: A process during which leg 1 is replaced by leg 2.
- **table destruction process**: A process resulting in wood losing table function 1.
- **i1**: The temporal interval during which wood is bearer of table function.
- **i2**: The temporal interval during which leg 1 is bearer of leg function 1.
- **i3**: The temporal interval during which leg 1 is proper continuant part of wood.
- **i4**: The temporal interval occupied by leg replacement process, which leg 1, leg 2, and wood participate in.
- **i5**: The temporal interval during which leg 2 is proper continuant part of wood.
- **i6**: The temporal interval at which leg 2 exists at.
- **i7**: The temporal interval occupied by table destruction process in which wood loses table function.

#### Relation Usage

- **bearer of**: Holds between a portion of wood and a function it bears. Bearer of is the inverse of inheres in.
- **exists at**: Holds between an entity and the temporal interval when it exists.
- **occupies temporal region**: Holds a process and intervals over which the process unfolds.
- **has participant**: Holds between a process, a material entity involved in that process, and the temporal region at which the process occurs.
- **proper continuant part of**: Holds between a proper mereological part of wood and wood itself, at the temporal region during which they are parts.

### Formalization of Case 1

Wood is an instance of **portion of wood** throughout interval i and its seven sub-intervals:

1. is a(portion of wood, material entity)
2. instance of(wood, portion of wood, i)

Wood bears a table function and has proper continuant part several legs. We focus on leg 1. We relate respective functions and material bearers:

3. instance of(leg function 1, leg function, i2)
4. instance of(table function, table function, i1)
5. instance of(leg 1, object, i3)
6. instance of(wood, object, i2)
7. bearer of(wood, table function)
8. bearer of(leg 1, leg function 1)
9. proper continuant part of(leg 1, wood, i2)

Wood, leg 1, and leg 2 participate in leg replacement process:

10. instance of(leg function 2, leg function, i)
11. instance of(leg 2, object, i6)
12. bearer of(leg 2, leg function 2)
13. :continuant part of(leg 2, wood, i3)11
14. instance of(leg replacement process, leg replacement process, i4)

15. occupies temporal region(leg replacement process, i4)
16. participates in(leg 1, leg replacement process, i4)
17. :continuant part of(leg 1, wood, i5)12
18. participates in(leg 2, leg replacement process, i4)
19. proper continuant part of(leg 2, wood, i5)

Afterwards, wood and its parts participate in an instance of table destruction process:

20. instance of(table destruction process, table destruction process, i7)
21. occupies temporal region(table destruction process, i7)
22. participates in(wood, table destruction process, i7)
23. 9toccurrent part of(t, i7) Λ:exists at(table function, t)

We leave open whether proper parts of wood maintain their respective functions. That is compatible with the case that most proper parts of wood parts maintain their functions but are arranged such that wood loses table function. In any event, wood exists at i7 though table function does not and thus wood no longer instantiates table. Figure 4 provides an illustration of the change described in this case.

## Roles

### CASE 2: Mr. Potter and Mrs. Bumblebee

### GOAL: Modeling Relationships Between Roles, Players, and Organizations

### FOCUS: Change of Roles/Players; Vacancy of Teaching Position; Persistence of the Class While Students Come and Go

Mr. Potter is – we assume – the only teacher of class 2C prior to Spring Break and participates in an act of resignation prior to this break. Classes at Shapism School are not in session during the break, but during this time Mrs. Bumblebee and Shapism School agree that Mrs. Bumblebee will bear a 2C teacher role at the end of Spring Break.

### Class Definitions or Elucidations

- **person**: An object belonging to the species primate and distinguished by a high level of intelligence.
- **organization**: An independent continuant that can play roles, has members, and has a set of organization rules.

### Particular Descriptions

- **Mr. Potter**: An instance of person.
- **Mrs. Bumblebee**: An instance of person.
- **Shapism School**: An instance of organization, the academic employer of Mr. Potter and Mrs. Bumblebee.
- **2C**: A member part of Shapism School, in which Mr. Potter and Mrs. Bumblebee teach.
- **2C teacher role 1**: The role borne by Mr. Potter as the teacher of class 2C.
- **2C teacher role 2**: The role borne by Mrs. Bumblebee as the teacher of class 2C.
- **act of resignation**: The process during which Mr. Potter resigns from his role as teacher of class 2C.
- **act of teaching assignment**: The process during which Shapism School and Mrs. Bumblebee coordinate resulting in Mrs. Bumblebee bearing the 2C teacher role.

### Relation Descriptions

- **bearer of**: Holds between instances of person and the teacher roles which inhere in that person.
- **proper temporal part of**: Holds between temporal intervals and the larger interval of which they are occurent part.
- **occupies temporal region**: Holds between processes and just those temporal intervals over which they unfold.
- **participates in**: Holds between material entities and the processes in which they are involved.
- **member part of**: Holds between object aggregates and their members.
- **has specified output**: Holds between act of teaching assignment and Mrs. Bumblebee’s 2C teacher role.

### Formalization of Case 2

Mr. Potter and Mrs. Bumblebee are instances of person [19]. Shapism School is an instance of organization [20,21]. Organizations may have other organizations as member parts, allowing for class 2C to be member part of Shapism School:

1. is a(person, object)
2. is a(organization, object aggregate)
3. instance of(Mr. Potter, person, i)
4. instance of(Mrs. Bumblebee, person, i)
5. instance of(Shapism School, organization, i)
6. member part of(2C, Shapism School, i)

Mr. Potter was a member part of 2C prior to the start of spring break. Mrs. Bumblebee was not a member of 2C during this time. Before spring break begins, Mr. Potter participates in an act of resignation so that during and after spring break Mr. Potter is no longer a member part of 2C. We leave open whether Mr. Potter remains a member of Shapism School during and after spring break:

7. member part of(Mr. Potter, 2C, i1)
8. :member part of(Mrs. Bumblebee, 2C, i1)
9. instance of(spring break, process, i)
10. instance of(act of resignation, process, i3)
11. participates in(Mr. Potter, act of resignation, i3)

```markdown
## Detailed Analysis of BFO Framework

### 12. Case Study: Teaching Assignment and Resignation

#### 12.1 Member Part Relationships

- **member part of**(Mr. Potter, 2C, i4)
- **participates in**(Shapism School, act of teaching assignment, i6)
- **participates in**(Mrs. Bumblebee, act of teaching assignment, i4)
- **member part of**(Mrs. Bumblebee, 2C, i7)

#### 12.2 Temporal Regions and Proper Temporal Parts

- **occupies temporal region**(act of teaching assignment, i5)
- **proper temporal part of**(i4, i5)
- **proper temporal part of**(i6, i5)

#### 12.3 Role Transitions

- Mr. Potter bears **2C teacher role 1** during interval i4.
- Mrs. Bumblebee becomes the unique bearer of **2C teacher role 2** after the act of teaching assignment.
- **Figure 5**: Resignation and Assignment of 2C Teacher Roles in Case 2

### 12.4 Formalization Details

- **bearer of**(Mr. Potter, 2C teacher role 1)
- **exists at**(2C teacher role 1, i4)
- **has specified output**(act of teaching assignment, 2C teacher role 2)
- **bearer of**(Mrs. Bumblebee, 2C teacher role 2)

### 4.3 Property Change

#### CASE 3: Color Change of a Flower

##### Goal

The example aims to show if and how the ontology models change in qualities/properties.

##### Focus

The change of the color of a flower.

##### Key Concepts

- **Color** is a messy phenomenon that can be described at different levels of granularity.
- We focus on colors as **qualities** of entities rather than dispositions or experiences.

##### Class Definitions

- **flower**: A material entity that generates seeds during a reproductive cycle.
- **petal**: A material entity leaf that often surrounds reproductive parts of some flower.
- **color**: A quality borne by a material entity that underwrites the reflection of light.
- **red**: A color with wavelength between 625 and 740 nanometers.
- **brown**: A color with wavelength of approximately 600 nanometers, with low saturation and luminance.

##### Particular Descriptions

- **petal**: The petal that bears a color quality that changes from red to brown.
- **flower**: The flower whose petal continuant part changes color through the season change.
- **summer**: The process during which the petal begins as red and gradually becomes closer in color to brown.
- **fall**: The process during which the petal begins as reddish brown but gradually becomes brown.
- **process of withering**: The process during which the flower loses elasticity and vibrancy.

##### Intervals

- **i1**: Interval occupied by summer.
- **i2**: Interval occupied by fall.
- **i3**: Interval during which color is an instance of red.
- **i4**: Interval occupied by the process of withering.
- **i5**: Interval during which color is an instance of brown.
- **i6**: Interval during which color is an instance of color.

##### Relations Usage

- **participates in**: Holds between flower and process of withering.
- **occupies temporal region**: Holds between summer, fall, process of withering, and the respective temporal regions they each occupy.
- **occurrent part of**: Holds between temporal intervals and larger intervals of which they are parts.
- **proper continuant part of**: Holds between petal and the flower of which it is a part.
- **bearer of**: Holds between petal and the color that it bears.

##### Formalization Steps

1. **instance of**(flower, flower, i)
2. **instance of**(petal, petal, i)
3. **proper continuant part of**(petal, flower, i)
4. **is a**(color, quality)
5. **is a**(red, color)
6. **is a**(brown, color)
7. **instance of**(color, color, i6)
8. **bearer of**(petal, color)
9. **instance of**(summer, process, i1)
10. **instance of**(fall, process, i2)
11. **occupies temporal region**(summer, i1)
12. **occupies temporal region**(fall, i2)
13. **instance of**(color, red, i3)
14. **instance of**(color, brown, i5)
15. **occurrent part of**(i3, i1)
16. **occurrent part of**(i3, i6)
17. **occurrent part of**(i5, i4)
18. **occurrent part of**(i5, i6)
19. **instance of**(process of withering, process, i4)
20. **occupies temporal region**(process of withering, i4)
21. **occurrent part of**(i4, i2)

### CASE 4: Change in Locomotion Speed and Mode

#### Goal

The example aims to show if and how the ontology models change during an event.

#### Focus

The change in the speed and mode of locomotion.

#### Processes and Participation

Processes do not change; they are changes. Participating in an act of locomotion may have proper process parts such as walking, accelerating, and running.

#### Particulars Descriptions

- **man**: An instance of person who bears some male gender.
- **act of locomotion**: An instance of process in which the man changes spatial position.
- **act of walking**: An instance of process in which the man changes spatial position exerting little effort, at a low speed.
- **act of accelerating**: An instance of process in which the man increases speed at which he changes spatial position.
- **act of running**: An instance of process in which the man changes spatial position while exerting significant effort, at a high speed.
- **i1**: Interval during which the man participates in an act of walking.
- **i2**: Interval during which the man participates in an act of accelerating.
- **i3**: Interval during which the man participates in an act of running.

#### Relations Usage

- **proper occurrent part of**: Holds between acts of accelerating, walking, and the larger act of locomotion of which they are parts.
- **participates in**: Holds between the man and processes in which he participates.

#### Formalization

The man participates in an act of locomotion [18].
```

This structured Markdown format retains the original logic and context while enhancing readability and clarity.

```markdown
## Event Change

### CASE 5: A man is walking to the station, but before he gets there, he turns around and goes home.

#### GOAL
The example aims to show if and how the **ontology** models change in goal-directed activities.

#### FOCUS
An activity/event is not completed and another activity/event is completed instead.

---

The man commits himself to a plan to walk to the station, which is specified in terms of actions he might take and the objective he seeks. Prior to arriving at the station, the man abandons his initial plan and forms another, this time to turn around and walk home. As before, the man’s plan to walk home is specified in terms of actions he might take and the objective he seeks. In this case, the man achieves his objective.

### Class Definitions or Elucidations

- **plan**: A realizable entity that inheres in a bearer who is committed to realizing it as a planned process.
- **plan specification**: An information entity with action specifications and objective specifications as continuant parts that, when concretized, is realized in a process in that the bearer tries to achieve the objectives by taking the actions specified.
- **information content entity**: A generically dependent entity that depends on some artifact and stands in a relation of aboutness to some entity.
- **action specification**: An information entity that describes an action the bearer will take.
- **objective specification**: An information entity that describes an intended process endpoint. When a continuant part of a plan specification, the concretization is realized in a planned process in which the bearer tries to effect the world so that the process endpoint is achieved.
- **facility**: A material entity that is designed as a building or campus dedicated to some specific purpose.
- **planned process**: A process that realizes a plan that is the concretization of a plan specification.

### Particulars Descriptions

- **man**: The person who bears some male gender in the scenario.
- **plan 1**: The plan that the man forms to walk to the station.
- **plan 2**: The plan that the man forms to turn around and walk home.
- **station plan specification**: The plan specification having continuant parts station action specification and station objective specification.
- **station action specification**: An action specification describing the steps the man intends to take to walk to the station.
- **station objective specification**: The objective specification describing reaching the station as the objective of the station plan specification.
- **home plan specification**: The plan specification having parts home action specification and home objective specification.
- **home action specification**: The action specification describing the steps the man intends to take to turn around and walk home.
- **home objective specification**: The objective specification describing reaching home as the objective of the home objective plan.
- **station**: The facility to which the man initially intends to walk.
- **home**: The facility to which the man later walks.
- **station description**: The information content entity describing the station, that is a continuant part of the station objective specification.
- **home description**: The information content entity describing the man’s home, that is a continuant part of the home objective specification.
- **4mph walk**: The process during a uniform velocity which the man walks at 4 mph.
- **3mph walk**: The process during a uniform velocity which the man walks at 3 mph.
- **180 turn**: The process during which the man turns 180 degrees.

### Relations Descriptions

- **concretized by**: Holds between station plan specification, home plan specification, and plan 1 and plan 2, respectively.
- **proper continuant part of**: Holds between action and objective specifications and plan specifications, as well as between descriptions and objective specifications.
- **exists at**: Holds between plan specifications and the temporal intervals at which they exist.
- **is about**: Holds between descriptions and the entities they describe.
- **bearer of**: Holds between the man and plan 1 and plan 2.
- **prescribes**: Holds between an action specification and the processes that the specification prescribes.
- **achieves planned objective**: Holds between a planned process and objective specification when the criteria specified in the objective specification are met at the end of the planned process.
- **participates in**: Holds between man and the processes in which he participates.

### Temporal Intervals

- **i1**: Interval during which the station plan specification exists, and during which the station action specification and objective specification are proper continuant parts of the station plan specification.
- **i2**: Interval during which the station plan specification is concretized by plan 1.
- **i3**: Interval during which the man participates in the 4mph walk process.
- **i4**: Interval during which the man participates in the 180 turn process.
- **i5**: Interval during which the man participates in the 3mph walk process.
- **i6**: Interval during which home plan specification is concretized by plan 2.
- **i7**: Interval during which the home plan specification exists, and during which the home action specification and objective specification are proper continuant parts of the home plan specification.

### Formalization Summary

The man bears **plan 1**, which is a concretization of **station plan specification**. Station plan specification has continuant parts both an action specification that prescribes the steps the man might take to walk to the station and the objective specification that describes the goal of plan 1:

---

This formalization captures the detailed relationships and changes in the man's activities and plans over time, demonstrating how **BFO** can model complex sequences of events and their associated goals and actions.
```

```markdown
## 4.5 Concept Evolution

### CASE 6: Marriage Contract and Its Evolution

#### GOAL
The example aims to show if and how the **ontology** models the evolution of the meaning of a term.

#### FOCUS
The continuity/discontinuity of the meaning of marriage in the presence of changing qualifications.

Speaking of ‘the meaning’ of marriage is spurious. Like most words, ‘marriage’ is polysemous. It can refer to:
- A process in which spouses participate.
- Information content entities (i.e., the idea of marriage in the minds of particular people, or as represented in legal documents).
- A pair of mutually dependent spousal roles and their associated powers and privileges.

Some uses of ‘marriage’ pull together all three meanings, as when we speak of the institution of marriage and denote a set of practices (processes) realizing marital powers (roles) that are prescribed by social or religious doctrine and law (information content entities). In representing marriage, we should take care not to conflate these different notions. As Groucho Marx once quipped: "Marriage is a wonderful institution, but who wants to live in an institution?"

#### Marriage License Regulations
Marriage license regulations vary by geographical region, population, and organizational affiliation. In the U.S., for example, marriage requirements, laws, and associated rights are established by states. All states impose eligibility requirements on individuals. For example:
- Individuals entering marriage must have the capacity to consent to the arrangement and must be above a certain age.
- States also impose eligibility requirements on the couple. For example, at least one member of the union must be a U.S. citizen.
- Before 1967, several states prohibited interracial marriage.
- Until 2015, several prohibited same-sex marriage [28].

Governments also grant obligations to spouses—married partners bear financial responsibilities to one another—and privileges—married partners are not required to testify against one another in court. Obligations and privileges can, like eligibility requirements, be changed by governing agencies.

We focus on the present status of a marriage contract issued in the U.S. between 1967 and 2015, and subsequent legal changes after 2015.

### Class Definitions or Elucidation
- **document**: A collection of information content entities intended to be understood together as a whole.
- **government**: An organization that exercises executive, legislative, or judicial authority over a region.
- **marriage license**: A document issued by a government, which legally binds agents as spouses and invests them with associated instances of deontic role.
- **deontic declaration**: A social act that creates or revokes a deontic role.
- **social act**: A planned process that is carried out by a person or an organization, and is self-generated, directed towards another person or an aggregate of persons, an organization or an aggregate of organizations, and that needs to be perceived.
- **deontic role**: A role that inheres in a person and that is externally grounded in the normative expectations that other persons within a social context have concerning how that person should behave.
- **action regulation**: An information content entity that prescribes an act as required, prohibited, or permitted, and is the output of an act that realizes some authority role.
- **authority role**: A role that is realized by actions that create, modify, transfer, or eliminate action regulations or other authority roles, and inheres in an agent in virtue of collective acceptance of that agent’s ability to issue binding directives.

### Particulars Descriptions
- **U.S. Supreme Court**: The branch of government able to legally create or revoke deontic powers of state government.
- **deontic declaration 1**: The deontic declaration that has specified output marriage license.
- **deontic declaration 2**: The deontic declaration that has specified output action regulation 1.
- **deontic declaration 3**: The deontic declaration that legally revokes deontic role 1 and deontic role 3.
- **deontic role 1**: The deontic role inhering in Alex realized in Alex legally refraining from testifying against Bailey in court.
- **deontic role 2**: The deontic role inhering in Alex realized in Alex’s legal permission to file income taxes jointly with Bailey.
- **deontic role 3**: The deontic role inhering in Bailey realized in Bailey legally refraining from testifying against Alex in court.
- **deontic role 4**: The deontic role inhering in Bailey realized in Bailey’s legal permission to file income taxes jointly with Alex.
- **marriage license**: The marriage license issued by state government, which legally binds Alex and Bailey together as spouses, and invests them with associated instances of deontic role.
- **state government**: The government participating in the marriage of Alex and Bailey.
- **Alex**: The person entering acquiring a marriage license with Bailey.
- **Bailey**: The person entering acquiring a marriage license with Alex.
- **marriage licensure document**: A document describing the objective of issuing, and steps that must be taken to issue marriage license.
- **action regulation 1**: An action regulation requiring state government to issue instances of marriage license for consenting same-sex couples.
- **authority role 1**: An authority role borne by state government, prescribed by action regulation 1.
- **i1**: The interval during which state government, Alex, and Bailey participate in deontic declaration 1 resulting in the creation of marriage contract.
- **i2**: The interval during which U.S. Supreme Court participates in deontic declaration 2 requiring state government to recognize same-sex marriage.
- **i3**: The interval during which state government legally revokes deontic role 1 and deontic role 3.

### Relations Descriptions
```

This structured Markdown format organizes the provided text into clear sections and sub-sections, emphasizing key terms and maintaining the original logical structure.

## Participates in Holds Between Agents and Instances of Deontic Declaration

### Deontic Declarations and Marriage Licensure

The following text describes the relationships between agents, instances of deontic declarations, and documents, specifically focusing on the marriage license case.

#### Classes, Particulars, and Relations Used to Formalize Case 6

The **marriage license** is an instance of the class **marriage license**, which is a subclass of **document** [29,30 31,32]. The **state government**, which issues the marriage license, is an instance of **government**, which is a type of organization able to exercise judicial, legislative, or executive authority over a site.

1. is a(document, information content entity)
2. is a(marriage license, document)
3. is a(government, organization)
4. instance of(marriage license, marriage license, i)
5. instance of(state government, government, i)

The **state government** participates in **deontic declaration 1**, a type of social act [28,29,30], which has specified input a **marriage licensure document** that includes a plan specification. This plan specification describes the intended legal entities created according to the objective specification, as well as the manner in which the deontic declaration should be performed to achieve that objective – as described by the action specification. For simplicity, we do not include these continuant parts of the marriage licensure document. 

6. is a(deontic declaration, social act)
7. instance of(deontic declaration 1, deontic declaration, i1)
8. participates in(state government, deontic declaration 1, i1)
9. has specified input(deontic declaration 1, marriage licensure document)
10. has specified output(deontic declaration 1, marriage license)

### Roles Inherent in Alex and Bailey

**Alex** and **Bailey** each participate in **deontic declaration 1** as well. Instances of **deontic declaration** involve the creation or revoking of **deontic roles**. Instances of **deontic role** inhere in persons or organizations but are externally grounded in the normative expectations others have concerning how bearers should behave. In this case, instances of **deontic role** inhere in Alex and Bailey, respectively. These respective roles are realized in processes typically associated with marriage, such as filing taxes jointly and making medical decisions on behalf of the spouse. For simplicity, we focus on only two such **deontic roles** each for Alex and Bailey.

11. instance of(Alex, person, i)
12. instance of(Bailey, person, i)
13. participates in(Alex, deontic declaration 1, i1)
14. participates in(Bailey, deontic declaration 1, i1)
15. is a(deontic role, role)
16. instance of(deontic role 1, deontic role, i1)
17. instance of(deontic role 2, deontic role, i1)
18. instance of(deontic role 3, deontic role, i1)
19. instance of(deontic role 4, deontic role, i1)
20. inheres in(deontic role 1, Alex)
21. inheres in(deontic role 2, Alex)
22. inheres in(deontic role 3, Bailey)
23. inheres in(deontic role 4, Bailey)

### Changes in Legal Framework

At some point, following **deontic declaration 1** that results in the state government issuing a marriage license for Alex and Bailey, the **U.S. Supreme Court** participates in **deontic declaration 2**, resulting in all state prohibitions on same-sex marriage being deemed unconstitutional. **Deontic declaration 2** has specified output **action regulation 1** permitting the authorization of same-sex marriage. This prescription sanctions new realizations of state and local agent instances of **authority role** relevant to marriage contracts, by broadening the class of those eligible to participate in an act of marrying.

24. instance of(U.S. Supreme Court, organization, i)
25. instance of(deontic declaration 2, deontic declaration, i2)
26. participates in(U.S. Supreme Court, deontic declaration 2, i2)
27. is a(action regulation, information content entity)
28. instance of(action regulation, action regulation, i2)
29. has specified output(deontic declaration 2, action regulation 1)
30. is a(authority role, role)
31. instance of(authority role 1, authority role, i2)
32. prescribes(action regulation, authority role 1)
33. inheres in(authority role 1, state government 1)

The expansion of sanctioned realizations of instances of **authority role** by the state government does not undermine that Alex and Bailey have a marriage license. This is because instances of **deontic role** borne by Alex and Bailey are not altered by **action regulation 1**, since **action regulation 1** targets eligibility constraints on marriage.

### Revocation of Deontic Roles

As discussed, governments may alter marriage contracts in another way, by changing spousal obligations and powers. To illustrate, suppose the **state government** participates in **deontic declaration 3**, which legally revokes the **deontic role 1** that inheres in Alex and **deontic role 2** that inheres in Bailey, which we assume correspond to privileges bearers have to refrain from testifying against their spouse. This results in Alex and Bailey losing these respective roles, though they maintain **deontic role 2** and **deontic role 4**.

34. participates in(state government, deontic declaration 3, i3)
35. legally revokes(deontic declaration 3, deontic role 1, i3)
36. legally revokes(deontic declaration 3, deontic role 3, i3)
37. 9t occurrent part of(t, i3) Λ:exists at(deontic role 1, t) Λ:exists at(deontic role 3, t)

At least two types of change to marriage licenses can be represented with BFO, reflecting changes to eligibility requirements – which either narrow or extend participants – or changes to associated roles – which either narrow or extend spousal rights and obligations. In each case, the meaning of marriage, in some sense, remains the same.

## Ontology Usage and Community Impact

BFO is committed to there being a single reality, with scientific investigation often resulting in clarifications of our picture of this reality. As science updates, ontology should follow. Other conceptions, past or present, of the way the world is, or might be, are merely informational entities and impose no further ontological commitments.

As the core architecture of OBO and IOF [1,2], BFO is widely used across a range of scientific disciplines. BFO is, for example, used extensively in the biomedical domain [33], providing domain specialists foundational support when modeling phenotypes [34], disease [35,36,37], diagnosis [38,39], and resistance [40]. BFO is presently used in over 350 ontology products, and with its recent standardization, this number will no doubt increase in the coming years.

### Acknowledgements

Thanks to Barry Smith for his comments on an early draft of this manuscript. J. Neil Otte and Alan Ruttenberg gratefully acknowledge The Digital Manufacturing and Design Innovation Institute (DMDII) for their research funding in support of this work.