# Basic Formal Ontology: Case Studies

**J. Neil Otte**<sup>1</sup>, **John Beverley**<sup>2</sup>, and **Alan Ruttenberg**<sup>3</sup>  
<sup>1</sup>Johns Hopkins University Applied Physics Laboratory  
<sup>2</sup>Northwestern University  
<sup>3</sup>University at Buffalo  

**August 11, 2021**

## Abstract

**Basic Formal Ontology (BFO)** is a top-level ontology consisting of thirty-eight classes, designed to support information integration, retrieval, and analysis across all domains of scientific investigation, presently employed in over 350 ontology projects around the world. BFO is a genuine top-level ontology, containing no terms particular to material domains, such as physics, medicine, or psychology. In this paper, we demonstrate how a series of cases illustrating common types of change may be represented by universals, defined classes, and relations employing the BFO framework. We provide discussion of these cases to provide a template for other ontologists using BFO, as well as to facilitate comparison with the strategies proposed by ontologists using different top-level ontologies.

**Keywords:** BFO, top-level ontology, ontological analysis, formal ontology

## 1. Introduction

In this paper, we demonstrate how **Basic Formal Ontology (BFO)** may be used to represent seven cases involving change. These cases, their goals, and their accompanying focus statements are discussed in order to provide a template for other ontologists using BFO, as well as to facilitate comparison with the strategies proposed by ontologists using different top-level ontologies.

**Basic Formal Ontology** is a top-level ontology designed to support information integration, retrieval, and analysis across all domains of scientific investigation. Containing only general terms common across disciplines, BFO serves as the top-level ontology of the Open Biomedical and Bioinformatic Ontology (OBO) Foundry [1] and the Industrial Ontology Foundry (IOF) [2].

All authors contributed equally to this work.

International Organization for Standardization. (2016). Information technology — Top-level ontologies (TLO) — Part 2: Basic Formal Ontology (BFO)(ISO Standard No. 21838-2:2020). Retrieved from https://www.iso.org/standard/74572.html

Moreover, BFO provides a starting point for over 350 known ontology extensions covering more specific domains, such as infectious disease [3], plant development [4], and processed materials [5]. BFO has been designated an ISO standard [6] and BFO’s ISO 21838-2 specification has been axiomatized in First-Order Logic, OWL 2, and CLIF.

### Principles Distinguishing BFO from Other Top-Level Ontologies

BFO is committed to the following principles [7], which distinguish it from other top-level ontologies [8]:

- **Ontological Realism** – The goal of an ontology is to describe reality. Scientific investigation is concerned with general features of reality and relations among them. Consequently, BFO consists fundamentally of representations of reality rather than merely language, concepts, or mental representations about reality [9].
- **Fallibilism** – Whereas universals themselves do not change, our understanding of them must in light of new discoveries. While present scientific theories are assumed to be our best sources of accurate statements about reality, BFO recognizes, of course, that present scientific theories may be incorrect. Consequently, BFO is committed to tracking scientific developments over time, and updating ontologies in accordance with scientific developments [2].
- **Adequatism** – Entities in a domain should not be assumed to be reducible to other kinds of entities. All scientific disciplines are worthy of representation in their own terms, and it is not necessary to paraphrase talk of these entities in terms of a privileged set of entities (e.g., those described by physics). This commitment contrasts with reductionism, which seeks to reduce entities described by some domain of science to another deemed more fundamental [9].

## 2. Principles and Structure of BFO

BFO adopts the following fundamental categories [6, 8]:

- **Universal and Particular** – Particulars are individual denizens of reality restricted to specific times and places, which instantiate universals, but which cannot be instantiated. Universals are repeatable across time and space and may have an indefinite number of instantiated particulars [13, 14].
- **Continuant and Occurrent** – BFO is largely bifurcated into disjoint universals, distinguished by how particulars relate to time. Continuants endure through time maintaining identity, have no temporal parts, and are fully-present at any time they exist. Examples include house cats, the

### Exceptions to Disjointedness

The exceptions to disjointedness are BFO’s classes **fiat object part**, **object**, and **object aggregate**. Some instances may belong to more than one of these classes.

#### References
1. Users of BFO. Accessed December 25, 2020 at http://basic-formal-ontology.org/users.html
2. BFO-2020. Accessed December 25, 2020 at https://github.com/BFO-ontology/BFO-2020/tree/21838-2/21838-2

## Basic Formal Ontology (BFO) Entities and Relations

### Continuant Entities

Continuant entities persist through time without change in their identity. Examples include the **color of an apple** and the **function of mitochondria**. By contrast, occurrent entities unfold over time or have temporal parts. Examples include: the history of Japan, drinking a cup of coffee, the temporal interval on which a mitotic division occurs [15].

#### Relations

BFO adopts three basic relation types:

- **Universal-universal**: Relate sub-types to parent types.
- **Universal-particular**: The sole universal-particular relation is the **instance of** relation, which holds between particulars and the universals under which they fall.
- **Particular-particular**: These may be time-indexed.

We discuss here only those classes necessary for the comprehension of the cases. In what follows, definitions are indicated with the use of “=def”, and entries regarding classes that lack this symbol are elucidations.

#### Sub-classes of Continuant

- **Independent continuant** =def a continuant which is such that there is no b such that a specifically depends on b and no b such that a generically depends on b.

  - **Material entity** – An independent continuant that at all times at which it exists has some portion of matter as continuant part.
  
    - **Object** – A material entity that manifests causal unity and is of a type instances of which are maximal relative to the sort of causal unity manifested.
    - **Object aggregate** – A material entity consisting exactly of (≥1) object(s) as member(s).

  - **Immaterial entity** =def a continuant which is such that there is no time t when it has a material entity as continuant part.
  
    - **Site** – A three-dimensional immaterial entity whose boundaries either (partially or wholly) coincide with the boundaries of one or more material entities or have locations determined in relation to some material entity.

An independent continuant may bear dependent continuants, including:

- **Generically dependent continuant** – An entity that exists in virtue of the fact that there is at least one of what may be multiple copies; it is the content or the pattern that the multiple copies share.

#### Specifically Dependent Continuants

- **Specifically dependent continuant** =def a continuant and there is some independent continuant c which is not a spatial region and which is such that b specifically depends on c.

  - **Quality** – A specifically dependent continuant that, in contrast to roles and dispositions, does not require any further process in order to be realized.
  - **Realizable entity** – A specifically dependent continuant that inheres in some independent continuant which is not a spatial region and is of a type some instances of which are realized in processes of a correlated type.

    - **Role** – A realizable entity that exists because there is some single bearer that is in some special physical, social, or institutional set of circumstances in which this bearer does not have to be and which is not such that, if it ceases to exist, then the physical make-up of the bearer is thereby changed.
    - **Disposition** – A realizable entity such that if it ceases to exist, then its bearer is physically changed, and whose realization occurs when and because its bearer is in some special physical circumstances, and this realization occurs in virtue of the bearer’s physical make-up.

      - **Function** – A disposition that exists in virtue of the bearer’s physical make-up and this physical make-up is something the bearer possesses because it came into being either through evolution (in the case of natural biological entities) or through intentional design (in the case of artifacts), in order to realize processes of a certain sort.

### Occurrent Entities

From the occurrent portion of the hierarchy, we include the following:

- **Process** =def p is an occurrent that has some temporal proper part and for some time has some material entity as participant.
- **Temporal region** – An occurrent over which processes can unfold.

  - **Temporal instant** – A zero-dimensional temporal region that has no proper temporal part.
  - **Temporal interval** – A one-dimensional temporal region that is continuous, thus without gaps or breaks.

### Defined Classes

There is often a practical need to accommodate terms in scientific discourse that do not correspond to universals. Examples of such terms include ‘medical doctor’ and disjunctions such as ‘dog or cat’. Such classes are called **defined classes**, and are represented as equivalent to any member satisfying a set of assertions whose non-logical symbols are satisfied by models consisting only of relations, universals, or instances of universals. In this way, we hold that

---

This structured Markdown format retains the original logical structure, uses appropriate headings to denote sections, and highlights key terms using bold formatting.

## Formalization of BFO in First-Order Logic

We describe a fragment of the **BFO ISO 21838-2 First-Order Logic (FOL)** axiomatization [6]. The domain is comprised of particulars that stand in the primitive instances of relation to universals at times. **BFO's hierarchy of universals** can be represented by defining the relation:

\[ \forall x,t \, \text{is a}(A, B) =_{\text{def}} \text{instance of}(x,A, t) \rightarrow \text{instance of}(x, B, t) \]

For example, **material entity** is a **independent continuant**. Visual representation of **BFO’s hierarchy** can be found in Figure 1 and Figure 2.

### Figure 1: BFO Continuant Hierarchy

By **rigid universal** \( U_r \), we mean any entity that is instantiated by \( U_r \), instantiates \( U_r \) for the whole of its existence. All classes in **BFO** are rigid other than the three subclasses of **material entity**: **fiat object part**, **object**, and **object aggregate**. For example, an instance of **object aggregate** at some time may later instantiate **object**.

### BFO’s Theory of Parts

**BFO’s theory of parts** is modeled after **Minimal Extension Mereology (MEM)** [7]. MEM is described in terms of binary part relations, but is extended to handle the time-indexed relations. The **MEM axioms** state that a part relation is **reflexive**, **antisymmetric**, **transitive**, **weakly supplemented**, and exhibits the unique product property. Any time-indexed relation implies that the first two relata exist, and holds at any time the relata exist. For instance, when a time-indexed relation is reflexive we mean that the self-relationship refers to the first two relata and it must hold at any time the relata exist.

**BFO** has two part of relations, one for **continuants**, called **continuant part of** and one for **occurrents** called **occurrent part of**. **Continuant part of** is time indexed, whereas **occurrent part of** is not. Worth noting is the treatment of the anti-symmetry of **continuant part of** applied to **object aggregates**. If a **continuant part of b** at some \( t \) and \( b \) **continuant part of a** at the same time \( t \), we do not conclude that \( a=b \).

Using these relations we can define **irreflexive**, **asymmetric**, **transitive proper occurrent part of** and **proper continuant part of** relations in the usual way.

### Continuant Side of the BFO Hierarchy

Starting at the **continuant side** of the **BFO hierarchy** in Figure 1, an **independent continuant** is distinguished from other continuants in that they neither generically nor specifically depend on other entities. In contrast, a **specifically dependent continuant** specifically depends on an **independent continuant** rigidly. If \( x \) specifically depends on \( y \), then as long as \( x \) exists, the relation holds. If \( y \) ceases to exist, then \( x \) does as well.

A **specifically dependent continuant** is said to **inhere in** – a relation defined in terms of **specifically depends on** – an instance of **independent continuant**. The inverse of **inheres in** is **bearer of**. A **generically dependent continuant**

> Note: In a number of relations involving independent continuants, the relation is actually valid only if the entity is a spatial region. In order to keep the discussion simpler, we do not mention it in the body.

### Figure 2: BFO Occurrent Hierarchy

---

The above text maintains the original structure and logic while applying Markdown formatting and emphasizing key terms with bold.

## Basic Formal Ontology (BFO) and Its Applications

### Description of BFO in First-Order Logic

The **Basic Formal Ontology (BFO)** framework distinguishes between **continuants** (such as independent continuants and specifically dependent continuants) and **occurrants** (such as processes and time regions), defining three fundamental types of relationships between them: universal-universal, universal-particular, and particular-particular relations.

This section describes the formalization of BFO (ISO 21838-2) in first-order logic, including its **universals' hierarchy**, the definition of **rigid universals**, the parts theory based on **Minimal Extension Mereology (MEM)**, and the part-whole relationships for **continuants** and **occurrents**, particularly focusing on the distinctions and dependencies between **independent continuants** and **specifically dependent continuants**.

### Continuants and Their Relationships

#### Spatial and Temporal Characteristics

All **independent continuants** other than spatial regions occupy a spatial region and are thus extended in space and time. Some may be located within others at some point in time. For example, food you ingest is eventually located in the lumen of your stomach after you have eaten. The relation "located in" is transitive.

#### Part-Whole Relationships

A material entity can be a **continuant part** of another material entity at some time. Material entities can have both material and immaterial parts. An object can be a **member part** of an object aggregate. The relation "member part of" is not transitive but implies "continuant part of". An object aggregate always has at least one member and must, at some time, have more than one.

#### Participation in Processes

Any **independent continuant**, **specifically dependent continuant**, or **generically dependent continuant** can participate in a process. In the latter two cases, it is implied that their bearer also participates in the process. When a process realizes a realizable entity, the realizable entity’s bearer also participates in the process. When a **generically dependent continuant** participates in a process \( p \), some concretization of the generically dependent continuant participates in \( p \). If that concretization is a process, it is a **temporal part** of \( p \).

### Occurrents and Temporal Regions

#### Temporal Structure of Processes

A process occupies a **temporal region**. Processes have at least one **process boundary** as part. The temporal region that a process occupies must include a **temporal interval**. A **process boundary** can only occupy a **temporal instant**.

#### Temporal Parts

An **occurrent** can be a **temporal part** of another occurrent. Occurrent parts can differ from what they are part of both spatially and temporally (e.g., the process occurring in the left half of a soccer field during the first period of a game). By contrast, a **temporal part** of an occurrent differs in that there is no difference in the spatial extent of the part and the whole.

#### Temporal Indices

Temporal regions provide the indices for all time-indexed ternary relations in BFO. A temporal region has a **first instant** and a **last instant**, marking its extrema. A first or last instant can be a temporal part of the region or not. A temporal instant that precedes the last instant of a temporal interval and is preceded by the interval’s first instant is necessarily part of the interval. Using these relations, Allen's interval algebra may be formulated [17].

### Analysis and Formalization in BFO: Examples

In this section, we examine several cases reflecting composition, roles, property and event change, and scientific progress. Since BFO is a small top-level ontology comprised of domain-neutral terms, the examples use either terms defined in this paper or, wherever possible, existing terms from BFO-aligned ontologies within the OBO Foundry library [18] and The Common Core Ontologies (CCO) [19].

Since the cases reflect changes over time, temporal intervals will be used throughout. We introduce some formalization here to avoid repetitions. In each case, we will use “\( i \)” to represent the interval during which the case unfolds. We will use subscripts on “\( i \)” to represent proper interval parts of \( i \) ordered by precedence. Formally:

---

This structured format maintains the original logical flow and terminology while enhancing readability through Markdown formatting.

## Basic Formal Ontology (BFO) in First-Order Logic

### 1. Temporal Intervals and Information Content Entities

1. instance of(i, temporal interval, i)
2. ^1≤k≤n instance of(ik, temporal interval, ik)
3. ^1≤k≤n proper temporal part(ik, i)
4. ^1≤k≤n precedes(ik, ik+1)

Many of the cases involve **information content entities**. An information content entity is a **generically dependent continuant** that is about some entity. The term originates in the **Information Artifact Ontology (IAO)**, an ontology that extends BFO. Because an information content entity is a direct subclass of generically dependent continuant, it may generically depend on one or more material entities.

One example is the content of a novel, which may be concretized by patterns of ink in multiple physical books or by digital patterns in different network servers. When this occurs, the novel (an information content entity) then generically depends on the physical books and network servers.

Although it is possible to define a subclass of information content entity as always having a unique serialization (e.g., as in the case of an International Standard Book Number ISBN, which would have a unique serialization such as “978-0-393-28857-5”), it is preferable in many cases to track information that can be common across serializations or translations, much like a proposition may be expressed by different sentences. One way to enable this is to treat the serialization as a property of the bearer of the information content entity, rather than the information content entity itself.

To illustrate, Figure 3 depicts a measurement information content entity, its subject (an instance of process of walking), a material entity, and the measurement unit and string associated with that material entity. If the measurement information content entity was converted to kilometers, the instance of information content entity would remain the same, but would now also generically depend on a distinct instance of information bearing entity that would have text value “3.22 kilometers per hour”.

### 4.1 Composition/Constitution

#### CASE 1: Four-Legged Wooden Table

There is a four-legged table made of wood. Sometime later, a leg of the table is replaced. Even later, the table is demolished so it ceases to exist, although the wood is still there after the demolition.

Any “proper” relation R(x,y) used here should be understood as R(x,y) Λ x≠y.

In figures throughout, we use circular nodes to represent both universals and defined classes, and diamonds to represent particulars.

![Figure 3](#)  
*Figure 3: Relationships among Information Content Entities and Bearers*

#### Goal

The example aims to show if and how the ontology models materials, objects, and components and the relationships among them.

#### Focus

The relationship between the wood and the table and the table’s parts over time. (Artefacts and functions are not the focus.)

BFO does not have a constitution relation such as “made of,” typically related to an entity described as a mass noun. Instead, our example directly represents the particular portion of wood and its parts which are, when the table exists, part of the table.

In Table 1, we describe the classes, particulars, and relations we will use in our discussion.

| Class | Definition or Elucidation |
|-------|---------------------------|
| Portion of wood | A material entity that was formerly part of one or more tree trunks or branches |
| Table function | A function that inheres in a material entity with a flat surface that has realization a process during which a material entity is placed on the bearer without it falling off |
| Leg function | A function that inheres in a stiff object and which has realization a process of support and elevation of other objects |
| Table destruction process | A process during which a material entity bearer of a table function loses that table function |

The portion of wood exists throughout the interval but changes. At the beginning of the interval, the portion of wood bears a table function and has parts that bear leg functions. The portion of wood participates in a leg replacement process, during which one of its proper parts that bears a leg function is replaced by a material entity bearing a leg function. After the replacement, the original leg is no longer part of the portion of wood, and the replacement leg is now part of it. Afterward, the portion of wood participates in a destruction process, during which it loses its table function, and so no longer instantiates a table.

## Particular Description

### Wood and its Parts

- **Wood** the portion of wood that has continuant part leg
  - **Leg 1** at **i2** and **Leg 2** at **i5**

### Object Descriptions

- **Leg 1**: The object that is bearer of **leg function 1**. Leg 1 is replaced in the example.
- **Leg 2**: The object that is bearer of **leg function 2**. Leg 2 replaces Leg 1 in the example.
- **Table function**: The table function that inheres in wood.
- **Leg function 1**: The leg function that inheres in Leg 1.
- **Leg function 2**: The leg function that inheres in Leg 2.
- **Leg replacement process**: A process during which Leg 1 is replaced by Leg 2.
- **Table destruction process**: A process resulting in wood losing **table function**.

### Temporal Intervals

- **i1**: The temporal interval during which wood is bearer of **table function**.
- **i2**: The temporal interval during which Leg 1 is bearer of **leg function 1**.
- **i3**: The temporal interval during which Leg 1 is proper continuant part of wood.
- **i4**: The temporal interval occupied by **leg replacement process**, which Leg 1, Leg 2, and wood participate in.
- **i5**: The temporal interval during which Leg 2 is proper continuant part of wood.
- **i6**: The temporal interval at which Leg 2 exists at.
- **i7**: The temporal interval occupied by **table destruction process** in which wood loses **table function**.

## Relation Usage

- **Bearer of**: Holding between a portion of wood and a function it bears. **Bearer of** is the inverse of **inheres in**.
- **Exists at**: Holding between an entity and the temporal interval when it exists.
- **Occupies temporal region**: Holding a process and intervals over which the process unfolds.
- **Has participant**: Holding between a process, a material entity involved in that process, and the temporal region at which the process occurs.
- **Proper continuant part of**: Holding between a proper mereological part of wood and wood itself, at the temporal region during which they are parts.

### Table 1: Classes, Particulars, and Relations used to Formalize Case 1

**Wood** is an instance of **portion of wood** throughout interval **i** and its seven sub-intervals:

1. **is a**(portion of wood, material entity)
2. **instance of**(wood, portion of wood, i)

   Wood bears a **table function** and has proper continuant part several legs. We focus on **Leg 1**. We relate respective functions and material bearers:

3. **instance of**(leg function 1, leg function, i2)
4. **instance of**(table function, table function, i1)
5. **instance of**(leg 1, object, i3)
6. **instance of**(wood, object, i2)
7. **bearer of**(wood, table function)
8. **bearer of**(leg 1, leg function 1)
9. **proper continuant part of**(leg 1, wood, i2)

   Wood, **Leg 1**, and **Leg 2** participate in **leg replacement process**:

10. **instance of**(leg function 2, leg function, i)
11. **instance of**(leg 2, object, i6)
12. **bearer of**(leg 2, leg function 2)
13. **continuant part of**(leg 2, wood, i3)  
    11 Strictly speaking, Leg 2 is also not a continuant part of wood at earlier times. Corresponding axioms are assumed but not displayed here.
14. **instance of**(leg replacement process, leg replacement process, i4)

```markdown
## 信息内容实体与物质实体的关系

该文本主要探讨了**Basic Formal Ontology (BFO)**中**信息内容实体**（information content entities）作为**泛依赖持续体**（generically dependent continuants）的特性及其与物质实体的关系，并通过一个四腿木桌的例子详细说明了材料、对象及其组成部分之间的关系如何随时间变化。该文本详细描述了木头及其组成部分（特别是腿1和腿2）在不同时间间隔内的存在和功能变化，包括腿替换过程和桌子功能的丧失，使用了特定的专业术语如**bearer of**、**proper continuant part of**和**temporal interval**。

### 腿替换过程

15. occupies **temporal region**(leg replacement process, i4)
16. participates in(leg 1, leg replacement process, i4)
17. :continuant part of(leg 1, wood, i5)  
18. participates in(leg 2, leg replacement process, i4)
19. **proper continuant part of**(leg 2, wood, i5)

之后，木头及其部分参与了一个实例的桌子破坏过程：

20. instance of(table destruction process, table destruction process, i7)
21. occupies **temporal region**(table destruction process, i7)
22. participates in(wood, table destruction process, i7)
23. **occurrent part of**(t, i7) Λ:exists at(table function, t)

我们保留是否木头的适当部分维持其各自的功能这一问题。这与大多数木头部分维持其功能但排列方式导致木头失去桌子功能的情况兼容。无论如何，木头在i7期间存在，尽管桌子功能不存在，因此木头不再实例化为桌子。图4提供了这种情况变化的图示。

### 角色

#### CASE 2: 教师角色变更

**GOAL:** 该例子旨在展示本体论如何建模角色、参与者和组织之间的关系。

**FOCUS:** 角色/参与者的变更；教学职位的空缺；班级在学生进出时的持久性。

Mr. Potter是——我们假设——春假前2C班唯一的老师，并参与了辞职行为。Shapism School在春假期间不进行课程，但在这一期间，Mrs. Bumblebee和Shapism School达成协议，Mrs. Bumblebee将在春假结束时承担2C班教师的角色。我们仅关注Mr. Potter和Mrs. Bumblebee的形式化，因为在此期间学生Mary的离开和新学生John的加入与教师Mr. Potter的离职和Mrs. Bumblebee的入职没有显著差异。我们在形式化中使用以下赋值：

12. 严格来说，腿1在更早的时间也不是木头的持续部分。相应的公理被假设但未在此显示。

#### 角色功能

##### 类定义或阐释

- **person**: 属于灵长类物种且以高智商区别的对象。
- **organization**: 可以扮演角色、拥有成员并有一套组织规则的独立持续体。

##### 特殊描述

- **Mr. Potter**: 一个person的实例
- **Mrs. Bumblebee**: 一个person的实例
- **Shapism School**: 一个organization的实例，Mr. Potter和Mrs. Bumblebee的学术雇主
- **2C**: Shapism School的一个成员部分，其中Mr. Potter和Mrs. Bumblebee授课
- **2C teacher role 1**: Mr. Potter作为2C班教师所承担的角色
- **2C teacher role 2**: Mrs. Bumblebee作为2C班教师所承担的角色
- **act of resignation**: Mr. Potter从2C班教师角色辞职的过程
- **act of teaching assignment**: Shapism School和Mrs. Bumblebee协调的结果，使Mrs. Bumblebee承担2C班教师角色

##### 关系描述

- **bearer of**: 持有person实例和其内在的教师角色之间的关系
- **proper temporal part of**: 持有时间区间与其较大的发生区间之间的关系
- **occupies temporal region**: 持有过程及其展开的时间区间之间的关系
- **participates in**: 持有物质实体及其参与的过程之间的关系
- **member part of**: 持有对象聚合体及其成员之间的关系
- **has specified output**: 持有教学分配行为和Mrs. Bumblebee的2C班教师角色之间的关系

表2：用于形式化案例2的特殊和关系

Mr. Potter和Mrs. Bumblebee是person的实例 [19]。Shapism School是organization的实例 [20,21]。组织可以有其他组织作为成员部分，允许2C成为Shapism School的成员部分：
```

这个Markdown格式的文本保持了原始逻辑结构，并使用加粗字体标记了关键术语。章节层级根据内容进行了适当的划分。

```markdown
## Basic Formal Ontology (BFO) and Information Content Entities

### Information Content Entities as Generically Dependent Continuants

The text primarily explores the characteristics of **information content entities** as **generically dependent continuants** within the framework of **Basic Formal Ontology (BFO)**, focusing on their relationship with material entities. It uses a four-legged wooden table as an illustrative example to detail how materials, objects, and their components change over time.

### Example: Teacher Role Changes at Shapism School

#### Entities and Relationships

1. **is a**(person, object)
2. **is a**(organization, object aggregate)
3. **instance of**(Mr. Potter, person, i)
4. **instance of**(Mrs. Bumblebee, person, i)
5. **instance of**(Shapism School, organization, i)
6. **member part of**(2C, Shapism School, i)

#### Contextual Events

- Mr. Potter was a member part of 2C prior to the start of spring break.
- Mrs. Bumblebee was not a member of 2C during this time.
- Before spring break begins, Mr. Potter participates in an act of resignation so that during and after spring break, Mr. Potter is no longer a member part of 2C.
- We leave open whether Mr. Potter remains a member of Shapism School during and after spring break:

#### Formal Statements

7. **member part of**(Mr. Potter, 2C, i1)
8. **:member part of**(Mrs. Bumblebee, 2C, i1)
9. **instance of**(spring break, process, i)
10. **instance of**(act of resignation, process, i3)
11. **participates in**(Mr. Potter, act of resignation, i3)

#### Teaching Assignment Process

- Shapism School and Mrs. Bumblebee participate in an act of teaching assignment resulting in Mrs. Bumblebee being a member part of 2C after spring break.
12. **occupies temporal region**(act of teaching assignment, i5)
13. **proper temporal part of**(i4, i5)
14. **proper temporal part of**(i6, i5)
15. **participates in**(Shapism School, act of teaching assignment, i6)
16. **participates in**(Mrs. Bumblebee, act of teaching assignment, i4)
17. **member part of**(Mrs. Bumblebee, 2C, i7)

#### Role Bearing

- With respect to relevant roles, Mr. Potter bears 2C teacher role 1 – a role borne by a unique person who is a member part of 2C at a given time.
- Following the act of teaching assignment in which Shapism School and Mrs. Bumblebee participate, Mrs. Bumblebee becomes the unique bearer of 2C teacher role 2.
- There is currently no well-developed treatment of titles, organizational positions, and offices as such, where these are understood to be independent of the particular role that persons bear when holding such offices.

#### Formal Role Assignments

18. **bearer of**(Mr. Potter, 2C teacher role 1)
19. **exists at**(2C teacher role 1, i4)
20. **has specified output**(act of teaching assignment, 2C teacher role 2)
21. **bearer of**(Mrs. Bumblebee, 2C teacher role 2)

### Property Change

#### Case Study: Flower Color Change

##### Goal

The goal of this case study is to illustrate how the ontology models changes in qualities or properties.

##### Focus

The focus is on the change in the color of a flower from red in summer to brown in autumn.

##### Explanation

Color is a complex phenomenon. Color ascriptions can be described at different levels of granularity, for example:
- The whole flower
- Flower petals
- Proper surface parts of petals

Distributions of colors at one level of granularity often determine color at higher levels of granularity. For instance, classifying a petal as "red" depends on the distribution of red on proper parts of the petal's surface. Additionally, color may be understood as qualities, dispositions to cause color experiences, or the color experiences themselves.

For simplicity, we focus on a specific petal of the flower, noting that our formalization can be applied to lower or higher levels of granularity. Moreover, we focus on colors as qualities of entities rather than dispositions to cause experiences or as experiences.

Broadly speaking, the petal bears a red color quality during summer that becomes brown during fall. During this time, the flower participates in an act of withering.

##### Class Definitions

- **petal**: A material entity leaf that often surrounds reproductive parts of some flower.
- **flower**: A material entity that generates seeds during a reproductive cycle.
- **color**: A quality borne by a material entity that underwrites the reflection of light.
- **red**: A color with a wavelength between 625 and 740 nanometers.
- **brown**: A color with a wavelength of approximately 600 nanometers, with low saturation and luminance.

##### Temporal Considerations

- **2C teacher role does not exist during subsequent intervals**.
- **2C teacher role does not exist before interval i5**.
```

This structured Markdown format captures the hierarchical nature of the content while preserving key terminology and logical structure.

## Particular Description

### Petal
- **petal**: The petal that bears a color quality that changes from red to brown.

### Flower
- **flower**: The flower whose petal **proper continuant part** changes color through the season change.

### Color
- **color**: The color borne by the petal that changes from red to brown.

### Summer
- **summer**: The process during which the petal begins as red and gradually becomes closer in color to brown.

### Fall
- **fall**: The process during which the petal begins as reddish brown, but gradually becomes brown.

### Process of Withering
- **process of withering**: The process during which the flower loses elasticity and vibrancy.

### Temporal Intervals
- **i1**: The interval occupied by summer.
- **i2**: The interval occupied by fall.
- **i3**: The interval during which color is an instance of red, which is an **occurrent part** of both i1 and i6.
- **i4**: The interval occupied by the process of withering, which is an **occurrent part** of i2.
- **i5**: The interval during which color is an instance of brown, which is an **occurrent part** of both i4 and i6.
- **i6**: The interval during which color is an instance of color.

### Relation Usage
- **participates in**: Holds between flower and process of withering.
- **occupies temporal region**: Holds between summer, fall, process of withering, and the respective temporal regions they each occupy.
- **occurrent part of**: Holds between temporal intervals and larger intervals of which they are parts.
- **proper continuant part of**: Holds between petal and the flower of which it is a part.
- **bearer of**: Holds between petal and the color that it bears.

### Table 3: Classes, Particulars, and Relations Used to Formalize Case 3

We use the classes **flower** and **petal** [4,22] and assert the instance **flower** has **continuant part** petal, which is an instance of the latter:

1. `instance of(flower, flower, i)`
2. `instance of(petal, petal, i)`
3. `proper continuant part of(petal, flower, i)`

Color is a specifically dependent **continuant** in BFO [23]. We assert two subclasses of color: red and brown, and we furthermore assert that petal bears an instance of color:

4. `is a(color, quality)`
5. `is a(red, color)`
6. `is a(brown, color)`
7. `instance of(color, color, i6)`
8. `bearer of(petal, color)`

The color borne by petal is an instance of red during summer, and an instance of brown during fall:

9. `instance of(summer, process, i1)`
10. `instance of(fall, process, i2)`
11. `occupies temporal region(summer, i1)`
12. `occupies temporal region(fall, i2)`
13. `instance of(color, red, i3)`
14. `instance of(color, brown, i5)`
15. `occurrent part of(i3, i1)`
16. `occurrent part of(i3, i6)`
17. `occurrent part of(i5, i4)`
18. `occurrent part of(i5, i6)`
19. `instance of(process of withering, process, i4)`
20. `occupies temporal region(process of withering, i4)`
21. `occurrent part of(i4, i2)`

## CASE 4: A Man Participating in an Act of Locomotion

### Goal
The example aims to show if and how the ontology models change during an event.

### Focus
The change in the speed and mode of locomotion.

### Processes
Processes do not change; they are changes. Participating in an act of locomotion, however, may have proper process parts such as walking, accelerating, and running. Intuitively, walking and running consist of sequences involving an agent who makes patterned contact with the ground using their feet, over some duration. For a given agent and given duration, walking is distinguished from running based on the number of moments of contact between the agent’s feet and the ground. If this number is above some threshold, which may vary given the agent’s size and shape, then it will count as running. An individual is accelerating when there is a patterned decrease in the duration between contacts with the ground and an increase in the spatial distance traversed by the agent.

### Particulars Descriptions
- **man**: An instance of person who bears some male gender.
- **act of locomotion**: An instance of process in which the man changes spatial position.
- **act of walking**: An instance of process in which the man changes spatial position exerting little effort, at a low speed.
- **act of accelerating**: An instance of process in which the man increases speed at which he changes spatial position.
- **act of running**: An instance of process in which the man changes spatial position, while exerting significant effort, at a high speed.
- **i1**: The interval during which the man participates in an act of walking.
- **i2**: The interval during which the man participates in an act of accelerating.
- **i3**: The interval during which the man participates in an act of running.

### Relations Usage
- **proper occurrent part of**: Holds between acts of accelerating, walking, and the larger act of locomotion of which they are parts.
- **participates in**: Holds between the man and processes in which he participates.

### Table 4: Classes, Particulars, and Relations Used to Formalize Case 4
The man participates in an act of locomotion [18].

## 事件变化

### CASE 5: 一个男人走到车站，但在到达之前他转身回家

#### 目标
该例子旨在展示本体论如何建模目标导向活动中的变化。

#### 焦点
一个活动/事件未完成，而另一个活动/事件完成了。

---

**The man commits himself to a plan to walk to the station**, which is specified in terms of actions he might take and the objective he seeks. Prior to arriving at the station, the man abandons his initial plan and forms another, this time to turn around and walk home. **As before, the man’s plan to walk home is specified in terms of actions he might take and the objective he seeks. In this case, the man achieves his objective.**

### 类定义或阐明

#### **plan**
- **定义**: 一个可实现的实体，存在于承担者中，后者致力于将其作为计划过程来实现。

#### **plan specification**
- **定义**: 一个信息实体，包含行动规范和目标规范作为持续体部分。当具体化时，在过程中实现，承担者通过采取规定的行动来尝试实现目标。

#### **information content entity**
- **定义**: 一个泛依赖实体，依赖于某些人工制品，并与某个实体存在关于性的关系。

#### **action specification**
- **定义**: 描述承担者将采取的行动的信息实体。

#### **objective specification**
- **定义**: 描述预期过程终点的信息实体。当作为计划规范的持续体部分时，具体化是在计划过程中实现的，其中承担者试图改变世界以实现过程终点。

#### **facility**
- **定义**: 设计为用于特定目的的建筑物或校园的物质实体。

#### **planned process**
- **定义**: 实现一个计划的过程，该计划是计划规范的具体化。

### 特殊描述

- **man**: 在场景中具有男性性别的承担者。
- **plan 1**: 男人形成的计划，目的是走到车站。

---

### 行走、加速和跑步的参与

1. **instance of**(man, person, i)
2. **instance of**(act of locomotion, process, i)
3. **participates in**(man, act of locomotion, i)

这个过程由适当的偶发部分组成，包括行走行为、加速行为和跑步行为。男人参与了每一个行为。图7展示了我们对这个案例的形式化说明。

4. **proper occurrent part of**(act of walking, act of locomotion)
5. **proper occurrent part of**(act of accelerating, act of locomotion)
6. **proper occurrent part of**(act of running, act of locomotion)
7. **proper occurrent part of**(act of accelerating, act of walking)
8. **proper occurrent part of**(act of accelerating, act of running)
9. **participates in**(man, act of walking, i1)
10. **participates in**(man, act of accelerating, i2)
11. **participates in**(man, act of running, i3)

虽然我们对这个案例的描述是一般的，但可以添加补充的细化。例如，男人在这个案例中的不同时间间隔内的速度变化可以用测量表示。图3提供了一个使用泛依赖持续体实例表征测量的方法。此外，我们对下一个案例的分析进一步展示了对变化运动的补充表征。

## CASE 5: Formalizing Changes in Goal-Directed Activities

### Plan Specifications and Related Entities

#### Plan 2
- **plan 2**: The plan that the man forms to turn around and walk home.

#### Station Plan Specification
- **station plan specification**: The plan specification having **continuant part** station action specification and station objective specification.
  - **station action specification**: An action specification describing the steps the man intends to take to walk to the station.
  - **station objective specification**: The objective specification describing reaching the station as the objective of the station plan specification.

#### Home Plan Specification
- **home plan specification**: The plan specification having parts home action specification and home objective specification.
  - **home action specification**: The action specification describing the steps the man intends to take to turn around and walk home.
  - **home objective specification**: The objective specification describing reaching home as the objective of the home objective plan.

### Facilities and Descriptions
- **station**: The facility to which the man initially intends to walk.
- **home**: The facility to which the man later walks.
- **station description**: The **information content entity** describing the station, which is a **continuant part** of the station objective specification.
- **home description**: The **information content entity** describing the man’s home, which is a **continuant part** of the home objective specification.

### Processes and Temporal Intervals
- **4mph walk**: The process during a uniform velocity at which the man walks at 4 mph.
- **3mph walk**: The process during a uniform velocity at which the man walks at 3 mph.
- **180 turn**: The process during which the man turns 180 degrees.
  
#### Temporal Intervals
- **i1**: Interval during which the station plan specification exists, and during which the station action specification and objective specification are **proper continuant parts** of the station plan specification.
- **i2**: Interval during which the station plan specification is concretized by plan 1.
- **i3**: Interval during which the man participates in the 4mph walk process.
- **i4**: Interval during which the man participates in the 180 turn process.
- **i5**: Interval during which the man participates in the 3mph walk process.
- **i6**: Interval during which the home plan specification is concretized by plan 2.
- **i7**: Interval during which the home plan specification exists, and during which the home action specification and objective specification are **proper continuant parts** of the home plan specification.

### Relations Descriptions

| Relation             | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| **concretized by**   | Holds between station plan specification, home plan specification, and plan 1 and plan 2, respectively. |
| **proper continuant part of** | Holds between action and objective specifications and plan specifications, as well as between descriptions and objective specifications. |
| **exists at**        | Holds between plan specifications and the temporal intervals at which they exist. |
| **is about**         | Holds between descriptions and the entities they describe.                   |
| **bearer of**        | Holds between the man and plan 1 and plan 2.                                 |
| **prescribes**       | Holds between an action specification and the processes that the specification prescribes. |
| **achieves planned objective** | Holds between a planned process and objective specification when the criteria specified in the objective specification are met at the end of the planned process. |
| **participates in**  | Holds between the man and the processes in which he participates.             |

### Table 5: Classes, Particulars, and Relations Used to Formalize Case 5

The man bears **plan 1**, which is a concretization of station plan specification. Station plan specification has **continuant part** both an action specification that prescribes the steps the man might take to walk to the station and the objective specification that describes the goal of plan 1:

This formalization demonstrates how ontological changes in goal-directed activities can be modeled using the **Basic Formal Ontology (BFO)** framework, emphasizing the roles of **information content entities** and their relationships with material entities over time.

```markdown
## CASE 5: Modeling Changes in Goal-Directed Activities

### Plan and Specification Instances

1. **is a**(plan, realizable entity)
2. **is a**(plan specification, information content entity)
3. **instance of**(plan 1, plan, i)
4. **instance of**(station plan specification, plan specification, i2)
5. **instance of**(station action specification, action specification, i2)
6. **instance of**(station objective specification, objective specification, i2)

### Relationships and Inherence

7. **inheres in**(plan 1, man)
8. **concretized by**(station plan specification, plan 1, i3)
9. **continuant part of**(station action specification, station plan specification, i2)
10. **continuant part of**(station objective specification, station plan specification, i2)

**Station** is an instance of facility [18]. Because **plan 1** is an instance of a realizable entity, it is not strictly speaking about anything, as only **information content entities** may be about some entity. Nevertheless, there is an instance of an **information content entity** that is part of the **station objective specification** and concretized by **plan 1**, which includes the station in its description. We can thus say **man’s plan 1 (derivatively) is about the station**. Moreover, the **station action specification** includes the walking plan he intends to take in pursuit of that objective. Additionally, the man participates in a 4mph walk:

11. **instance of**(station, facility, i)
12. **instance of**(station description, information content entity, i)
13. **continuant part of**(station description, station objective specification, i2)
14. **described by**(station, station description)
15. **participates in**(man, 4mph walk, i4)

### Plan 2 and Return Home

At some time, the man forms **plan 2** to walk back home, then participates in an instance of 180 turn, then participates in a 3mph walk until he arrives home:

16. **instance of**(plan 2, plan, i)
17. **instance of**(home plan specification, plan specification, i)
18. **instance of**(home action specification, action specification, i6)
19. **instance of**(home objective specification, objective specification, i6)
20. **continuant part of**(home action specification, home plan specification, i6)
21. **continuant part of**(home objective specification, home plan specification, i6)
22. **inheres in**(plan 2, man)
23. **concretized by**(home plan specification, plan 2, i6)
24. **prescribes**(home plan specification, 180 turn)
25. **prescribes**(home plan specification, 3mph walk)
26. **participates in**(man, 180 turn, i4)
27. **participates in**(man, 3mph walk, i5)
28. **realized in**(plan 2, 180 turn)
29. **realized in**(plan 2, 3mph walk)

The man’s home is a facility. There is an instance of an **information content entity** that is part of the **home objective specification** and concretized by **plan 2**, where **plan 2** includes home in its description. We can thus say the man’s **plan 2 is (derivatively) about the home**. As before, the **home action specification** includes the walking plan the man intends to take. In this case, the man does achieve his planned objective, which we can represent by the man’s participating in an instance of **planned process** and bearing an **achieves objective relation** to the **home objective specification**, which we import from [21,22].

### Detailed Specifications

30. **is a**(planned process, process)
31. **instance of**(planned process, planned process, i)
32. **instance of**(home, facility, i)
33. **instance of**(home description, information content entity, i7)
34. **continuant part of**(home description, home objective specification, i7)
35. **described by**(home, home description)
36. **participates in**(man, planned process, i6)
37. **achieves planned objective**(planned process, home objective specification)

For further specification of the man’s walk, formalizations of distance measurement using **BFO** and its extensions illustrated in Figure 3 can be leveraged to describe how far the man traveled in his initial trip before turning back.

![Figure 8: Man Walking to Station, then Home in Case 5](#)

## 4.5 Concept Evolution

### CASE 6: Marriage as a Contract

#### GOAL:
The example aims to show if and how the ontology models the evolution of the meaning of a term.

#### FOCUS:
The continuity/discontinuity of the meaning of marriage in the presence of changing qualifications.

Speaking of ‘the meaning’ of marriage is spurious. Like most words, ‘marriage’ is polysemous. It can refer to a process in which spouses participate; it can refer to **information content entities** (i.e., the idea of marriage in the minds of particular people, or as represented in legal documents); and it can refer to a pair of mutually dependent spousal roles and their associated powers and privileges. Some uses of ‘marriage’ pull together all three meanings, as when we speak of
```

This structured Markdown format organizes the text into clear sections, maintains the original logic structure, and highlights key terms for better readability.

## 通过本体论建模目标导向活动中的变化：CASE 5

### 上下文线索

该文本通过**CASE 5**展示了本体论如何建模目标导向活动中的变化，重点在于一个未完成的活动（走到车站）和一个完成的活动（转身回家），并定义了相关专业术语如**plan**、**plan specification**、**information content entity**等。该文本核心内容是：通过使用**Basic Formal Ontology (BFO)**框架，详细描述和形式化了个体在目标导向活动中计划的变更，特别是通过**information content entities**、**continuant parts**及其与物质实体的时间关系来建模这些变化。

### 核心内容

该文本的核心内容是通过具体的实例（如目标导向活动的建模、车站和回家计划、以及婚姻合同的概念演变），展示了如何使用本体论模型来表示和追踪实体、计划、动作和目标之间的关系及其演变，特别是在信息内容实体和实现过程中的关联。

### 婚姻制度及其演变

婚姻制度是一系列实践（过程）的集合，这些实践实现了由社会或宗教教义和法律（**information content entities**）规定的婚姻权力（角色）。在表示婚姻时，我们应该注意不要混淆这些不同的概念。正如格劳乔·马克斯曾经打趣说：“婚姻是一个美好的机构，但谁愿意住在机构里呢？”

#### 婚姻许可证规定

婚姻许可证的规定因地理位置、人口和组织隶属关系而异。例如，在美国，婚姻要求、法律和相关权利由各州制定。所有州都对个人施加资格要求。例如，进入婚姻的个人必须有能力同意该安排，并且必须达到一定年龄。各州还对夫妻双方施加资格要求。例如，至少有一方必须是美国公民；1967年之前，一些州禁止跨种族婚姻；直到2015年，一些州禁止同性婚姻 [28]。政府还授予配偶义务——已婚伴侣彼此承担财务责任——以及特权——已婚伴侣不需要在法庭上作证反对对方。义务和特权可以像资格要求一样由政府机关更改。

我们专注于1967年至2015年间在美国颁发的婚姻合同的现状，以及2015年后的法律变化。

### 类定义或阐明

#### 定义

- **document**：一组旨在作为一个整体理解的信息内容实体。
- **government**：行使执行、立法或司法权威的组织。
- **marriage license**：由政府颁发的文件，合法地将代理人绑定为配偶，并赋予他们相应的**deontic role**。
- **deontic declaration**：一种创造或撤销**deontic role**的社会行为。
- **social act**：由个人或组织计划并自行实施的过程，面向另一人或一群人、组织或一群组织，并需要被感知。
- **deontic role**：一个人拥有的角色，这种角色以外部规范为基础，即其他人在社会背景下对该人的行为期望。
- **action regulation**：规定某行为为必需、禁止或允许的信息内容实体，是实现某种权威角色的行为输出。
- **authority role**：通过创建、修改、转移或消除行动法规或其他权威角色的行为实现的角色，内在于代理人在集体接受其发布具有约束力指令的能力的基础上。

### 特殊描述

- **U.S. Supreme Court**：能够合法创建或撤销州政府**deontic powers**的政府分支。
- **deontic declaration 1**：具有指定输出**marriage license**的**deontic declaration**。
- **deontic declaration 2**：具有指定输出**action regulation 1**的**deontic declaration**。
- **deontic declaration 3**：依法撤销**deontic role 1**和**deontic role 3**的**deontic declaration**。
- **deontic role 1**：Alex在法律上不需在法庭上作证反对Bailey的**deontic role**。
- **deontic role 2**：Alex有法律权限与Bailey联合报税的**deontic role**。
- **deontic role 3**：Bailey在法律上不需在法庭上作证反对Alex的**deontic role**。
- **deontic role 4**：Bailey有法律权限与Alex联合报税的**deontic role**。
- **marriage license**：由州政府颁发的婚姻许可证，将Alex和Bailey合法绑定为配偶，并赋予他们相关的**deontic role**。
- **state government**：参与Alex和Bailey婚姻的政府。
- **Alex**：与Bailey一起获取婚姻许可证的人。
- **Bailey**：与Alex一起获取婚姻许可证的人。
- **marriage licensure document**：描述颁发婚姻许可证的目标及所需步骤的文件。
- **action regulation 1**：要求州政府向同意的同性伴侣发放婚姻许可证的行动法规。
- **authority role 1**：由州政府承担的、由**action regulation 1**规定的权威角色。
- **i1**：州政府、Alex和Bailey参与**deontic declaration 1**并创建婚姻合同的时间间隔。
- **i2**：美国最高法院参与**deontic declaration 2**，要求州政府承认同性婚姻的时间间隔。
- **i3**：州政府依法撤销**deontic role 1**和**deontic role 3**的时间间隔。

### 关系描述

## Modeling Deontic Declarations and Their Relations in the Context of Marriage Licenses

### Classes, Particulars, and Relations Used to Formalize Case 6

The marriage license is an instance of the class **marriage license**, which is a subclass of **document** [29,30 31,32]. The **state government**, which issues the marriage license, is an instance of **government**, which is a type of organization able to exercise judicial, legislative, or executive authority over a site.

#### Ontological Relationships

1. **is a**(document, information content entity)
2. **is a**(marriage license, document)
3. **is a**(government, organization)
4. **instance of**(marriage license, marriage license, i)
5. **instance of**(state government, government, i)

#### Deontic Declaration and Its Components

The **state government** participates in **deontic declaration 1**, a type of social act [28,29,30], which has specified input a **marriage licensure document** that has, as part, a **plan specification**. This plan specification describes the intended legal entities created according to the objective specification, as well as the manner in which the deontic declaration should be performed to achieve that objective – as described by the **action specification**. For simplicity, we do not include these continuant parts of the marriage licensure document.

The **deontic declaration 1** has specified output the **marriage license**:

6. **is a**(deontic declaration, social act)
7. **instance of**(deontic declaration 1, deontic declaration, i1)
8. **participates in**(state government, deontic declaration 1, i1)
9. **has specified input**(deontic declaration 1, marriage licensure document)
10. **has specified output**(deontic declaration 1, marriage license)

### Additional Relations

- **participates in** holds between agents and instances of deontic declaration
- **has specified input** holds between deontic declaration 1 and marriage licensure document
- **has specified output** holds between instances of deontic declaration and document, and action regulation 1
- **inheres in** holds between instances of deontic role and Alex and Bailey, respectively
- **prescribes** holds between action regulation 1 and authority role 1
- **legally revokes** holds between deontic declaration 3 and deontic role 1 and deontic role 3

This section demonstrates how the **Basic Formal Ontology (BFO)** framework can be used to model the relationships and changes in goal-directed activities, particularly focusing on the **information content entities** and their roles in legal and social acts such as marriage licenses.

## 使用本体论模型表示和追踪实体、计划、动作和目标之间的关系及其演变

### 通过具体实例展示本体论模型的应用

该文本通过具体的实例展示了如何使用**本体论模型**，特别是在**Basic Formal Ontology (BFO)**框架下，建模目标导向活动中的变化以及婚姻制度中信息内容实体和法律角色的演变。

### 婚姻许可证的本体论关系

该文本使用**Basic Formal Ontology (BFO)**框架，通过类、实例和关系的形式化定义，详细描述了婚姻许可证的本体论关系及其作为政府发布的文件在法律和社会行为（如义务声明）中的角色。

### Alex 和 Bailey 的德性声明实例

Alex 和 Bailey 各自参与了德性声明1。德性声明实例涉及创建或撤销德性角色。德性角色存在于个人或组织中，但其基础在于他人对持有者行为的规范期望。在此案例中，德性角色分别存在于 Alex 和 Bailey 中。这些角色通常通过与婚姻相关的流程实现，例如联合报税和为配偶做出医疗决策。为了简化，我们仅关注 Alex 和 Bailey 的两个德性角色：

```markdown
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
```

### 美国最高法院的德性声明2

在某个时间点，随着德性声明1导致州政府为 Alex 和 Bailey 发放结婚证后，美国最高法院参与了德性声明2，结果是所有州对同性婚姻的禁令被裁定为违宪。德性声明2指定了输出行动法规1，允许授权同性婚姻。这一规定扩大了有资格参与结婚行为的代理人类别，从而批准了新的州和地方代理实例的权威角色。

```markdown
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
```

### 德性角色的扩展与保持

州政府对权威角色的新授权并不影响 Alex 和 Bailey 持有的结婚证。这是因为德性声明1针对的是婚姻资格限制，并未改变 Alex 和 Bailey 承担的德性角色。

### 改变婚姻合同的其他方式

政府还可以通过改变配偶义务和权力来修改婚姻合同。例如，假设州政府参与了德性声明3，合法撤销了存在于 Alex 的德性角色1和存在于 Bailey 的德性角色2，这假设对应于持有人不作证反对其配偶的特权。结果是 Alex 和 Bailey 失去了这些角色，但他们仍然保留了德性角色2和德性角色4。

```markdown
34. participates in(state government, deontic declaration 3, i3)
35. legally revokes(deontic declaration 3, deontic role 1, i3)
36. legally revokes(deontic declaration 3, deontic role 3, i3)
37. ∃t occurrent part of(t, i3) ∧ exists at(deontic role 1, t) ∧ exists at(deontic role 3, t)
```

### 结婚证变更的两种类型

至少有两种类型的婚姻许可证变更可以通过 BFO 表示：反映资格要求的变化——这可能会缩小或扩大参与者——或关联角色的变化——这可能会缩小或扩展配偶的权利和义务。在每种情况下，婚姻的意义在某种程度上仍然保持不变。

## 本体论的使用及其对社区的影响

### BFO 的单一现实承诺

BFO 致力于存在单一现实，科学调查往往会导致我们对这一现实的理解更加清晰。随着科学的更新，本体论也应随之更新。其他关于世界现状或可能状态的概念只是信息实体，不会进一步产生本体论承诺。

### BFO 在各学科中的广泛应用

作为 OBO 和 IOF [1,2] 的核心架构，BFO 广泛应用于多个科学领域。例如，在生物医学领域 [33]，BFO 被广泛用于建模表型 [34]、疾病 [35,36,37]、诊断 [38,39] 和抗性 [40]。目前，BFO 已应用于超过 350 个本体产品，并且随着其最近的标准化，这一数字在未来几年内无疑会增加。

### 致谢

感谢 Barry Smith 对本文初稿的评论。J. Neil Otte 和 Alan Ruttenberg 感谢 The Digital Manufacturing and Design Innovation Institute (DMDII) 提供的研究资金支持这项工作。