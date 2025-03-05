# Type Theory
# 类型理论

_First published Wed Feb 8, 2006; substantive revision Tue Sep 6, 2022_
_首次发布于2006年2月8日星期三；实质性修订于2022年9月6日星期二_

The topic of **type theory** is fundamental both in logic and computer science. We limit ourselves here to sketch some aspects that are important in logic. For the importance of types in computer science, we refer the reader for instance to Reynolds 1983 and 1985.
**类型理论(Type Theory)**这一主题在逻辑学和计算机科学中都具有基础性地位。我们在此仅限于概述一些在逻辑学中重要的方面。关于类型在计算机科学中的重要性，我们建议读者参考例如Reynolds 1983和1985年的著作。

*   [1\. Paradoxes and Russell’s Type Theories](#ParaRussTypeTheo)
*   [1. 悖论与罗素的类型理论](#ParaRussTypeTheo)
*   [2\. Simple Type Theory and the λ-Calculus](#SimpTypeTheoLCalc)
*   [2. 简单类型论与λ演算](#SimpTypeTheoLCalc)
*   [3\. Ramified Hierarchy and Impredicative Principles](#RamiHierImprPrin)
*   [3\. 分支层级与不可判定原则](#RamiHierImprPrin)
*   [4\. Type Theory/Set Theory](#TypeTheoTheo)
*   [4\. 类型理论/集合理论](#TypeTheoTheo)
*   [5\. Type Theory/Category Theory](#TypeTheoCatTheo)
*   [5. 类型理论/范畴理论](#TypeTheoCatTheo)
*   [6\. Extensions of Type System, Polymorphism, Paradoxes](#ExteTypeSystPolyPara)
*   [6. 类型系统的扩展、多态性、悖论](#ExteTypeSystPolyPara)
*   [7\. Univalent Foundations](#UnivFoun)
*   [7\. 单值基础](#UnivFoun)
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

The theory of types was introduced by **Russell** in order to cope with some contradictions he found in his account of set theory and was introduced in “Appendix B: The Doctrine of Types” of Russell 1903. This contradiction was obtained by analysing a theorem of Cantor that no mapping
类型理论是由**Russell**提出的，目的是为了解决他在集合论描述中发现的一些矛盾，并在1903年Russell的“附录B：类型学说”中引入。这一矛盾是通过分析Cantor的一个定理得出的，该定理指出不存在映射

\[ F:X \rightarrow \Pow(X) \]
\[ F:X \rightarrow \Pow(X) \]

(where \(\Pow(X)\) is the class of subclasses of a class \(X\)) can be surjective; that is, \(F\) cannot be such that every member \(b\) of \(\Pow(X)\) is equal to \(F(a)\) for some element \(a\) of \(X\). This can be phrased "intuitively" as the fact that there are more subsets of \(X\) than elements of \(X\). The proof of this fact is so simple and basic that it is worthwhile giving it here. Consider the following subset of \(X\):
（其中 \(\Pow(X)\) 是类 \(X\) 的子类类）可以是满射的；也就是说，\(F\) 不能使得 \(\Pow(X)\) 的每个成员 \(b\) 都等于某个 \(X\) 的元素 \(a\) 的 \(F(a)\)。这可以“直观地”表述为 \(X\) 的子集比 \(X\) 的元素多。这个事实的证明非常简单和基础，值得在这里给出。考虑 \(X\) 的以下子集：

\[ A = \{ x \in X \mid x \not\in F(x) \}. \]
\[ A = \{ x \in X \mid x \not\in F(x) \}. \]

这个子集不能是 \(F\) 的值域中的元素。因为如果 \(A = F(a)\)，对于某个 \(a\)，那么

This subset cannot be in the range of \(F\). For if \(A = F(a)\), for some \(a\), then
这个子集不可能在 \(F\) 的范围内。因为如果对于某个 \(a\)，有 \(A = F(a)\)，那么

\[
\[

a \in F(a) \text{ 当且仅当 } a \in A \text{ 当且仅当 } a \not\in F(a)

\]
a \in F(a) \text{ iff } a \in A \text{ iff } a \not\in F(a)
\[

a \in F(a) \text{ 当且仅当 } a \in A \text{ 当且仅当 } a \not\in F(a)

\]
\]
\]
这是一个矛盾。

which is a contradiction.
这是一个矛盾。

Some remarks are in order. First, the proof does not use the law of excluded middle and is thus valid intuitionistically. Second, the method that is used, called _diagonalisation_ was already present in the work of du Bois-Reymond for building real functions growing faster than any function in a given sequence of functions.
需要做一些说明。首先，该证明没有使用排中律，因此在直觉主义意义下是有效的。其次，所使用的方法称为**对角线法**，这种方法在 du Bois-Reymond 的工作中已经出现，用于构造比给定函数序列中任何函数增长更快的实函数。

**Russell** analysed what happens if we apply this theorem to the case where \(A\) is the class of all classes, admitting that there is such a class. He was then lead to consider the special class of classes that do not belong to themselves
**Russell** 分析了当我们把这个定理应用到 \(A\) 是所有类的类这一情况时会发生什么，假设存在这样一个类。他随后被引导去考虑那些不属于自身的类的特殊类。

(\*) \( R = \{ w \mid w \not\in w \} \).
(\*) \( R = \{ w \mid w \not\in w \} \).

We then have
我们于是有

\[ R \in R \text{ iff } R \not\in R. \]
\[ R \in R \text{ 当且仅当 } R \not\in R. \]

It seems indeed that Cantor was already aware of the fact that the class of all sets cannot be considered itself to be a set.
确实，Cantor 似乎已经意识到所有集合的类本身不能被看作是一个集合。

**Russell** communicated this problem to **Frege**, and his letter, together with Frege’s answer appear in van Heijenoort 1967. It is important to realise that the formulation (\*) does not apply as it is to Frege’s system. As Frege himself wrote in his reply to Russell, the expression “a predicate is predicated of itself” is not exact. Frege had a distinction between **predicates** (concepts) and **objects**. A (first-order) predicate applies to an object but it cannot have a predicate as argument. The exact formulation of the paradox in Frege’s system uses the notion of the **extension** of a predicate \(P\), which we designate as \(\varepsilon P\). The extension of a predicate is itself an object. The important **Axiom V** is:
**Russell** 将这个问题传达给了 **Frege**，他的信件以及 Frege 的回复出现在 van Heijenoort 1967 中。重要的是要认识到，表述 (\*) 并不直接适用于 Frege 的系统。正如 Frege 本人在回复 Russell 时写道，“一个谓词被用于自身”这一表述并不准确。Frege 区分了**谓词(概念)**和**对象**。一个（一阶）谓词适用于一个对象，但它不能以谓词作为参数。在 Frege 的系统中，悖论的精确表述使用了谓词 \(P\) 的**外延**概念，我们将其表示为 \(\varepsilon P\)。谓词的外延本身是一个对象。重要的**公理 V**是：

(Axiom V) \[ \varepsilon P = \varepsilon Q \equiv \forall x [P(x) \equiv Q(x)] \]
(公理 V) \[ \varepsilon P = \varepsilon Q \equiv \forall x [P(x) \equiv Q(x)] \]

This axiom asserts that the extension of \(P\) is identical to the extension of \(Q\) if and only if \(P\) and \(Q\) are materially equivalent. We can then translate Russell’s paradox (\*) in Frege’s system by defining the predicate
该公理断言，当且仅当 \(P\) 和 \(Q\) 在实质上等价时，\(P\) 的外延与 \(Q\) 的外延相同。然后，我们可以通过在 Frege 的系统中定义谓词来翻译 Russell 悖论 (\*)。

\[ R(x) \text{ iff } \exists P[x = \varepsilon P \wedge \neg P(x)] \]
\[ R(x) \text{ 当且仅当 } \exists P[x = \varepsilon P \wedge \neg P(x)] \]

It can then been checked, using Axiom V in a crucial way, that
然后可以验证，以公理V为关键，

\[ R(\varepsilon R) \equiv \neg R(\varepsilon R) \]
\[ R(\varepsilon R) \equiv \neg R(\varepsilon R) \]

翻译为：

\[ R(\varepsilon R) \equiv \neg R(\varepsilon R) \]

解释：该公式表示 \( R(\varepsilon R) \) 与 \( \neg R(\varepsilon R) \) 在逻辑上等价，即两者同时为真或同时为假。这导致了一个矛盾，因为一个命题不能同时为真和假。

and we have a contradiction as well. (Notice that for defining the predicate \(R\), we have used an **impredicative** existential quantification on predicates. It can be shown that the **predicative** version of Frege’s system is consistent (see Heck 1996 and for further refinements Ferreira 2002).
我们也得到了一个矛盾。（注意，在定义谓词 \(R\) 时，我们使用了**非直谓的(impredicative)** 存在量化。可以证明，弗雷格系统的**直谓的(predicative)** 版本是一致的（参见 Heck 1996 以及 Ferreira 2002 的进一步改进）。

It is clear from this account that an idea of types was already present in Frege’s work: there we find a distinction between objects, predicates (or concepts), predicates of predicates, etc. (This point is stressed in Quine 1940.) This hierarchy is called the “extensional hierarchy” by Russell (1959), and its necessity was recognised by Russell as a consequence of his paradox.从这段论述中可以清楚地看出，类型(type)的概念已经存在于Frege的工作中：我们发现对象、谓词（或概念）、谓词的谓词等之间存在区分。（这一点在Quine 1940中被强调。）Russell（1959）将这种层次结构称为"外延层次(extensional hierarchy)"，并且Russell认识到其必要性是他悖论的结果。