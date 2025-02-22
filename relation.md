# Relations 关系

Relations (also known as relationships) between objects in an ontology specify how objects are related to other objects. Typically a relation is of a particular type (or class) that specifies in what sense the object is related to the other object in the ontology. For example, in the ontology that contains the concept Ford Explorer and the concept Ford Bronco might be related by a relation of type ⟨is defined as a successor of⟩. The full expression of that fact then becomes:
本体中对象之间的关系（也称为关系）指定对象与其他对象的关系。通常，关系属于特定类型（或类），它指定对象与本体中的其他对象在何种意义上相关。例如，在包含概念 Ford Explorer 和概念 Ford Bronco 的本体中，可以通过 ⟨定义为 ⟩ 的后继者“类型的关系进行关联。该事实的完整表达就变成了：

    Ford Explorer is defined as a successor of : Ford Bronco
    Ford Explorer 被定义为以下的继任者：Ford Bronco

This tells us that the Explorer is the model that replaced the Bronco. This example also illustrates that the relation has a direction of expression. The inverse expression expresses the same fact, but with a reverse phrase in natural language.
这告诉我们 Explorer 是取代 Bronco 的车型。此示例还说明了关系具有 expression 方向。反向表达式表示相同的事实，但在自然语言中使用反向短语。

Much of the power of ontologies comes from the ability to describe relations. Together, the set of relations describes the semantics of the domain: that is, its various semantic relations, such as synonymy, hyponymy and hypernymy, coordinate relation, and others. The set of used relation types (classes of relations) and their subsumption hierarchy describe the expression power of the language in which the ontology is expressed.
本体论的大部分力量来自描述关系的能力。这组关系共同描述了域的语义：即它的各种语义关系，例如同义词、下位词和上位词、坐标关系等。使用的关系类型集（关系类）及其包含层次结构描述了表达本体的语言的表达能力。
Ford Explorer is-a-subclass-of 4-Wheel Drive Car, which in turn is-a-subclass-of Car.

An important type of relation is the subsumption relation (is-a-superclass-of, the converse of is-a, is-a-subtype-of or is-a-subclass-of). This defines which objects are classified by which class. For example, we have already seen that the class Ford Explorer is-a-subclass-of 4-Wheel Drive Car, which in turn is-a-subclass-of Car.
一种重要的关系类型是归纳关系（is-a-superclass-of，与 is-a、is-a-subtype-of 或 is-a-subclass-of 相反）。这定义了哪些对象按哪个类进行分类。例如，我们已经看到 Ford Explorer 类是 4-Wheel Drive Car 的子类，而 4-Wheel Drive Car 又是 Car 的子类。

The addition of the is-a-subclass-of relationships creates a taxonomy; a tree-like structure (or, more generally, a partially ordered set) that clearly depicts how objects relate to one another. In such a structure, each object is the 'child' of a 'parent class' (Some languages restrict the is-a-subclass-of relationship to one parent for all nodes, but many do not).
添加 is-a-subclass-of 关系将创建一个分类法;一个树状结构（或者更一般地说，部分有序的集合），清楚地描述了对象如何相互关联。在这样的结构中，每个对象都是 'parent class' 的 'child' （一些语言将所有节点的 is-a-subclass-of 关系限制为一个父节点，但许多语言则不这样做）。

Another common type of relations is the mereology relation, written as part-of, that represents how objects combine to form composite objects. For example, if we extended our example ontology to include concepts like Steering Wheel, we would say that a "Steering Wheel is-by-definition-a-part-of-a Ford Explorer" since a steering wheel is always one of the components of a Ford Explorer. If we introduce meronymy relationships to our ontology, the hierarchy that emerges is no longer able to be held in a simple tree-like structure since now members can appear under more than one parent or branch. Instead this new structure that emerges is known as a directed acyclic graph.
另一种常见的关系类型是 mereology relation，它写为 part-of，它表示对象如何组合形成复合对象。例如，如果我们扩展示例本体以包括 Steering Wheel 等概念，我们会说“根据定义，Steering Wheel 是 Ford Explorer 的一部分”，因为方向盘始终是 Ford Explorer 的组件之一。如果我们将 meronymy 关系引入到我们的本体中，那么出现的层次结构就不再能够以简单的树状结构来保持，因为现在成员可以出现在多个父级或分支下。相反，这种出现的新结构被称为有向无环图。

As well as the standard is-a-subclass-of and is-by-definition-a-part-of-a relations, ontologies often include additional types of relations that further refine the semantics they model. Ontologies might distinguish between different categories of relation types. For example:
除了标准的 is-a-subclass-of 和 is-by-definition-a-part-of-a 关系外，本体通常还包括其他类型的关系，这些关系进一步完善了它们建模的语义。本体可以区分不同类别的关系类型。例如：

    relation types for relations between classes
    类之间关系的 relation types
    relation types for relations between individuals
    个人之间关系的 Relation Types
    relation types for relations between an individual and a class
    个人与类之间的关系
    relation types for relations between a single object and a collection
    关系类型 用于单个对象和集合之间的关系
    relation types for relations between collections
    集合之间关系的 relation types

Relation types are sometimes domain-specific and are then used to store specific kinds of facts or to answer particular types of questions. If the definitions of the relation types are included in an ontology, then the ontology defines its own ontology definition language. An example of an ontology that defines its own relation types and distinguishes between various categories of relation types is the Gellish ontology.
关系类型有时是特定于域的，然后用于存储特定类型的事实或回答特定类型的问题。如果关系类型的定义包含在本体中，则本体定义自己的本体定义语言。定义自己的关系类型并区分各种关系类型的本体论的一个例子是 Gellish 本体论。

For example, in the domain of automobiles, we might need a made-in type relationship which tells us where each car is built. So the Ford Explorer is made-in Louisville. The ontology may also know that Louisville is-located-in Kentucky and Kentucky is-classified-as-a state and is-a-part-of the U.S. Software using this ontology could now answer a question like "which cars are made in the U.S.?"
例如，在汽车领域，我们可能需要一个 made-in 类型的关系，它告诉我们每辆车是在哪里制造的。所以福特探险者是在路易斯维尔制造的。本体可能还知道路易斯维尔位于肯塔基州，而肯塔基州被归类为一个州，并且是美国的一部分。使用此本体的软件现在可以回答诸如“哪些汽车是美国制造的”之类的问题。

---

Relations are ways in which several entities stand to each other. They usually connect distinct entities but some associate an entity with itself. The adicity of a relation is the number of entities it connects. The direction of a relation is the order in which the elements are related to each other. The converse of a relation carries the same information and has the opposite direction, like the contrast between "two is less than five" and "five is greater than two". Both relations and properties express features in reality with a key difference being that relations apply to several entities while properties belong to a single entity.
关系是多个实体相互站立的方式。它们通常连接不同的实体，但有些实体将实体与自身相关联。关系的 adicity 是它连接的实体数。关系的方向是元素彼此相关的顺序。关系的反面携带相同的信息，并且具有相反的方向，例如“2 is less than 5”和“five is greater than two”之间的对比。关系和属性都表示现实中的特征，关键区别在于关系适用于多个实体，而属性属于单个实体。

Many types of relations are discussed in the academic literature. Internal relations, like resemblance, depend only on the monadic properties of the relata. They contrast with external relations, like spatial relations, which express characteristics that go beyond what their relata are like. Formal relations, like identity, involve abstract and topic-neutral ideas while material relations, like loving, have concrete and substantial contents. Logical relations are relations between propositions while causal relations connect concrete events. Symmetric, transitive, and reflexive relations are distinguished by their structural features.
学术文献中讨论了许多类型的关系。内部关系，如相似性，仅取决于 relata 的 monadic 属性。它们与外部关系形成对比，例如空间关系，空间关系所表达的特征超出了它们的相对关系。形式关系，如身份，涉及抽象和主题中立的观念，而物质关系，如爱，具有具体和实质性的内容。逻辑关系是命题之间的关系，而因果关系连接具体事件。对称、传递和反身关系以其结构特征来区分。

Metaphysical difficulties like the question of where relations are located lie at the center of discussions of their ontological status. Eliminativism is the thesis that relations are mental abstractions that are not a part of external reality. A less radical position is reductionism, which claims that relations can be explained in terms of other entities, like monadic properties, and are not a substantial addition to reality. According to realists, relations have a mind-independent existence. A strong form of realism is relationalism, which states that all of reality is relational at its most basic level. Historically, eliminativism and reductionism were the dominant views. This only changed toward the end of the 19th century, when various developments in the fields of mathematics, logic, and science prompted a more realist outlook.
形而上学的困难，如关系位于何处的问题，是讨论其本体论地位的中心。消除论是这样一个论点，即关系是心理抽象，不属于外部现实的一部分。一个不那么激进的立场是还原论，它声称关系可以用其他实体来解释，比如单子属性，而不是对现实的实质性补充。根据现实主义者的说法，关系具有独立于思想的存在。现实主义的一种强大形式是关系主义，它指出所有现实在其最基本的层面上都是关系的。从历史上看，消除论和还原论是占主导地位的观点。这种情况直到 19 世纪末才有所改变，当时数学、逻辑和科学领域的各种发展促使人们产生了更现实主义的观点。

## Definition and essential features 定义和基本特征

A relation is a manner in which multiple entities stand to each other.[1] It is a connection or association between entities and can be understood as a feature characterizing these entities as a whole.[2] Many relations hold between distinct entities. For example, the first-born sibling stands in the relation of being older than to their other siblings. But an entity can also stand in a relation to itself. For instance, every entity stands in the relation of identity to itself.[3] Relations can hold between diverse entities, including objects, people, and concepts.[4] If a relation holds between entities then the relation together with the entities constitutes a fact or state of affairs.[5]
关系是多个实体相互站立的一种方式。[1] 它是实体之间的联系或关联，可以理解为将这些实体作为一个整体来表征的特征。[2] 不同实体之间存在许多关系。例如，长子的兄弟姐妹代表比其他兄弟姐妹年长的关系。但实体也可以存在于与自身的关系中。例如，每个实体都站在身份与自身的关系中。[3] 不同实体（包括对象、人和概念）之间可以建立关系。[4] 如果实体之间存在一种关系，那么该关系与实体一起构成事实或事态。[5]

The word "relationship" is often used as a synonym.[6] The entities related to each other are called the relata.[7] The term "relation" comes from the Latin terms relatio and referre, which mean reference or towardness.[8]
“relationship” 这个词经常被用作同义词。[6] 彼此相关的实体称为 relata。[7] “关系”一词来自拉丁语 relatio 和 referre，意思是参考或向。[8]

In mathematics and logic, relations are defined as set-theoretic structures. For example, the relation less than is defined as the set of all ordered pairs in which the first element is less than the second element. This set includes pairs like [1,2], [1,3], and [2,17].[9] Mathematical functions are a special type of relation in which one or several elements are uniquely associated with exactly one other element.[10]
在数学和逻辑中，关系被定义为集合论结构。例如，小于关系定义为第一个元素小于第二个元素的所有有序对的集合。此集合包括 [1,2]、[1,3] 和 [2,17] 等对。[9] 数学函数是一种特殊类型的关系，其中一个或多个元素与另一个元素唯一关联。[10]

Relations have various characteristic features, like the number of relata they have and the direction in which they connect them.[11] They are closely associated with properties and share several aspects with them.[12]
关系具有各种特征，例如它们拥有的相对关系的数量以及它们连接它们的方向。[11]它们与房产密切相关，并在几个方面与房产共享。[12]

### Adicity 公司

The adicity of a relation is the number of places or relata it has. The terms "arity" and "degree" are used as synonyms. For instance, the relation being larger than has an adicity of two since it involves two entities: a smaller entity and a larger entity. Another example is the relation of being adjacent to. Relations with an adicity of two are called dyadic or binary.[13] Triadic or ternary relations have an adicity of three, like the relation of giving, which involves a giver, a receiver, and a given object. The relation of being between is also triadic since it requires two entities on the sides and one in the middle, as in "5 is between 2 and 23".[14]
关系的 adici 是它所拥有的位数或相对数。术语 “arity” 和 “degree” 用作同义词。例如，关系大于 （is greater than） 的 adicity 为 2，因为它涉及两个实体：一个较小的实体和一个较大的实体。另一个例子是相邻的关系。具有 2 的 adicity 的关系称为二元或二进制。[13] 三元或三元关系具有 3 的 adcity，就像给予的关系一样，它涉及一个给予者、一个接受者和一个给定的对象。存在之间的关系也是三元的，因为它需要两个实体在侧面，一个在中间，就像“5 在 2 和 23 之间”一样。[14]

Unigrade relations are relations that have a fixed adicity: they always apply to the same number of entities. They contrast with multigrade relations, for which the number of their relata varies from one occasion to another.[15] It is controversial whether there are genuine multigrade relations.[16] Some theorists, like David M. Armstrong, argue that the adicity of a relation is an essential feature of it. According to this view, there are no multigrade relations on the fundamental level of reality.[17] However, this view is not generally accepted and some cases of multigrade relations have been suggested. Putative examples include causal relations (which may relate several causes to several effects), logical consequence (which relates several premises to a conclusion they support), and expressions like being the tallest among (for which the adicity depends on the size of the comparison group).[18] Multigrade predicates are also common in everyday language. For instance, the predicate "lift" is dyadic in the sentence "John is lifting a table" and triadic in the sentence "John and Mary are lifting a table". Other examples are predicates that have optional arguments, as in the sentences "John is eating a cake" and "John is eating".[5]
Unigrade 关系是具有固定 adic 的关系：它们始终适用于相同数量的实体。它们与多级关系形成对比，在多级关系中，它们的相对数量因场合而异。[15] 是否存在真正的多级关系是有争议的。[16]一些理论家，如大卫·阿姆斯特朗（David M. Armstrong），认为关系的 adi 性是它的一个基本特征。根据这种观点，在现实的基本层面上不存在多级关系。[17]然而，这种观点并未被普遍接受，并且已经提出了一些多级关系的情况。推定的例子包括因果关系（可能将多个原因与多个结果联系起来）、逻辑结果（将几个前提与它们支持的结论联系起来）和像 being-the tallest among 这样的表达（其 adicity 取决于比较组的大小）。[18] 多级谓词在日常语言中也很常见。例如，谓词 “lift” 在句子 “John is lifting a table” 中是二元的，在句子 “John and Mary are lifting a table” 中是三元的。其他示例是具有可选参数的谓词，如句子 “John is eating a cake” 和 “John is eating”。[5]

### Direction and converse

方向和反向

The direction of a relation is the order in which the elements are related to each other.[19] For instance, if Abelard loves Eloise then the relation of loving goes from Abelard to Eloise. If Eloise loves Abelard then the direction goes in the opposite direction. Both of these facts have the same constituents. They are only distinguished by their direction.[20] Only non-symmetric relations have a direction since the order of the relata does not make a difference for symmetric relations.[21]
关系的方向是元素彼此相关的顺序。[19] 例如，如果阿伯拉尔爱埃洛伊兹，那么爱的关系就是从阿伯拉尔到埃洛伊兹。如果埃洛伊兹爱阿伯拉尔，那么方向就会相反。这两个事实具有相同的成分。他们只是通过他们的方向来区分。[20] 只有非对称关系有方向，因为相对的阶数对对称关系没有影响。[21]

The converse of a non-symmetric relation is a second relation that always accompanies the first relation but has a different order of elements. For example, the converse of above is below. This means that whenever x is above y then y is below x. The same is the case for relations like coming before and coming after as well as being a parent of and being a child of.[22] Binary relations have exactly one converse while tertiary and higher-degree relations have several converses.[16]
非对称关系的反面是第二个关系，它总是伴随着第一个关系，但具有不同的元素顺序。例如，上面的相反情况如下。这意味着只要 x 高于 y，那么 y 就低于 x。对于像 come before 和 come after 以及作为父母和孩子这样的关系也是如此。[22] 二元关系恰好有一个 converse，而三级和更高阶关系有几个 converse。[16]

A relation and its converse carry the same information. For this reason, it is controversial whether they should be considered as two distinct relations instead of seeing them as the same relation.[23] This difficulty has prompted some philosophers to conceptualize the directional aspect of non-symmetric relations differently or to deny the existence of converse relations. According to positionalism, relations do not have a direction but have different unique positions that are filled by their relata.[24] For instance, the relation love has two positions: one for the lover and one for the beloved.[25] This view explains how relata can play different roles in a relation without implying that the relation has a direction or a converse.[26]
关系及其 converse 携带相同的信息。出于这个原因，是否应该将它们视为两个不同的关系而不是将它们视为相同的关系是有争议的。[23]这种困难促使一些哲学家以不同的方式概念化非对称关系的定向方面，或者否认逆向关系的存在。根据位置主义，关系没有方向，但具有不同的独特位置，这些位置由其关系填充。[24] 例如，爱这个关系有两个位置：一个是给爱人的，一个是给被爱的人的。[25] 这种观点解释了 relata 如何在一个关系中扮演不同的角色，而不暗示该关系有一个方向或相反。[26]

### Contrast to properties

与属性对比

Relations are usually contrasted with properties. Properties are held by a single entity and express what this entity is like. Relations connect several entities and are features that apply to them as a whole.[27] A closely associated contrast is that properties belong to entities or inhere in them while relations are not found in the relata but stand between them.[12]
关系通常与属性形成对比。属性由单个实体持有，并表示此实体的外观。关系连接多个实体，并且是作为一个整体应用于它们的特征。[27]一个密切相关的对比是，属性属于实体或存在于实体中，而关系不在相对关系中找到，而是位于它们之间。[12]

However, there are also many parallels between properties and relations and there is no general agreement on a strict dichotomy between the two.[28] Both are often used to describe and explain repeating patterns in the world[12] and many of the ontological distinctions applied to properties also affect relations.[29] For example, both properties and relations may be understood as universals that are instantiated by individuals at a specific place and time. Like properties, relations are either determinable or determinate. Determinable relations are not specified, like the relation of being distant from. Determinate relations are fully specified, like the relation of being exactly one meter distant from.[30]
然而，属性和关系之间也有许多相似之处，并且对于两者之间的严格二分法没有普遍的共识。[28]两者都经常被用来描述和解释世界上的重复模式[12]，许多应用于属性的本体论区别也会影响关系。[29] 例如，属性和关系都可以被理解为由个人在特定地点和时间实例化的普遍性。与属性一样，关系可以是 deterable 或 deterd。没有指定可确定的关系，就像 being distant from 的关系一样。确定关系是完全指定的，例如正好相距一米的关系。[30]

It is possible to conceptualize properties and propositions as special types of relations. According to this view, the difference between these phenomena only concerns how many entities they apply to: regular relations are polyadic and thus apply to several entities; properties are monadic relations and only apply to a single entity; propositions are relations with a degree of zero and do not apply to any entities.[31]
可以将属性和命题概念化为特殊类型的关系。根据这种观点，这些现象之间的区别只在于它们适用于多少个实体：常规关系是多元的，因此适用于多个实体;properties 是 monadic 关系，仅适用于单个实体;命题是度数为零的关系，不适用于任何实体。[31]

The opposite perspective is also possible: to conceptualize relations as polyadic or relational properties.[32] It is usually accepted that relational properties accompany relations: if x stands in a relation to y, then x has the relational property of bearing a relation to y. For example, since Antony was married to Cleopatra, he had the relational property of being married to Cleopatra. However, it is not generally accepted that relations are correctly understood as or can be reduced to relational properties.[16] Historically, properties have received significantly more attention from metaphysicists than relations.[33]
相反的观点也是可能的：将关系概念化为多元或关系属性。[32] 人们通常认为关系属性伴随着关系：如果 x 与 y 处于关系中，那么 x 具有与 y 的关系属性。例如，由于安东尼嫁给了克利奥帕特拉，他具有与克利奥帕特拉结婚的关系属性。然而，人们并不普遍接受关系被正确理解为或可以简化为关系属性。[16]从历史上看，形而上学学家对属性的关注要比关系多得多。[33]

## Types 类型

Various types of relations are distinguished in the academic literature based on their ontological status, the domains they apply to, and the structures they form.[34]
在学术文献中，各种类型的关系根据它们的本体论地位、它们适用的领域以及它们形成的结构来区分。[34]

### Internal and external

内部和外部

An influential distinction differentiates between internal and external relations. A relation is internal if it only depends on what the relata are like: it is determined by the characteristics or the nature of the relata alone. External relations are not fixed this way and carry characteristics that go beyond the intrinsic features of their relata.[35] Mathematical relations between numbers are examples of internal relations. For instance, the number six stands in the relation of being greater than to the number five. This relation is internal because it is essential to the numbers six and five that six is greater than five.[36] Other traditional examples of internal relations are resemblance and difference.[37] Spatial relations are normally understood as external relations, like the relation of a book to the table it is lying on.[38] The same is true for temporal and causal relations.[37]
有影响力的区别区分了内部关系和外部关系。如果一个关系只取决于相对关系是什么样的，那么它就是内部的：它是由相对关系的特征或性质单独决定的。外部关系不是以这种方式固定的，它所具有的特征超出了其关系的内在特征。[35] 数字之间的数学关系是内部关系的例子。例如，数字 6 代表大于数字 5 的关系。这种关系是内在的，因为对于数字 6 和 5 来说，6 大于 5 是必不可少的。[36] 内部关系的其他传统例子是相似性和差异性。[37]空间关系通常被理解为外部关系，就像一本书与它所躺着的桌子的关系一样。[38] 时间关系和因果关系也是如此。[37]
Photo of George Edward Moore
G. E. Moore introduced the distinction between internal and external relations.[16]

However, the precise characterization of the distinction between internal and external relations is disputed and there are various incompatible ways to define them. According to G. E. Moore, a relation is internal if it follows from the existence of its relata that the relation also exists. This means that the relation is essential to the relata and the relata cannot exist without this relation. For Moore, external relations are different since they could fail to obtain even if its relata exist.[39] Another definition is defended by philosophers like Armstrong, who hold that a relation is internal if it is necessitated by the properties or the intrinsic features of the relata.[40] David K. Lewis provides a slightly different formulation by claiming that internal relations supervene on the intrinsic properties of their elements.[41] Some philosophers talk of ideal relations to refer to relations that solely depend on the qualities of the related terms, in contrast to real relations, for which this is not the case.[42]
然而，对内部和外部关系之间区别的精确描述是有争议的，并且有各种不相容的定义方式。根据 G. E. Moore 的说法，如果从其相对关系的存在得出关系也存在，那么该关系就是内部的。这意味着这种关系对 relata 来说是必不可少的，没有这种关系，relata 就不能存在。对 Moore 来说，外部关系是不同的，因为即使其相对关系存在，它们也可能无法获得。[39]另一个定义由阿姆斯特朗等哲学家捍卫，他们认为，如果关系的属性或内在特征需要这种关系，那么它就是内部的。[40] 大卫·刘易斯（David K. Lewis）提供了一个略有不同的表述，他声称内部关系取决于其元素的内在属性。[41]一些哲学家谈到理想关系是指完全取决于相关术语的质量的关系，与实际关系相反，事实并非如此。[42]

The difference between these definitions affects whether some relations are characterized as internal or external.[43] An example is the relation of having the same shape. This relation applies if x is a cube and y is also a cube. According to Armstrong, this relation is internal since it only depends on the intrinsic nature of x and y. This is not the case for Moore since y could have been a sphere rather than a cube, meaning that the relation is external since it is not necessitated by the existence of x and y.[16]
这些定义之间的差异会影响某些关系是被描述为内部关系还是外部关系。[43] 一个例子是具有相同形状的关系。如果 x 是多维数据集，而 y 也是多维数据集，则此关系适用。根据阿姆斯特朗的说法，这种关系是内部的，因为它只取决于 x 和 y 的内在本质。摩尔的情况并非如此，因为 y 可能是一个球体而不是一个立方体，这意味着这种关系是外部的，因为它不是 x 和 y 存在的必要条件[16]。

The difference between internal and external relations has various consequences for the ontological status of relations.[44] According to a common view, internal relations do not form part of reality on the most fundamental level since they supervene on their relata. In this regard, they are already included in some sense in the relata and constitute no addition to being.[45] That is not the case for external relations, which are more than the entities they connect and thus introduce additional ontological commitments.[46] Discussions about the existence of relations usually focus on the question of whether external relations exist.[47] One difficulty in this regard is where to locate them since it seems that they are not contained within the relata while they also cannot exist without them.[48]
内部和外部关系之间的差异对关系的本体论地位有各种影响。[44]根据一种普遍的观点，内部关系在最基本的层面上并不构成现实的一部分，因为它们依赖于它们的关系。在这方面，它们在某种意义上已经包含在相对论中，并不构成对存在的补充。[45]外部关系并非如此，外部关系不仅仅是它们所连接的实体，因此引入了额外的本体论承诺。[46]关于关系存在的讨论通常集中在外部关系是否存在的问题上。[47]这方面的一个困难是在哪里找到它们，因为它们似乎不包含在相对论中，而没有它们也无法存在。[48]

### Formal and material 形式和材料

Another distinction is between formal and material relations,[49] sometimes also termed thin and thick relations.[50] Formal relations involve abstract ideas that do not carry any concrete content. According to a commonly held view, all formal relations are internal.[51] They are often characterized as topic-neutral, meaning that they pertain to all categories of being.[52] Material relations are associated with concrete ideas. They involve specific and substantial contents that are accessible to perceptual experience. Examples of formal relations are identity, entailment, being greater than, set membership, and resemblance. By contrast, the relations of collision, smiling, loving, killing, and giving are material relations.[53]
另一个区别是形式关系和物质关系，[49] 有时也称为薄关系和厚关系。[50]形式关系涉及不携带任何具体内容的抽象概念。根据一种普遍的观点，所有正式关系都是内部的。[51]它们通常被描述为主题中立的，这意味着它们与所有类别的存在有关。[52]物质关系与具体的想法有关。它们涉及感知经验可访问的特定和实质性内容。正式关系的例子是身份、蕴涵、大于、集合成员资格和相似性。相比之下，碰撞、微笑、爱、杀戮和给予的关系是物质关系。[53]

### Logical and causal 逻辑和因果关系

Diagram of the square of opposition
The square of opposition shows logical relations between the four basic categorical propositions in Aristotelian logic.[54]

Logical relations are relations between elements of thought, specifically between propositions or statements. Two propositions are logically related if the truth value of one depends on the truth value of the other.[55] In this regard, it is not important whether the propositions are true but only how the truth value of one proposition would affect the truth value of the other.[56] For instance, the claims "John has a high IQ and is immensely popular" and "John has a high IQ" are logically related since the first claim cannot be true if the second claim is false.[54] Logical relations are discovered through a priori reasoning rather than perceptual experience and are studied by logic.[56] They are often used to demonstrate or prove a claim.[57]
逻辑关系是思想元素之间的关系，特别是命题或陈述之间的关系。如果一个命题的真值取决于另一个命题的真值，那么两个命题在逻辑上是相关的。[55] 在这方面，命题是否为真并不重要，重要的是一个命题的真值将如何影响另一个命题的真值。[56]例如，“约翰智商高”和“约翰智商高”这两个说法在逻辑上是相关的，因为如果第二个说法是假的，那么第一个说法就不可能是真的。[54] 逻辑关系是通过先验推理而不是感知经验发现的，并通过逻辑进行研究。[56]它们通常用于证明或证明一项主张。[57]

Of primary interest in logic is the relation of logical consequence or entailment. This relation holds between the premises of an argument and its conclusion if the argument is governed by a valid rule of inference. It determines what follows logically from what and is present if the truth of the premises ensures the truth of the conclusion. This means that if the premises are true, the conclusion cannot be false.[58] Other examples of logical relations are being contrary and being contradictory. Two statements are contradictory if it is necessary that one is true and the other is false, like the statements "the coffee is cold" and "the coffee is not cold". Two statements are contraries if both can be false but both cannot be true, like the statements "the coffee is cold" and "the coffee is hot".[59]
逻辑学的主要兴趣是逻辑结果或蕴涵的关系。如果论证受有效推理规则支配，则这种关系在论证的前提和结论之间成立。它决定了从逻辑上遵循什么，如果前提的真实性确保了结论的真实性，那么它就存在。这意味着，如果前提是真的，结论就不可能是假的。[58] 逻辑关系的其他例子是相反和矛盾。如果有必要一个是真的，另一个是假的，那么两个陈述是矛盾的，比如“咖啡是冷的”和“咖啡不冷”的陈述。如果两个陈述都可以是假的，但都不能是真的，那么这两个陈述就是矛盾的，比如 “the coffee is cold” 和 “the coffee is hot” 这两个陈述。[59]

Causal relations are cause-effect relations between concrete events.[55] This is the case if an earlier event brings about a later event. An example is a white billiard ball that hits a red billiard ball, which in turn starts rolling toward a corner pocket. In this case, there is a causal relation between the collision-event and the rolling-event.[60] Causal relations are studied by the empirical sciences and can be known through perceptual experience.[56] They play a role in explaining why something happened.[57]
因果关系是具体事件之间的因果关系。[55]如果一个较早的事件导致了较晚的事件，就会出现这种情况。一个例子是白色台球撞到红色台球，而红色台球又开始向角袋滚动。在这种情况下，碰撞事件和滚动事件之间存在因果关系。[60] 因果关系由实证科学研究，可以通过感知经验来了解。[56]它们在解释为什么会发生某事方面发挥作用。[57]

Causal relations are traditionally understood as external relations. According to this view, they obey external causal laws or laws of nature that determine how effects follow from causes and are not fixed by the internal nature of the involved events. They are traditionally seen as contingent: they are the way they are but they could have been different because the causal laws could have been different.[61] An alternative position understands causation not in terms of causal laws but in terms of the powers of objects. In this case, the effect is a manifestation of the powers of the involved objects. According to this view, causal relations are internal relations if powers are understood as intrinsic properties of objects.[62]
因果关系传统上被理解为外部关系。根据这种观点，他们服从外部因果法则或自然法则，这些法则决定了结果如何从原因产生，而不是由所涉及事件的内部性质所固定。它们传统上被视为偶然的：他们就是他们本来的样子，但他们可能不同，因为因果法则可能不同。[61]另一种立场不是根据因果法则，而是根据客体的力量来理解因果关系。在这种情况下，效果是所涉及对象的力量的体现。根据这种观点，如果权力被理解为对象的内在属性，那么因果关系就是内部关系。[62]

One difficulty in distinguishing between causal and logical relations is that both can be expressed with the term "because". For instance, the sentence "John came back because he loved her" expresses a causal relation with love being the cause of John's return. The sentence "John loved her, because he came back" expresses a logical relation in which the existence of John's love is inferred from the fact that he came back.[63]
区分因果关系和逻辑关系的一个难点是，两者都可以用术语 “因为 ”来表示。例如，句子 “John came back because he love her” 表达了与爱是 John 回来的原因的因果关系。“约翰爱她，因为他回来了”这句话表达了一种逻辑关系，其中约翰的爱的存在是从他回来的事实中推断出来的。[63]

### Spatial and temporal

空间和时间

Spatial and temporal relations structure the physical world and organize how concrete objects and events stand to each other. Spatial relations affect where entities are located and how close or distant they are from each other. Examples are being three feet from, being below, and being within.[64] Temporal relations concern when something happens relative to something else. Examples are occurring before, occurring after, and occurring simultaneously.[65] It is usually held that spatiotemporal relations only hold between concrete objects but not between abstract objects.[66] Spatial and temporal relations are normally categorized as external relations.[67]
空间和时间关系构建了物理世界，并组织了具体对象和事件如何相互站立。空间关系会影响实体的位置以及它们之间的距离。例如，距离三英尺、低于 3 英尺和在内部。[64] 时间关系关注某事相对于其他事物发生的时间。示例发生在之前、之后发生和同时发生。[65]人们通常认为，时空关系只存在于具体对象之间，而不适用于抽象对象之间。[66] 空间和时间关系通常被归类为外部关系。[67]

The ontological status of spatial and temporal relations depends on how space and time are conceived. The theory of relationalism states that spacetime is nothing but the spatial and temporal relations in which entities stand to each other. According to this view, spatial and temporal relations are fundamental and constitute spacetime. A different view is substantivalism, which holds that spacetime is a substance that exists independently of the entities that occupy it.[68] Both relationalists and substantivalists accept regular statements about spatiotemporal relations, for example, that "the two towers of the Golden Gate Bridge are 4,200 feet apart". According to relationalists, this sentence is true because there is a fundamental spatial relation between the towers themselves. According to substantivalists, this is true because the two towers occupy two distinct and spatially distant regions in the spacetime substance.[69]
空间和时间关系的本体论状态取决于空间和时间是如何构想的。关系主义理论指出，时空只不过是实体彼此站立的时空关系。根据这种观点，空间和时间关系是基础，构成了时空。另一种观点是实体论，它认为时空是一种独立于占据它的实体而存在的物质。[68]关系论者和实体论者都接受关于时空关系的常规陈述，例如，“金门大桥的两座塔楼相距 4,200 英尺”。根据关系论者的说法，这句话是正确的，因为塔楼本身之间存在着基本的空间关系。根据实体论者的说法，这是真的，因为这两座塔在时空物质中占据了两个截然不同且空间相距遥的区域。[69]

In classical physics, space and time are understood as independent dimensions that are absolute and can be measured and analyzed separately from each other. In modern physics, space and time are seen as interdependent dimensions that form a unified continuum whose curvature is affected by the presence of mass and energy.[70]
在经典物理学中，空间和时间被理解为绝对的独立维度，可以彼此分开进行测量和分析。在现代物理学中，空间和时间被视为相互依存的维度，它们形成了一个统一的连续体，其曲率受质量和能量的影响。[70]

### By structural features

按结构特征

Binary relations are often distinguished based on several formal or structural features of how their elements are connected to one another. Symmetric relations always come in pairs: if x is related to y then y is related to x. An example is the relation being as old as: if Tom is as old as Zoe then Zoe is as old as Tom. Symmetric relations contrast with non-symmetric relations, for which this pair-like behavior is not always observed. An example is the love-relation: if Dave loves Sara then it is possible but not necessary that Sara loves Dave. A special case of non-symmetric relations is asymmetric relations, which only go one way. An example is the relation being heavier than: if Ben is heavier than Nia then it is not possible at the same time that Nia is heavier than Ben.[71] Symmetric relations are not sensitive to how their elements are ordered since they go both ways. However, the order of the elements matters for non-symmetric relations.[16]
二元关系通常根据其元素如何相互连接的几个形式或结构特征来区分。对称关系总是成对出现：如果 x 与 y 相关，则 y 与 x 相关。一个例子是关系的年龄 as ：如果 Tom 和 Zoe 一样老，那么 Zoe 和 Tom 一样老。对称关系与非对称关系形成对比，对于非对称关系，并不总是观察到这种类似对的行为。一个例子是爱情关系：如果 Dave 爱 Sara，那么 Sara 爱 Dave 是可能的，但不是必要的。非对称关系的一个特例是非对称关系，它只有一种方式。一个例子是关系 is heavyerty than： 如果 Ben 比 Nia 重，那么 Nia 不可能同时比 Ben 重。[71] 对称关系对它们的元素如何排序不敏感，因为它们是双向的。但是，元素的顺序对于非对称关系很重要。[16]

A further distinction is between transitive and intransitive relations. Transitive relations exhibit a chain-like nature: if x is related to y and y is related to z, then x is related to z. An example is the relation being larger than: if a truck is larger than a car and a car is larger than a bicycle then a truck is larger than a bicycle. A relation is intransitive if this chain-like behavior is not always present. An example is the relation being a parent: if Tess is a parent of Bob and Bob is a parent of Carol, then it is not automatically the case that Tess is a parent of Carol.[72]
进一步的区别是及物关系和不及物关系。传递关系表现出链状性质：如果 x 与 y 相关，y 与 z 相关，则 x 与 z 相关。一个例子是关系大于：如果卡车比汽车大，汽车比自行车大，那么卡车比自行车大。如果这种链状行为并不总是存在，则关系是不及物的。例如，关系是父级：如果 Tess 是 Bob 的父级，而 Bob 是 Carol 的父级，则 Tess 不会自动成为 Carol 的父级。[72]

Another distinction is between reflexive and irreflexive relations. Reflexive relations are those in which each entity is related to itself. An example is the relation being as old as since every entity is as old as itself. Irreflexive relations are relations that never connect an entity to itself.[72] An example is the relation being a sibling of: no one is their own sibling.[73]
另一个区别是反身关系和非反身关系。反身关系是每个实体都与自身相关的关系。一个例子是关系与 since each entity 都与自身一样古老。非反身关系是永远不会将实体与自身联系起来的关系。[72] 一个例子是关系是兄弟姐妹：没有人是他们自己的兄弟姐妹。[73]

These structural features are used to define further types of relations, like equivalence and strict partial order. An equivalence relation is a relation that is reflexive, symmetric, and transitive, like equality expressed through the symbol "=".[74] A strict partial order is a relation that is irreflexive, anti-symmetric, and transitive, like the relation being less than expressed through the symbol "<".[75]
这些结构特征用于定义更多类型的关系，例如等价和严格的部分顺序。等价关系是自反的、对称的和传递的，就像通过符号 “=” 表示的相等一样。[74] 严格的部分顺序是一种非反射性、反对称性和传递性的关系，就像关系小于通过符号 “<” 来表达一样。[75]

## Ontological status 本体论状态

Various debates in metaphysics are concerned with the ontological status of relations. Relations come with certain problems that are not present for other ontological categories, like substances and monadic properties.[76] They are different from substances because they depend on the entities they connect. They are different from properties since they apply to several entities and cannot be located in any one of their relata.[77]
形而上学中的各种争论都与关系的本体论地位有关。关系带来了一些问题，这些问题在其他本体论类别中不存在，比如物质和单子属性。[76]它们与物质不同，因为它们依赖于它们所连接的实体。它们与属性不同，因为它们适用于多个实体，并且不能位于其任何一个 relata 中。[77]

The ontological status of relations is disputed and various theories have been proposed. They are often divided into realism and anti-realism. Realists hold that relations have mind-independent existence in external reality, which is denied by anti-realists.[78] However, various intermediate positions between these views can be distinguished. Strict anti-realists or eliminativists deny that there are any relations. A slightly weaker position sees relations as mental inventions or projections. Another perspective is to accept that relations exist while regarding them as non-fundamental entities. This type of position is taken by reductionists, who claim that relations are emergent entities that can be reduced to other entities. Strong realists advance a more robust view and see relations as part of the fundamental ontological inventory of reality.[79] The difference between internal and external relations is central to their ontological status and the two types are often treated separately.[77]
关系的本体论地位存在争议，并提出了各种理论。它们通常分为现实主义和反现实主义。现实主义者认为，关系在外部现实中存在着独立于心智的存在，这一点被反现实主义者所否认。[78]然而，这些观点之间的各种中间位置是可以区分的。严格的反现实主义者或消除论者否认存在任何关系。稍微弱一点的立场将关系视为心理发明或投射。另一种观点是接受关系的存在，同时将它们视为非基本实体。这种立场被还原论者所采取，他们声称关系是可以简化为其他实体的涌现实体。强实在论者提出了更稳健的观点，并将关系视为现实的基本本体论清单的一部分。[79]内部关系和外部关系之间的差异是它们本体论地位的核心，这两种类型经常被分开处理。[77]

The issue of the ontological status of relations is closely connected to the problem of the one and the many.[42] This problem consists in explaining how reality can at the same time be both a multiplicity (because there are many distinct entities) and a unity (because all the distinct entities participate in one common reality).[80]
关系的本体论地位问题与一与多的问题密切相关。[42] 这个问题在于解释现实如何同时是多重性（因为有许多不同的实体）和统一性（因为所有不同的实体都参与一个共同的现实）。[80]

### Location problem 位置问题

Many of the difficulties associated with the ontological status of relations are connected to the location problem.[81] The location problem consists of the question of where relations are located.[82] For example, the sentence "Glasgow is west of Edinburgh" describes the location of two cities based on the relation being west of. However, it does not specify where the relation itself is located.[77]
许多与关系的本体论状态相关的困难都与位置问题有关。[81] 位置问题包括关系位于何处的问题。[82]例如，句子“Glasgow is west of Edinburgh”根据关系 is west of of （在爱丁堡以西）描述两个城市的位置。但是，它没有指定关系本身的位置。[77]

Different solutions to the location problem have been suggested. One suggestion is that the location of relations is divided.[83] According to this view, the relation of being west of resides in both Glasgow and Edinburgh together.[77] A different approach is to hold that relations exist in a place between their relata.[76] A further theory states that relations are abstract objects that do not have a location in space and time.[77]
已经提出了针对位置问题的不同解决方案。一种建议是关系的位置是分开的。[83]根据这种观点，“西”的关系同时存在于格拉斯哥和爱丁堡。[77]另一种方法是认为关系存在于它们之间的关系之间的某个地方。[76]进一步的理论指出，关系是在空间和时间中没有位置的抽象对象。[77]

A closely connected issue concerns how relations depend on their relata. Like properties, relations are traditionally conceived as accidents or dependent entities.[84] A traditionally common view says that properties are located in the object they characterize. However, this solution is more difficult for relations, specifically for external relations, since they do not inhere in a single entity but form connections between entities. Their external location makes it more difficult to conceive how they can be dependent entities at the same time.[85] The difficulties concerning the location of relations have prompted some philosophers to deny that relations exist or to hold that they exist only as ideas in the mind.[86]
一个密切相关的问题涉及关系如何依赖于它们的关系。与属性一样，关系传统上被视为事故或从属实体。[84]一种传统的普遍观点认为，属性位于它们所表征的对象中。但是，这种解决方案对于关系来说更加困难，特别是对于外部关系，因为它们不是存在于单个实体中，而是在实体之间形成连接。它们的外部位置使得更难想象它们如何同时成为依赖实体。[85]关于关系位置的困难促使一些哲学家否认关系的存在，或者认为它们仅作为思想存在于头脑中。[86]

### Eliminativism 消除主义

Eliminativists about relations hold that relations do not exist.[77] They often see relations as intellectual abstractions that are not part of reality at the most fundamental level.[33] Some eliminativists defend this view for all relations while others focus specifically on external relations.[77] They often justify their position by the ontological problems associated with relations, such as the location problem.[87] Metaphysical monists, like some defenders of absolute idealism, often reject the existence of genuine relations by claiming that there exists only one ultimate subject of predication.[42]
关于关系的排除论者认为关系不存在。[77]他们经常把关系看作是知识抽象的东西，在最基本的层面上不是现实的一部分。[33]一些消除论者为所有关系捍卫这一观点，而另一些则特别关注外部关系。[77]他们经常通过与关系相关的本体论问题来证明自己的立场，例如位置问题。[87]形而上学一元论者，就像一些绝对唯心主义的捍卫者一样，经常拒绝真实关系的存在，声称只有一个终极的谓词。[42]
Photo of F. H. Bradley
F. H. Bradley formulated a regress argument to defend the claim that relations do not exist.

A well-known argument for eliminativism is called Bradley's regress. It was formulated by F. H. Bradley, who argues that relations do not exist because they involve a vicious infinite regress. Bradley understands relations as universals and holds that a relation can only connect two entities if it is related to them. He claims that to be related to them, a second relation is required to relate the first relation to its relata. However, the same problem is repeated on the level of the second relation, which requires a third relation, and so on. This leads to a vicious infinite regress since the same problem arises for all additional relations. Bradley concludes from the resulting paradox that relations do not exist.[88]
消除论的一个著名论点称为布拉德利回归。它是由 F. H. Bradley 提出的，他认为关系不存在，因为它们涉及恶性无限回归。布拉德利将关系理解为普遍关系，并认为一个关系只有在与两个实体相关时才能连接两个实体。他声称，要与它们相关，需要第二个关系才能将第一个关系与其关系相关联。但是，在第二个关系的级别上重复相同的问题，这需要第三个关系，依此类推。这导致了恶性无限回归，因为所有其他关系都会出现相同的问题。布拉德利从由此产生的悖论中得出结论，关系不存在。[88]

The conclusion of Bradley's regress is not generally accepted and various arguments have been formulated to reject it. One approach is to distinguish between relations as universals and relational facts corresponding to particular instances. According to this view, the connection between a relation and its relata is made by the fact that instantiates the relation without the need for a second relation. A closely connected explanation understands relations not as universals but as particular entities, so-called tropes.[89] Opponents of these approaches have argued that they fail to truly solve the problem since they do not explain how facts or tropes connect a relation to its relata without requiring a second relation.[77] Another argument against Bradley's regress rejects the initial assumption that relations need to be related to the relata.[90]
布拉德利回归的结论并未被普遍接受，并且已经提出了各种论点来拒绝它。一种方法是区分作为普遍性的关系和对应于特定实例的关系事实。根据这种观点，一个关系和它的相对关系之间的联系是通过实例化关系而不需要第二个关系的事实来实现的。一个紧密相连的解释不是将关系理解为普遍性，而是将关系理解为特定的实体，即所谓的比喻。[89]这些方法的反对者认为，它们未能真正解决问题，因为它们没有解释事实或比喻如何在不需要第二种关系的情况下将关系与其相对关系联系起来。[77] 另一个反对布拉德利回归的论点拒绝了关系需要与关系相关的最初假设。[90]

Objections to eliminativism are often based on the idea that relations are required to describe reality. For instance, relations seem to be an indispensable part of mathematics and the empirical sciences.[91]
对消除论的反对往往是基于这样一种观点，即需要关系来描述现实。例如，关系似乎是数学和实证科学中不可或缺的一部分。[91]

### Reductionism 还原论

Reductionism is the view that relations can ultimately be reduced to or explained in terms of non-relational entities. In this regard, they are not a substantial addition to reality but only accompany other phenomena.[92] Some theorists understand reductionism as a form of anti-realism while others hold that reductionism allows that relations exist in a weak sense but denies that they are part of the most fundamental level of reality.[93]
还原论认为关系最终可以简化为非关系实体或用非关系实体来解释。在这方面，它们并不是对现实的实质性补充，而只是伴随着其他现象。[92]一些理论家将还原论理解为一种反现实主义的形式，而另一些理论家则认为还原论允许关系以微弱的意义存在，但否认它们是最基本的现实层次的一部分。[93]

A common form of reductionism states that relations can be understood in terms of the monadic properties of the related entities.[94] For example, the mountain Ben Vorlich stands in the relation of being taller than to its neighbor Ben Vane. This is explained by the properties of the two mountains: Ben Vorlich is 3094 feet high while Ben Vane is 3002 feet high. According to this view, no additional relational facts besides these properties are required.[50] Another example is the relation of similarity, which is often analyzed in terms of shared properties.[95]
还原论的一种常见形式指出，关系可以根据相关实体的单子属性来理解。[94]例如，本·沃利希山（Ben Vorlich）的立场是比它的邻居本·维恩（Ben Vane）还要高。这可以通过两座山的特性来解释：Ben Vorlich 高 3094 英尺，而 Ben Vane 高 3002 英尺。根据这种观点，除了这些属性之外，不需要额外的关系事实。[50]另一个例子是相似性关系，它通常根据共享属性进行分析。[95]

The claim that all relations, including external relations, can be reduced to monadic properties is controversial. For instance, it is not clear how spatial relations can be analyzed this way.[96] A further argument against reductionism comes from modern physics and holds that the non-relational properties it discusses are not sufficient to explain all phenomena.[50]
所有关系（包括外部关系）都可以简化为单子属性的说法是有争议的。例如，目前尚不清楚如何以这种方式分析空间关系。[96]反对还原论的进一步论点来自现代物理学，它认为它讨论的非关系属性不足以解释所有现象。[50]

Reductionism is common when applied to internal relations,[97] but it is not universally accepted. One anti-reductionist argument holds that some kind of minimal formal relation between the monadic properties themselves is required even in the case of internal relations. For example, to explain that Ben Vorlich is higher than Ben Vane, the properties being 3094 feet high and being 3002 feet high by themselves are not sufficient if one does not assume that the relation of being greater than holds between these properties.[50]
还原论在应用于内部关系时很常见，[97]但它并未被普遍接受。一个反还原论的论点认为，即使在内部关系的情况下，单子属性本身之间的某种最小形式关系也是必需的。例如，要解释 Ben Vorlich 高于 Ben Vane，如果不假设大于的关系，那么 3094 英尺高和 3002 英尺高的属性本身是不够的。[50]

### Realism 现实主义

Realists hold that relations are part of reality. This view is usually combined with the claim that relations have mind-independent existence. In a strong form, it states that relations belong to the most fundamental level of reality.[98] However, there are also weaker forms of realism. They hold that relations are real but do not exist on the most fundamental level. According to this view, they emerge from non-relational features and are in this sense "no addition to being".[99]
现实主义者认为，关系是现实的一部分。这种观点通常与关系具有独立于心智的存在的说法相结合。它以强有力的形式指出，关系属于现实的最基本层次。[98]然而，也有较弱的现实主义形式。他们认为关系是真实的，但在最基本的层面上并不存在。根据这种观点，它们从非关系特征中出现，在这个意义上是 “没有附加的存在”。[99]

Some realists understand relations as universals. According to this view, relations are repeatable and can be instantiated by different groups of individuals.[100] A different view holds that relations are tropes or non-repeatable particulars.[101]
一些现实主义者将关系理解为普遍性。根据这种观点，关系是可重复的，并且可以由不同的个体组实例化。[100]另一种观点认为，关系是比喻或不可重复的细节。[101]

#### Relationalism 关系主义

Relationalism is a strong form of realism about relations. In its widest sense, it states that all of reality is relational at its most fundamental level and denies the existence of non-relational properties.[102] The terms "relationism" and "relational ontology" are sometimes used as synonyms.[103] Relationalism contrasts with substantivalism, also known as substantivism, which sees substances, and not relations, as the fundamental constituents of reality.[104]
关系主义是关于关系的一种强烈现实主义形式。从最广泛的意义上讲，它指出所有现实在其最基本的层面上都是关系性的，并否认非关系属性的存在。[102] 术语“关系主义”和“关系本体论”有时被用作同义词。[103]关系主义与实质主义形成对比，后者也被称为实体主义，后者将物质而不是关系视为现实的基本组成部分。[104]

One core intuition motivating relationalism is that a key to understanding any object is to grasp how it is related to other objects.[105] Some relationalists state that objects do not exist at all while others hold that they only exist as dependent entities.[106] For example, the position of ontic structuralism claims that objects are structures made up of relations.[107] According to philosopher Randal Dipert, the world is made up of relations that form the structure of a mathematical graph and the concrete entities in it are subgraphs.[108]
激励关系主义的一个核心直觉是，理解任何对象的关键是掌握它与其他对象的关系。[105]一些关系论者指出，对象根本不存在，而另一些人则认为它们仅作为依赖实体存在。[106] 例如，本体结构主义的立场声称对象是由关系组成的结构。[107]根据哲学家兰德尔·迪珀特（Randal Dipert）的说法，世界是由构成数学图结构的关系组成的，其中的具体实体是子图。[108]

Relationalism is a controversial view when understood in its strongest form as a theory of reality in general. Besides its clash with common sense, one difficulty is that relations are usually understood as dependent entities that apply to the objects they connect rather than as independent entities that could exist without their relata. Another difficulty is that purely relational structures seem to be abstract objects that cannot by themselves account for the concrete reality they aim to describe.[109]
关系主义（relationalism）若以激进形态（strongest form）被诠释为关于实在（reality）的普遍理论，将引发重大争议。该立场除与常识直觉（commonsense intuition）相悖外，其理论困境主要体现在两方面：首先，传统本体论框架中，关系通常被视为依附于其所关联项（relata）的依存实体（dependent entities），而非可独立于关系项存在的自存实体（independent entities）；其次，纯粹关系结构（purely relational structures）作为抽象客体（abstract objects），难以独立构成（account for）其试图描述的具体实在（concrete reality）之本体论基底[109]。

Some relationalists defend more restricted theories by limiting their claims to specific domains rather than trying to explain reality as a whole.[110] In the philosophy of space and time, relationalism is the view that spacetime is not a substance, as substantivalists claim, but a network of spatiotemporal relations between individual physical phenomena.[111] In the philosophy of perception, relationalism about color is the view that colors are not regular monadic properties of objects but relations between perceptual circumstances and the subjects that perceive them.[112] In the philosophy of sociology, relationalism is an approach that investigates wide social phenomena by studying the relations between interactants. Examples are seeing society as the totality of interactions between people or understanding the world of art in terms of the relations between artists, producers, audiences, and critics.[113]
部分关系论者（relationalists）通过将理论适用范围限定于特定领域（而非全域性解释现实），发展出更具限定性（domain-restricted）的理论范式。在时空哲学中，关系论（relationalism）否定实体论者（substantivalists）将时空视为独立实体的主张，认为时空本质是物理现象间时空关系（spatiotemporal relations）构成的拓扑网络。在感知哲学领域，颜色关系论（color relationalism）主张：颜色并非对象的一元属性（monadic properties），而是感知情境（perceptual circumstances）与感知主体（perceiving subjects）之间的关系性显现（relational manifestation）。社会学哲学中的关系主义（sociological relationalism）主张：宏观社会现象应通过行动者（actors）间的动态关系（dynamic relations）进行研究。其典型方法论包括：将社会重构为人类互动的总体性构成（total constitution），或通过分析艺术家-生产者-受众-评论家的关系矩阵（relational matrix）来解码艺术场域。

## History 历史

The nature of relations was reconceptualized following various academic developments in the 19th century, such as the formulation of the logic of relations by Augustus De Morgan.

The history of the philosophy of relations can roughly be divided into two periods. Traditionally up until the late 19th century, metaphysicists were suspicious about the nature of relations. They usually regarded them as lower entities that do not play a role on the fundamental level of reality. This outlook changed in the 19th century, when various developments in the fields of mathematics, logic, and science prompted philosophers to reconceptualize the nature of relations and the need for relations to describe reality on its most basic level.[114]
关系哲学的历史进程可大致划分为两个时期。传统观点直至 19 世纪晚期，形而上学家普遍对关系的本体论地位持怀疑态度，通常将其视为不参与现实基础建构的次级实体。这一观念在 19 世纪发生重大转变——数学、逻辑学及科学领域的发展促使哲学家重新审视关系的本质，并认识到其在基础现实描述中的必要性[114]。

### 古希腊与中世纪传统

Aristotle's distinction between substances and accidents was influential in how relations were conceived by later philosophers.[115] Substances are the fundamental constituents of reality. They exist in themselves and are not predicable of something else, like an individual man or a horse. Accidents cannot exist without a substance. They are possible but non-necessary modifications of substances, like being in a sitting position.[116] Aristotle conceived relations as the lowest form of accidents that depend not just on substances but also on other accidents. Many subsequent philosophers accepted the idea that relations are non-substantial entities that are unable to exist on their own and depend on other entities.[117] For example, the neo-Platonists Plotinus and Porphyry followed Aristotle in seeing relations as accidents while emphasizing at the same time that relations are real entities.[118]
亚里士多德关于**实体（substances）与偶性（accidents）**的区隔深刻影响了后世哲学家的关系观[115]。实体作为现实的基本构成要素独立自存（如个体的人或马），而偶性作为实体的非必然属性依附存在（如坐姿状态）[116]。亚氏将关系归为最低层级的偶性，其存在既依赖实体又关联其他偶性。这一观点为众多后世哲学家所继承，认为关系作为非自存实体需依附他者存在[117]。新柏拉图主义者普罗提诺与波菲利在承认关系之实在性的同时，延续了亚氏的偶性分类[118]。

The nature and role of relations were discussed in detail in medieval philosophy, specifically by scholastic philosophers.[119] They agreed with Aristotle that relations are accidents. A common approach was to reduce relations to pairs of monadic properties.[120] This approach was exemplified by Peter Abelard and William Ockham, who explained relations in terms of non-relational qualities possessed by the relata. For instance, they held that if Socrates is similar to Theaetetus then this is because they share certain qualities, like color.[121] Some scholastic philosophers, like Peter Auriol, rejected relations and held instead that they are merely mental associations of entities not found outside the mind.[122] A different approach was followed by Albert the Great and John Duns Scotus, who understood relations as a distinct and irreducible type of entity.[121] Thomas Aquinas defended a middle position by holding that some relations have a substantial foundation in reality, like being a father, while others merely exist on the verbal level, like being moved by.[123]
中世纪经院哲学对关系本体论展开深度探讨[119]，主流观点仍将关系视为偶性。彼得·阿伯拉尔与奥卡姆的威廉提出关系还原论，主张用一元属性对（pairs of monadic properties）解释关系[120]。例如，"苏格拉底与泰阿泰德相似"可归因于二者共享颜色等属性[121]。对此，彼得·奥里奥尔等学者持反实在论立场，认为关系仅是心智的联想构造[122]。而大阿尔伯特与邓斯·司各脱则提出关系作为不可还原的实体类型，托马斯·阿奎那折衷地区分了具有现实基础的关系（如父子）与纯语言层面的关系（如被移动）[123]。

### 近代

近代哲学呈现关系实在论的消解趋势，霍布斯的唯名论主张仅个体具完全存在，关系作为心智比较产物缺乏本体论地位[124][125]。莱布尼茨基于单子论否定关系的根本实在性，认为单子（monads）作为无窗实体彼此独立，关系仅是突现于单子内在属性的心智建构[42][126][127]。

康德将关系纳入其范畴体系，作为理解现象世界互动联结的核心范畴（如实体-属性、因果依存）[128][129]。黑格尔进一步强调关系对事物本质的构成性作用，主张意义与价值产生于关系网络[130]。

According to a common view in the modern period, relations are reducible to other entities or exist merely in the mind.[124] For example, Thomas Hobbes defended a form of nominalism according to which only individuals have full existence. This implies that relations lack a proper ontological status and only exist in the mind as a form of mental comparison.
根据现代的普遍观点，关系可以简化为其他实体或仅存在于头脑中。[124]例如，托马斯·霍布斯（Thomas Hobbes）为一种唯名论辩护，根据这种形式，只有个体才有完整的存在。这意味着关系缺乏适当的本体论地位，仅作为心理比较的一种形式存在于头脑中。

Gottfried Wilhelm Leibniz rejected the fundamental reality of relations based on the claim that they would lack a proper location in this case. These ontological difficulties prompted Leibniz to propose his monadology, according to which reality is made up of windowless and unconnected monads. For him, relations are emergent entities that arise from the intrinsic properties of the relata.They are understood as pairs of monadic properties and not as ontologically distinct entities. For instance, if Adam is the father of Cain then Adam has the property of being a father of Cain and Cain has the property of being a child of Adam. In this regard, relations have a foundation in reality but are at the same time mental constructions that arise by comparing things.
戈特弗里德·威廉·莱布尼茨 （Gottfried Wilhelm Leibniz） 拒绝了关系的基本现实，理由是在这种情况下它们将缺乏适当的位置。这些本体论上的困难促使莱布尼茨提出了他的单子论，根据该论，现实是由无窗和无联系的单子组成的。对他来说，关系是从关系的内在属性中产生的涌现实体。它们被理解为一对单子属性，而不是本体论上不同的实体。例如，如果亚当是该隐的父亲，那么亚当就有该隐的父亲的特性，该隐也有亚当的孩子的特性。在这方面，关系在现实中有一个基础，但同时也是通过比较事物而产生的心理建构。

Leibniz's idealist outlook on relations influenced Immanuel Kant,who included relation in his system of categories as one of the four basic groups of categories. It covers the topic of how human minds organize and understand objects and concepts in terms of their mutual connections, dependencies, and interactions, for example, how properties inhere in substances and how effects depend on their causes.[128] Kant gave a prominent role to relations and held that phenomenal reality is at its core constituted by relations.[129] This idealist outlook on the importance of relations was also defended by Georg Wilhelm Friedrich Hegel, who argued that the nature, meaning, and value of things arises from how they participate in relations.[130]
莱布尼茨的唯心主义关系观影响了伊曼纽尔·康德（Immanuel Kant）[127]，康德将关系作为四个基本范畴组之一纳入他的范畴系统。它涵盖了人类思维如何根据它们的相互联系、依赖关系和相互作用来组织和理解物体和概念的主题，例如，物质中的属性如何以及效果如何取决于它们的原因。[128] 康德对关系起着突出的作用，并认为现象现实的核心是由关系构成的。[129]这种关于关系重要性的唯心主义观点也得到了乔治·威廉·弗里德里希·黑格尔（Georg Wilhelm Friedrich Hegel）的捍卫，他认为事物的性质、意义和价值源于它们如何参与关系。[130]

### 现代逻辑与科学影响

前现代逻辑受制于主谓形式，难以处理多元关系命题[131]。德摩根于 19 世纪创立关系逻辑，引入复合关系（如"叔侄"由"父子"与"兄弟"合成）的形式化分析[133]，皮尔斯进一步以"化合价"类比关系的外延度（如二元、三元关系）[134]，奠定现代逻辑处理关系的基础。

Difficulties about the ontological status of relations were also reflected in how they were treated in the field of logic before modern formal logic. For example, Aristotelian logic restricts itself to propositions in a subject-predicate form in which the predicate expresses qualities or attributes of a single entity in the subject position.[131] Modern logic, by contrast, also allows reasoning with relations to express how several entities stand to each other.[132] An important early development in this regard was the formulation of the logic of relations by Augustus De Morgan in the 19th century. It introduces formal devices to assess the validity of reasoning regarding relations, including compound relations like combining the relations of father of and brother of into uncle of.[133] De Morgan's logic of relations was further developed by Charles Sanders Peirce, who conceptualized the adicity of relations in analogy to chemical elements that form molecules based on their valency.[134]
关于关系本体论地位的困难也反映在现代形式逻辑之前它们在逻辑领域的处理方式上。例如，亚里士多德逻辑将自身限制在主谓形式的命题中，其中谓词在主语位置上表达单个实体的品质或属性。[131]相比之下，现代逻辑也允许用关系进行推理来表达几个实体如何相互站立。[132]这方面的一个重要早期发展是奥古斯都·德·摩根（Augustus De Morgan）在 19 世纪对关系逻辑的制定。它引入了形式化的手段来评估关于关系的推理的有效性，包括复合关系，例如将父亲和兄弟的关系组合成叔叔。[133]查尔斯·桑德斯·皮尔斯 （Charles Sanders Peirce） 进一步发展了德摩根的关系逻辑，他将关系的相等性概念化为类比根据化合价形成分子的化学元素。[134]

The problem of relations played a central role in Bradley's philosophy. He defended a form of monist idealism. According to it, there are no real separate entities and only one substance exists in the form of an idea or experience. For Bradley, the plurality of things in the world, as it appears to us, is ultimately an illusion. A consequence of this view is that there are no genuine relations since there are no distinct entities that could be related to each other.[135] He argued for this conclusion by trying to show that relations cannot exist because they would involve a vicious infinite regress.[136]
关系问题在布拉德利的哲学中起着核心作用。他为一种一元论唯心主义辩护。根据它，没有真正的独立实体，只有一种物质以思想或经验的形式存在。对布拉德利来说，世界上事物的多元性，正如我们所看到的，最终是一种幻觉。这种观点的结果是，没有真正的关系，因为没有可以相互关联的不同实体。[135]他通过试图证明关系不存在，因为它们将涉及一种恶性的无限回归，从而为这一结论辩护。[136]

Various early analytic philosophers, like Moore and Bertrand Russell, rejected Bradley's monist idealism and the associated theory of relations.[137] Moore based his rejection of Bradley's doctrine on the claim that it is not in tune with common sense, which favors a pluralistic ontology with genuine relations. Moore was further influential in developing the distinction between internal and external relations. [138] Russell argued in favor of the reality of external relations by pointing out that they are required to give an accurate scientific description of the external world.[77] Arguments for the reality of relations based on science were also defended by David Malet Armstrong. He conceived relations as universals that are instantiated in spacetime. According to him, it is the role of science to determine which relational universals exist.[139]
各种早期分析哲学家，如摩尔和伯特兰·罗素，都拒绝了布拉德利的一元论唯心主义和相关的关系理论。[137]摩尔对布拉德利学说的拒绝是基于这样一种主张，即它与常识不一致，而常识则支持具有真正关系的多元本体论。摩尔在区分内部和外部关系方面具有进一步的影响力。[138]罗素支持外部关系的现实，指出它们需要对外部世界进行准确的科学描述。[77]大卫·马莱特·阿姆斯特朗（David Malet Armstrong）也为基于科学的关系的现实性辩护。他将关系设想为在时空中实例化的普遍性。据他介绍，科学的作用是确定存在哪些关系普遍性。[139]

Various other solutions to the problem of relations have been suggested. For example, Gottlob Frege understood them as incomplete objects with open positions. They are completed when these positions are filled by the relata. In this regard, relations do not occur on their own and exist only insofar as they establish connections between other entities.[140] A further approach is found in Ludwig Wittgenstein's early philosophy, where he stated that objects can form connections with each other without requiring any additional elements. In this way, they are similar to chains: the different links of the chain are directly connected to each other without the additional need for relational entities to establish the connection.
已经提出了各种其他解决关系问题的方法。例如，Gottlob Frege 将它们理解为具有持仓的不完整对象。当 relata 填补这些位置时，它们就完成了。在这方面，关系不是单独发生的，只有在它们之间建立了其他实体之间的联系时才存在。[140]在路德维希·维特根斯坦（Ludwig Wittgenstein）的早期哲学中发现了另一种方法，他指出物体可以彼此形成连接，而不需要任何额外的元素。以这种方式，它们类似于链：链的不同环节直接相互连接，而无需额外的关系实体来建立连接。
