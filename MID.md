# Category Theory

_First published Fri Dec 6, 1996; substantive revision Thu Aug 29, 2019_

Category theory has come to occupy a central position in contemporary mathematics and theoretical computer science, and is also applied to mathematical physics. Roughly, it is a general mathematical theory of structures and of systems of structures. As category theory is still evolving, its functions are correspondingly developing, expanding and multiplying. At minimum, it is a powerful language, or conceptual framework, allowing us to see the universal components of a family of structures of a given kind, and how structures of different kinds are interrelated. Category theory is both an interesting object of philosophical study, and a potentially powerful formal tool for philosophical investigations of concepts such as space, system, and even truth. It can be applied to the study of logical systems in which case category theory is called “categorical doctrines” at the syntactic, proof-theoretic, and semantic levels. Category theory even leads to a different theoretical conception of set and, as such, to a possible alternative to the standard set theoretical foundation for mathematics. As such, it raises many issues about mathematical ontology and epistemology. Category theory thus affords philosophers and logicians much to use and reflect upon.

- [1. General Definitions, Examples and Applications](#GeneDefiExamAppl)
    - [1.1 Definitions](#Defi)
    - [1.2 Examples](#Exam)
    - [1.3 Fundamental Concepts of the Theory](#FundConcTheo)
- [2. Brief Historical Sketch](#BrieHistSket)
- [3. Philosophical Significance](#PhilSign)
- [Bibliography](#Bib)
- [Academic Tools](#Aca)
- [Other Internet Resources](#Oth)
- [Related Entries](#Rel)

---

## 1. General Definitions, Examples and Applications

### 1.1 Definitions

Categories are algebraic structures with many complementary natures, e.g., geometric, logical, computational, combinatorial, just as **groups** are many-faceted algebraic structures. Eilenberg & Mac Lane (1945) introduced categories in a purely auxiliary fashion, as preparation for what they called **functors** and **natural transformations**. The very definition of a category evolved over time, according to the author’s chosen goals and metamathematical framework. Eilenberg & Mac Lane at first gave a purely abstract definition of a category, along the lines of the axiomatic definition of a group. Others, starting with Grothendieck (1957) and Freyd (1964), elected for reasons of practicality to define categories in set-theoretic terms. An alternative approach, that of Lawvere (1963, 1966), begins by characterizing the **category of categories**, and then stipulates that a category is an object of that universe. This approach, under active development by various mathematicians, logicians, and mathematical physicists, lead to what are now called “higher-dimensional categories” (Baez 1997, Baez & Dolan 1998a, Batanin 1998, Leinster 2002, Hermida _et al_. 2000, 2001, 2002). The very definition of a category is not without philosophical importance, since one of the objections to category theory as a foundational framework is the claim that since categories are _defined_ as sets, category theory cannot provide a philosophically enlightening foundation for mathematics. We will briefly go over some of these definitions, starting with Eilenberg’s & Mac Lane’s (1945) algebraic definition. However, before going any further, the following definition will be required.

**Definition**: A mapping \( e \) will be called an **identity** if and only if the existence of any product \( e \alpha \) or \( \beta e \) implies that \( e \alpha = \alpha \) and \( \beta e = \beta \).

Here is the original definition of a category.

**Definition** (Eilenberg & Mac Lane 1945): A **category** \( \mathbf{C} \) is an aggregate \( \mathbf{Ob} \) of abstract elements, called the **objects** of \( \mathbf{C} \), and abstract elements \( \mathbf{Map} \), called **mappings** of the category. The mappings are subject to the following five axioms:

1. **(C1)** Given three mappings \( \alpha_1, \alpha_2 \) and \( \alpha_3 \), the triple product \( \alpha_3 (\alpha_2 \alpha_1) \) is defined if and only if \( (\alpha_3 \alpha_2) \alpha_1 \) is defined. When either is defined, the associative law
   \[
   \alpha_3 (\alpha_2 \alpha_1) = (\alpha_3 \alpha_2) \alpha_1
   \]
   holds. This triple product is written \( \alpha_3 \alpha_2 \alpha_1 \).

2. **(C2)** The triple product \( \alpha_3 \alpha_2 \alpha_1 \) is defined whenever both products \( \alpha_3 \alpha_2 \) and \( \alpha_2 \alpha_1 \) are defined.

3. **(C3)** For each mapping \( \alpha \), there is at least one identity \( e_1 \) such that \( \alpha e_1 \) is defined, and at least one identity \( e_2 \) such that \( e_2 \alpha \) is defined.

4. **(C4)** The mapping \( e_X \) corresponding to each object \( X \) is an identity.

## (C3) and (C4) Conditions

### (C3) Mapping Definitions

For each mapping **α**, there is at least one identity **e₁** such that **αe₁** is defined, and at least one identity **e₂** such that **e₂α** is defined.

### (C4) Identity Mappings

The mapping **eₓ** corresponding to each object **X** is an identity.

### (C5) Uniqueness of Objects for Identities

For each identity **e**, there is a unique object **X** of **C** such that **eₓ = e**.

As Eilenberg & Mac Lane promptly remark, objects play a secondary role and could be entirely omitted from the definition. Doing so, however, would make the manipulation of the applications less convenient. It is practically suitable, and perhaps psychologically more simple to think in terms of mappings and objects. The term “aggregate” is used by Eilenberg & Mac Lane themselves, presumably so as to remain neutral with respect to the background set theory one wants to adopt.

Eilenberg & Mac Lane defined categories in 1945 for reasons of rigor. As they note:

> It should be observed first that the whole concept of a category is essentially an auxiliary one; our basic concepts are essentially those of a functor and of natural transformation (…). The idea of a category is required only by the precept that every function should have a definite class as domain and a definite class as range, for the categories are provided as the domains and ranges of functors. Thus one could drop the category concept altogether and adopt an even more intuitive standpoint, in which a functor such as “Hom” is not defined over the category of “all” groups, but for each particular pair of groups which may be given. The standpoint would suffice for applications, inasmuch as none of our developments will involve elaborate constructions on the categories themselves. (1945, chap. 1, par. 6, p. 247)

## Evolution of Category Theory

### Categories in Algebraic Topology and Homological Algebra

Things changed in the following ten years, when categories started to be used in algebraic topology and homological algebra. Mac Lane, Buchsbaum, Grothendieck, and Heller were considering categories in which the collections of morphisms between two fixed objects have an additional structure. More specifically, given any two objects **X** and **Y** of a category **C**, the _set_ **Hom(X, Y)** of morphisms from **X** to **Y** form an abelian group. Furthermore, for reasons related to the ways homology and cohomology theories are linked, the definition of a category had to satisfy an additional formal property (which we will leave aside for the moment): it had to be self-dual.

### Definition of a Category

A category **C** can be described as a set **Ob**, whose members are the objects of **C**, satisfying the following three conditions:

#### Morphisms

For every pair **X, Y** of objects, there is a set **Hom(X, Y)**, called the _morphisms_ from **X** to **Y** in **C**. If **f** is a morphism from **X** to **Y**, we write **f: X → Y**.

#### Identity

For every object **X**, there exists a morphism **idₓ** in **Hom(X, X)**, called the _identity_ on **X**.

#### Composition

For every triple **X, Y, Z** of objects, there exists a partial binary operation from **Hom(X, Y) × Hom(Y, Z)** to **Hom(X, Z)**, called the composition of morphisms in **C**. If **f: X → Y** and **g: Y → Z**, the composition of **f** and **g** is notated **(g ∘ f): X → Z**.

Identity, morphisms, and composition satisfy two axioms:

#### Associativity

If **f: X → Y, g: Y → Z, h: Z → W**, then **h ∘ (g ∘ f) = (h ∘ g) ∘ f**.

#### Identity

If **f: X → Y**, then **(idᵧ ∘ f) = f** and **(f ∘ idₓ) = f**.

This is the definition one finds in most textbooks of category theory. As such it explicitly relies on a set theoretical background and language.

### Alternative Frameworks

An alternative, suggested by Lawvere in the early sixties, is to develop an adequate language and background framework for a category of categories. We will not present the formal framework here, for it would take us too far from our main concern, but the basic idea is to define what are called weak **n**-categories (and weak **ω**-categories), and what had been called categories would then be called weak **1-categories** (and sets would be weak **0-categories**).

Also in the sixties, Lambek proposed to look at categories as deductive systems.

## Weak n-Categories and Deductive Systems

We will not present the formal framework here, for it would take us too far from our main concern, but the basic idea is to define what are called **weak n-categories** (and weak ω-categories), and what had been called categories would then be called **weak 1-categories** (and sets would be **weak 0-categories**). (See, for instance, Baez 1997, Makkai 1998, Leinster 2004, Baez & May 2010, Simpson 2011.)

### Deductive Systems in Category Theory

Also in the sixties, Lambek proposed to look at categories as deductive systems. This begins with the notion of a **graph**, consisting of two classes **Arrows** and **Objects**, and two mappings between them, s: Arrows → Objects and t: Arrows → Objects, namely the source and the target mappings. The arrows are usually called the “oriented edges” and the objects “nodes” or “vertices”. Following this, a **deductive system** is a graph with a specified arrow:

- (R1) id_X : X → X,

and a binary operation on arrows:

- (R2) Given f: X → Y and g: Y → Z, the composition of f and g is (g ∘ f): X → Z.

Of course, the objects of a deductive system are normally thought of as **formulas**, the arrows are thought of as **proofs** or **deductions**, and operations on arrows are thought of as **rules of inference**. A **category** is then defined thus:

### Definition (Lambek)

A **category** is a deductive system in which the following equations hold between proofs: for all f: X → Y, g: Y → Z and h: Z → W,

- (E1) f ∘ id_X = f,   id_Y ∘ f = f,   h ∘ (g ∘ f) = (h ∘ g) ∘ f.

Thus, by imposing an adequate equivalence relation upon proofs, any deductive system can be turned into a category. It is therefore legitimate to think of a category as an algebraic encoding of a deductive system. This phenomenon is already well-known to logicians, but probably not to its fullest extent. An example of such an algebraic encoding is the **Lindenbaum-Tarski algebra**, a Boolean algebra corresponding to classical propositional logic. Since a Boolean algebra is a poset, it is also a category. (Notice also that Boolean algebras with appropriate homomorphisms between them form another useful category in logic.) 

Thus far we have merely a change of vocabulary. Things become more interesting when first-order and higher-order logics are considered. The Lindenbaum-Tarski algebra for these systems, when properly carried out, yields categories, sometimes called “conceptual categories” or “syntactic categories” (Mac Lane & Moerdijk 1992, Makkai & Reyes 1977, Pitts 2000).

## Examples of Categories

Almost every known example of a mathematical structure with the appropriate structure-preserving map yields a category.

1. **The category Set**: with objects sets and morphisms the usual functions. There are variants here: one can consider partial functions instead, or injective functions or again surjective functions. In each case, the category thus constructed is different.
   
2. **The category Top**: with objects topological spaces and morphisms continuous functions. Again, one could restrict morphisms to open continuous functions and obtain a different category.
   
3. **The category hoTop**: with objects topological spaces and morphisms equivalence classes of homotopic functions. This category is not only important in mathematical practice, it is at the core of algebraic topology, but it is also a fundamental example of a category in which morphisms are **not** structure preserving functions.
   
4. **The category Vec**: with objects vector spaces and morphisms linear maps.
   
5. **The category Diff**: with objects differential manifolds and morphisms smooth maps.
   
6. **The categories Pord and PoSet**: with objects preorders and posets, respectively, and morphisms monotone functions.
   
7. **The categories Lat and Bool**: with objects lattices and Boolean algebras, respectively, and morphisms structure preserving homomorphisms, i.e., (⊤,⊥,∧,∨) homomorphisms.
   
8. **The category Heyt**: with objects Heyting algebras and (⊤,⊥,∧,∨,→) homomorphisms.
   
9. **The category Mon**: with objects monoids and morphisms monoid homomorphisms.
   
10. **The category AbGrp**: with objects abelian groups and morphisms group homomorphisms, i.e., (1,×,(−)^{-1}) homomorphisms.
   
11. **The category Grp**: with objects groups and morphisms group homomorphisms, i.e., (1,×,(−)^{-1}) homomorphisms.

```markdown
## 11. The Category **Grp**

The category **Grp** with objects **groups** and morphisms **group homomorphisms**, i.e., $(1, \times, (-)^{-1})$ homomorphisms.

## 12. The Category **Rings**

The category **Rings** with objects **rings** (with unit) and morphisms **ring homomorphisms**, i.e., $(0, 1, +, \times)$ homomorphisms.

## 13. The Category **Fields**

The category **Fields** with objects **fields** and morphisms **field homomorphisms**, i.e., $(0, 1, +, \times)$ homomorphisms.

## 14. Deductive Systems

Any deductive system $T$ with objects **formulae** and morphisms **proofs**. These examples nicely illustrate how category theory treats the notion of structure in a uniform manner. Note that a category is characterized by its **morphisms**, and not by its objects. Thus the category of topological spaces with open maps differs from the category of topological spaces with continuous maps — or, more to the point, the categorical properties of the latter differ from those of the former.

### Preordered Sets and Monoids

We should underline again the fact that not all categories are made of structured sets with structure-preserving maps. Thus any **preordered set** is a category. For given two elements $p, q$ of a preordered set, there is a morphism $f: p \rightarrow q$ if and only if $p \le q$. Hence a preordered set is a category in which there is at most one morphism between any two objects.

Any **monoid** (and thus any **group**) can be seen as a category: in this case, the category has only one object, and its morphisms are the elements of the monoid. Composition of morphisms corresponds to multiplication of monoid elements. That the monoid axioms correspond to the category axioms is easily verified. Hence the notion of category generalizes those of preorder and monoid.

### Groupoids

We should also point out that a **groupoid** has a very simple definition in a categorical context: it is a category in which every morphism is an isomorphism, that is for any morphism $f: X \rightarrow Y$, there is a morphism $g: Y \rightarrow X$ such that $f \circ g = \mathbf{id}_X$ and $g \circ f = \mathbf{id}_Y$.

### 1.3 Fundamental Concepts of the Theory

Category theory unifies mathematical structures in two different ways. First, as we have seen, almost every set theoretically defined mathematical structure with the appropriate notion of homomorphism yields a category. This is a unification provided _within_ a set theoretical environment. Second, and perhaps even more important, once a type of structure has been defined, it is imperative to determine how new structures can be constructed out of the given one. For instance, given two sets $A$ and $B$, set theory allows us to construct their Cartesian product $A \times B$. It is also imperative to determine how given structures can be decomposed into more elementary substructures. For example, given a finite Abelian group, how can it be decomposed into a product of certain of its subgroups?

In both cases, it is necessary to know how structures of a certain kind may combine. The nature of these combinations might appear to be considerably different when looked at from a purely set theoretical perspective. Category theory reveals that many of these constructions are in fact certain objects in a category having a “universal property”.

Indeed, from a categorical point of view, a **Cartesian product** in set theory, a **direct product of groups** (Abelian or otherwise), a **product of topological spaces**, and a **conjunction of propositions** in a deductive system are all instances of a categorical product characterized by a universal property.

Formally, a **product** of two objects $X$ and $Y$ in a category $\mathbf{C}$ is an object $Z$ of $\mathbf{C}$ together with two morphisms, called the projections, $p: Z \rightarrow X$ and $q: Z \rightarrow Y$ such that—and this is the universal property—for all objects $W$ with morphisms $f: W \rightarrow X$ and $g: W \rightarrow Y$, there is a unique morphism $h: W \rightarrow Z$ such that $p \circ h = f$ and $q \circ h = g$.

Note that we have defined a product for $X$ and $Y$ and not _the_ product for $X$ and $Y$. Indeed, products and other objects with a universal property are defined only up to a (unique) isomorphism. Thus in category theory, the nature of the elements constituting a certain construction is irrelevant. What matters is the way an object is related to the other objects of the category, that is, the morphisms going in and the morphisms going out, or, put differently, how certain structures can be mapped into a given object and how a given object can map its structure into other structures of the same kind. Category theory reveals how different kinds of structures are related to one another.
```

## What Matters in Category Theory

### Morphisms and Structures

What matters is the way an object is related to the other objects of the category, that is, the **morphisms** going in and the morphisms going out, or, put differently, how certain structures can be mapped into a given object and how a given object can map its structure into other structures of the same kind. 

### Connections Between Different Kinds of Structures

Category theory reveals how different kinds of structures are related to one another. For instance, in algebraic topology, **topological spaces** are related to **groups** (and modules, rings, etc.) in various ways (such as homology, cohomology, homotopy, K-theory). As noted above, groups with group homomorphisms constitute a category. Eilenberg & Mac Lane invented category theory precisely in order to clarify and compare these connections.

### Functors: Structure-Preserving Maps Between Categories

What matters are the **morphisms between categories**, given by **functors**. Informally, functors are structure-preserving maps between categories. Given two categories \(\mathbf{C}\) and \(\mathbf{D}\), a functor \(F\) from \(\mathbf{C}\) to \(\mathbf{D}\) sends objects of \(\mathbf{C}\) to objects of \(\mathbf{D}\), and morphisms of \(\mathbf{C}\) to morphisms of \(\mathbf{D}\), in such a way that composition of morphisms in \(\mathbf{C}\) is preserved, i.e., \(F(g \circ f) = F(g) \circ F(f)\), and identity morphisms are preserved, i.e., \(F(\mathbf{id}_X) = \mathbf{id}_{FX}\).

It immediately follows that a functor preserves commutativity of diagrams between categories. Homology, cohomology, homotopy, K-theory are all examples of functors. A more direct example is provided by the power set operation, which yields two functors on the category of sets, depending on how one defines its action on functions.

### Example: Power Set Functor

Thus given a set \(X\), \(\wp(X)\) is the usual set of subsets of \(X\), and given a function \(f: X \rightarrow Y\), \(\wp(f): \wp(X) \rightarrow \wp(Y)\) takes a subset \(A\) of \(X\) and maps it to \(B = f(A)\), the image of \(f\) restricted to \(A\) in \(X\). It is easily verified that this defines a functor from the category of sets into itself.

### Natural Transformations

In general, there are many functors between two given categories, and the question of how they are connected suggests itself. For instance, given a category \(\mathbf{C}\), there is always the **identity functor** from \(\mathbf{C}\) to \(\mathbf{C}\) which sends every object/morphism of \(\mathbf{C}\) to itself. In particular, there is the identity functor over the category of sets.

Now, the identity functor is related in a natural manner to the power set functor described above. Indeed, given a set \(X\) and its power set \(\wp(X)\), there is a function \(h_X\) which takes an element \(x\) of \(X\) and sends it to the singleton set \(\{x\}\), a subset of \(X\), i.e., an element of \(\wp(X)\). This function in fact belongs to a family of functions indexed by the objects of the category of sets \(\{\mathbf{h}_Y : Y \rightarrow \wp(X) | Y \text{ in } \mathbf{Ob(Set)}\}\).

Moreover, it satisfies the following commutativity condition: given any function \(f: X \rightarrow Y\), the identity functor yields the same function \(\mathbf{Id}(f): \mathbf{Id}(X) \rightarrow \mathbf{Id}(Y)\). The commutativity condition thus becomes: \(\mathbf{h}_Y \circ \mathbf{Id}(f) = \wp(f) \circ \mathbf{h}_X\). Thus the family of functions \(\mathbf{h}(-)\) relates the two functors in a natural manner. Such families of morphisms are called **natural transformations** between functors.

### Adjunctions: Conceptual Inverses

The above notions, while important, are not fundamental to category _theory_. The latter heading arguably includes the notions of **limit/colimit**; in turn, these are special cases of what is certainly the cornerstone of category theory, the concept of **adjoint functors**, first defined by Daniel Kan in 1956 and published in 1958.

Adjoint functors can be thought of as being conceptual inverses. This is probably best illustrated by an example. Let \(U: \mathbf{Grp} \rightarrow \mathbf{Set}\) be the forgetful functor, that is, the functor that sends to each group \(G\) its underlying set of elements \(U(G)\), and to a group homomorphism \(f: G \rightarrow H\) the underlying set function \(U(f): U(G) \rightarrow U(H)\). In other words, \(U\) forgets about the group structure and forgets the fact that morphisms are group homomorphisms. The categories \(\mathbf{Grp}\) and \(\mathbf{Set}\) are certainly not isomorphic, as categories, to one another.

## The Conceptual Inverse to Forgetting Group Structure

In other words, **UUU** forgets about the group structure and forgets the fact that morphisms are group homomorphisms. The categories **Grp** and **Set** are certainly not isomorphic, as categories, to one another. (A simple argument runs as follows: the category **Grp** has a zero object, whereas **Set** does not.) Thus, we certainly cannot find an inverse, in the usual algebraic sense, to the functor **U**.

### Free Groups as Conceptual Inverses

But there are many non-isomorphic ways to define a group structure on a given set **X**, and one might hope that among these constructions at least one is functorial and systematically related to the functor **U**. What is the conceptual inverse to the operation of forgetting all the group theoretical structure and obtaining a set? It is to construct a group from a set solely on the basis of the concept of group and nothing else, i.e., with no extraneous relation or data. Such a group is constructed “freely”; that is, with no restriction whatsoever except those imposed by the axioms of the theory. In other words, all that is remembered in the process of constructing a group from a given set is the fact that the resulting construction has to be a group. 

Such a construction exists; it is functorial and it yields what are called **free groups**. In other words, there is a functor **F: Set → Grp**, which to any set **X** assigns the free group **F(X)** on **X**, and to each function **f: X → Y**, the group homomorphism **F(f): F(X) → F(Y)**, defined in the obvious manner.

### Adjoint Functors

The situation can be described thusly: we have two conceptual contexts, a group theoretical context and a set theoretical context, and two functors moving systematically from one context to the other in opposite directions. One of these functors is elementary, namely the **forgetful functor U**. It is apparently trivial and uninformative. The other functor is mathematically significant and important. The surprising fact is that **F** is related to **U** by a simple rule and, in some sense, it arises from **U**. One of the striking features of adjoint situations is precisely the fact that fundamental mathematical and logical constructions arise out of given and often elementary functors.

### Formal Relationship Between U and F

The fact that **U** and **F** are conceptual inverses expresses itself formally as follows: applying **F** first and then **U** does not yield the original set **X**, but there is a fundamental relationship between **X** and **UF(X)**. Indeed, there is a function **η: X → UF(X)**, called the _unit of the adjunction_, that simply sends each element of **X** to itself in **UF(X)** and this function satisfies the following universal property: given any function **g: X → U(G)**, there is a unique _group homomorphism_ **h: F(X) → G** such that **U(h) ∘ η = g**. In other words, **UF(X)** is the best possible solution to the problem of inserting elements of **X** into a group (what is called “insertion of generators” in the mathematical jargon).

Composing **U** and **F** in the opposite order, we get a morphism **ξ: FU(G) → G**, called the _counit of the adjunction_, satisfying the following universal property: for any group homomorphism **g: F(X) → G**, there is a unique function **h: X → U(G)** such that **ξ ∘ F(h) = g**. In other words, **FU(G)** constitutes the best possible solution to the problem of finding a representation of **G** as a quotient of a free group.

### Identity Properties

If **U** and **F** were simple algebraic inverses to one another, we would have the following identity: **UF = I_Set** and **FU = I_Grp**, where **I_Set** denotes the identity functor on **Set** and **I_Grp** the identity functor on **Grp**. As we have indicated, these identities certainly do not hold in this case. However, some identities do hold: they are best expressed with the help of the commutative diagrams:

\[
\begin{array}{rcl}
U & \xrightarrow{\eta \circ U} & UFU \\
 & \searrow & \downarrow \scriptsize{U \circ \xi} \\
 & & U
\end{array}
\]

\[
\begin{array}{rcl}
F & \xrightarrow{F \circ \eta} & FUF \\
 & \searrow & \downarrow \scriptsize{\xi \circ F} \\
 & & F
\end{array}
\]

where the diagonal arrows denote the appropriate identity natural transformations.

## Adjoints and Commutative Diagrams

As we have indicated, these identities certainly do not hold in this case. However, some identities do hold: they are best expressed with the help of the **commutative diagrams**:

|     |     |     |
| --- | --- | --- |
| $U \xrightarrow{\eta \circ U} UFU$ | $\searrow$ | $\downarrow U \circ \xi$ |
|     |     | $U$ |

|     |     |     |
| --- | --- | --- |
| $F \xrightarrow{F \circ \eta} FUF$ | $\searrow$ | $\downarrow \xi \circ F$ |
|     |     | $F$ |

where the diagonal arrows denote the appropriate identity natural transformations.

This is but one case of a very common situation: every **free construction** can be described as arising from an appropriate forgetful functor between two adequately chosen categories. The number of mathematical constructions that can be described as adjoints is simply stunning. Although the details of each one of these constructions vary considerably, the fact that they can all be described using the same language illustrates the profound unity of mathematical concepts and mathematical thinking.

### Definition of Adjoint Functors

Before we give more examples, a formal and abstract definition of **adjoint functors** is in order.

**Definition**: Let $F: \mathbf{C} \rightarrow \mathbf{D}$ and $G: \mathbf{D} \rightarrow \mathbf{C}$ be functors going in opposite directions. $F$ is a _left adjoint_ to $G$ ($G$ a _right adjoint_ to $F$), denoted by $F \dashv G$, if there exists natural transformations $\eta: I_{\mathbf{C}} \rightarrow GF$ and $\xi: FG \rightarrow I_{\mathbf{D}}$, such that the composites

\[ G \xrightarrow{\eta \circ G} GFG \xrightarrow{G \circ \xi} G \]

and

\[ F \xrightarrow{F \circ \eta} FGF \xrightarrow{\xi \circ F} F \]

are the identity natural transformations. (For different but equivalent definitions, see Mac Lane 1971 or 1998, chap. IV.)

### Important Facts Regarding Adjoint Functors

Here are some of the important facts regarding adjoint functors:

1. **Adjoints are unique up to isomorphism**: That is, any two left adjoints $F$ and $F'$ of a functor $G$ are naturally isomorphic.
2. **Equivalence to Universal Morphisms and Representable Functors**: The notion of adjointness is formally equivalent to the notion of a universal morphism (or construction) and to that of representable functor. Each and every one of these notions exhibit an aspect of a given situation.
3. **Preservation of Limits and Colimits**: A left adjoint preserves all the colimits which exist in its domain, and, dually, a right adjoint preserves all the limits which exist in its domain.

### Examples of Adjoint Situations

We now give some examples of adjoint situations to illustrate the pervasiveness of the notion.

#### Example 1: Partially Forgetting Structure

Instead of having a forgetful functor going into the category of sets, in some cases only a part of the structure is forgotten. Here are two standard examples:

* **Abelian Groups and Abelian Monoids**: There is an obvious forgetful functor $U: \mathbf{AbGrp} \rightarrow \mathbf{AbMon}$ from the category of abelian groups to the category of abelian monoids: $U$ forgets about the inverse operation. The functor $U$ has a left adjoint $F: \mathbf{AbMon} \rightarrow \mathbf{AbGrp}$ which, given an abelian monoid $M$, assigns to it the best possible abelian group $F(M)$ such that $M$ can be embedded in $F(M)$ as a submonoid. For instance, if $M = \mathbb{N}$, then $F(\mathbb{N})$ “is” $\mathbb{Z}$, that is, it is isomorphic to $\mathbb{Z}$.

* **Hausdorff Topological Spaces and Topological Spaces**: Similarly, there is an obvious forgetful functor $U: \mathbf{Haus} \rightarrow \mathbf{Top}$ from the category of Hausdorff topological spaces to the category of topological spaces which forgets the Hausdorff condition. Again, there is a functor $F: \mathbf{Top} \rightarrow \mathbf{Haus}$ such that $F \dashv U$. Given a topological space $X$, $F(X)$ yields the best Hausdorff space constructed from $X$: it is the quotient of $X$ by the closure of the diagonal $\overline{\Delta}_X \subseteq X \times X$, which is an equivalence relation. In contrast with the previous example where we had an embedding, this time we get a quotient of the original structure.

#### Example 2: Compact Hausdorff Spaces

Consider now the category of **compact** Hausdorff spaces $\mathbf{kHaus}$ and the forgetful functor $U: \mathbf{kHaus} \rightarrow \mathbf{Top}$, which forgets the compactness property and the separation property. The left adjoint to this $U$ is the Stone-Cech compactification.

#### Example 3: Modules and Abelian Groups

There is a forgetful functor $U: \textbf{Mod}_R \rightarrow \mathbf{AbGrp}$ from a category of $R$-modules to the category of abelian groups, where $R$ is a commutative ring with unit. The functor $U$ forgets the action of $R$ on a group $G$. The functor $U$ has both a left and a right adjoint.

```markdown
## The Functor UUU

The functor **UUU** forgets the action of **RRR** on a group **G.G.G.** The functor **UUU** has both a left and a right adjoint. 

### Left Adjoint
The left adjoint is **R⊗−R \\otimes -: AbGrp → ModR**, which sends an abelian group **GGG** to the tensor product **R⊗GR \\otimes G**.

### Right Adjoint
The right adjoint is given by the functor **Hom(R,−): AbGrp → ModR**, which assigns to any group **GGG** the modules of linear mappings **Hom(R,G)**.

## Special Case: Posets as Categories

The case where the categories **C** and **D** are posets deserves special attention here. Adjoint functors in this context are usually called _Galois connections_.

### Diagonal Functor
Let **C** be a poset. Consider the diagonal functor **Δ : C → C × C**, with **Δ(X) = ⟨X, X⟩** and for **f: X → Y**, **Δ(f) = ⟨f, f⟩ : ⟨X, X⟩ → ⟨Y, Y⟩**.

In this case:
- The left-adjoint to **Δ** is the coproduct, or the sup.
- The right-adjoint to **Δ** is the product, or the inf.

The adjoint situation can be described in the following special form:

\[
\frac{X \vee Y \le Z}{X \le Z, Y \le Z}\Updownarrow \qquad \frac{Z \le X \wedge Y}{Z \le Y, Z \le X}\Updownarrow
\]

where the vertical double arrow can be interpreted as rules of inference going in both directions.

## Implication

Consider a functor with a parameter: **(- ∧ X): C → C**. It can easily be verified that when **C** is a poset, the function **(- ∧ X)** is order preserving and therefore a functor. A right adjoint to **(- ∧ X)** is a functor that yields the largest element of **C** such that its infimum with **X** is smaller than **Z**. This element is sometimes called the relative pseudocomplement of **X** or, more commonly, the _implication_. It is denoted by **X ⇒ Z** or by **X ⊃ Z**. The adjunction can be presented as follows:

\[
\frac{Y \wedge X \le Z}{Y \le X \Rightarrow Z}\Updownarrow
\]

## Negation

The negation operator **¬X** can be introduced from the last adjunction. Indeed, let **Z** be the bottom element **⊥** of the lattice. Then, since **Y ∧ X ≤ ⊥** is always true, it follows that **Y ≤ X ⇒ ⊥** is also always true. But since **X ⇒ ⊥ ≤ X** is always the case, we get at the numerator that **(X ⇒ ⊥ ∧ X) = ⊥**. Hence, **X ⇒ ⊥** is the largest element disjoint from **X**. We can therefore put **¬X =_{def} X ⇒ ⊥**.

## Limits and Colimits

Limits, colimits, and all the fundamental constructions of category theory can be described as adjoints. Thus, products and coproducts are adjoints, as are equalizers, coequalizers, pullbacks and pushouts, etc. This is one of the reasons adjointness is central to category theory itself: because all the fundamental operations of category theory arise from adjoint situations.

## Equivalence of Categories

An _equivalence of categories_ is a special case of adjointness. Indeed, if in the above triangular identities the arrows **η : I_C → GF** and **ξ : FG → I_D** are natural _isomorphisms_, then the functors **F** and **G** constitute an _equivalence_ of categories. In practice, it is the notion of equivalence of categories that matters and not the notion of isomorphism of categories.

### Example: Implication

Consider, for instance, implication. Let **Z = X**. Then we get at the numerator that **Y ∧ X ≤ X**, which is always true in a poset (as is easily verified). Hence, **Y ≤ X ⇒ X** is also true for all **Y** and this is only possible if **X ⇒ X = ⊤**, the top element of the lattice.

Not only can logical operations be described as adjoints, but they naturally arise as adjoints to basic operations. In fact, adjoints can be used to define various structures, distributive lattices, Heyting algebras, Boolean algebras, etc. (See Wood, 2004.) It should be clear from the simple foregoing example how the formalism of adjointness can be used to give syntactic presentations of various logical theories. Furthermore, and this is a key element, the standard universal and existential quantifiers can be shown to be arising as adjoints to the operation of substitution. Thus, quantifiers are on a par with the other logical operations, in sharp contrast with the other algebraic approaches to logic.
```

## 2. Brief Historical Sketch

It is difficult to do justice to the short but intricate history of the field. In particular, it is not possible to mention all those who have contributed to its rapid development. With this word of caution out of the way, we will look at some of the main historical threads.

### Categories and Functors: The Early Days

Categories, functors, natural transformations, limits, and colimits appeared almost out of nowhere in a paper by **Eilenberg & Mac Lane (1945)** entitled “General Theory of Natural Equivalences.” We say “almost,” because their earlier paper (1942) contains specific functors and natural transformations at work, limited to groups. A desire to clarify and abstract their 1942 results led Eilenberg & Mac Lane to devise category theory. The central notion at the time, as their title indicates, was that of **natural transformation**. In order to give a general definition of the latter, they defined **functor**, borrowing the term from Carnap, and in order to define functor, they borrowed the word ‘category’ from the philosophy of Aristotle, Kant, and C. S. Peirce, but redefining it mathematically.

### Initial Reception and Applications

After their 1945 paper, it was not clear that the concepts of category theory would amount to more than a convenient language; this indeed was the status quo for about fifteen years. Category theory was employed in this manner by **Eilenberg & Steenrod (1952)**, in an influential book on the foundations of algebraic topology, and by **Cartan & Eilenberg (1956)**, in a groundbreaking book on homological algebra. (Curiously, although Eilenberg & Steenrod defined categories, Cartan & Eilenberg simply assumed them!) These books allowed new generations of mathematicians to learn algebraic topology and homological algebra directly in the categorical language, and to master the method of diagrams. Indeed, without the method of diagram chasing, many results in these two books seem inconceivable, or at the very least would have required a considerably more intricate presentation.

### Grothendieck's Breakthrough

The situation changed radically with **Grothendieck’s (1957)** landmark paper entitled “Sur quelques points d’algèbre homologique,” in which the author employed categories intrinsically to define and construct more general theories which he then applied to specific fields, e.g., to **algebraic geometry**.

## Duality and Adjoint Functors

Furthermore, and this is a key element, the standard **universal and existential quantifiers** can be shown to be arising as adjoints to the operation of substitution. Thus, quantifiers are on a par with the other logical operations, in sharp contrast with the other algebraic approaches to logic. (See, for instance **Awodey 1996** or **Mac Lane & Moerdijk 1992**.) More generally, **Lawvere** showed how syntax and semantics are related by adjoint functors. (See **Lawvere 1969b**.)

### Dualities in Mathematics

Dualities play an important role in mathematics and they can be described with the help of equivalences between categories. In other words, many important mathematical theorems can be translated as statements about the existence of adjoint functors, sometimes satisfying additional properties. This is sometimes taken as expressing the _conceptual_ content of the theorem.

#### Pontryagin Duality

Consider the following fundamental case: let **C** be the category whose objects are the locally compact abelian groups and the morphisms are the continuous group homomorphisms. Then, the **Pontryagin duality theorem** amounts to the claim that the category **C** is equivalent to the category **C°**, that is, to the opposite category. Of course, the precise statement requires that we describe the functors **F: C → C°** and **G: C° → C** and prove that they constitute an equivalence of categories.

#### Stone Duality

Another well-known and important duality was discovered by **Stone** in the thirties and now bears his name. In one direction, an arbitrary Boolean algebra yields a topological space, and in the other direction, from a (compact Hausdorff and totally disconnected) topological space, one obtains a Boolean algebra. Moreover, this correspondence is functorial: any Boolean homomorphism is sent to a continuous map of topological spaces, and, conversely, any continuous map between the spaces is sent to a Boolean homomorphism. In other words, there is an equivalence of categories between the category of Boolean algebras and the dual of the category of Boolean spaces (also called **Stone spaces**). (See **Johnstone 1982** for an excellent introduction and more developments.)

### Categorical Study of Duality

The connection between a category of algebraic structures and the opposite of a category of topological structures established by **Stone’s theorem** constitutes but one example of a general phenomenon that did attract and still attracts a great deal of attention from category theorists. Categorical study of duality theorems is still a very active and significant field, and is largely inspired by Stone’s result. (For recent applications in logic, see, for instance **Makkai 1987**, **Taylor 2000, 2002a, 2002b**, **Caramello 2011**.)

## The Role of Diagram Chasing and Category Theory

Indeed, without the method of **diagram chasing**, many results in these two books seem inconceivable, or at the very least would have required a considerably more intricate presentation. 

### Grothendieck's Pioneering Work

The situation changed radically with Grothendieck’s (1957) landmark paper entitled “Sur quelques points d’algèbre homologique”, in which the author employed categories intrinsically to define and construct more general theories which he (Grothendieck 1957) then applied to specific fields, e.g., to algebraic geometry.

### Kan's Contribution on Adjoint Functors

Kan (1958) showed that **adjoint functors** subsume the important concepts of limits and colimits and could capture fundamental concepts in other areas (in his case, homotopy theory). At this point, category theory became more than a convenient language, by virtue of two developments:

#### 1. Abstract Definitions and Constructions in Category Theory

Employing the axiomatic method and the language of categories, Grothendieck (1957) defined in an abstract fashion types of categories, e.g., **additive** and **Abelian categories**, showed how to perform various constructions in these categories, and proved various results about them. 

- It should be pointed out that Mac Lane in his 1950 paper had made a previous attempt which introduced certain key ideas, for instance using arrows to define certain fundamental concepts.
- Buchsbaum had essentially introduced the notion of an abelian category independently under the name of “exact category” in 1955.

In a nutshell, Grothendieck showed how to develop part of homological algebra in an abstract setting of this sort. From then on, a specific category of structures, e.g., a category of sheaves over a topological space \( X \), could be seen as a token of an abstract category of a certain type, e.g., an Abelian category. One could therefore immediately see how the methods of, e.g., homological algebra could be applied to, for instance, algebraic geometry. Furthermore, it made sense to look for other types of abstract categories, ones that would encapsulate the fundamental and formal aspects of various mathematical fields in the same way that Abelian categories encapsulated fundamental aspects of homological algebra.

#### 2. The Central Role of Adjoint Functors

Thanks in large part to the efforts of Freyd and Lawvere, category theorists gradually came to see the pervasiveness of the concept of adjoint functors. Not only does the existence of adjoints to given functors permit definitions of abstract categories (and presumably those which are defined by such means have a privileged status) but as we mentioned earlier, many important theorems and even theories in various fields can be seen as equivalent to the existence of specific functors between particular categories. By the early 1970s, the concept of adjoint functors was seen as central to category theory.

### Autonomy and Growth of Category Theory

With these developments, category theory became an autonomous field of research, and pure category theory could be developed. And indeed, it did grow rapidly as a discipline, but also in its applications, mainly in its source contexts, namely algebraic topology and homological algebra, but also in algebraic geometry and, after the appearance of Lawvere’s Ph.D. thesis, in universal algebra.

#### Lawvere's Contributions

This thesis also constitutes a landmark in this history of the field, for in it Lawvere proposed the category of categories as a foundation for category theory, set theory and, thus, the whole of mathematics, as well as using categories for the study of the logical aspects of mathematics. Over the course of the 1960s, Lawvere outlined the basic framework for an entirely original approach to logic and the foundations of mathematics. He achieved the following:

- Axiomatized the category of sets (Lawvere 1964) and of categories (Lawvere 1966);
- Gave a categorical description of theories that was independent of syntactical choices and sketched how completeness theorems for logical systems could be obtained by categorical methods (Lawvere 1967);
- Characterized Cartesian closed categories and showed their connections to logical systems and various logical paradoxes (Lawvere 1969);
- Showed that the quantifiers and the comprehension schemes could be captured as adjoint functors to given elementary operations (Lawvere 1966, 1969, 1970, 1971);
- Argued that adjoint functors should generally play a major foundational role through the notion of “categorical doctrines” (Lawvere 1969).

Meanwhile, Lambek (1968, 1969, 1972) described categories in terms of deductive systems and employed categorical methods for proof-theoretical purposes.

### Emergence of Topos Theory

All this work culminated in another notion, thanks to Grothendieck and his school: that of a **topos**. Even though toposes appeared in the 1960s, in the context of algebraic geometry, again from the mind of Grothendieck, it was certainly Lawvere and Tierney’s (1972) elementary axiomatization of a topos which gave impetus to its attaining foundational status.

## The Development and Applications of Topos Theory

### Emergence of the Concept of a Topos

All this work culminated in another notion, thanks to **Grothendieck** and his school: that of a _topos_. Even though **toposes** appeared in the 1960s, in the context of algebraic geometry, again from the mind of Grothendieck, it was certainly **Lawvere** and **Tierney’s (1972)** elementary axiomatization of a topos which gave impetus to its attaining foundational status. Very roughly, an elementary topos is a category possessing a logical structure sufficiently rich to develop most of “ordinary mathematics”, that is, most of what is taught to mathematics undergraduates. As such, an elementary topos can be thought of as a categorical theory of sets. But it is also a generalized topological space, thus providing a direct connection between logic and geometry. (For more on the history of categorical logic, see Marquis & Reyes 2012, Bell 2005.)

### Applications and Extensions of Topos Theory

#### Developments in the 1970s

The 1970s saw the development and application of the topos concept in many different directions. The very first applications outside algebraic geometry were in set theory, where various independence results were recast in terms of topos (Tierney 1972, Bunge 1974, but also Blass & Scedrov 1989, Blass & Scedrov 1992, Freyd 1980, Mac Lane & Moerdijk 1992, Scedrov 1984).

Connections with intuitionistic and, more generally constructive mathematics were noted early on, and toposes are still used to investigate models of various aspects of intuitionism and constructivism (Lambek & Scott 1986, Mac Lane & Moerdijk 1992, Van der Hoeven & Moerdijk 1984a, 1984b, 1984c, Moerdijk 1984, Moerdijk 1995a, Moerdijk 1998, Moerdijk & Palmgren 1997, Moerdijk & Palmgren 2002, Palmgren 2012, Palmgren 2018). For more on the history of topos theory, see McLarty 1992 and Bell 2012.

#### Recent Developments

More recently, topos theory has been employed to investigate various forms of constructive mathematics or set theory (Joyal & Moerdijk 1995, Taylor 1996, Awodey 2008), recursiveness, and models of higher-order type theories generally. The introduction of the so-called “effective topos” and the search for axioms for synthetic domain theory are worth mentioning (Hyland 1982, Hyland 1988, 1991, Hyland et al. 1990, McLarty 1992, Jacobs 1999, Van Oosten 2008, Van Oosten 2002 and the references therein).

**Lawvere’s** early motivation was to provide a new foundation for differential geometry, a lively research area which is now called “synthetic differential geometry” (Lawvere 2000, 2002, Kock 2006, Bell 1988, 1995, 1998, 2001, Moerdijk & Reyes 1991). This is only the tip of the iceberg; toposes could prove to be for the 21st century what Lie groups were to the 20th century.

### Broader Applications of Category Theory

From the 1980s to the present, category theory has found new applications. In theoretical computer science, category theory is now firmly rooted, and contributes, among other things, to the development of new logical systems and to the semantics of programming. (Pitts 2000, Plotkin 2000, Scott 2000, and the references therein). Its applications to mathematics are becoming more diverse, even touching on theoretical physics, which employs higher-dimensional category theory — which is to category theory what higher-dimensional geometry is to plane geometry — to study the so-called “quantum groups” and quantum field theory (Majid 1995, Baez & Dolan 2001 and other publications by these authors).

## Philosophical Significance

Category theory challenges philosophers in two ways, which are not necessarily mutually exclusive. On the one hand, it is certainly the task of philosophy to clarify the general epistemological and ontological status of categories and categorical methods, both in the practice of mathematics and in the foundational landscape. On the other hand, philosophers and philosophical logicians can employ category theory and categorical logic to explore philosophical and logical problems. I now discuss these challenges, briefly, in turn.

### Category Theory as a Mathematical Tool

Category theory is now a common tool in the mathematician’s toolbox; that much is clear. It is also clear that category theory organizes and unifies much of mathematics. Contemporary mathematical fields would not be what they are without category theory, for instance **algebraic topology**, **homological algebra**, **homotopy theory** and **homotopical algebra**, **representation theory**, **arithmetic geometry** and **algebraic geometry**. (See for instance Mac Lane 1971, 1998 or Pedicchio & Tholen 2004.) No one will deny these simple facts.

### New Practices and Abstractions

Furthermore, vast portions of contemporary mathematics now rest on a different practice which rely, in large part, on the manipulation of new graphical notations, on the one hand, and on different levels of abstraction, on the other hand. It is not simply that category theory and the mathematical disciplines developed within that framework use commutative diagrams, although this in itself leads to some interesting philosophical explorations, as for instance in De Toffoli 2017, but category theorists have seen the need to develop systematic and formal graphical languages to express directly various forms of argumentations.

## Contemporary Mathematics and Graphical Notations

### Different Practices in Modern Mathematics

Furthermore, vast portions of contemporary mathematics now rest on a different practice which rely, in large part, on the manipulation of **new graphical notations**, on the one hand, and on different levels of abstraction, on the other hand. It is not simply that **category theory** and the mathematical disciplines developed within that framework use **commutative diagrams**, although this in itself leads to some interesting philosophical explorations, as for instance in De Toffoli 2017. But category theorists have seen the need to develop systematic and formal **graphical languages** to express directly various forms of argumentations. (See, for instance, Joyal & Street 1993; Joyal, Street & Verity 1996; Fong & Spivak 2019, Other Internet Resources.)

Whereas since Bourbaki, mathematics was done “up to isomorphism”, in some cases, it is now done “up to equivalence” or up to “bi-equivalence” or even up to “n-equivalence”. (For an attempt at clarifying what these levels of abstraction mean, see Marquis 2014, Marquis 2016.)

### Categorical vs Set-Theoretical Frameworks

Doing mathematics in a **categorical framework** is almost always radically different from doing it in a set-theoretical framework (the exception being working with the internal language of a Boolean topos; whenever the topos is not Boolean, then the main difference lies in the fact that the logic is _intuitionistic_). Hence, as is often the case when a different conceptual framework is adopted, many basic issues regarding the nature of the objects studied, the nature of the knowledge involved, and the nature of the methods used have to be reevaluated. We will take up these three aspects in turn.

#### Nature of Mathematical Objects in a Categorical Framework

Two facets of the nature of mathematical objects within a categorical framework have to be emphasized:

1. **Objects are always given in a category**: An object exists in and depends upon an ambient category. Furthermore, an object is characterized by the morphisms going in it and/or the morphisms coming out of it.
   
2. **Objects are always characterized up to isomorphism**: There is no such thing, for instance, as _the_ natural numbers. However, it can be argued that there is such a thing as _the concept_ of natural numbers. Indeed, the concept of natural numbers can be given unambiguously, via the Dedekind-Peano-Lawvere axioms, but what this concept refers to in specific cases depends on the context in which it is interpreted, e.g., the category of sets or a topos of sheaves over a topological space. Thus, it seems that sense does not determine reference in a categorical context.

It is hard to resist the temptation to think that **category theory embodies a form of structuralism**, that it describes mathematical objects as structures since the latter, presumably, are always characterized up to isomorphism. Thus, the key here has to do with the kind of criterion of identity at work within a categorical framework and how it resembles any criterion given for objects which are thought of as forms in general. One of the standard objections presented against this view is that if objects are thought of as structures and only as _abstract_ structures, meaning here that they are separated from any specific or concrete representation, then it is impossible to locate them within the mathematical universe. (See Hellman 2003 for a standard formulation of the objection, McLarty 1993, Awodey 2004, Landry & Marquis 2005, Shapiro 2005, Landry 2011, Linnebo & Pettigrew 2011, Hellman 2011, Shapiro 2011, McLarty 2011, Logan 2015 for relevant material on the issue.)

### Mathematical Objects as Types

A slightly different way to make sense of the situation is to think of mathematical objects as **types** for which there are tokens given in different contexts. This is strikingly different from the situation one finds in set theory, in which mathematical objects are defined uniquely and their reference is given directly. Although one can make room for types within set theory via equivalence classes or isomorphism types in general, the _basic_ criterion of identity within that framework is given by the axiom of extensionality and thus, ultimately, reference is made to specific sets.

Furthermore, it can be argued that the relation between a type and its token is _not_ represented adequately by the membership relation. A token does not belong to a type, it is not an element of a type, but rather it is an instance of it. In a categorical framework, one always refers to a _token_ of a type, and what the theory characterizes directly is the type, not the tokens. In this framework, one does not have to locate a type, but tokens of it are, at least in mathematics, epistemologically required.

## Categorical Framework and Epistemology

### Tokens and Types

In a **categorical framework**, one always refers to a *token* of a type, and what the theory characterizes directly is the **type**, not the tokens. In this framework, one does not have to locate a type, but tokens of it are, at least in mathematics, epistemologically required. This is simply the reflection of the interaction between the abstract and the concrete in the epistemological sense (and not the ontological sense of these latter expressions.) (See Ellerman 1988, Ellerman 2017, Marquis 2000, Marquis 2006, Marquis 2013.)

### Historical Context and Impact

The history of **category theory** offers a rich source of information to explore and take into account for an historically sensitive epistemology of mathematics. It is hard to imagine, for instance, how **algebraic geometry** and **algebraic topology** could have become what they are now without categorical tools. (See, for instance, Carter 2008, Corfield 2003, Krömer 2007, Marquis 2009, McLarty 1994, McLarty 2006.)

### Reconceptualizations and Interdisciplinary Connections

Category theory has led to reconceptualizations of various areas of mathematics based on purely abstract foundations. Moreover, when developed in a categorical framework, traditional boundaries between disciplines are shattered and reconfigured; to mention but one important example, **topos theory** provides a direct bridge between algebraic geometry and logic, to the point where certain results in algebraic geometry are directly translated into logic and vice versa. Certain concepts that were geometrical in origin are more clearly seen as logical (for example, the notion of coherent topos). **Algebraic topology** also lurks in the background. (See, for instance, Caramello 2018 for a systematic exploitation of the idea of toposes as bridges in mathematics.)

### Mathematical Practice and Foundations

On a different but important front, it can be argued that the distinction between mathematics and metamathematics cannot be articulated in the way it has been. All these issues have to be reconsidered and reevaluated. Moving closer to mathematical practice, category theory allowed for the development of methods that have changed and continue to change the face of mathematics. It could be argued that category theory represents the culmination of one of the deepest and most powerful tendencies in twentieth-century mathematical thought: the search for the most general and abstract ingredients in a given situation. 

Category theory is, in this sense, the legitimate heir of the **Dedekind-Hilbert-Noether-Bourbaki tradition**, with its emphasis on the axiomatic method and algebraic structures. (For a different reading, see Rodin 2014.) When used to characterize a specific mathematical domain, category theory reveals the frame upon which that area is built, the overall structure presiding over its stability, strength, and coherence.

### Philosophical Implications

The structure of this specific area, in a sense, might not need to rest on anything, that is, on some solid soil, for it might very well be just one part of a larger network that is without any **Archimedean point**, as if floating in space. To use a well-known metaphor: from a categorical point of view, Neurath’s ship has become a spaceship. Still, it remains to be seen whether category theory should be “on the same plane,” so to speak, as set theory, whether it should be taken as a serious alternative to set theory as a foundation for mathematics, or whether it is foundational in a different sense altogether. (That this very question applies even more forcefully to topos theory will not detain us.)

### Lawvere's Proposal and Higher-Dimensional Categories

Lawvere from early on promoted the idea that a **category of categories** could be used as a foundational framework. (See Lawvere 1964, 1966.) This proposal now rests in part on the development of higher-dimensional categories, also called **weak n-categories**. (See, for instance, Makkai 1998.)

### Topos Theory and Foundations

The advent of topos theory in the seventies brought new possibilities. Mac Lane has suggested that certain toposes be considered as a genuine foundation for mathematics. (See Mac Lane 1986.) Lambek proposed the so-called **free topos** as the best possible framework, in the sense that mathematicians with different philosophical outlooks might nonetheless agree to adopt it. (See Couture & Lambek 1991, 1992, Lambek 1994.) He has also argued that there is no topos that can thoroughly satisfy a classical mathematician. (See Lambek 2004.) (For more on the various foundational views among category theorists, see Landry & Marquis 2005.)

### Debates on Foundational Status

Arguments have been advanced for and against category theory as a foundational framework. (Blass 1984 surveys the relationships between category theory and set theory. Feferman 1977, Bell 1981, and Hellman 2003 argue against category theory. See Marquis 1995 for a quick overview and proposal and McLarty 2004 and Awodey 2004 for replies to Hellman 2003.) The debate has advanced slowly but surely.

## Debates and Foundations of Category Theory

### Arguments Against Category Theory

Feferman 1977, Bell 1981, and Hellman 2003 argue against **category theory**. See Marquis 1995 for a quick overview and proposal and McLarty 2004 and Awodey 2004 for replies to Hellman 2003. The debate has advanced slowly but surely. It has been recognized that it is possible to present a foundational framework in the language of category theory, be it in the form of the **Elementary Theory of the Category of Sets (ETCS)** or a **category of categories**, such as Makkai's **Structuralist foundations for abstract mathematics (SFAM)**. Thus, it seems that the community no longer questions the logical and conceptual autonomy of these approaches, to use the terminology introduced by Linnebo & Pettigrew 2011. The main issue seems to be whether one can provide a philosophically satisfying justification for one of those frameworks. (See Hellman 2013, Landry 2013, Marquis 2013b, McLarty 2018.)

### Foundations of Category Theory

This matter is further complicated by the fact that the foundations of **category theory** itself have yet to be clarified. For there may be many different ways to think of a universe of higher-dimensional categories as a foundation for mathematics. It is safe to say that we now have a good understanding of what are called **(∞,1)-categories** and important mathematical results have been obtained in that framework. (See, for instance, Cisinski 2019 for a presentation.) An adequate language for the universe of arbitrary higher-dimensional categories still has to be presented together with definite axioms for mathematics. (See Makkai 1998 for a short description of such a language. A different approach based on **homotopy theory** but with closed connections with higher-dimensional categories has been proposed by Voevodsky et al. and is being vigorously pursued. See the book _Homotopy Type Theory_, by Awodey et al. 2013.)

### Category Theory in Logic and Philosophy

It is an established fact that **category theory** is employed to study logic and philosophy. Indeed, **categorical logic**, the study of logic by categorical means, has been underway for about 40 years now and is still vigorous. Some of the philosophically relevant results obtained in categorical logic are:

#### Key Results in Categorical Logic

- **The hierarchy of categorical doctrines**: regular categories, coherent categories, Heyting categories, and Boolean categories; all these correspond to well-defined logical systems, together with deductive systems and completeness theorems; they suggest that logical notions, including quantifiers, arise naturally in a specific order and are not haphazardly organized (see Walsh 2017 for a philosophical justification of logical connectives using category theory and Halvorson & Tsementzis 2018 for a look from the point of view of scientific theories).
- **Joyal’s generalization of Kripke-Beth semantics for intuitionistic logic to sheaf semantics** (Lambek & Scott 1986, Mac Lane & Moerdijk 1992).
- **Coherent and geometric logic**, whose practical and conceptual significance has yet to be explored (Makkai & Reyes 1977, Mac Lane & Moerdiejk 1992, Johnstone 2002, Caramello 2011b, 2012a).
- **The notions of generic model and classifying topos of a theory** (Makkai & Reyes 1977, Boileau & Joyal 1981, Bell 1988, Mac Lane & Moerdijk 1992, Johnstone 2002, Caramello 2012b).
- **The notion of strong conceptual completeness and the associated theorems** (Makkai & Reyes 1977, Butz & Moerdijk 1999, Makkai 1981, Pitts 1989, Johnstone 2002).
- **Geometric proofs of the independence of the continuum hypothesis and other strong axioms of set theory** (Tierney 1972, Bunge 1974, Freyd 1980, 1987, Blass & Scedrov 1983, 1989, 1992, Mac Lane & Moerdijk 1992).
- **Models and development of constructive mathematics** (see bibliography below).
- **Synthetic differential geometry**, an alternative to standard and non-standard analysis (Kock 1981, Bell 1998, 2001, 2006).
- **The construction of the so-called effective topos**, in which every function on the natural numbers is recursive (McLarty 1992, Hyland 1982, 1991, Van Oosten 2002, Van Oosten 2008).
- **Categorical models of linear logic, modal logic, fuzzy sets, and general higher-order type theories** (Reyes 1991, Reyes & Zawadoski 1993, Reyes & Zolfaghari 1991, 1996, Makkai & Reyes 1995, Ghilardi & Zawadowski 2002, Rodabaugh & Klement 2003, Jacobs 1999, Taylor 1999, Johnstone 2002, Blute & Scott 2004, Awodey & Warren 2009, Awodey et al. 2013, Kishida 2018, Cockett & Seely 2018).
- **A graphical syntax called “sketches”** (Barr & Wells 1985, 1999, Makkai 1997a, 1997b, 1997c, Johnstone 2002).

#### Quantum Logic and Physics

- **Quantum logic, the foundations of quantum physics, and quantum field theory** (Brunetti et al. 2003, Abramsky & Duncan 2006, Heunen et al. 2009, Baez & Stay 2010, Baez & Lauda 2011, Coecke 2011, Isham 2011, Döring 2011, Eva 2017, Coecke & Kissinger 2018). 

Categorical tools in logic offer considerable flexibility, as is illustrated by the fact that almost all the surprising results of constructive and intuitionistic mathematics can be modeled in a proper categorical setting. At the same time, the standard set-theoretic notions, e.g.

## Categorical Tools in Logic

Categorical tools in logic offer considerable flexibility, as is illustrated by the fact that almost all the surprising results of **constructive** and **intuitionistic mathematics** can be modeled in a proper categorical setting. At the same time, the standard set-theoretic notions, e.g., **Tarski’s semantics**, have found natural generalizations in categories.

### Roots and Impact of Categorical Logic

Thus, **categorical logic** has roots in logic as it was developed in the twentieth century, while at the same time providing a powerful and novel framework with numerous links to other parts of mathematics. **Category theory** also bears on more general philosophical questions. From the foregoing discussion, it should be obvious that category theory and categorical logic ought to have an impact on almost all issues arising in **philosophy of logic**: from the nature of identity criteria to the question of alternative logics, category theory always sheds a new light on these topics.

#### Ontology and Formal Ontology

Similar remarks can be made when we turn to **ontology**, in particular **formal ontology**: the part/whole relation, boundaries of systems, ideas of space, etc. **Ellerman (1988)** has bravely attempted to show that category theory constitutes a theory of universals, one having properties radically different from **set theory**, which is also seen as a theory of universals.

#### Cognitive Science and Complex Systems

Moving from ontology to **cognitive science**, **MacNamara & Reyes (1994)** have tried to employ categorical logic to provide a different logic of reference. In particular, they have attempted to clarify the relationships between count nouns and mass terms. Other researchers are using category theory to study complex systems, cognitive neural networks, and analogies. (See, for instance, **Ehresmann 2018**, **Ehresmann & Vanbremeersch 1987, 2007**, **Healy 2000**, **Healy & Caudell 2006**, **Arzi-Gonczarowski 1999**, **Brown & Porter 2006**.)

#### Structuralism in Science

Finally, philosophers of science have turned to category theory to shed a new light on issues related to **structuralism in science**. (See, for instance, **Brading & Landry 2006**, **Bain 2013**, **Lam & Wüthrich 2015**, **Eva 2016**, **Lal & Teh 2017**, **Landry 2007, 2012, 2018**.)

### Philosophical Challenges

Category theory offers thus many philosophical challenges, challenges which will hopefully be taken up in years to come.