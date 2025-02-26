# Class (set theory) 类（集合论）

In set theory and its applications throughout mathematics, a class is a collection of sets (or sometimes other mathematical objects) that can be unambiguously defined by a property that all its members share. Classes act as a way to have set-like collections while differing from sets so as to avoid paradoxes, especially Russell's paradox (see § Paradoxes). The precise definition of "class" depends on foundational context. In work on Zermelo–Fraenkel set theory, the notion of class is informal, whereas other set theories, such as von Neumann–Bernays–Gödel set theory, axiomatize the notion of "proper class", e.g., as entities that are not members of another entity.
在集合论及其在整个数学中的应用中，类是集合（有时是其他数学对象）的集合，可以由其所有成员共享的属性明确定义。类充当一种具有类似集合的集合的方式，同时与集合不同，以避免悖论，尤其是罗素悖论（参见 § 悖论）。“类”的准确定义取决于基本上下文。在 Zermelo-Fraenkel 集合论的工作中，类的概念是非正式的，而其他集合论，如冯·诺依曼-伯奈斯-哥德尔集合论，将“适当的类”的概念公理化，例如，作为不是另一个实体成员的实体。

A class that is not a set (informally in Zermelo–Fraenkel) is called a proper class, and a class that is a set is sometimes called a small class. For instance, the class of all ordinal numbers, and the class of all sets, are proper classes in many formal systems.
不是集合的类（在 Zermelo-Fraenkel 中非正式地称为 Proper 类），而作为集合的类有时称为小类。例如，所有序数的类和所有集合的类，在许多正式系统中都是适当的类。

In Quine's set-theoretical writing, the phrase "ultimate class" is often used instead of the phrase "proper class" emphasising that in the systems he considers, certain classes cannot be members, and are thus the final term in any membership chain to which they belong.
在奎因的集合论著作中，经常使用“终极类”一词来代替“适当的类”一词，强调在他所考虑的系统中，某些类不能成为成员，因此是它们所属的任何成员链中的最后一个术语。

Outside set theory, the word "class" is sometimes used synonymously with "set". This usage dates from a historical period where classes and sets were not distinguished as they are in modern set-theoretic terminology.[1] Many discussions of "classes" in the 19th century and earlier are really referring to sets, or rather perhaps take place without considering that certain classes can fail to be sets.[non-primary source needed]
在集合论之外，“class” 一词有时与 “set” 同义使用。这种用法可以追溯到一个历史时期，当时 class 和 sets 并不像现代集合论术语那样被区分。[1] 19 世纪及更早的许多关于“类”的讨论实际上指的是集合，或者更确切地说，也许是在没有考虑某些类可能不是集合的情况下进行的。[需要非主要来源]

## Examples 例子

The collection of all algebraic structures of a given type will usually be a proper class. Examples include the class of all groups, the class of all vector spaces, and many others. In category theory, a category whose collection of objects forms a proper class (or whose collection of morphisms forms a proper class) is called a large category.
给定类型的所有代数结构的集合通常是一个合适的类。示例包括 all groups 的 class、all vector spaces 的 class 等等。在范畴论中，其对象集合形成适当类（或其形态集合形成适当类）的类别称为大类别。

The surreal numbers are a proper class of objects that have the properties of a fieldi.
超实数是一类具有字段属性的适当对象。

Within set theory, many collections of sets turn out to be proper classes. Examples include the class of all sets (the universal class), the class of all ordinal numbers, and the class of all cardinal numbers.
在集合论中，许多集合被证明是合适的类。示例包括所有集合的类 （通用类） 、所有序数的类和所有基数的类。

One way to prove that a class is proper is to place it in bijection with the class of all ordinal numbers. This method is used, for example, in the proof that there is no free complete lattice on three or more generators.
证明一个类是正确的一种方法是将其与所有序数的类放在双射中。例如，这种方法用于证明三个或更多发电机上没有自由完全晶格。

## Paradoxes 悖论

The paradoxes of naive set theory can be explained in terms of the inconsistent tacit assumption that "all classes are sets". With a rigorous foundation, these paradoxes instead suggest proofs that certain classes are proper (i.e., that they are not sets). For example, Russell's paradox suggests a proof that the class of all sets which do not contain themselves is proper, and the Burali-Forti paradox suggests that the class of all ordinal numbers is proper. The paradoxes do not arise with classes because there is no notion of classes containing classes. Otherwise, one could, for example, define a class of all classes that do not contain themselves, which would lead to a Russell paradox for classes. A conglomerate, on the other hand, can have proper classes as members.[2]
朴素集合论的悖论可以用“所有类都是集合”的不一致默认假设来解释。在严格的基础下，这些悖论反而提出了某些类是正确的证明（即，它们不是集合）。例如，罗素悖论证明了所有不包含自身的集合的类都是正确的，而 Burali-Forti 悖论表明所有序数的类都是正确的。悖论不会出现在类中，因为没有包含类的类的概念。否则，例如，可以定义一个包含所有不包含自身的类的类，这将导致类的罗素悖论。另一方面，企业集团可以有适当的类作为成员。[2]

## Classes in formal set theories 形式集合论中的类

ZF set theory does not formalize the notion of classes, so each formula with classes must be reduced syntactically to a formula without classes.[3] For example, one can reduce the formula A = { x ∣ x = x } {\displaystyle A=\{x\mid x=x\}} to ∀ x ( x ∈ A ↔ x = x ) {\displaystyle \forall x(x\in A\leftrightarrow x=x)}. For a class A {\displaystyle A} and a set variable symbol x {\displaystyle x}, it is necessary to be able to expand each of the formulas x ∈ A {\displaystyle x\in A}, x = A {\displaystyle x=A}, A ∈ x {\displaystyle A\in x}, and A = x {\displaystyle A=x} into a formula without an occurrence of a class.[4]p. 339
ZF 集合论没有正式化类的概念，因此每个带有类的公式都必须在语法上简化为没有类的公式。 x {\displaystyle x} 例如，可以将公式 A = { x ∣ x = x } {\displaystyle A=\{x\mid x=x\}} 简化为 ∀ x ( x ∈ A ↔ x = x ) {\displaystyle \forall x(x\in A\leftrightarrow x=x)}。对于类 A {\displaystyle A} 和集合变量符号 x {\displaystyle x}，必须能够将每个公式 x ∈ A {\displaystyle x\in A}、 x = A {\displaystyle x=A}、 A ∈ x {\displaystyle A\in x} 和 A = x {\displaystyle A=x} 扩展为一个公式，而不出现类。 x ∈ A {\displaystyle x\in A}第 339 页

Semantically, in a metalanguage, the classes can be described as equivalence classes of logical formulas: If A {\displaystyle {\mathcal {A}}} is a structure interpreting ZF, then the object language "class-builder expression" { x ∣ ϕ } {\displaystyle \{x\mid \phi \}} is interpreted in A {\displaystyle {\mathcal {A}}} by the collection of all the elements from the domain of A {\displaystyle {\mathcal {A}}} on which λ x ϕ {\displaystyle \lambda x\phi } holds; thus, the class can be described as the set of all predicates equivalent to ϕ {\displaystyle \phi } (which includes ϕ {\displaystyle \phi } itself). In particular, one can identify the "class of all sets" with the set of all predicates equivalent to x = x {\displaystyle x=x}.[citation needed]
从语义上讲，在元语言中，类可以被描述为逻辑公式的等价类：如果 A {\displaystyle {\mathcal {A}}} 是解释 ZF 的结构，那么对象语言“类构建器表达式” { x ∣ ϕ } {\displaystyle \{x\mid \phi \}} 在 A {\displaystyle {\mathcal {A}}} 中由来自 A {\displaystyle {\mathcal {A}}} 的域的所有元素的集合来解释 λ x ϕ {\displaystyle \lambda x\phi };因此，该类可以描述为等效于 ϕ {\displaystyle \phi } 的所有谓词的集合（包括 ϕ {\displaystyle \phi } 本身）。特别是，可以用等价于 x = x {\displaystyle x=x} 的所有谓词的集合来识别“所有集合的类”。[来源请求]

Because classes do not have any formal status in the theory of ZF, the axioms of ZF do not immediately apply to classes. However, if an inaccessible cardinal κ {\displaystyle \kappa } is assumed, then the sets of smaller rank form a model of ZF (a Grothendieck universe), and its subsets can be thought of as "classes".
因为类在 ZF 理论中没有任何正式的地位，所以 ZF 的公理并不立即适用于类。但是，如果假设一个不可访问的基数 κ {\displaystyle \kappa }，那么较小秩的集合形成一个 ZF 模型（一个 Grothendieck 宇宙），它的子集可以被认为是 “类”。

In ZF, the concept of a function can also be generalised to classes. A class function is not a function in the usual sense, since it is not a set; it is rather a formula Φ ( x , y ) {\displaystyle \Phi (x,y)} with the property that for any set x {\displaystyle x} there is no more than one set y {\displaystyle y} such that the pair ( x , y ) {\displaystyle (x,y)} satisfies Φ {\displaystyle \Phi }. For example, the class function mapping each set to its powerset may be expressed as the formula y = P ( x ) {\displaystyle y={\mathcal {P}}(x)}. The fact that the ordered pair ( x , y ) {\displaystyle (x,y)} satisfies Φ {\displaystyle \Phi } may be expressed with the shorthand notation Φ ( x ) = y {\displaystyle \Phi (x)=y}.
在 ZF 中，函数的概念也可以推广到类。类函数不是通常意义上的函数，因为它不是集合;它是一个公式 Φ ( x , y ) {\displaystyle \Phi (x,y)}，其属性是对于任何集合 x {\displaystyle x} ，只有一个集合 y {\displaystyle y} 使得对 ( x , y ) {\displaystyle (x,y)} 满足 Φ {\displaystyle \Phi }。例如，将每个集合映射到其幂集的类函数可以表示为公式 y = P ( x ) {\displaystyle y={\mathcal {P}}(x)}。有序对 ( x , y ) {\displaystyle (x,y)} 满足 Φ {\displaystyle \Phi } 的事实可以用速记符号 Φ ( x ) = y {\displaystyle \Phi (x)=y} 来表示。

Another approach is taken by the von Neumann–Bernays–Gödel axioms (NBG); classes are the basic objects in this theory, and a set is then defined to be a class that is an element of some other class. However, the class existence axioms of NBG are restricted so that they only quantify over sets, rather than over all classes. This causes NBG to be a conservative extension of ZFC.
另一种方法是冯·诺依曼-伯奈斯-哥德尔公理 （NBG）;类是这个理论中的基本对象，然后一个集合被定义为一个类，该类是其他类的元素。但是，NBG 的类存在公理受到限制，因此它们仅在集合上量化，而不是在所有类上量化。这导致 NBG 成为 ZFC 的保守扩展。

Morse–Kelley set theory admits proper classes as basic objects, like NBG, but also allows quantification over all proper classes in its class existence axioms. This causes MK to be strictly stronger than both NBG and ZFC.
Morse-Kelley 集合论承认适当的类是基本对象，如 NBG，但也允许对其类存在公理中的所有适当的类进行量化。这导致 MK 严格强于 NBG 和 ZFC。

In other set theories, such as New Foundations or the theory of semisets, the concept of "proper class" still makes sense (not all classes are sets) but the criterion of sethood is not closed under subsets. For example, any set theory with a universal set has proper classes which are subclasses of sets.
在其他集合论中，例如新基础或半集合理论，“适当类”的概念仍然有意义（并非所有类都是集合），但集合性的标准并不封闭在子集下。例如，任何具有通用集的集合论都有适当的类，这些类是集合的子类。
