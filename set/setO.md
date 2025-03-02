Set theory is the branch of mathematical logic that studies sets, which can be informally described as collections of objects. Although objects of any kind can be collected into a set, set theory – as a branch of mathematics – is mostly concerned with those that are relevant to mathematics as a whole.
集合论是研究集合的数理逻辑分支，可以非正式地描述为对象的集合。尽管任何类型的对象都可以收集到一个集合中，但集合论作为数学的一个分支，主要关注与整个数学相关的对象。

The modern study of set theory was initiated by the German mathematicians Richard Dedekind and Georg Cantor in the 1870s. In particular, Georg Cantor is commonly considered the founder of set theory. The non-formalized systems investigated during this early stage go under the name of naive set theory. After the discovery of paradoxes within naive set theory (such as Russell's paradox, Cantor's paradox and the Burali-Forti paradox), various axiomatic systems were proposed in the early twentieth century, of which Zermelo–Fraenkel set theory (with or without the axiom of choice) is still the best-known and most studied.
集合论的现代研究是由德国数学家理查德·戴德金 （Richard Dedekind） 和乔治·康托 （Georg Cantor） 在 1870 年代发起的。特别是，Georg Cantor 通常被认为是集合论的创始人。在这个早期阶段研究的非形式化系统被冠以朴素集合论的名义。在朴素集合论中发现悖论（如罗素悖论、康托尔悖论和 Burali-Forti 悖论）后，20 世纪初提出了各种公理系统，其中 Zermelo-Fraenkel 集合论（有或没有选择的公理）仍然是最著名和研究最多的。

Set theory is commonly employed as a foundational system for the whole of mathematics, particularly in the form of Zermelo–Fraenkel set theory with the axiom of choice. Besides its foundational role, set theory also provides the framework to develop a mathematical theory of infinity, and has various applications in computer science (such as in the theory of relational algebra), philosophy, formal semantics, and evolutionary dynamics. Its foundational appeal, together with its paradoxes, and its implications for the concept of infinity and its multiple applications have made set theory an area of major interest for logicians and philosophers of mathematics. Contemporary research into set theory covers a vast array of topics, ranging from the structure of the real number line to the study of the consistency of large cardinals.
集合论通常被用作整个数学的基础系统，特别是以 Zermelo-Fraenkel 集合论的形式，具有选择公理。除了其基础作用外，集合论还为发展无穷数学理论提供了框架，并在计算机科学（例如关系代数理论）、哲学、形式语义学和进化动力学中具有多种应用。它的基本吸引力，连同它的悖论，以及它对无限概念及其多种应用的影响，使集合论成为逻辑学家和数学哲学家主要感兴趣的领域。集合论的当代研究涵盖了广泛的主题，从实数线的结构到大基数一致性的研究。

Basic concepts and notation
基本概念和符号
Main articles: Set (mathematics) and Algebra of sets

Set theory begins with a fundamental binary relation between an object o and a set A. If o is a member (or element) of A, the notation o ∈ A is used. A set is described by listing elements separated by commas, or by a characterizing property of its elements, within braces { }.[8] Since sets are objects, the membership relation can relate sets as well, i.e., sets themselves can be members of other sets.
集合论从对象 o 和集合 A 之间的基本二进制关系开始。如果 o 是 A 的成员（或元素），则使用表示法 o ∈ A。一个集合的描述方式是列出用逗号分隔的元素，或者用大括号 { } 列出其元素的特征属性。[8] 由于集合是对象，因此隶属关系也可以关联集合，即集合本身可以是其他集合的成员。

A derived binary relation between two sets is the subset relation, also called set inclusion. If all the members of set A are also members of set B, then A is a subset of B, denoted A ⊆ B. For example, {1, 2} is a subset of {1, 2, 3}, and so is {2} but {1, 4} is not. As implied by this definition, a set is a subset of itself. For cases where this possibility is unsuitable or would make sense to be rejected, the term proper subset is defined. A is called a proper subset of B if and only if A is a subset of B, but A is not equal to B. Also, 1, 2, and 3 are members (elements) of the set {1, 2, 3}, but are not subsets of it; and in turn, the subsets, such as {1}, are not members of the set {1, 2, 3}. More complicated relations can exist; for example, the set {1} is both a member and a proper subset of the set {1, {1}}.
两个集合之间的派生二进制关系是子集关系，也称为集合包含。如果集 A 的所有成员也是集 B 的成员，则 A 是 B 的子集，表示为 A ⊆ B。例如，{1， 2} 是 {1， 2， 3} 的子集，{2} 也是如此，但 {1， 4} 不是。正如这个定义所暗示的那样，一个集合是其自身的子集。对于这种可能性不合适或被拒绝有意义的情况，定义了术语 proper subset 。当且仅当 A 是 B 的子集，但 A 不等于 B 时，A 才称为 B 的适当子集。此外，1、2 和 3 是集合 {1， 2， 3} 的成员（元素），但不是它的子集;反过来，子集（如 {1}）不是集合 {1， 2， 3} 的成员。可能存在更复杂的关系;例如，集{1}既是集 {1， {1}} 的成员，也是集的适当子集。

Just as arithmetic features binary operations on numbers, set theory features binary operations on sets.[9] The following is a partial list of them:
正如算术的特点是对数字进行二进制运算一样，集合论的特点是对集合进行二进制运算。[9]以下是它们的部分列表：

    Union of the sets A and B, denoted A ∪ B, is the set of all objects that are a member of A, or B, or both.[10] For example, the union of {1, 2, 3} and {2, 3, 4} is the set {1, 2, 3, 4}.
    集合 A 和 B 的并集（表示为 A ∪ B）是属于 A 和/或 B 的所有对象的集合。[10] 例如，{1， 2， 3} 和 {2， 3， 4} 的并集是集合 {1， 2， 3， 4}。
    Intersection of the sets A and B, denoted A ∩ B, is the set of all objects that are members of both A and B. For example, the intersection of {1, 2, 3} and {2, 3, 4} is the set {2, 3}.
    集合 A 和 B 的交集（表示为 A ∩ B）是同时属于 A 和 B 的所有对象的集合。例如，{1， 2， 3} 和 {2， 3， 4} 的交集是集合 {2， 3}。
    Set difference of U and A, denoted U \ A, is the set of all members of U that are not members of A. The set difference {1, 2, 3} \ {2, 3, 4} is {1}, while conversely, the set difference {2, 3, 4} \ {1, 2, 3} is {4}. When A is a subset of U, the set difference U \ A is also called the complement of A in U. In this case, if the choice of U is clear from the context, the notation Ac is sometimes used instead of U \ A, particularly if U is a universal set as in the study of Venn diagrams.
    U 和 A 的集合差值（表示为 U \ A）是 U 中不是 A 成员的所有成员的集合。集合差异 {1， 2， 3} \ {2， 3， 4} 是 {1}，而相反，集合差异 {2， 3， 4} \ {1， 2， 3} 是 {4}。当 A 是 U 的子集时，集合差值 U \ A 也称为 A 在 U 中的补数。在这种情况下，如果从上下文中清楚地选择了 U，则有时会使用符号 Ac 而不是 U \ A，特别是如果 U 是通用集，如维恩图研究。
    Symmetric difference of sets A and B, denoted A △ B or A ⊖ B, is the set of all objects that are a member of exactly one of A and B (elements which are in one of the sets, but not in both). For instance, for the sets {1, 2, 3} and {2, 3, 4}, the symmetric difference set is {1, 4}. It is the set difference of the union and the intersection, (A ∪ B) \ (A ∩ B) or (A \ B) ∪ (B \ A).
    集合 A 和 B 的对称差值，表示为 A △ B 或 A ⊖ B，是恰好属于 A 和 B 之一的所有对象的集合（元素在其中一个集合中，但不在两个集合中）。例如，对于集合 {1， 2， 3} 和 {2， 3， 4}，对称差集为 {1， 4}。它是并集和交集的集合差，（A ∪ B） \ （A ∩ B） 或 （A \ B） ∪ （B \ A）。
    Cartesian product of A and B, denoted A × B, is the set whose members are all possible ordered pairs (a, b), where a is a member of A and b is a member of B. For example, the Cartesian product of {1, 2} and {red, white} is {(1, red), (1, white), (2, red), (2, white)}.
    A 和 B 的笛卡尔积（表示为 A × B）是其成员都是可能的有序对 （a， b） 的集合，其中 a 是 A 的成员，b 是 B 的成员。例如，{1， 2} 和 {red， white} 的笛卡尔积是 {（1， red）， （1， white）， （2， red）， （2， white）}。

Some basic sets of central importance are the set of natural numbers, the set of real numbers and the empty set – the unique set containing no elements. The empty set is also occasionally called the null set,[11] though this name is ambiguous and can lead to several interpretations.
一些基本的重要性是自然数集、实数集和空集 – 不包含元素的唯一集。空集有时也被称为空集，[11]尽管这个名称是模棱两可的，并且可能导致多种解释。

The power set of a set A, denoted P ( A ) {\displaystyle {\mathcal {P}}(A)}, is the set whose members are all of the possible subsets of A. For example, the power set of {1, 2} is { {}, {1}, {2}, {1, 2} }. Notably, P ( A ) {\displaystyle {\mathcal {P}}(A)} contains both A and the empty set.
集合 A 的幂集（表示为 P ( A ) {\displaystyle {\mathcal {P}}(A)}）是其成员是 A 的所有可能子集的集合。例如，{1， 2} 的幂集是 { {}， {1}， {2}， {1， 2} }。值得注意的是， P ( A ) {\displaystyle {\mathcal {P}}(A)} 同时包含 A 和空集。
Ontology 本体
Main article: von Neumann universe
An initial segment of the von Neumann hierarchy

A set is pure if all of its members are sets, all members of its members are sets, and so on. For example, the set containing only the empty set is a nonempty pure set. In modern set theory, it is common to restrict attention to the von Neumann universe of pure sets, and many systems of axiomatic set theory are designed to axiomatize the pure sets only. There are many technical advantages to this restriction, and little generality is lost, because essentially all mathematical concepts can be modeled by pure sets. Sets in the von Neumann universe are organized into a cumulative hierarchy, based on how deeply their members, members of members, etc. are nested. Each set in this hierarchy is assigned (by transfinite recursion) an ordinal number α {\displaystyle \alpha }, known as its rank. The rank of a pure set X {\displaystyle X} is defined to be the least ordinal that is strictly greater than the rank of any of its elements. For example, the empty set is assigned rank 0, while the set containing only the empty set is assigned rank 1. For each ordinal α {\displaystyle \alpha }, the set V α {\displaystyle V_{\alpha }} is defined to consist of all pure sets with rank less than α {\displaystyle \alpha }. The entire von Neumann universe is denoted  V {\displaystyle V}.
如果一个集的所有成员都是集，其成员的所有成员都是集，依此类推，则该集是纯集。例如，仅包含空集的集是非空纯集。在现代集合论中，通常将注意力限制在纯集的冯·诺依曼宇宙上，并且许多公理化集合论系统旨在仅将纯集公理化。这个限制有很多技术优势，而且几乎没有失去通用性，因为基本上所有的数学概念都可以用纯集合建模。冯·诺依曼宇宙中的集合根据其成员、成员的成员等的嵌套深度组织成累积层次结构。此层次结构中的每个集合都被分配（通过跨有限递归）一个序数 α {\displaystyle \alpha }，称为其等级。纯集 X {\displaystyle X} 的秩被定义为严格大于其任何元素的秩的最小序数。例如，为空集分配了等级 0，而仅包含空集的集被分配了等级 1。对于每个序数 α {\displaystyle \alpha }，集合 V α {\displaystyle V_{\alpha }} 被定义为由秩小于 α {\displaystyle \alpha } 的所有纯集组成。整个冯·诺依曼宇宙都被表示出来 V {\displaystyle V}。
Formalized set theory
形式化集合论

Elementary set theory can be studied informally and intuitively, and so can be taught in primary schools using Venn diagrams. The intuitive approach tacitly assumes that a set may be formed from the class of all objects satisfying any particular defining condition. This assumption gives rise to paradoxes, the simplest and best known of which are Russell's paradox and the Burali-Forti paradox. Axiomatic set theory was originally devised to rid set theory of such paradoxes.[note 1]
初等集合论可以非正式和直观地学习，因此可以在小学使用维恩图进行教学。直觉方法默认了一个集合，可以从满足任何特定定义条件的所有对象的类中形成。这个假设产生了悖论，其中最简单和最著名的是罗素悖论和 Burali-Forti 悖论。公理集合论最初是为了消除集合论中的此类悖论而设计的。[注 1]

The most widely studied systems of axiomatic set theory imply that all sets form a cumulative hierarchy.[b] Such systems come in two flavors, those whose ontology consists of:
研究最广泛的公理集合论系统意味着所有集合都形成一个累积层次结构。[b] 这样的系统有两种类型，其本体包括：

    Sets alone. This includes the most common axiomatic set theory, Zermelo–Fraenkel set theory with the axiom of choice (ZFC). Fragments of ZFC include:
        Zermelo set theory, which replaces the axiom schema of replacement with that of separation;
        Zermelo 集合论，它用分离的公理模式代替了替换的公理模式;
        General set theory, a small fragment of Zermelo set theory sufficient for the Peano axioms and finite sets;
        广义集合论，Zermelo 集合论的一小段，足以满足 Peano 公理和有限集的要求;
        Kripke–Platek set theory, which omits the axioms of infinity, powerset, and choice, and weakens the axiom schemata of separation and replacement.
        Kripke-Platek 集合论，它省略了无穷大、幂集和选择的公理，并削弱了分离和替换的公理图式。
    Sets and proper classes. These include Von Neumann–Bernays–Gödel set theory, which has the same strength as ZFC for theorems about sets alone, and Morse–Kelley set theory and Tarski–Grothendieck set theory, both of which are stronger than ZFC.
    集合和适当的类。这些理论包括 Von Neumann-Bernays-Gödel 集合论，对于单独的集合定理，它与 ZFC 具有相同的强度，以及 Morse-Kelley 集合论和 Tarski-Grothendieck 集合论，两者都比 ZFC 更强大。

The above systems can be modified to allow urelements, objects that can be members of sets but that are not themselves sets and do not have any members.
可以修改上述系统以允许 urelements，这些对象可以是 sets 的成员，但本身不是 sets 并且没有任何成员。

The New Foundations systems of NFU (allowing urelements) and NF (lacking them), associate with Willard Van Orman Quine, are not based on a cumulative hierarchy. NF and NFU include a "set of everything", relative to which every set has a complement. In these systems urelements matter, because NF, but not NFU, produces sets for which the axiom of choice does not hold. Despite NF's ontology not reflecting the traditional cumulative hierarchy and violating well-foundedness, Thomas Forster has argued that it does reflect an iterative conception of set.[12]
与 Willard Van Orman Quine 相关的 NFU（允许 urelements）和 NF（缺少它们）的新基础系统并不是基于累积层次结构的。NF 和 NFU 包括一个 “万物的集合”，相对于它，每个集合都有一个补码。在这些系统中，urelements 很重要，因为 NF 而不是 NFU 产生的集合的选择公理不成立。尽管 NF 的本体论没有反映传统的累积层次结构并且违背了有根据的，但托马斯·福斯特 （Thomas Forster） 认为它确实反映了集合的迭代概念。[12]

Systems of constructive set theory, such as CST, CZF, and IZF, embed their set axioms in intuitionistic instead of classical logic. Yet other systems accept classical logic but feature a nonstandard membership relation. These include rough set theory and fuzzy set theory, in which the value of an atomic formula embodying the membership relation is not simply True or False. The Boolean-valued models of ZFC are a related subject.
构造集合论系统，例如 CST、CZF 和 IZF，将其集合公理嵌入到直觉而不是经典逻辑中。然而，其他系统接受经典逻辑，但具有非标准的成员关系。这些包括粗糙集论和模糊集论，其中体现隶属关系的原子公式的值不仅仅是 True 或 False。ZFC 的布尔值模型是一个相关的主题。

An enrichment of ZFC called internal set theory was proposed by Edward Nelson in 1977.[13]
Edward Nelson 于 1977 年提出了一种称为内部集合论的 ZFC 丰富化。[13]
Applications 应用

Many mathematical concepts can be defined precisely using only set theoretic concepts. For example, mathematical structures as diverse as graphs, manifolds, rings, vector spaces, and relational algebras can all be defined as sets satisfying various (axiomatic) properties. Equivalence and order relations are ubiquitous in mathematics, and the theory of mathematical relations can be described in set theory.[14][15]
许多数学概念可以仅使用集合论概念来精确定义。例如，图、流形、环、向量空间和关系代数等各种数学结构都可以定义为满足各种（公理）属性的集合。等价关系和顺序关系在数学中无处不在，数学关系理论可以用集合论来描述。[14][15]

Set theory is also a promising foundational system for much of mathematics. Since the publication of the first volume of Principia Mathematica, it has been claimed that most (or even all) mathematical theorems can be derived using an aptly designed set of axioms for set theory, augmented with many definitions, using first or second-order logic. For example, properties of the natural and real numbers can be derived within set theory, as each of these number systems can be defined by representing their elements as sets of specific forms.[16]
集合论也是许多数学的一个有前途的基础系统。自《数学原理》第一卷出版以来，人们声称大多数（甚至所有）数学定理都可以使用一组适当设计的集合论公理推导出来，并使用一阶或二阶逻辑通过许多定义进行增强。例如，自然数和实数的属性可以在集合论中推导出来，因为这些数系中的每一个都可以通过将它们的元素表示为特定形式的集合来定义。[16]

Set theory as a foundation for mathematical analysis, topology, abstract algebra, and discrete mathematics is likewise uncontroversial; mathematicians accept (in principle) that theorems in these areas can be derived from the relevant definitions and the axioms of set theory. However, it remains that few full derivations of complex mathematical theorems from set theory have been formally verified, since such formal derivations are often much longer than the natural language proofs mathematicians commonly present. One verification project, Metamath, includes human-written, computer-verified derivations of more than 12,000 theorems starting from ZFC set theory, first-order logic and propositional logic.[17]
集合论作为数学分析、拓扑学、抽象代数和离散数学的基础同样是没有争议的;数学家（原则上）接受这些领域的定理可以从集合论的相关定义和公理中推导出来。然而，从集合论中得到的复杂数学定理的完整推导仍然很少得到正式验证，因为这种形式推导通常比数学家通常提供的自然语言证明要长得多。一个验证项目 Metamath 包括从 ZFC 集合论、一阶逻辑和命题逻辑开始的 12,000 多个定理的人工编写、计算机验证的推导。[17]
Areas of study 研究领域

Set theory is a major area of research in mathematics with many interrelated subfields:
集合论是数学的一个主要研究领域，有许多相互关联的子领域：
Combinatorial set theory
组合集合论
Main article: Infinitary combinatorics

Combinatorial set theory concerns extensions of finite combinatorics to infinite sets. This includes the study of cardinal arithmetic and the study of extensions of Ramsey's theorem such as the Erdős–Rado theorem.
组合集合论涉及有限组合学到无限集的扩展。这包括基数算术的研究和拉姆齐定理的扩展研究，例如 Erdős-Rado 定理。
Descriptive set theory
描述性集合论
Main article: Descriptive set theory

Descriptive set theory is the study of subsets of the real line and, more generally, subsets of Polish spaces. It begins with the study of pointclasses in the Borel hierarchy and extends to the study of more complex hierarchies such as the projective hierarchy and the Wadge hierarchy. Many properties of Borel sets can be established in ZFC, but proving these properties hold for more complicated sets requires additional axioms related to determinacy and large cardinals.
描述性集合论是对实线子集的研究，更一般地说，是对波兰空间子集的研究。它从研究 Borel 层次结构中的点类开始，并扩展到对更复杂的层次结构的研究，例如投影层次结构和 Wadge 层次结构。Borel 集合的许多性质可以在 ZFC 中建立，但要证明这些性质适用于更复杂的集合，需要与确定性和大基数相关的额外公理。

The field of effective descriptive set theory is between set theory and recursion theory. It includes the study of lightface pointclasses, and is closely related to hyperarithmetical theory. In many cases, results of classical descriptive set theory have effective versions; in some cases, new results are obtained by proving the effective version first and then extending ("relativizing") it to make it more broadly applicable.
有效描述性集合论的领域介于集合论和递归论之间。它包括对 lightface 点类的研究，并且与超算术理论密切相关。在许多情况下，经典描述性集合论的结果具有有效的版本;在某些情况下，通过首先证明有效版本，然后扩展（“相对化”）它以使其更广泛地适用，可以获得新的结果。

A recent area of research concerns Borel equivalence relations and more complicated definable equivalence relations. This has important applications to the study of invariants in many fields of mathematics.
最近的一个研究领域涉及 Borel 等价关系和更复杂的可定义等价关系。这对数学许多领域的不变量研究具有重要应用。
Fuzzy set theory 模糊集论
Main article: Fuzzy set theory

In set theory as Cantor defined and Zermelo and Fraenkel axiomatized, an object is either a member of a set or not. In fuzzy set theory this condition was relaxed by Lotfi A. Zadeh so an object has a degree of membership in a set, a number between 0 and 1. For example, the degree of membership of a person in the set of "tall people" is more flexible than a simple yes or no answer and can be a real number such as 0.75.
在 Cantor 定义的集合论以及 Zermelo 和 Fraenkel 公理化的集合论中，对象要么是集合的成员，要么不是集合的成员。在模糊集合论中，Lotfi A. Zadeh 放宽了这个条件，因此对象在集合中具有一定程度的隶属度，即介于 0 和 1 之间的数字。例如，一个人在“高个子”集合中的隶属程度比简单的是或否答案更灵活，并且可以是实数，例如 0.75。
Inner model theory 内部模型理论
Main article: Inner model theory

An inner model of Zermelo–Fraenkel set theory (ZF) is a transitive class that includes all the ordinals and satisfies all the axioms of ZF. The canonical example is the constructible universe L developed by Gödel. One reason that the study of inner models is of interest is that it can be used to prove consistency results. For example, it can be shown that regardless of whether a model V of ZF satisfies the continuum hypothesis or the axiom of choice, the inner model L constructed inside the original model will satisfy both the generalized continuum hypothesis and the axiom of choice. Thus the assumption that ZF is consistent (has at least one model) implies that ZF together with these two principles is consistent.
Zermelo-Fraenkel 集合论 （ZF） 的内部模型是一个及物类，它包括所有序数并满足 ZF 的所有公理。典型的例子是哥德尔开发的可构造宇宙 L。对内部模型的研究感兴趣的一个原因是它可以用来证明一致性结果。例如，可以证明，无论 ZF 的模型 V 是满足连续介质假设还是选择公理，在原始模型内构建的内部模型 L 都将同时满足广义连续介质假设和选择公理。因此，ZF 是一致的（至少有一个模型）的假设意味着 ZF 与这两个原则是一致的。

The study of inner models is common in the study of determinacy and large cardinals, especially when considering axioms such as the axiom of determinacy that contradict the axiom of choice. Even if a fixed model of set theory satisfies the axiom of choice, it is possible for an inner model to fail to satisfy the axiom of choice. For example, the existence of sufficiently large cardinals implies that there is an inner model satisfying the axiom of determinacy (and thus not satisfying the axiom of choice).[18]
在确定性和大基数的研究中，对内部模型的研究很常见，尤其是在考虑与选择公理相矛盾的公理（例如确定性公理）时。即使集合论的固定模型满足选择公理，内部模型也有可能不满足选择公理。例如，足够大的基数的存在意味着存在一个满足确定性公理的内部模型（因此不满足选择公理）。[18]
Large cardinals 大红衣主教
Main article: Large cardinal property

A large cardinal is a cardinal number with an extra property. Many such properties are studied, including inaccessible cardinals, measurable cardinals, and many more. These properties typically imply the cardinal number must be very large, with the existence of a cardinal with the specified property unprovable in Zermelo–Fraenkel set theory.
大基数是具有额外属性的基数。研究了许多这样的属性，包括不可接近的基数、可测量的基数等等。这些性质通常意味着基数必须非常大，具有指定性质的基数的存在在 Zermelo-Fraenkel 集合论中是无法证明的。
Determinacy 确定性
Main article: Determinacy

Determinacy refers to the fact that, under appropriate assumptions, certain two-player games of perfect information are determined from the start in the sense that one player must have a winning strategy. The existence of these strategies has important consequences in descriptive set theory, as the assumption that a broader class of games is determined often implies that a broader class of sets will have a topological property. The axiom of determinacy (AD) is an important object of study; although incompatible with the axiom of choice, AD implies that all subsets of the real line are well behaved (in particular, measurable and with the perfect set property). AD can be used to prove that the Wadge degrees have an elegant structure.
确定性是指这样一个事实，即在适当的假设下，某些具有完美信息的双人游戏从一开始就被确定，即一个玩家必须有一个获胜的策略。这些策略的存在在描述性集合论中具有重要影响，因为确定更广泛的博弈类的假设通常意味着更广泛的集合类将具有拓扑属性。确定性公理 （AD） 是一个重要的研究对象;虽然与选择公理不兼容，但 AD 意味着实线的所有子集都表现良好（特别是，可测量且具有完美的集合属性）。AD 可用于证明 Wadge 度具有优雅的结构。
Forcing 迫使
Main article: Forcing (mathematics)

Paul Cohen invented the method of forcing while searching for a model of ZFC in which the continuum hypothesis fails, or a model of ZF in which the axiom of choice fails. Forcing adjoins to some given model of set theory additional sets in order to create a larger model with properties determined (i.e. "forced") by the construction and the original model. For example, Cohen's construction adjoins additional subsets of the natural numbers without changing any of the cardinal numbers of the original model. Forcing is also one of two methods for proving relative consistency by finitistic methods, the other method being Boolean-valued models.
Paul Cohen 在寻找连续体假设失败的 ZFC 模型或选择公理失败的 ZF 模型时发明了强迫方法。强制与集合论的某些给定模型相邻额外的集合，以便创建一个更大的模型，其属性由构造和原始模型决定（即“强制”）。例如，Cohen 的构造将自然数的其他子集相邻，而不会更改原始模型的任何基数。强制也是通过有限方法证明相对一致性的两种方法之一，另一种方法是布尔值模型。
Cardinal invariants 基数不变量
Main article: Cardinal characteristics of the continuum

A cardinal invariant is a property of the real line measured by a cardinal number. For example, a well-studied invariant is the smallest cardinality of a collection of meagre sets of reals whose union is the entire real line. These are invariants in the sense that any two isomorphic models of set theory must give the same cardinal for each invariant. Many cardinal invariants have been studied, and the relationships between them are often complex and related to axioms of set theory.
基数不变量是由基数测量的实线的属性。例如，经过充分研究的不变量是一组微不足道的实数集的最小基数，其并集是整条实数线。这些是不变量，因为集合论的任意两个同构模型必须为每个不变量给出相同的基数。已经研究了许多基数不变量，它们之间的关系通常很复杂，并且与集合论的公理有关。
Set-theoretic topology
集合论拓扑
Main article: Set-theoretic topology

Set-theoretic topology studies questions of general topology that are set-theoretic in nature or that require advanced methods of set theory for their solution. Many of these theorems are independent of ZFC, requiring stronger axioms for their proof. A famous problem is the normal Moore space question, a question in general topology that was the subject of intense research. The answer to the normal Moore space question was eventually proved to be independent of ZFC.
集合论拓扑学研究一般拓扑学中本质上是集合论的或需要高级集合论方法来解决的问题。这些定理中的许多都是独立于 ZFC 的，需要更强的公理来证明它们。一个著名的问题是普通的摩尔空间问题，这是一般拓扑学中的一个问题，是深入研究的主题。正常摩尔空间问题的答案最终被证明独立于 ZFC。
Controversy 争议
Main article: Controversy over Cantor's theory

From set theory's inception, some mathematicians have objected to it as a foundation for mathematics. The most common objection to set theory, one Kronecker voiced in set theory's earliest years, starts from the constructivist view that mathematics is loosely related to computation. If this view is granted, then the treatment of infinite sets, both in naive and in axiomatic set theory, introduces into mathematics methods and objects that are not computable even in principle. The feasibility of constructivism as a substitute foundation for mathematics was greatly increased by Errett Bishop's influential book Foundations of Constructive Analysis.[19]
从集合论诞生之初，一些数学家就反对将其作为数学的基础。Kronecker 在集合论的早期就提出了对集合论最常见的反对意见，它从建构主义的观点开始，即数学与计算松散相关。如果这种观点是正确的，那么在朴素和公理集合论中对无限集的处理，将即使在原则上也不可计算的方法和对象引入数学。埃雷特·毕晓普 （Errett Bishop） 有影响力的著作《建构分析的基础》（Foundations of Constructive Analysis） 大大提高了建构主义作为数学替代基础的可行性。[19]

A different objection put forth by Henri Poincaré is that defining sets using the axiom schemas of specification and replacement, as well as the axiom of power set, introduces impredicativity, a type of circularity, into the definitions of mathematical objects. The scope of predicatively founded mathematics, while less than that of the commonly accepted Zermelo–Fraenkel theory, is much greater than that of constructive mathematics, to the point that Solomon Feferman has said that "all of scientifically applicable analysis can be developed [using predicative methods]".[20]
亨利·庞加莱 （Henri Poincaré） 提出的另一个反对意见是，使用规范和替换的公理模式以及幂集的公理来定义集合，将不预测性（一种循环性）引入数学对象的定义中。基于预测的数学的范围虽然小于普遍接受的 Zermelo-Fraenkel 理论，但比建设性数学的范围要大得多，以至于所罗门·费弗曼 （Solomon Feferman） 曾说过，“所有科学适用的分析都可以 [使用预测方法] 发展出来”。[20]

Ludwig Wittgenstein condemned set theory philosophically for its connotations of mathematical platonism.[21] He wrote that "set theory is wrong", since it builds on the "nonsense" of fictitious symbolism, has "pernicious idioms", and that it is nonsensical to talk about "all numbers".[22] Wittgenstein identified mathematics with algorithmic human deduction;[23] the need for a secure foundation for mathematics seemed, to him, nonsensical.[24] Moreover, since human effort is necessarily finite, Wittgenstein's philosophy required an ontological commitment to radical constructivism and finitism. Meta-mathematical statements – which, for Wittgenstein, included any statement quantifying over infinite domains, and thus almost all modern set theory – are not mathematics.[25] Few modern philosophers have adopted Wittgenstein's views after a spectacular blunder in Remarks on the Foundations of Mathematics: Wittgenstein attempted to refute Gödel's incompleteness theorems after having only read the abstract. As reviewers Kreisel, Bernays, Dummett, and Goodstein all pointed out, many of his critiques did not apply to the paper in full. Only recently have philosophers such as Crispin Wright begun to rehabilitate Wittgenstein's arguments.[26]
路德维希·维特根斯坦 （Ludwig Wittgenstein） 在哲学上谴责集合论的数学柏拉图主义的内涵。[21]他写道，“集合论是错误的”，因为它建立在虚构象征主义的“荒谬”之上，有“有害的习语”，谈论“所有数字”是荒谬的。[22] 维特根斯坦将数学与算法人类演绎相结合;[23]在他看来，需要一个安全的数学基础似乎是荒谬的。[24]此外，由于人类的努力必然是有限的，维特根斯坦的哲学要求对激进的建构主义和有限主义进行本体论承诺。元数学陈述——对维特根斯坦来说，包括任何在无限域上量化的陈述，因此几乎所有现代集合论——都不是数学。[25]在《数学基础评论》中犯下重大错误后，很少有现代哲学家采纳维特根斯坦的观点：维特根斯坦在只读了摘要后试图反驳哥德尔的不完备性定理。正如评论家 Kreisel、Bernays、Dummett 和 Goodstein 都指出的那样，他的许多批评并不完整篇。直到最近，克里斯平·赖特（Crispin Wright）等哲学家才开始恢复维特根斯坦的论点。[26]

Category theorists have proposed topos theory as an alternative to traditional axiomatic set theory. Topos theory can interpret various alternatives to that theory, such as constructivism, finite set theory, and computable set theory.[27][28] Topoi also give a natural setting for forcing and discussions of the independence of choice from ZF, as well as providing the framework for pointless topology and Stone spaces.[29]
范畴论家提出了 topos 理论作为传统公理集合论的替代方案。Topos 理论可以解释该理论的各种替代方案，例如建构主义、有限集理论和可计算集合论。[27][28] Topoi 还为强制和讨论独立于 ZF 的选择提供了一个自然的背景，并为无意义的拓扑和 Stone 空间提供了框架。[29]

An active area of research is the univalent foundations and related to it homotopy type theory. Within homotopy type theory, a set may be regarded as a homotopy 0-type, with universal properties of sets arising from the inductive and recursive properties of higher inductive types. Principles such as the axiom of choice and the law of the excluded middle can be formulated in a manner corresponding to the classical formulation in set theory or perhaps in a spectrum of distinct ways unique to type theory. Some of these principles may be proven to be a consequence of other principles. The variety of formulations of these axiomatic principles allows for a detailed analysis of the formulations required in order to derive various mathematical results.[30][31]
一个活跃的研究领域是单价基础和与之相关的同伦型理论。在同伦类型理论中，集合可以被视为同伦 0 型，集合的普遍性质源于更高归纳类型的归纳和递归性质。诸如选择公理和排除中间定律等原则可以以与集合论中的经典表述相对应的方式表述，或者可能以类型论独有的一系列不同方式来表述。其中一些原则可能被证明是其他原则的结果。这些公理原理的表述多种多样，可以对得出各种数学结果所需的公式进行详细分析。[30][31]