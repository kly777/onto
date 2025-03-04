# Type Theory

_First published Wed Feb 8, 2006; substantive revision Tue Sep 6, 2022_

The topic of type theory is fundamental both in logic and computer science. We limit ourselves here to sketch some aspects that are important in logic. For the importance of types in computer science, we refer the reader for instance to Reynolds 1983 and 1985.

-   [1\. Paradoxes and Russell’s Type Theories](#ParaRussTypeTheo)
-   [2\. Simple Type Theory and the λλ\\lambda\-Calculus](#SimpTypeTheoLCalc)
-   [3\. Ramified Hierarchy and Impredicative Principles](#RamiHierImprPrin)
-   [4\. Type Theory/Set Theory](#TypeTheoTheo)
-   [5\. Type Theory/Category Theory](#TypeTheoCatTheo)
-   [6\. Extensions of Type System, Polymorphism, Paradoxes](#ExteTypeSystPolyPara)
-   [7\. Univalent Foundations](#UnivFoun)
-   [Bibliography](#Bib)
-   [Academic Tools](#Aca)
-   [Other Internet Resources](#Oth)
-   [Related Entries](#Rel)

---

## 1\. Paradoxes and Russell’s Type Theories

The theory of types was introduced by Russell in order to cope with some contradictions he found in his account of set theory and was introduced in “Appendix B: The Doctrine of Types” of Russell 1903. This contradiction was obtained by analysing a theorem of Cantor that no mapping

F:X→Pow(X)F:X→Pow(X) F:X \\rightarrow \\Pow(X)

(where Pow(X)Pow(X)\\Pow(X) is the class of subclasses of a class X)X)X) can be surjective; that is, FFF cannot be such that every member bbb of Pow(X)Pow(X)\\Pow(X) is equal to F(a)F(a)F(a) for some element aaa of XXX. This can be phrased “intuitively” as the fact that there are more subsets of XXX than elements of XXX. The proof of this fact is so simple and basic that it is worthwhile giving it here. Consider the following subset of XXX:

A\={x∈X∣x∉F(x)}.A\={x∈X∣x∉F(x)}. A = \\{ x \\in X \\mid x \\not\\in F(x)\\}.

This subset cannot be in the range of FFF. For if A\=F(a)A\=F(a)A = F(a), for some aaa, then

a∈F(a) iff a∈A iff a∉F(a)a∈F(a) iff a∈A iff a∉F(a)\\begin{align} a \\in F(a) &\\text{ iff } a \\in A \\\\ &\\text{ iff } a \\not\\in F(a) \\end{align}

which is a contradiction.

Some remarks are in order. First, the proof does not use the law of excluded middle and is thus valid intuitionistically. Second, the method that is used, called _diagonalisation_ was already present in the work of du Bois-Reymond for building real functions growing faster than any function in a given sequence of functions.

Russell analysed what happens if we apply this theorem to the case where A is the class of all classes, admitting that there is such a class. He was then lead to consider the special class of classes that do not belong to themselves

(\*)R\={w∣w∉w}.(\*)R\={w∣w∉w}.\\tag{\*} R = \\{ w \\mid w \\not\\in w \\}.

We then have

R∈R iff R∉R.R∈R iff R∉R. R \\in R \\text{ iff } R \\not\\in R.

It seems indeed that Cantor was already aware of the fact that the class of all sets cannot be considered itself to be a set.

Russell communicated this problem to Frege, and his letter, together with Frege’s answer appear in van Heijenoort 1967. It is important to realise that the formulation (\*) does not apply as it is to Frege’s system. As Frege himself wrote in his reply to Russell, the expression “a predicate is predicated of itself” is not exact. Frege had a distinction between _predicates_ (concepts) and _objects_. A (first-order) predicate applies to an object but it cannot have a predicate as argument. The exact formulation of the paradox in Frege’s system uses the notion of the _extension_ of a predicate PPP, which we designate as εPεP\\varepsilon P. The extension of a predicate is itself an object. The important axiom V is:

(Axiom V)εP\=εQ≡∀x\[P(x)≡Q(x)\](Axiom V)εP\=εQ≡∀x\[P(x)≡Q(x)\]\\tag{Axiom V} \\varepsilon P = \\varepsilon Q \\equiv \\forall x \[P(x) \\equiv Q(x)\]

This axiom asserts that the extension of PPP is identical to the extension of QQQ if and only if PPP and QQQ are materially equivalent. We can then translate Russell’s paradox (\*) in Frege’s system by defining the predicate

R(x) iff ∃P\[x\=εP∧¬P(x)\]R(x) iff ∃P\[x\=εP∧¬P(x)\] R(x) \\text{ iff } \\exists P\[x = \\varepsilon P \\wedge \\neg P(x)\]

It can then been checked, using Axiom V in a crucial way, that

R(εR)≡¬R(εR)R(εR)≡¬R(εR) R(\\varepsilon R) \\equiv \\neg R(\\varepsilon R)

and we have a contradiction as well. (Notice that for defining the predicate RRR, we have used an _impredicative_ existential quantification on predicates. It can be shown that the _predicative_ version of Frege’s system is consistent (see Heck 1996 and for further refinements Ferreira 2002).

It is clear from this account that an idea of types was already present in Frege’s work: there we find a distinction between objects, predicates (or concepts), predicates of predicates, etc. (This point is stressed in Quine 1940.) This hierarchy is called the “extensional hierarchy” by Russell (1959), and its necessity was recognised by Russell as a consequence of his paradox.

## 2\. Simple Type Theory and the λλ\\lambda\-Calculus

As we saw above, the distinction: objects, predicates, predicate of predicates, etc., seems enough to block Russell’s paradox (and this was recognised by Chwistek and Ramsey). We first describe the type structure as it is in _Principia_ and later in this section we present the elegant formulation due to Church 1940 based on λλ\\lambda\-calculus. The types can be defined as

1.  iii is the type of individuals
2.  ()()(\\,) is the type of propositions
3.  if A1,…,AnA1,…,AnA_1 ,\\ldots ,A_n are types then (A1,…,An)(A1,…,An)(A_1 ,\\ldots ,A_n) is the type of nnn\-ary relations over objects of respective types A1,…,AnA1,…,AnA_1 ,\\ldots ,A_n

For instance, the type of binary relations over individuals is (i,i)(i,i)(i, i), the type of binary connectives is ((),())((),())((\\,),(\\,)), the type of quantifiers over individuals is ((i))((i))((i)).

For forming propositions we use this type structure: thus R(a1,…,an)R(a1,…,an)R(a_1 ,\\ldots ,a_n) is a proposition if RRR is of type (A1,…,An)(A1,…,An)(A_1 ,\\ldots ,A_n) and aiaia_i is of type AiAiA_i for i\=1,…,ni\=1,…,ni = 1,\\ldots ,n. This restriction makes it impossible to form a proposition of the form P(P)P(P)P(P): the type of PPP should be of the form (A)(A)(A), and PPP can only be applied to arguments of type AAA, and thus cannot be applied to itself since AAA is not the same as (A)(A)(A).

However simple type theory is not predicative: we can define an object Q(x,y)Q(x,y)Q(x, y) of type (i,i)(i,i)(i, i) by

∀P\[P(x)⊃P(y)\]∀P\[P(x)⊃P(y)\] \\forall P\[P(x) \\supset P(y)\]

Assume that we have two individuals aaa and bbb such that Q(a,b)Q(a,b)Q(a, b) holds. We can define P(x)P(x)P(x) to be Q(x,a)Q(x,a)Q(x, a). It is then clear that P(a)P(a)P(a) holds, since it is Q(a,a)Q(a,a)Q(a, a). Hence P(b)P(b)P(b) holds as well. We have proved, in an impredicative way, that Q(a,b)Q(a,b)Q(a, b) implies Q(b,a)Q(b,a)Q(b, a).

Alternative simpler formulations, which retain only the notion of classes, classes of classes, etc., were formulated by Gödel and Tarski. Actually this simpler version was used by Gödel in his 1931 paper on formally undecidable propositions. The discovery of the undecidable propositions may have been motivated by a heuristic argument that it is unlikely that one can extend the completeness theorem of first-order logic to type theory (see the end of his Lecture at Königsberg 1930 in Gödel Collected Work, Volume III, Awodey and Carus 2001 and Goldfarb 2005). Tarski had a version of the definability theorem expressed in type theory (see Hodges 2008). See Schiemer and Reck 2013.

We have objects of type 0, for individuals, objects of type 1, for classes of individuals, objects of type 2, for classes of classes of individuals, and so on. Functions of two or more arguments, like relations, need not be included among primitive objects since one can define relations to be classes of ordered pairs, and ordered pairs to be classes of classes. For example, the ordered pair of individuals _a, b_ can be defined to be {{a},{a,b}}{{a},{a,b}}\\{\\{a\\},\\{a,b\\}\\} where {x,y}{x,y}\\{x,y\\} denotes the class whose sole elements are xxx and yyy. (Wiener 1914 had suggested a similar reduction of relations to classes.) In this system, all propositions have the form a(b)a(b)a(b), where aaa is a sign of type n+1n+1n+1 and bbb a sign of type nnn. Thus this system is built on the concept of an arbitrary class or subset of objects of a given domain and on the fact that the collection of _all subsets_ of the given domain can form a new domain of the next type. Starting from a given domain of individuals, this process is then iterated. As emphasised for instance in Scott 1993, in set theory this process of forming subsets is iterated into the _transfinite_.

In these versions of type theory, as in set theory, functions are not primitive objects, but are represented as functional relation. The addition function for instance is represented as a ternary relation by an object of type (i,i,i)(i,i,i)(i,i,i). An elegant formulation of the simple type theory which extends it by introducing functions as primitive objects was given by Church in 1940. It uses the λλ\\lambda\-calculus notation (Barendregt 1997). Since such a formulation is important in computer science, for the connection with category theory, and for Martin-Löf type theory, we describe it in some detail. In this formulation, predicates are seen as a special kind of functions (propositional functions), an idea that goes back to Frege (see for instance Quine 1940). Furthermore, the notion of function is seen as more primitive than the notion of predicates and relations, and a function is not defined anymore as a special kind of relation. (Oppenheimer and Zalta 2011 presents some arguments against such a primitive representation of functions.) The types of this system are defined inductively as follows

1.  there are two basic types iii (the type of individuals) and ooo (the type of propositions)
2.  if A,BA,BA, B are types then A→BA→BA \\rightarrow B, the type of functions from AAA to BBB, is a type

We can form in this way the types:

|                                                |                                    |
| ---------------------------------------------- | ---------------------------------- |
| i→oi→oi\\rightarrow o                          | (type of predicates)               |
| (i→o)→o(i→o)→o(i\\rightarrow o) \\rightarrow o | (type of predicates of predicates) |

which correspond to the types (i)(i)(i) and ((i))((i))((i)) but also the new types

|                                                |                       |
| ---------------------------------------------- | --------------------- |
| i→ii→ii\\rightarrow i                          | (type of functions)   |
| (i→i)→i(i→i)→i(i\\rightarrow i) \\rightarrow i | (type of functionals) |

It is convenient to write

A1,…,An→BA1,…,An→B A_1 ,\\ldots ,A_n \\rightarrow B

for

A1→(A2→…→(An→B))A1→(A2→…→(An→B)) A_1 \\rightarrow(A_2 \\rightarrow \\ldots \\rightarrow(A_n \\rightarrow B))

In this way

A1,…,An→oA1,…,An→o A_1 ,\\ldots ,A_n \\rightarrow o

corresponds to the type (A1,…,An)(A1,…,An)(A_1 ,\\ldots ,A_n).

First-order logic considers only types of the form

|                                           |                                       |     |
| ----------------------------------------- | ------------------------------------- | --- |
| i,…,i→ii,…,i→ii,\\ldots ,i \\rightarrow i | (type of function symbols),           | and |
| i,…,i→oi,…,i→oi,\\ldots ,i \\rightarrow o | (type of predicate, relation symbols) |     |

Notice that

A→B→CA→B→C A \\rightarrow B \\rightarrow C

stands for

A→(B→C)A→(B→C) A \\rightarrow(B\\rightarrow C)

(association to the right).

For the terms of this logic, we shall not follow Church’s account but a slight variation of it, due to Curry (who had similar ideas before Church’s paper appeared) and which is presented in detail in R. Hindley’s book on type theory. Like Church, we use λλ\\lambda\-calculus, which provides a general notation for functions

M::\=x∣MM∣λx.MM::=x∣MM∣λx.M M ::= x \\mid M M \\mid \\lambda x.M

Here we have used the so-called BNF notation, very convenient in computing science. This gives a syntactic specification of the λλ\\lambda\-terms which, when expanded, means:

-   every variable is a function symbol;
-   every juxtaposition of two function symbols is a function symbol;
-   every λx.Mλx.M\\lambda x.M is a function symbol;
-   there are no other function symbols.

The notation for function application MNMNM N is a little different than the mathematical notation, which would be M(N)M(N)M(N). In general,

M1M2M3M1M2M3 M_1 M_2 M_3

stands for

(M1M2)M3(M1M2)M3 (M_1 M_2) M_3

(association to the left). The term λx.Mλx.M\\lambda x.M represents the function which to NNN associates M\[x:\=NM\[x:=NM\[x:=N\]. This notation is so convenient that one wonders why it is not widely used in mathematics. The main equation of λλ\\lambda\-calculus is then (β(β(\\beta\-conversion)

(λx.M)N\=M\[x:\=N\](λx.M)N\=M\[x:=N\] (\\lambda x.M) N = M\[x:=N\]

which expresses the meaning of λx.Mλx.M\\lambda x.M as a function. We have used M\[x:\=NM\[x:=NM\[x:=N\] as a notation for the value of the expression that results when NNN is substituted for the variable xxx in the matrix MMM. One usually sees this equation as a rewrite rule (β(β(\\beta\-reduction)

(λx.M)N→M\[x:\=N\](λx.M)N→M\[x:=N\] (\\lambda x.M) N \\rightarrow M\[x:=N\]

In _untyped_ lambda calculus, it may be that such rewriting does not terminate. The canonical example is given by the term Δ\=λx.xxΔ\=λx.xx\\Delta = \\lambda x.x x and the application

ΔΔ→ΔΔΔΔ→ΔΔ \\Delta \\Delta \\rightarrow \\Delta \\Delta

(Notice the similarity with Russell’s paradox.) The idea of Curry is then to look at types as predicates over lambda terms, writing M:AM:AM:A to express that MMM satisfies the predicate/type AAA. The meaning of

N:A→BN:A→B N:A\\rightarrow B

is then

∀M, if M:A then NM:B∀M, if M:A then NM:B \\forall M, \\text{ if } M:A \\text{ then } N M:B

which justifies the following rules

N:A→BM:ANM:BN:A→BM:ANM:B \\frac{N:A\\rightarrow B M:A}{N M:B} M:B\[x:A\]λx.M:A→BM:B\[x:A\]λx.M:A→B \\frac{M:B \[x:A\]}{\\lambda x.M:A \\rightarrow B}

In general one works with judgements of the form

x1:A1,...,xn:An⊢M:Ax1:A1,...,xn:An⊢M:A x_1 :A_1,...,x_n :A_n \\vdash M:A

where x1,...,xnx1,...,xnx_1,..., x_n are distinct variables, and MMM is a term having all free variables among x1,...,xnx1,...,xnx_1,..., x_n. In order to be able to get Church’s system, one adds some constants in order to form propositions. Typically

|         |                                                |
| ------- | ---------------------------------------------- |
| not:    | o→oo→oo\\rightarrow o                          |
| imply:  | o→o→oo→o→oo\\rightarrow o\\rightarrow o        |
| and:    | o→o→oo→o→oo\\rightarrow o\\rightarrow o        |
| forall: | (A→o)→o(A→o)→o(A\\rightarrow o) \\rightarrow o |

The term

λx.¬(xx)λx.¬(xx) \\lambda x. \\neg(x x)

represents the predicate of predicates that do not apply to themselves. This term does not have a type however, that is, it is not possible to find AAA such that

λx.¬(xx):(A→o)→oλx.¬(xx):(A→o)→o \\lambda x. \\neg(x x) : (A\\rightarrow o) \\rightarrow o

which is the formal expression of the fact that Russell’s paradox cannot be expressed. Leibniz equality

Q:i→i→oQ:i→i→o Q: i \\rightarrow i \\rightarrow o

will be defined as

Q\=λx.λy.∀(λP.imply(Px)(Py))Q\=λx.λy.∀(λP.imply(Px)(Py)) Q = \\lambda x . \\lambda y. \\forall(\\lambda P.\\imply(P x) (P y))

One usually writes ∀x\[M∀x\[M\\forall x\[M\] instead of ∀(λx.M)∀(λx.M)\\forall(\\lambda x.M), and the definition of QQQ can then be rewritten as

Q\=λx.λy.∀P\[imply(Px)(Py)\]Q\=λx.λy.∀P\[imply(Px)(Py)\] Q = \\lambda x.\\lambda y.\\forall P\[\\imply (P x) (P y)\]

This example again illustrates that we can formulate impredicative definitions in simple type theory.

The use of λλ\\lambda\-terms and ββ\\beta\-reduction is most convenient for representing the complex substitution rules that are needed in simple type theory. For instance, if we want to substitute the predicate λx.Qaxλx.Qax\\lambda x.Q a x for PPP in the proposition

imply(Pa)(Pb)imply(Pa)(Pb) \\imply (P a) (P b)

we get

imply((λx.Qax)a)((λx.Qax)b)imply((λx.Qax)a)((λx.Qax)b) \\imply ((\\lambda x.Q a x) a) ((\\lambda x.Q a x) b)

and, using ββ\\beta\-reduction,

imply(Qaa)(Qab)imply(Qaa)(Qab) \\imply (Q a a) (Q a b)

In summary, simple type theory forbids self-application but not the circularity present in impredicative definitions.

The λλ\\lambda\-calculus formalism also allows for a clearer analysis of Russell’s paradox. We can see it as the definition of the predicate

Rx\=¬(xx)Rx\=¬(xx) R x = \\neg(x x)

If we think of ββ\\beta\-reduction as the process of unfolding a definition, we see that there is a problem already with understanding the definition of R R

RR→¬(RR)→¬(¬(RR))→…RR→¬(RR)→¬(¬(RR))→… R R \\rightarrow \\neg(R R) \\rightarrow \\neg(\\neg(R R)) \\rightarrow \\ldots

In some sense, we have a non-wellfounded definition, which is as problematic as a contradiction (a proposition equivalent to its negation). One important theorem, the normalisation theorem, says that this cannot happen with simple types: if we have M:AM:AM:A then MMM is normalisable in a strong way (any sequence of reductions starting from MMM terminates).

For more information on this topic, we refer to the entry on Church’s simple type theory.

## 3\. Ramified Hierarchy and Impredicative Principles

Russell introduced another hierarchy, that was not motivated by any formal paradoxes expressed in a formal system, but rather by the fear of “circularity” and by informal paradoxes similar to the paradox of the liar. If a man says “I am lying”, then we have a situation reminiscent of Russell’s paradox: a proposition which is equivalent to its own negation. Another informal such paradoxical situation is obtained if we define an integer to be the “least integer not definable in less than 100 words”. In order to avoid such informal paradoxes, Russell thought it necessary to introduce another kind of hierarchy, the so-called “ramified hierarchy”. The need for such a hierarchy is hinted in Appendix B of Russell 1903. Interestingly this is connected there to the question of the identity of equivalent propositions and of the logical product of a class of propositions. A thorough discussion can be found in Chapter 10 of Russell 1959. Since this notion of ramified hierarchy has been extremely influential in logic and especially proof theory, we describe it in some details.

In order to further motivate this hierarchy, here is one example due to Russell. If we say

Napoleon was Corsican.

we do not refer in this sentence to any assemblage of properties. The property “to be Corsican” is said to be _predicative_. If we say on the other hand

Napoleon had all the qualities of a great general

we are referring to a totality of qualities. The property “to have all qualities of a great general” is said to be _impredicative_.

Another example, also coming from Russell, shows how impredicative properties can potentially lead to problems reminiscent of the liar paradox. Suppose that we suggest the definition

A typical Englishman is one who possesses all the properties possessed by a majority of Englishmen.

It is clear that most Englishmen do not possess _all_ the properties that most Englishmen possess. Therefore, a typical Englishman, according to this definition, should be untypical. The problem, according to Russell, is that the word “typical” has been defined by a reference to all properties and has been treated as itself a property. (It is remarkable that similar problems arise when defining the notion of _random_ numbers, cf. Martin-Löf “Notes on constructive mathematics” (1970).) Russell introduced the _ramified hierarchy_ in order to deal with the apparent circularity of such impredicative definitions. One should make a distinction between the _first-order_ properties, like being Corsican, that do not refer to the totality of properties, and consider that the _second-order_ properties refer only to the totality of _first-order properties_. One can then introduce third-order properties, that can refer to the totality of second-order property, and so on. This clearly eliminates all circularities connected to impredicative definitions.

At about the same time, Poincaré carried out a similar analysis. He stressed the importance of “predicative” classifications, and of not defining elements of a class using a quantification over this class (Poincaré 1909). Poincaré used the following example. Assume that we have a collection with elements 0, 1 and an operation + satisfying

x+0\=0x+(y+1)\=(x+y)+1x+0\=0x+(y+1)\=(x+y)+1\\begin{align} x+0 &= 0 \\\\ x+(y+1) &= (x+y)+1 \\end{align}

Let us say that a property is _inductive_ if it holds of 0 and holds for x+1x+1x+1 if it holds for xxx.

An impredicative, and potentially “dangerous”, definition would be to define an element to be a _number_ if it satisfies _all_ inductive properties. It is then easy to show that this property “to be a number” is itself inductive. Indeed, 0 is a number since it satisfies all inductive properties, and if xxx satisfies all inductive properties then so does x+1x+1x+1. Similarly it is easy to show that x+yx+yx+y is a number if x,yx,yx,y are numbers. Indeed the property Q(z)Q(z)Q(z) that x+zx+zx+z is a number is inductive: QQQ(0) holds since x+0\=xx+0\=xx+0=x and if x+zx+zx+z is a number then so is x+(z+1)\=(x+z)+1x+(z+1)\=(x+z)+1x+(z+1) = (x+z)+1. This whole argument however is circular since the property “to be a number” is not predicative and should be treated with suspicion.

Instead, one should introduce a ramified hierarchy of properties and numbers. At the beginning, one has only _first-order_ inductive properties, which do not refer in their definitions to a totality of properties, and one defines the numbers of order 1 to be the elements satisfying all first-order inductive properties. One can next consider the second-order inductive properties, that can refer to the collection of first-order properties, and the numbers of order 2, that are the elements satisfying the inductive properties of order 2. One can then similarly consider numbers of order 3, and so on. Poincaré emphasizes the fact that a number of order 2 is _a fortiori_ a number of order 1, and more generally, a number of order n+1n+1n+1 is _a fortiori_ a number of order nnn. We have thus a sequence of more and more restricted properties: inductive properties of order 1, 2, … and a sequence of more and more restricted collections of objects: numbers of order 1, 2, … Also, the property “to be a number of order nnn” is itself an inductive property of order n+1n+1n+1.

It does not seem possible to prove that x+yx+yx+y is a number of order nnn if x,yx,yx,y are numbers of order nnn. On the other hand, it is possible to show that if xxx is a number of order n+1n+1n+1, and yyy a number of order n+1n+1n+1 then x+yx+yx+y is a number of order nnn. Indeed, the property P(z)P(z)P(z) that “x+zx+zx+z is a number of order nnn” is an inductive property of order n+1:Pn+1:Pn+1: P(0) holds since x+0\=xx+0\=xx+0 = x is a number of order n+1n+1n+1, and hence of order nnn, and if P(z)P(z)P(z) holds, that is if x+zx+zx+z is a number of order nnn, then so is x+(z+1)\=(x+z)+1x+(z+1)\=(x+z)+1x+(z+1) = (x+z)+1, and so P(z+1)P(z+1)P(z+1) holds. Since yyy is a number of order n+1n+1n+1, and P(z)P(z)P(z) is an inductive property of order n+1,P(y)n+1,P(y)n+1, P(y) holds and so x+yx+yx+y is a number of order nnn. This example illustrates well the complexities introduced by the ramified hierarchy.

The complexities are further amplified if one, like Russell as for Frege, defines even basic objects like natural numbers as classes of classes. For instance the number 2 is defined as the class of all classes of individuals having exactly two elements. We again obtain natural numbers of different orders in the ramified hierarchy. Besides Russell himself, and despite all these complications, Chwistek tried to develop arithmetic in a ramified way, and the interest of such an analysis was stressed by Skolem. See Burgess and Hazen 1998 for a recent development.

Another mathematical example, often given, of an impredicative definition is the definition of least upper bound of a bounded class of real numbers. If we identify a real with the set of rationals that are less than this real, we see that this least upper bound can be defined as the union of all elements in this class. Let us identify subsets of the rationals as predicates. For example, for rational numbers q,P(q)q,P(q)q, P(q) holds iff qqq is a member of the subset identified as PPP. Now, we define the predicate LCLCL_C (a subset of the rationals) to be the least upper bound of class CCC as:

∀q\[LC(q)↔∃P\[C(P)∧P(q)\]\]∀q\[LC(q)↔∃P\[C(P)∧P(q)\]\] \\forall q\[L_C (q) \\leftrightarrow \\exists P\[C(P) \\wedge P(q)\]\]

which is impredicative: we have defined a predicate LLL by an existential quantification over all predicates. In the ramified hierarchy, if CCC is a class of first-order classes of rationals, then LLL will be a second-order class of rationals. One obtains then not _one_ notion or real numbers, but real numbers of different orders 1, 2, … The least upper bound of a collection of reals of order 1 will then be at least of order 2 in general.

As we saw earlier, yet another example of an impredicative definition is given by Leibniz’ definition of equality. For Leibniz, the predicate “is equal to aaa” is true for bbb iff bbb satisfies all the predicates satisfied by aaa.

How should one deal with the complications introduced by the ramified hierarchy? Russell showed, in the introduction to the second edition to [_Principia Mathematica_](../principia-mathematica/), that these complications can be avoided in some cases. He even thought, in Appendix B of the second edition of _Principia Mathematica_, that the ramified hierarchy of natural numbers of order 1,2,… collapses at order 5 for defining the reflexive transitive closure of a relation. However, Gödel later found a problem in his argument, and indeed, it was shown by Myhill 1974 that this hierarchy actually _does not_ collapse at any finite level. A similar problem, discussed by Russell in the introduction to the second edition to [_Principia Mathematica_](../principia-mathematica/) arises in the proof of Cantor’s theorem that there cannot be any injective functions from the collection of all predicates to the collection of all objects (the version of Russell’s paradox in Frege’s system that we presented in the introduction). Can this be done in a ramified hierarchy? Russell doubted that this could be done within a ramified hierarchy of predicates and this was indeed confirmed indeed later (see Chwistek 1926, Fitch 1939 and Heck 1996).

Because of these problems, Russell and Whitehead introduced in the first edition of _Principia Mathematica_ the following _reducibility axiom_: the hierarchy of predicates, first-order, second-order, etc., collapses at level 1. This means that for any predicate of any order, there is a predicate of the first-order level which is equivalent to it. In the case of equality for instance, we postulate a first-order relation “a\=ba\=ba=b” which is equivalent to “aaa satisfies all properties that bbb satisfies”. The motivation for this axiom was purely pragmatic. Without it, all basic mathematical notions, like real or natural numbers are stratified into different orders. Also, despite the apparent circularity of impredicative definitions, the axiom of reducibility does not seem to lead to inconsistencies.

As noticed however first by Chwistek, and later by Ramsey, in the presence of the axiom of reducibility, there is actually no point in introducing the ramified hierarchy at all! It is much simpler to accept impredicative definitions from the start. The simple “extensional” hierarchy of individuals, classes, classes of classes, … is then enough. We get in this way the simpler systems formalised in Gödel 1931 or Church 1940 that were presented above.

The axiom of reducibility draws attention to the problematic status of impredicative definitions. To quote Weyl 1946, the axiom of reducibility “is a bold, an almost fantastic axiom; there is little justification for it in the real world in which we live, and none at all in the evidence on which our mind bases its constructions”! So far, no contradictions have been found using the reducibility axiom. However, as we shall see below, proof-theoretic investigations confirm the extreme strength of such a principle.

The idea of the ramified hierarchy has been extremely important in mathematical logic. Russell considered only the finite iteration of the hierarchy: first-order, second-order, etc., but from the beginning, the possibility of extending the ramification transfinitely was considered. Poincaré (1909) mentions the work of Koenig in this direction. For the example above of numbers of different order, he also defines a number to be inductive of order ωω\\omega if it is inductive of all finite orders. He then points out that _x+y_ is inductive of order ωω\\omega if both xxx and yyy are. This shows that the introduction of transfinite orders can in some case play the role of the axiom of reducibility. Such transfinite extension of the ramified hierarchy was analysed further by Gödel who noticed the key fact that the following form of the reducibility axiom is actually _provable_: when one extends the ramified hierarchy of properties over the natural numbers into the transfinite this hierarchy collapses at level ω1ω1\\omega_1, the least uncountable ordinal (Gödel 1995, and Prawitz 1970). Furthermore, while at all levels <ω1<ω1\\lt \\omega_1, the collection of predicates is countable, the collection of predicates at level ω1ω1\\omega_1 is of cardinality ω1ω1\\omega_1. This fact was a strong motivation behind Gödel’s model of constructible sets. In this model the collection of all subsets of the set of natural numbers (represented by predicates) is of cardinality ω1ω1\\omega_1 and is similar to the ramified hierarchy. This model satisfies in this way the Continuum Hypothesis, and gives a relative consistency proof of this axiom. (The motivation of Gödel was originally only to build a model where the collection of all subsets of natural numbers is well-ordered.)

The ramified hierarchy has been also the source of much work in proof theory. After the discovery by Gentzen that the consistency of Arithmetic could be proved by transfinite induction (over decidable predicates) along the ordinal ε0ε0\\varepsilon_0, the natural question was to find the corresponding ordinal for the different levels of the ramified hierarchy. Schütte (1960) found that for the first level of the ramified hierarchy, that is if we extend arithmetic by quantifying only over first-order properties, we get a system of ordinal strength εε0εε0\\varepsilon\_{\\varepsilon_0}. For the second level we get the ordinal strength εεε0εεε0\\varepsilon\_{\\varepsilon\_{ \\varepsilon_0}}, etc. We recall that εαεα\\varepsilon\_{\\alpha} denotes the αα\\alpha\-th εε\\varepsilon\-ordinal number, an εε\\varepsilon\-ordinal number being an ordinal ββ\\beta such that ωβ\=βωβ\=β\\omega^{\\beta} = \\beta, see Schütte (1960).

Gödel stressed the fact that his approach to the problem of the continuum hypothesis was not constructive, since it needs the uncountable ordinal ω1ω1\\omega_1, and it was natural to study the ramified hierarchy along constructive ordinals. After preliminary works of Lorenzen and Wang, Schütte analysed what happens if we proceed in the following more constructive way. Since arithmetic has for ordinal strength ε0ε0\\varepsilon_0 we consider first the iteration of the ramified hierarchy up to ε0ε0\\varepsilon_0. Schütte computed the ordinal strength of the resulting system and found an ordinal strength u(1)\>ε0u(1)\>ε0u(1)\\gt \\varepsilon_0. We iterate then ramified hierarchy up to this ordinal u(1)u(1)u(1) and get a system of ordinal strength u(2)\>u(1)u(2)\>u(1)u(2)\\gt u(1), etc. Each u(k)u(k)u(k) can be computed in terms of the so-called Veblen hierarchy: u(k+1)u(k+1)u(k+1) is ϕu(k)(0)ϕu(k)(0)\\phi\_{u(k)}(0). The limit of this process gives an ordinal called Γ0Γ0\\Gamma_0: if we iterate the ramified hierarchy up to the ordinal Γ0Γ0\\Gamma_0 we get a system of ordinal strength Γ0Γ0\\Gamma_0. Such an ordinal was obtained independently about the same time by S. Feferman. It has been claimed that Γ0Γ0\\Gamma_0 plays for predicative systems a role similar to ε0ε0\\varepsilon_0 for Arithmetic. Recent proof-theoretical works however are concerned with systems having bigger proof-theoretical ordinals that can be considered predicative (see for instance Palmgren 1995).

Besides these proof theoretic investigations related to the ramified hierarchy, much work has been devoted in proof theory to analysing the consistency of the axiom of reducibility, or, equivalently, the consistency of impredicative definitions. Following Gentzen’s analysis of the cut-elimination property in the sequent calculus, Takeuti found an elegant sequent formulation of simple type theory (without ramification) and made the bold conjecture that cut-elimination should hold for this system. This conjecture seemed at first extremely dubious given the circularity of impredicative quantification, which is well reflected in this formalism. The rule for quantifications is indeed

Γ⊢∀X\[A(X)\]Γ⊢A\[X:\=T\]Γ⊢∀X\[A(X)\]Γ⊢A\[X:=T\] \\frac{\\Gamma \\vdash \\forall X\[A(X)\]}{\\Gamma \\vdash A\[X:=T\]}

where TTT is _any_ term predicate, which may itself involve a quantification over all predicates. Thus the formula A\[X:\=T\]A\[X:=T\]A\[X:=T\] may be itself much more complex than the formula A(X)A(X)A(X).

One early result is that cut-elimination for Takeuti’s impredicative system implies in a finitary way the consistency of second-order Arithmetic. (One shows that this implies the consistency of a suitable form of infinity axiom, see Andrews 2002.) Following work by Schütte (1960b), it was later shown by W. Tait and D. Prawitz that indeed the cut-elimination property holds (the proof of this has to use a stronger proof theoretic principle, as it should be according to the incompleteness theorem.)

What is important here is that these studies have revealed the extreme power of impredicative quantification or, equivalently, the extreme power of the axiom of reducibility. This confirms in some way the intuitions of Poincaré and Russell. The proof-theoretic strength of second-order Arithmetic is way above all ramified extensions of Arithmetic considered by Schütte. On the other hand, despite the circularity of impredicative definitions, which is made so explicit in Takeuti’s calculus, no paradoxes have been found yet in second-order Arithmetic.

Another research direction in proof theory has been to understand how much of impredicative quantification can be explained from principles that are available in intuitionistic mathematics. The strongest such principles are strong forms of inductive definitions. With such principles, one can explain a limited form of an impredicative quantification, called Π11Π11\\Pi\_{1}^1\-comprehension, where one uses only one level of impredicative quantification over predicates. Interestingly, almost all known uses of impredicative quantifications: Leibniz equality, least upper bound, etc., can be done with Π11Π11\\Pi\_{1}^1\-comprehension. This reduction of Π11Π11\\Pi\_{1}^1\-comprehension was first achieved by Takeuti in a quite indirect way, and was later simplified by Buchholz and Schütte using the so-called ΩΩ\\Omega\-rule. It can be seen as a constructive explanation of some restricted, but nontrivial, uses of impredicative definitions.

## 4\. Type Theory/Set Theory

Type theory can be used as a foundation for mathematics, and indeed, it was presented as such by Russell in his 1908 paper, which appeared the same year as Zermelo’s paper, presenting set theory as a foundation for mathematics.

It is clear intuitively how we can explain type theory in set theory: a type is simply interpreted as a set, and function types A→BA→BA \\rightarrow B can be explained using the set theoretic notion of function (as a functional relation, i.e. a set of pairs of elements). The type A→oA→oA \\rightarrow o corresponds to the powerset operation.

The other direction is more interesting. How can we explain the notion of sets in terms of types? There is an elegant solution, due to A. Miquel, which complements previous works by P. Aczel (1978) and which has also the advantage of explaining non necessarily well-founded sets a la Finsler. One simply interprets a _set_ as a _pointed graph_ (where the arrow in the graph represents the membership relation). This is very conveniently represented in type theory, a pointed graph being simply given by a type A and a pair of elements

a:A,R:A→A→oa:A,R:A→A→o a:A, R:A \\rightarrow A \\rightarrow o

We can then define in type theory when two such sets A,a,RA,a,RA, a, R and B,b,SB,b,SB, b, S are equal: this is the case iff there is a bisimulation TTT between AAA and BBB such that TabTabTab holds. A bisimulation is a relation

T:A→B→oT:A→B→o T:A\\rightarrow B\\rightarrow o

such that whenever TxyTxyTxy and RxuRxuRxu hold, there exists vvv such that TuvTuvTuv and SyvSyvSyv hold, and whenever TxyTxyTxy and RyvRyvRyv hold, there exists uuu such that TuvTuvTuv and RxuRxuRxu hold. We can then define the membership relation: the set represented B,b,SB,b,SB, b, S is a member of the set represented by A,a,RA,a,RA, a, R iff there exists a1a1a_1 such that Ra1aRa1aRa_1a and A,a1,RA,a1,RA, a_1, R and B,b,SB,b,SB, b, S are bisimilar.

It can then be checked that all the usual axioms of set theory extensionality, power set, union, comprehension over bounded formulae (and even antifoundation, so that the membership relation does not need to be well-founded) hold in this simple model. (A bounded formula is a formula where all quantifications are of the form ∀x∈a…∀x∈a…\\forall x \\in a\\ldots or ∃x∈a…∃x∈a…\\exists x \\in a\\ldots). In this way it can been shown that Church’s simple type theory is equiconsistent with the bounded version of Zermelo’s set theory.

## 5\. Type Theory/Category Theory

There are deep connections between type theory and category theory. We limit ourselves to presenting two applications of type theory to category theory: the constructions of the free cartesian closed category and of the free topos (see the entry on category theory for an explanation of “cartesian closed” and “topos”).

For building the free cartesian closed category, we extend simple type theory with the type 1 (unit type) and the product type A×BA×BA \\times B, for A,BA,BA, B types. The terms are extended by adding pairing operations and projections and a special element of type 1. As in Lambek and Scott 1986, one can then define a notion of _typed conversions_ between terms, and show that this relation is decidable. One can then show (Lambek and Scott 1986) that the category with types as objects and as morphisms from AAA to BBB the set of closed terms of type A→BA→BA \\rightarrow B (with conversion as equality) is the free cartesian closed category. This can be used to show that equality between arrows in this category is decidable.

The theory of types of Church can also be used to build the free topos. For this we take as objects pairs A,EA,EA,E with AAA type and EEE a partial equivalence relation, that is a closed term E:A→A→oE:A→A→oE:A \\rightarrow A \\rightarrow o which is symmetric and transitive. We take as morphisms between A,EA,EA, E and B,FB,FB, F the relations R:A→B→oR:A→B→oR:A\\rightarrow B\\rightarrow o that are _functional_ that is such that for any a:Aa:Aa:A satisfying EaaEaaE a a there exists one, and only one (modulo F)F)F) element bbb of BBB such that FbbFbbF b b and RabRabR a b. For the subobject classifier we take the pair o,Eo,Eo, E with E:o→o→oE:o→o→oE:o\\rightarrow o\\rightarrow o defined as

EMN\= and (implyMN)(implyNM)EMN\= and (implyMN)(implyNM) E M N = \\text{ and } (\\imply\\, M N) (\\imply\\,N M)

One can then show that this category forms a topos, indeed the free topos.

It should be noted that the type theory in Lambek and Scott 1986 uses a variation of type theory, introduced by Henkin and refined by P. Andrews (2002) which is to have an extensional equality as the only logical connective, i.e. a polymorphic constant

eq:A→A→oeq:A→A→o \\text{eq} : A \\rightarrow A \\rightarrow o

and to define all logical connectives from this connective and constants T,F:oT,F:oT, F : o. For instance, one defines

∀P\=dfeq(λx.T)P∀P\=dfeq(λx.T)P \\forall P =\_{df} \\text{eq} (\\lambda x.T) P

The equality at type ooo is logical equivalence.

One advantage of the intensional formulation is that it allows for a direct notation of proofs based on λλ\\lambda\-calculus (Martin-Löf 1971 and Coquand 1986).

## 6\. Extensions of Type System, Polymorphism, Paradoxes

We have seen the analogy between the operation A →→\\rightarrow A →→\\rightarrow o on types and the powerset operation on sets. In set theory, the powerset operation can be iterated transfinitely along the cumulative hierarchy. It is then natural to look for analogous transfinite versions of type theory.

One such extension of Church’s simple type theory is obtained by adding universes (Martin-Löf 1970). Adding a universe is a _reflection_ process: we add a type UUU whose objects are the types considered so far. For Church’s simple type theory we will have

o:U,i:U and A→B:U if A:U,B:Uo:U,i:U and A→B:U if A:U,B:U o:U, i:U \\text{ and } A\\rightarrow B:U \\text{ if } A:U, B:U

and, furthermore, AAA is a type if A:UA:UA:U. We can then consider types such as

(A:U)→A→A(A:U)→A→A (A:U) \\rightarrow A \\rightarrow A

and functions such as

id\=λA.λx.x:(A:U)→A→Aid\=λA.λx.x:(A:U)→A→A \\text{id} = \\lambda A.\\lambda x.x : (A:U) \\rightarrow A \\rightarrow A

The function id takes as argument a “small” type A:UA:UA:U and an element xxx of type AAA, and outputs an element of type AAA. More generally if T(A)T(A)T(A) is a type under the assumption A:UA:UA:U, one can form the dependent type

(A:U)→T(A)(A:U)→T(A) (A:U) \\rightarrow T(A)

That MMM is of this type means that MA:T(A)MA:T(A)M A:T(A) whenever A:UA:UA:U. We get in this way extensions of type theory whose strength is similar to the one of Zermelo’s set theory (Miquel 2001). More powerful form of universes are considered in (Palmgren 1998). Miquel (2003) presents a version of type theory of strength equivalent to the one of Zermelo-Fraenkel.

One very strong form of universe is obtained by adding the axiom U:UU:UU:U. This was suggested by P. Martin-Löf in 1970. J.Y. Girard showed that the resulting type theory is inconsistent as a logical system (Girard 1972). Though it seems at first that one could directly reproduce Russell’s paradox using a set of all sets, such a direct paradox is actually not possible due to the difference between sets and types. Indeed the derivation of a contradiction in such a system is subtle and has been rather indirect (though, as noticed in Miquel 2001, it can now be reduced to Russell’s paradox by representing sets as pointed graphs). J.Y. Girard first obtained his paradox for a weaker system. This paradox was refined later (Coquand 1994 and Hurkens 1995). (The notion of pure type system, introduced in Barendregt 1992, is convenient for getting a sharp formulation of these paradoxes.) Instead of the axiom U:UU:UU:U one assumes only

(A:U)→T(A):U(A:U)→T(A):U (A:U) \\rightarrow T(A) : U

if T(A):U\[A:U\]T(A):U\[A:U\]T(A) : U \[A:U\]. Notice the circularity, indeed of the same kind as the one that is rejected by the ramified hierarchy: we define an element of type UUU by quantifying over all elements of UUU. For instance the type

(A:U)→A→A:U(A:U)→A→A:U (A:U) \\rightarrow A \\rightarrow A:U

will be the type of the polymorphic identity function. Despite this circularity, J.Y. Girard was able to show normalisation for type systems with this form of polymorphism. However, the extension of Church’s simple type theory with polymorphism is inconsistent as a logical system, i.e. all propositions (terms of type o) are provable.

J.Y. Girard’s motivation for considering a type system with polymorphism was to extend Gödel’s Dialectica (Gödel 1958) interpretation to second-order arithmetic. He proved normalisation using the reducibility method, that had been introduced by Tait (1967) while analysing Gödel 1958. It is quite remarkable that the circularity inherent in impredicativity does not result in non-normalisable terms. (Girard’s argument was then used to show that cut-elimination terminates in Takeuti’s sequent calculus presented above.) A similar system was introduced independently by J. Reynolds (1974) while analysing the notion of polymorphism in computer science.

Martin-Löf’s introduction of a type of all types comes from the identification of the concept of propositions and types, suggested by the work of Curry and Howard. It is worth recalling here his three motivating points:

1.  Russell’s definition of types as ranges of significance of propositional functions
2.  the fact that one needs to quantify over all propositions (impredicativity of simple type theory)
3.  identification of proposition and types

Given (1) and (2) we should have a type of propositions (as in simple type theory), and given (3) this should also be the type of all types. Girard’s paradox shows that one cannot have (1),(2) and (3) simultaneously. Martin-Löf’s choice was to take away (2), restricting type theory to be predicative (and, indeed, the notion of universe appeared first in type theory as a predicative version of the type of all types). The alternative choice of taking away (3) is discussed in Coquand 1986.

## 7\. Univalent Foundations

The connections between type theory, set theory and category theory gets a new light through the work on Univalent Foundations (Voevodsky 2015) and the _Axiom of Univalence_. This involves in an essential way the extension of type theory described in the previous section, in particular dependent types, the view of propositions as types, and the notion of universe of types. These development are also relevant for discussing the notion of structure, the importance of which was for instance emphasized in Russell 1959.

Martin-Löf 1975 \[1973\] introduced a new basic type IdA(a,b)IdA(a,b)\\mathbf{Id}\_A (a,b), if aaa and bbb are in the type AAA, which can be thought as the type of equality proofs of the element aaa and bbb. An important feature of this new type is that it can be iterated, so that we can consider the type IdIdA(a,b)(p,q)IdIdA(a,b)(p,q)\\mathbf{Id}\_{\\mathbf{Id}\_A (a,b)}(p,q) if ppp and qqq are of type IdA(a,b)IdA(a,b)\\mathbf{Id}\_A (a,b). If we think of a type as a special kind of set, it is natural to conjecture that such a type of equality proofs is always inhabited for any two equality proofs ppp and qqq. Indeed, intuitively, there seems to be at most an equality proof between two elements aaa and bbb. Surprisingly, Hofmann and Streicher 1996 designed a model of dependent type theory where this is not valid, that is a model where they can be different proofs that two elements are equal. In this model, a type is interpreted by a _groupoid_ and the type IdA(a,b)IdA(a,b)\\mathbf{Id}\_A (a,b) by the set of isomorphisms between aaa and bbb, set which may have more than one element. The existence of this model has the consequence that it cannot be proved in general in type theory that an equality type has at most one element. This groupoid interpretation has been generalized in the following way, which gives an intuitive interpretation of the identity type. A _type_ is interpreted by a _topological space_, up to homotopy, and a type IdA(a,b)IdA(a,b)\\mathbf{Id}\_A (a,b) is interpreted by the type of _paths_ connecting aaa and bbb. (See Awodey et al. 2013 and \[HoTT 2013, Other Internet Resources\].)

Voevodsky 2015 introduced the following stratification of types. (This stratification was motivated in part by this interpretation of a type as a topological space, but can be understood directly without reference to this interpretation.) We say that a type AAA is a _proposition_ if we have IdA(a,b)IdA(a,b)\\mathbf{Id}\_A (a,b) for any element aaa and bbb of AAA (this means that the type AAA has at most one element). We say that a type AAA is a _set_ if the type IdA(a,b)IdA(a,b)\\mathbf{Id}\_A (a,b) is a proposition for any element aaa and bbb of AAA. We say that a type AAA is a _groupoid_ if the type IdA(a,b)IdA(a,b)\\mathbf{Id}\_A (a,b) is a set for any element aaa and bbb of AAA. The justification of this terminology is that it can be shown, only using the rules of type theory, that any such type can indeed be seen as a groupoid in the usual categorical sense, where the objects are the elements of this type, the set of morphisms between aaa and bbb being represented by the _set_ IdA(a,b)IdA(a,b)\\mathbf{Id}\_A (a,b). The composition is the proof of transitivity of equality, and the identity morphism is the proof of reflexivity of equality. The fact that each morphism has an inverse corresponds to the fact that identity is a symmetric relation. This stratification can then be extended and we can define when a type is a 2-groupoid, 3-groupoid and so on. In this view, _type theory_ appears as a vast generalization of _set theory_, since a set is a particular kind of type.

Voevodsky 2015 introduces also a notion of _equivalence_ between types, notion which generalizes in an uniform way the notions of _logical equivalence_ between propositions, _bijection_ between sets, _categorical equivalence_ between groupoids, and so on. We say that a map f:A→Bf:A→Bf:A\\rightarrow B is an equivalence if, for any element bbb in BBB the type of pairs a,pa,pa,p where ppp is of type IdB(fa,b)IdB(fa,b)\\mathbf{Id}\_B (f a,b), is a proposition and is inhabited. This expresses in a strong way that an element in BBB is the image of exactly one element in AAA, and if AAA and BBB are sets, we recover the usual notion of bijection between sets. (In general if f:A→Bf:A→Bf:A\\rightarrow B is an equivalence, then we have a map B→AB→AB\\rightarrow A, which can be thought of as the inverse of fff.) It can be shown for instance that the identity map is always an equivalence. Let Equiv(A,B)Equiv(A,B)\\text{Equiv}(A,B) be the type of pairs f,pf,pf,p where f:A→Bf:A→Bf:A\\rightarrow B and ppp is a proof that fff is an equivalence. Using the fact that the identity map is an equivalence we have an element of Equiv(A,A)Equiv(A,A)\\text{Equiv}(A,A) for any type AAA. This implies that we have a map

IdU(A,B)→Equiv(A,B)IdU(A,B)→Equiv(A,B) \\mathbf{Id}\_U (A,B)\\rightarrow \\text{Equiv}(A,B)

and the _Axiom of Univalence_ states that this map is an equivalence. In particular, we have the implication

Equiv(A,B)→IdU(A,B)Equiv(A,B)→IdU(A,B) \\text{Equiv}(A,B)\\rightarrow \\mathbf{Id}\_U (A,B)

and so if there is an equivalence between two small types then these types are equal.

This Axiom can be seen as a strong form of the extensionality principle. It indeed generalizes the Axiom of _propositional extensionality_ mentioned by Church 1940, which states that two logically equivalent propositions are equal. Surprisingly, it also implies the Axiom of _function extensionality_, Axiom 10 in Church 1940, which states that two pointwise equal functions are equal (Voevodsky 2015). It also directly implies that two isomorphic sets are equal, that two categorically equivalent groupoids are equal, and so one.

This can be used to give a formulation of the notion of _transport of structures_ (Bourbaki 1957) along equivalences. For instance, let MAMAM A be the type of monoid structures on the set AAA: this is the type of tuples m,e,pm,e,pm, e, p where mmm is a binary operation on AAA and eee an element of AAA and ppp a proof that these elements satisfy the usual monoid laws. The rule of substitution of equal by equal takes the form

IdU(A,B)→MA→MBIdU(A,B)→MA→MB \\mathbf{Id}\_U (A,B)\\rightarrow M A\\rightarrow M B

If there is a bijection between AAA and BBB they are equal by the Axiom of Univalence, and we can use this implication to transport any monoid structure of AAA in a monoid structure of BBB.

Both Russell 1919 and Russell 1959 stress the importance of the notion of structure. For instance, in Chapter VI of Russell 1919, it is noticed that two similar relations essentially have the same properties, and hence have the same “structure”. (The notion of “similarity” of relations was introduced in Russell 1901.) We can also use this framework to refine Russell’s discussions on the notion of structure. For instance, let **Monoid** be the type of pairs A,pA,pA,p where ppp is an element of MAMAM A. Two such pairs A,pA,pA,p and B,qB,qB,q are isomorphic if there exists a bijection fff from AAA to BBB such that qqq is equal to the transport of structure of ppp along fff. A consequence of the Axiom of Univalence is that two isomorphic elements of the type **Monoid** are equal, and hence shares the same properties. Notice that such a general transport of properties is _not_ possible when structures are formulated in a set theoretic framework. Indeed, in a set theoretic framework, it is possible to formulate properties using the membership relations, for instance the property that the carrier set of the structure contains the natural number 000, property that is not preserved in general by isomorphisms. Intuitively, the set theoretical description of a structure is not abstract enough since we can talk about the way this structure is built up. This difference between set theory and type theory is yet another illustration of the characterization by J.Reynolds 1983 of a type structure as a “syntactical discipline for enforcing level of abstraction”.
