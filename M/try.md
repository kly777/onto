# Type Theory

_First published Wed Feb 8, 2006; substantive revision Tue Sep 6, 2022_

The topic of type theory is fundamental both in logic and computer science. We limit ourselves here to sketch some aspects that are important in logic. For the importance of types in computer science, we refer the reader for instance to Reynolds 1983 and 1985.

*   [1\. Paradoxes and Russell’s Type Theories](#ParaRussTypeTheo)
*   [2\. Simple Type Theory and the λλ\\lambda\-Calculus](#SimpTypeTheoLCalc)
*   [3\. Ramified Hierarchy and Impredicative Principles](#RamiHierImprPrin)
*   [4\. Type Theory/Set Theory](#TypeTheoTheo)
*   [5\. Type Theory/Category Theory](#TypeTheoCatTheo)
*   [6\. Extensions of Type System, Polymorphism, Paradoxes](#ExteTypeSystPolyPara)
*   [7\. Univalent Foundations](#UnivFoun)
*   [Bibliography](#Bib)
*   [Academic Tools](#Aca)
*   [Other Internet Resources](#Oth)
*   [Related Entries](#Rel)

- - -

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
