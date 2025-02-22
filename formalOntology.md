# Formal ontology 形式本体
In philosophy, the term formal ontology is used to refer to an ontology defined by axioms in a formal language with the goal to provide an unbiased (domain- and application-independent) view on reality, which can help the modeler of domain- or application-specific ontologies to avoid possibly erroneous ontological assumptions encountered in modeling large-scale ontologies.
在哲学中，术语“形式本体论”用于指代由形式语言中的公理定义的本体论，其目标是提供一个公正的（独立于领域和应用程序）现实观，这可以帮助领域或应用程序特定本体论的建模者避免在建模大规模本体论时可能遇到的错误本体论假设。

By maintaining an independent view on reality, a formal (upper level) ontology gains the following properties:

通过保持对现实的独立看法，正式的（上层）本体论获得了以下属性：
    indefinite expandability:

        the ontology remains consistent with increasing content.
        本体与增加的内容保持一致。

    content and context independence:

        any kind of 'concept' can find its place.
        任何类型的“概念”都可以找到它的位置。

    accommodate different levels of granularity.
    适应不同级别的粒度

## Common terms in formal (upper-level) ontologies
正式（上层）本体中的常用术语

The differences in terminology used between separate formal upper-level ontologies can be quite substantial, but most formal upper-level ontologies apply one foremost dichotomy: that between endurants and perdurants.
单独的正式上层本体之间使用的术语差异可能相当大，但大多数正式的上层本体都适用一个最重要的二分法：Endurant 和 Perdurants 之间的二分法。
### Endurant 艰难

Also known as continuants, or in some cases as "substance", endurants are those entities that can be observed-perceived as a complete concept, at no matter which given snapshot of time. Were we to freeze time we would still be able to perceive/conceive the entire endurant.
也称为连续体，或在某些情况下称为“物质”，持久体是那些可以被观察-感知为完整概念的实体，无论给定的时间快照如何。如果我们冻结时间，我们仍然能够感知/构想整个 Endurant。

Examples include material objects (such as an apple or a human), and abstract "fiat" objects (such as an organization, or the border of a country).
示例包括物质对象（如苹果或人类）和抽象的“法定”对象（如组织或国家/地区的边界）。
### Perdurant 持久

Also known as occurrents, accidents or happenings, perdurants are those entities for which only a part exists if we look at them at any given snapshot in time. When we freeze time we can only see a part of the perdurant. Perdurants are often what we know as processes, for example: "running". If we freeze time then we only see a part of the running, without any previous knowledge one might not even be able to determine the actual process as being a process of running. Other examples include an activation, a kiss, or a procedure.
也称为 occurrents、accident 或 happenings，perdurants 是那些如果我们在任何给定的快照中观察它们，它们只存在一部分的实体。当我们定格时间时，我们只能看到 perdurant 的一部分。Perdurant 通常是我们所知道的进程，例如：“running”。如果我们冻结时间，那么我们只看到运行的一部分，在没有任何先前知识的情况下，我们甚至可能无法确定实际的过程是正在运行的过程。其他示例包括 activation、kiss 或 procedure。

### Qualities 光荣

In a broad sense, qualities can also be known as properties or tropes.
从广义上讲，品质也可以被称为属性或比喻。

Qualities do not exist on their own, but they need another entity (in many formal ontologies this entity is restricted to be an endurant) which they occupy. Examples of qualities and the values they assume include colors (red color), or temperatures (warm).
品质本身并不存在，但它们需要另一个实体（在许多正式的本体论中，这个实体被限制为一个持久实体），它们占据了这个实体。质量示例及其假定的值包括颜色（红色）或温度（暖色）。

Most formal upper-level ontologies recognize qualities, attributes, tropes, or something related, although the exact classification may differ. Some see qualities and the values they can assume (sometimes called quale) as a separate hierarchy besides endurants and perdurants (example: DOLCE). Others classify qualities as a subsection of endurants, e.g. the dependent endurants (example: BFO). Others consider property-instances or tropes that are single characteristics of individuals as the atoms of the ontology, the simpler entities of which all other entities are composed, so that all the entities are sums or bundles of tropes.
大多数正式的上层本体都承认品质、属性、比喻或相关的东西，尽管确切的分类可能不同。有些人将品质和他们可以承担的价值（有时称为 quale）视为除 endurants 和 perdurants（例如：DOLCE）之外的单独层次结构。其他人将 quality 归类为 endurants 的一个子部分，例如 dependent endurants（例如：BFO）。其他人将作为个体的单一特征的属性实例或比喻视为本体论的原子，所有其他实体都由这些更简单的实体组成，因此所有实体都是比喻的总和或捆绑。
## Formal versus nonformal
正式与非正式

In information science an ontology is formal if it is specified in a formal language, otherwise it is informal.
在信息科学中，如果用正式语言指定本体，则本体是正式的，否则它是非正式的。

In philosophy, a separate distinction between formal and nonformal ontologies exists, which does not relate to the use of a formal language.
在哲学中，形式和非形式本体之间存在单独的区别，这与形式语言的使用无关。
Example 例

An ontology might contain a concept representing 'mobility of the arm'. In a nonformal ontology a concept like this can often be classified as for example a 'finding of the arm', right next to other concepts such as 'bruising of the arm'. This method of modeling might create problems with increasing amounts information, as there is no foolproof way to keep hierarchies like this, or their descendant hierarchies (one is a process, the other is a quality) from entangling or knotting.
本体可能包含一个表示“手臂移动性”的概念。在非正式的本体论中，像这样的概念通常可以被归类为例如“发现手臂”，紧挨着其他概念，例如“手臂的瘀伤”。这种建模方法可能会产生信息量增加的问题，因为没有万无一失的方法来防止像这样的层次结构或其后代层次结构（一个是过程，另一个是质量）纠缠或打结。

In a formal ontology, there is an optimal way to properly classify this concept, it is a kind of 'mobility', which is a kind of quality/property (see above). As a quality, it is said to inhere in independent endurant entities (see above), as such, it cannot exist without a bearer (in the case the arm).
在形式本体论中，有一种最佳方法可以正确地分类这个概念，它是一种 “流动性”，是一种质量/属性（见上文）。作为一种品质，据说它存在于独立的持久实体中（见上文），因此，它不能没有承载者（在手臂的情况下）而存在。
## Applications for formal (upper-level) ontologies
正式 （上层） 本体的应用程序
### Formal ontology as a template to create novel specific domain ontologies
形式本体作为模板来创建新颖的特定领域本体

Having a formal ontology at your disposal, especially when it consists of a Formal upper layer enriched with concrete domain-independent 'middle layer' concepts, can really aid the creation of a domain specific ontology. It allows the modeller to focus on the content of the domain specific ontology without having to worry on the exact higher structure or abstract philosophical framework that gives his ontology a rigid backbone. Disjoint axioms at the higher level will prevent many of the commonly made ontological mistakes made when creating the detailed layer of the ontology.
拥有一个正式的本体，特别是当它由一个正式的上层组成时，充满了具体的、独立于领域的 “中间层 ”概念，可以真正帮助创建一个特定于领域的本体。它允许建模者专注于特定领域本体的内容，而不必担心确切的更高结构或抽象哲学框架，这些结构或抽象哲学框架为他的本体提供了刚性支柱。更高级别的不相交公理将防止在创建本体的详细层时犯的许多常见本体论错误。
### Formal ontology as a crossmapping hub: crossmapping taxonomies, databases and nonformal ontologies
形式本体作为交叉映射中心：交叉映射分类法、数据库和非形式本体

Aligning terminologies and ontologies is not an easy task. The divergence of the underlying meaning of word descriptions and terms within different information sources is a well known obstacle for direct approaches to data integration and mapping. One single description may have a completely different meaning in one data source when compared with another. This is because different databases/terminologies often have a different viewpoint on similar items. They are usually built with a specific application-perspective in mind and their hierarchical structure represents this.
对齐术语和本体并非易事。众所周知，不同信息源中单词描述和术语的基本含义存在差异，这是直接进行数据集成和映射的障碍。与另一个数据源相比，一个描述在一个数据源中可能具有完全不同的含义。这是因为不同的数据库/术语通常对相似的项目有不同的观点。它们通常是在考虑特定应用程序视角的情况下构建的，它们的层次结构代表了这一点。

A formal ontology, on the other hand, represents entities without a particular application scope. Its hierarchy reflects ontological principles and a basic class-subclass relation between its concepts. A consistent framework like this is ideal for crossmapping data sources. However, one cannot just integrate these external data sources in the formal ontology. A direct incorporation would lead to corruption of the framework and principles of the formal ontology.
另一方面，正式的本体表示没有特定应用程序范围的实体。它的层次结构反映了本体论原则和其概念之间的基本类-子类关系。像这样的一致框架非常适合交叉映射数据源。然而，我们不能仅仅将这些外部数据源集成到正式的本体中。直接合并将导致形式本体论的框架和原则的腐败。

A formal ontology is a great crossmapping hub only if a complete distinction between the content and structure of the external information sources and the formal ontology itself is maintained. This is possible by specifying a mapping relation between concepts from a chaotic external information source and a concept in the formal ontology that corresponds with the meaning of the former concept.
只有在外部信息源的内容和结构与形式本体本身之间保持完全区分时，形式本体才是一个很好的交叉映射枢纽。这可以通过指定来自混沌外部信息源的概念与形式本体中与前一个概念的含义相对应的概念之间的映射关系来实现。

Where two or more external information sources map to one and the same formal ontology concept a crossmapping/translation is achieved, as you know that those concepts—no matter what their phrasing is—mean the same thing.
当两个或多个外部信息源映射到同一个正式的本体概念时，就会实现交叉映射/翻译，因为你知道这些概念——无论它们的措辞是什么——都意味着同样的事情。
### Formal ontology to empower natural language processing
支持自然语言处理的形式本体

In ontologies designed to serve natural language processing (NLP) and natural language understanding (NLU) systems, ontology concepts are usually connected and symbolized by terms. This kind of connection represents a linguistic realization. Terms are words or a combination of words (multi-word units), in different languages, used to describe in natural language an element from reality, and hence connected to that formal ontology concept that frames this element in reality.
在旨在为自然语言处理 （NLP） 和自然语言理解 （NLU） 系统服务的本体中，本体概念通常由术语连接和符号化。这种联系代表了一种语言上的实现。术语是不同语言中的单词或单词的组合（多词单位），用于用自然语言描述现实中的元素，因此与在现实中构建该元素的正式本体概念相关联。

The lexicon, the collection of terms and their inflections assigned to the concepts and relationships in an ontology, forms the 'ontology interface to natural language', the channel through which the ontology can be accessed from a natural language input.
词典是分配给本体中概念和关系的术语及其屈折变化的集合，形成了“自然语言的本体界面”，通过该通道可以从自然语言输入访问本体。
### Formal ontology to normalize database/instance data
规范化数据库 / 实例数据的形式本体

The great thing about a formal ontology, in contrast to rigid taxonomies or classifications, is that it allows for indefinite expansion. Given proper modeling, just about any kind of conceptual information, no matter the content, can find its place.
与僵化的分类法或分类相比，形式本体论的伟大之处在于它允许无限扩展。如果建模得当，几乎任何类型的概念信息，无论内容如何，都可以找到它的位置。

To disambiguate a concept's place in the ontology, often a context model is useful to improve the classification power. The model typically applies rules to surrounding elements of the context to select the most valid classification.
为了消除概念在本体中位置的歧义，上下文模型通常有助于提高分类能力。该模型通常将规则应用于上下文的周围元素，以选择最有效的分类。