# 本体论

## 目的

An ontology serves to define a common vocabulary for a specific domain, enabling knowledge sharing and understanding among people or software agents. It helps in organizing information, facilitating data interoperability, and supporting the reuse of domain knowledge.
本体用于定义特定领域的通用词汇表，使人们或软件代理之间能够共享和理解知识。它有助于组织信息、促进数据互作性并支持域知识的重用。

## 信息科学中的本体论
在信息科学中，本体包括与一个、多个或所有话语领域相关的概念、数据或实体之间的类别、属性和关系的表示、正式命名和定义。更简单地说，本体是一种显示主题区域属性及其关系方式的方法，通过定义一组表示该主题区域中的实体的术语和关系表达式。研究如此构想的本体论的领域有时被称为应用本体论。
### 分支

#### 形式本体（Formal Ontology）

自 1970 年代中期以来，人工智能 （AI） 领域的研究人员已经认识到，知识工程是构建大型和强大 AI 系统的关键。AI 研究人员认为，他们可以创建新的本体作为计算模型，以实现某些类型的自动推理，但这只是微不足道的成功。在 1980 年代，AI 社区开始使用术语本体论来指代建模世界的理论和基于知识的系统的一个组成部分。特别是，David Powers 将本体论一词引入 AI 以指代现实世界或机器人接地，在 1990 年发表了文献综述，强调接地本体论，并与 AAAI 自然语言和本体的机器学习夏季研讨会的论文征集有关，扩展版本发表在 SIGART Bulletin 上，并作为会议记录的序言。一些研究人员从哲学本体论中汲取灵感，将计算本体论视为一种应用哲学。

形式本体（Formal Ontology）是本体论的一个分支，它研究了实体在逻辑、语义和语法中的表示形式。

 In 1993, the widely cited web page and paper "Toward Principles for the Design of Ontologies Used for Knowledge Sharing" by Tom Gruber[16] used ontology as a technical term in computer science closely related to earlier idea of semantic networks and taxonomies. Gruber introduced the term as a specification of a conceptualization:
1993 年，被广泛引用的网页和论文 “Towards Principles for the Design of Ontologies Used for Knowledge Sharing”[16] 将本体论用作计算机科学中的技术术语，与语义网络和分类法的早期概念密切相关。Gruber 将这个术语作为概念化的规范引入：

    An ontology is a description (like a formal specification of a program) of the concepts and relationships that can formally exist for an agent or a community of agents. This definition is consistent with the usage of ontology as set of concept definitions, but more general. And it is a different sense of the word than its use in philosophy.[17]
    本体是对代理或代理群体可以正式存在的概念和关系的描述（就像程序的正式规范一样）。此定义与将本体论作为一组概念定义一致，但更为通用。这个词的含义与它在哲学中的用法不同。[17]

Attempting to distance ontologies from taxonomies and similar efforts in knowledge modeling that rely on classes and inheritance, Gruber stated (1993):
Gruber 试图将本体与依赖于类和继承的分类法和知识建模中的类似工作区分开来，Gruber 说（1993）：

    Ontologies are often equated with taxonomic hierarchies of classes, class definitions, and the subsumption relation, but ontologies need not be limited to these forms. Ontologies are also not limited to conservative definitions, that is, definitions in the traditional logic sense that only introduce terminology and do not add any knowledge about the world (Enderton, 1972). To specify a conceptualization, one needs to state axioms that do constrain the possible interpretations for the defined terms.
    本体论通常等同于类的分类层次结构、类定义和归纳关系，但本体论不必局限于这些形式。本体论也不限于保守的定义，即传统逻辑意义上的定义，它们只引入术语，不添加任何关于世界的知识（Enderton， 1972）。要指定概念化，需要陈述确实限制了定义术语的可能解释的公理。
    本体论通常被等同于类的分类层次结构、类定义和包含关系，但本体论并不局限于这些形式。本体论也不限于保守定义，即传统逻辑意义上的定义，它们只引入术语而不添加关于世界的知识（Enderton, 1972）。要指定概念化，需要陈述限制定义术语的可能解释的公理。

As refinement of Gruber's definition Feilmayr and Wöß (2016) stated: "An ontology is a formal, explicit specification of a shared conceptualization that is characterized by high semantic expressiveness required for increased complexity."
作为对 Gruber 定义的改进，Feilmayr 和 Wöß (2016) 指出：“本体是对共享概念化的正式、明确规范，其特征是增加复杂性所需的高语义表达性。”

####  Basic Formal Ontology (BFO) 基本形式本体

BFO is a top-level ontology developed by Barry Smith and his associates for the purposes of promoting interoperability among domain ontologies built in its terms through a process of downward population. A guide to building BFO-conformant domain ontologies was published by MIT Press in 2015.[1]
基本形式本体 （BFO） 是由 Barry Smith 和他的同事开发的顶级本体，旨在通过向下填充的过程促进以其术语构建的领域本体之间的互作性。MIT Press 于 2015 年出版了构建符合 BFO 的域本体的指南。[1]

The ontology arose against the background of research in ontologies in the domain of geospatial information science by David Mark, Pierre Grenon, Achille Varzi and others,[2] with a special role for the study of vagueness and of the ways sharp boundaries in the geospatial and other domains are created by fiat.[3][4]
本体论是在 David Mark、Pierre Grenon、Achille Varzi 等人对地理空间信息科学领域本体论的研究背景下出现的，[2] 在研究模糊性以及地理空间和其他领域中锐利边界是如何由法定创造的。[3][4]

BFO has passed through four major releases.[5] The current revision was released in 2020,[6] and this forms the basis of the standard ISO/IEC 21838-2,[7] which was released by the Joint Committee of the International Standards Organization and International Electrotechnical Commission in 2021.[8]
BFO 已经经历了四个主要版本。[5]当前修订版于 2020 年发布，[6]这构成了国际标准组织和国际电工委员会联合委员会于 2021 年发布的标准 ISO/IEC 21838-2 的基础，[7]。[8]

The structure of BFO is based on a division of entities into two disjoint categories of continuant and occurrent, the former consists of objects and spatial regions, the latter contains processes conceived as extended through (or spanning) time. BFO thereby seeks to consolidate both time and space within a single framework.
BFO 的结构基于将实体分为连续和连续两个不相交的类别，前者由对象和空间区域组成，后者包含被认为通过（或跨越）时间延伸的过程。因此，BFO 寻求将时间和空间整合到一个框架中。


### 组件

当代本体论具有许多结构上的相似性，无论它们以何种语言表达。大多数本体描述个体（实例）、类（概念）、属性和关系。

Types 类型Domain ontology 域本体

A domain ontology (or domain-specific ontology) represents concepts which belong to a realm of the world, such as biology or politics. Each domain ontology typically models domain-specific definitions of terms. For example, the word card has many different meanings. An ontology about the domain of poker would model the "playing card" meaning of the word, while an ontology about the domain of computer hardware would model the "punched card" and "video card" meanings.
领域本体论（或特定领域的本体论）表示属于世界某个领域的概念，例如生物学或政治学。每个领域本体通常对术语的特定领域定义进行建模。例如，单词 card 有许多不同的含义。关于扑克领域的本体将模拟单词的“扑克牌”含义，而关于计算机硬件领域的本体将模拟“穿孔牌”和“视频卡”的含义。

Since domain ontologies are written by different people, they represent concepts in very specific and unique ways, and are often incompatible within the same project. As systems that rely on domain ontologies expand, they often need to merge domain ontologies by hand-tuning each entity or using a combination of software merging and hand-tuning. This presents a challenge to the ontology designer. Different ontologies in the same domain arise due to different languages, different intended usage of the ontologies, and different perceptions of the domain (based on cultural background, education, ideology, etc.)[citation needed].
由于领域本体是由不同的人编写的，因此它们以非常具体和独特的方式表示概念，并且通常在同一项目中不兼容。随着依赖领域本体的系统的扩展，它们通常需要通过手动调整每个实体或使用软件合并和手动调整的组合来合并领域本体。这给本体设计人员带来了挑战。由于语言不同、本体的预期用途不同以及对领域的看法不同（基于文化背景、教育、意识形态等），同一领域中会出现不同的本体。
由于领域本体由不同的人编写，因此它们以特定且独特的方式表示概念，通常在同一项目中不兼容。随着系统扩展，常常需要手动调整每个实体或结合软件合并与手动调整来合并这些本体。这对本体设计人员提出了挑战。
由于语言不同、本体的预期用途不同以及对领域的看法不同（基于文化背景、教育、意识形态等），同一领域中会出现不同的本体。

At present, merging ontologies that are not developed from a common upper ontology is a largely manual process and therefore time-consuming and expensive. Domain ontologies that use the same upper ontology to provide a set of basic elements with which to specify the meanings of the domain ontology entities can be merged with less effort. There are studies on generalized techniques for merging ontologies,[19] but this area of research is still ongoing, and it is a recent event to see the issue sidestepped by having multiple domain ontologies using the same upper ontology like the OBO Foundry.
目前，合并不是从通用的上层本体发展而来的本体在很大程度上是一个手动过程，因此既费时又昂贵。使用相同的上层本体来提供一组基本元素来指定领域本体实体含义的领域本体可以毫不费力地进行合并。有关于合并本体论的广义技术的研究，[19]但这一领域的研究仍在进行中，并且最近发生的一个事件是，通过让多个领域本体使用与 OBO Foundry 相同的上层本体来回避这个问题。
目前，合并不是从通用的上层本体发展而来的本体在很大程度上是一个手动过程，因此既费时又昂贵。使用相同上层本体的领域本体可以更轻松地合并。尽管有广义技术的研究，这一领域的研究仍在进行中。最近，OBO Foundry 提供了一种解决方案，通过让多个领域本体使用相同的上层本体来回避合并问题。


Contemporary ontologies share many structural similarities, regardless of the ontology language in which they are expressed. Most ontologies describe individuals (instances), classes (concepts), attributes, and relations.
当代本体论具有许多结构上的相似性，无论它们以何种本体语言表达。大多数本体描述个体（实例）、类（概念）、属性和关系。
List

Common components of ontologies include:
本体的常见组件包括：

Individuals
    instances or objects (the basic or "ground level" objects; the tokens).
    实例或对象（基本或“底层”对象;标记）。
Classes
    sets, collections, concepts, types of objects, or kinds of things.[1]
    集合、集合、概念、对象类型或各种事物。[1]
Attributes
    aspects, properties, features, characteristics, or parameters that individuals (and classes and relations) can have. [2]
    个人（以及类和关系）可以具有的方面、属性、特征、特征或参数。[2]
Relations
    ways in which classes and individuals can be related to one another. Relations can carry attributes that specify the relation further.[3]
    类和个人可以相互关联的方式。关系可以携带进一步指定关系的属性。[3]
Function terms
    complex structures formed from certain relations that can be used in place of an individual term in a statement.
    由某些关系组成的复杂结构，可用于代替语句中的单个术语。
Restrictions
    formally stated descriptions of what must be true in order for some assertion to be accepted as input.
    正式陈述了必须为真的描述，才能接受某些断言作为输入。
Rules
    statements in the form of an if-then (antecedent-consequent) sentence that describe the logical inferences that can be drawn from an assertion in a particular form.
    if-then（前因）句子形式的陈述，描述可从特定形式的断言中得出的逻辑推理。
Axioms
    assertions (including rules) in a logical form that together comprise the overall theory that the ontology describes in its domain of application.[4] This definition differs from that of "axioms" in generative grammar and formal logic. In these disciplines, axioms include only statements asserted as a priori knowledge. As used here, "axioms" also include the theory derived from axiomatic statements.[citation needed]
    逻辑形式的断言（包括规则），它们共同构成了本体在其应用领域中描述的整体理论。[4] 这个定义在生成语法和形式逻辑上与“公理”不同。在这些学科中，公理仅包括断言为先验知识的陈述。这里使用的“公理”还包括从公理陈述中得出的理论。[来源请求]
Events
    the changing of attributes or relations.
    属性或关系的更改。
Actions
    types of events. 事件类型。

Ontologies are commonly encoded using ontology languages.
本体通常使用本体语言进行编码。

## 哲学中的本体论
本体论是对存在的哲学研究。传统上，它被理解为形而上学的一个分支学科，专注于现实的最普遍特征。作为最基本的概念之一，存在包括所有现实及其中的每个实体。为了阐明存在的基本结构，本体论考察了所有事物之间的共性，并研究了它们被分类为基本类型，例如特殊性和普遍性的类别。Particulars 是唯一的、不可重复的实体，例如苏格拉底这个人，而普遍性是一般的、可重复的实体，例如绿色。存在于空间和时间中的具体对象（如树）与存在于空间和时间之外的抽象对象（如数字 7）之间存在另一个区别。类别系统旨在通过采用物质、属性、关系、事态和事件等类别来提供现实的全面清单。

本体论是哲学的一个分支，与形而上学、认识论和语言哲学等领域相交，因为它考虑了知识、语言和感知与现实本质的关系。形而上学处理诸如“存在什么”和“现实的本质是什么”等问题。形而上学是哲学的五个传统分支之一，它关注通过属性、实体和关系来探索存在，例如特殊与普遍、内在和外在属性或本质与存在之间的关系。自历史记载以来，形而上学一直是持续讨论的话题。

## 共通
信息科学和哲学中的本体论的共同点是试图根据一个范畴系统来表示实体，包括对象和事件，以及它们所有相互依存的属性和关系。在这两个领域，都有大量关于本体工程问题的工作（例如，哲学中的 Quine 和 Kripke，信息科学中的 Sowa 和 Guarino），[5] 以及关于规范本体在多大程度上可能的辩论（例如，哲学中的基础主义和连贯主义，人工智能中的 BFO 和 Cyc）。

## Upper ontology(上层本体)

### 上层本体（Upper Ontology）

在信息科学中，上层本体（也称为顶级本体、上层模型或基础本体）是一种本体，它由在所有领域中通用的非常笼统的术语（例如“对象”、“属性”、“关系”）组成。上层本体的一个重要功能是通过为定义的制定提供一个共同的起点，支持大量特定于领域的本体之间的广泛语义互作性。领域本体中的术语排在上层本体中的术语下，例如，上层本体类是领域本体中所有类的超类或超集。

已经提出了许多上层本体论，每个本体都有自己的支持者。图书馆分类系统早于上层本体系统。尽管图书馆分类使用在所有知识领域中相同的一般概念对知识进行组织和分类，但任何一个系统都不能替代另一个系统。

An upper ontology (or foundation ontology) is a model of the commonly shared relations and objects that are generally applicable across a wide range of domain ontologies. It usually employs a core glossary that overarches the terms and associated object descriptions as they are used in various relevant domain ontologies.
上层本体（或基础本体）是通常适用于广泛领域本体的常见共享关系和对象的模型。它通常使用一个核心词汇表，该词汇表覆盖了在各种相关领域本体中使用的术语和相关对象描述。

Standardized upper ontologies available for use include BFO, BORO method, Dublin Core, GFO, Cyc, SUMO, UMBEL, and DOLCE.[20][21] WordNet has been considered an upper ontology by some and has been used as a linguistic tool for learning domain ontologies.[22]
可供使用的标准化上层本体包括 BFO、BORO 方法、Dublin Core、GFO、Cyc、SUMO、UMBEL 和 DOLCE。[20][21] WordNet 被一些人认为是上层本体，并已被用作学习领域本体的语言工具。[22]
Hybrid ontology 混合本体

The Gellish ontology is an example of a combination of an upper and a domain ontology.
Gellish 本体是上层本体和域本体相结合的一个例子。

本体论者对于哪些实体存在于最基本的层面上存在分歧。柏拉图现实主义断言普遍性具有客观存在，而概念主义则认为普遍性只存在于头脑中，而唯名论则完全否认它们的存在。类似的争论涉及数学对象、科学理论假设的不可观察对象和道德事实。唯物主义认为从根本上说只有物质存在，而二元论则认为心灵和物质是独立的原则。根据一些本体论者的说法，本体论问题的客观答案并不存在，其观点是由不同的语言实践塑造的。