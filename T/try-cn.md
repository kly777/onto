# Type Theory
# 类型理论

_First published Wed Feb 8, 2006; substantive revision Tue Sep 6, 2022_
_首次发布于2006年2月8日，星期三；实质性修订于2022年9月6日，星期二_

The topic of type theory is fundamental both in logic and computer science. We limit ourselves here to sketch some aspects that are important in logic. For the importance of types in computer science, we refer the reader for instance to Reynolds 1983 and 1985.
类型理论(Type Theory)这一主题在逻辑学和计算机科学中都具有基础性地位。我们在此仅概述一些在逻辑学中重要的方面。关于类型在计算机科学中的重要性，读者可参考例如Reynolds 1983和1985年的著作。

*   [1\. Paradoxes and Russell’s Type Theories](#ParaRussTypeTheo)
*   [1. 悖论与罗素(Russell)的类型理论](#ParaRussTypeTheo)
*   [2\. Simple Type Theory and the λλ\\lambda\-Calculus](#SimpTypeTheoLCalc)
*   [2. 简单类型论与λλ\\lambda演算](#SimpTypeTheoLCalc)
*   [3\. Ramified Hierarchy and Impredicative Principles](#RamiHierImprPrin)
*   [3. 分支层级与不可判定原则](#RamiHierImprPrin)
*   [4\. Type Theory/Set Theory](#TypeTheoTheo)
*   [4. 类型理论/集合理论](#TypeTheoTheo)
*   [5\. Type Theory/Category Theory](#TypeTheoCatTheo)
*   [5. 类型理论/范畴理论](#TypeTheoCatTheo)
*   [6\. Extensions of Type System, Polymorphism, Paradoxes](#ExteTypeSystPolyPara)
*   [6. 类型系统的扩展、多态性、悖论](#ExteTypeSystPolyPara)
*   [7\. Univalent Foundations](#UnivFoun)
*   [7. 单值基础](#UnivFoun)
*   [Bibliography](#Bib)
*   [参考文献](#Bib)
*   [Academic Tools](#Aca)
*   [学术工具](#Aca)
*   [Other Internet Resources](#Oth)
*   [其他互联网资源](#Oth)
*   [Related Entries](#Rel)
*   [相关条目](#Rel)

- - -
- - -

## 1\. Paradoxes and Russell’s Type Theories
## 1. 悖论与罗素的类型理论

The theory of types was introduced by Russell in order to cope with some contradictions he found in his account of set theory and was introduced in “Appendix B: The Doctrine of Types” of Russell 1903. This contradiction was obtained by analysing a theorem of Cantor that no mapping
类型理论是由Russell提出的，旨在解决他在集合论描述中发现的一些矛盾，并在Russell 1903年的“附录B：类型学说”中引入。这一矛盾是通过分析Cantor的一个定理得出的，该定理指出不存在映射

F:X→Pow(X)F:X→Pow(X) F:X \\rightarrow \\Pow(X)
F:X→Pow(X) F:X → Pow(X)

(where Pow(X)Pow(X)\\Pow(X) is the class of subclasses of a class X)X)X) can be surjective; that is, FFF cannot be such that every member bbb of Pow(X)Pow(X)\\Pow(X) is equal to F(a)F(a)F(a) for some element aaa of XXX. This can be phrased “intuitively” as the fact that there are more subsets of XXX than elements of XXX. The proof of this fact is so simple and basic that it is worthwhile giving it here. Consider the following subset of XXX:
（其中 Pow(X) 是类 X 的子类类）可以是满射的；也就是说，F 不能使得 Pow(X) 的每个成员 b 都等于某个 X 的元素 a 的 F(a)。这可以“直观地”表述为 X 的子集比 X 的元素多这一事实。这个事实的证明非常简单和基础，因此值得在此给出。考虑 X 的以下子集：

A\={x∈X∣x∉F(x)}.A\={x∈X∣x∉F(x)}. A = \\{ x \\in X \\mid x \\not\\in F(x)\\}.
A = {x ∈ X | x ∉ F(x)}. A = {x ∈ X | x ∉ F(x)}. A = \\{ x \\in X \\mid x \\not\\in F(x)\\}.

This subset cannot be in the range of FFF. For if A\=F(a)A\=F(a)A = F(a), for some aaa, then
这个子集不可能在 F 的范围内。因为如果对于某个 a，A = F(a)，那么

a∈F(a) iff a∈A iff a∉F(a)a∈F(a) iff a∈A iff a∉F(a)\\begin{align} a \\in F(a) &\\text{ iff } a \\in A \\\\ &\\text{ iff } a \\not\\in F(a) \\end{align}
a ∈ F(a) 当且仅当 a ∈ A 当且仅当 a ∉ F(a)

\begin{align} 
a \in F(a) &\text{ 当且仅当 } a \in A \\ 
&\text{ 当且仅当 } a \not\in F(a) 
\end{align}

which is a contradiction.
这是一个矛盾。

Some remarks are in order. First, the proof does not use the law of excluded middle and is thus valid intuitionistically. Second, the method that is used, called _diagonalisation_ was already present in the work of du Bois-Reymond for building real functions growing faster than any function in a given sequence of functions.
需要做一些说明。首先，该证明没有使用排中律，因此在直觉主义意义下是有效的。其次，所使用的方法称为**对角线法**，这种方法在 du Bois-Reymond 的工作中已经出现，用于构造比给定函数序列中任何函数增长得更快的实函数。

Russell analysed what happens if we apply this theorem to the case where A is the class of all classes, admitting that there is such a class. He was then lead to consider the special class of classes that do not belong to themselves
Russell分析了如果我们把这个定理应用到A是所有类的类的情况会发生什么，他承认存在这样的类。然后他被引导去考虑那些不属于自身的类的特殊类。

(\*)R\={w∣w∉w}.(\*)R\={w∣w∉w}.\\tag{\*} R = \\{ w \\mid w \\not\\in w \\}.


We then have
我们于是得到

R∈R iff R∉R.R∈R iff R∉R. R \\in R \\text{ iff } R \\not\\in R.
R∈R 当且仅当 R∉R。R∈R 当且仅当 R∉R。R \\in R \\text{ 当且仅当 } R \\not\\in R。

It seems indeed that Cantor was already aware of the fact that the class of all sets cannot be considered itself to be a set.
确实，康托尔似乎已经意识到所有集合的类本身不能被视作一个集合。

Russell communicated this problem to Frege, and his letter, together with Frege’s answer appear in van Heijenoort 1967. It is important to realise that the formulation (\*) does not apply as it is to Frege’s system. As Frege himself wrote in his reply to Russell, the expression “a predicate is predicated of itself” is not exact. Frege had a distinction between _predicates_ (concepts) and _objects_. A (first-order) predicate applies to an object but it cannot have a predicate as argument. The exact formulation of the paradox in Frege’s system uses the notion of the _extension_ of a predicate PPP, which we designate as εPεP\\varepsilon P. The extension of a predicate is itself an object. The important axiom V is:
Russell 将这个问题传达给了 Frege，他的信件以及 Frege 的回复出现在 van Heijenoort 1967 年出版的文集中。重要的是要认识到，表述 (\*) 并不直接适用于 Frege 的系统。正如 Frege 本人在回复 Russell 时所写的那样，“一个谓词被用于自身”这一表述并不准确。Frege 对 _谓词_（概念）和 _对象_ 进行了区分。一个（一阶）谓词适用于一个对象，但它不能以谓词作为参数。在 Frege 的系统中，悖论的精确表述使用了谓词 PPP 的 _外延_ 概念，我们将其表示为 εPεP\\varepsilon P。谓词的外延本身就是一个对象。重要的公理 V 是：

(Axiom V)εP\=εQ≡∀x\[P(x)≡Q(x)\](Axiom V)εP\=εQ≡∀x\[P(x)≡Q(x)\]\\tag{Axiom V} \\varepsilon P = \\varepsilon Q \\equiv \\forall x \[P(x) \\equiv Q(x)\]
(公理 V) εP = εQ ≡ ∀x [P(x) ≡ Q(x)]

This axiom asserts that the extension of PPP is identical to the extension of QQQ if and only if PPP and QQQ are materially equivalent. We can then translate Russell’s paradox (\*) in Frege’s system by defining the predicate
该公理断言，当且仅当PPP和QQQ在实质上是等价的，PPP的外延与QQQ的外延是相同的。然后，我们可以通过定义谓词将罗素悖论(\*)翻译到弗雷格的系统中。

R(x) iff ∃P\[x\=εP∧¬P(x)\]R(x) iff ∃P\[x\=εP∧¬P(x)\] R(x) \\text{ iff } \\exists P\[x = \\varepsilon P \\wedge \\neg P(x)\]
R(x) 当且仅当 存在P\[x = εP 且 非P(x)\]

It can then been checked, using Axiom V in a crucial way, that
然后可以验证，以关键方式使用公理 V，

R(εR)≡¬R(εR)R(εR)≡¬R(εR) R(\\varepsilon R) \\equiv \\neg R(\\varepsilon R)
R(εR) ≡ ¬R(εR) R(εR) ≡ ¬R(εR) R(\\varepsilon R) \\equiv \\neg R(\\varepsilon R)

and we have a contradiction as well. (Notice that for defining the predicate RRR, we have used an _impredicative_ existential quantification on predicates. It can be shown that the _predicative_ version of Frege’s system is consistent (see Heck 1996 and for further refinements Ferreira 2002).
并且我们也得到了一个矛盾。（注意，为了定义谓词 RRR，我们使用了谓词上的**非直谓**存在量化。可以证明，弗雷格系统的**直谓**版本是一致的（参见 Heck 1996 以及 Ferreira 2002 的进一步改进）。

It is clear from this account that an idea of types was already present in Frege’s work: there we find a distinction between objects, predicates (or concepts), predicates of predicates, etc. (This point is stressed in Quine 1940.) This hierarchy is called the “extensional hierarchy” by Russell (1959), and its necessity was recognised by Russell as a consequence of his paradox.
从这段叙述中可以清楚地看出，类型的思想已经存在于弗雷格(Frege)的工作中：我们发现对象、谓词（或概念）、谓词的谓词等之间存在区别。（这一点在Quine 1940中被强调。）这种层级结构被罗素(Russell)（1959）称为“外延层级”，罗素认识到其必要性是他悖论的结果。