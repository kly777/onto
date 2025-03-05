
Objects in an ontology can be described by relating them to other things, typically aspects or parts. These related things are often called attributes, although they may be independent things. Each attribute can be a class or an individual. The kind of object and the kind of attribute determine the kind of relation between them. A relation between an object and an attribute express a fact that is specific to the object to which it is related. For example, the Ford Explorer object has attributes such as:
本体中的对象可以通过将它们与其他事物（通常是方面或部分）相关联来描述。这些相关事物通常称为属性，尽管它们可能是独立的事物。每个属性都可以是一个类或一个个体。对象的类型和属性的类型决定了它们之间的关系类型。对象与属性之间的关系表示特定于与其相关的对象的事实。例如，Ford Explorer 对象具有如下属性：

    ⟨has as name⟩ Ford Explorer
    ⟨有名⟩福特探险者
    ⟨as by definition as part⟩ 6-speed transmission
    ⟨根据定义作为部分⟩ 6 速变速器
    ⟨as by definition as part⟩ door (with as minimum and maximum cardinality: 4)
    ⟨根据定义作为 part⟩ 门（最小和最大基数为 4）
    ⟨as by definition as part one of⟩ {4.0L engine, 4.6L engine}
    ⟨根据定义作为第一部分⟩ {4.0L 发动机、4.6L 发动机}

The value of an attribute can be a complex data type; in this example, the related engine can only be one of a list of subtypes of engines, not just a single thing.
属性的值可以是复杂数据类型;在此示例中，related engine 只能是 engines 的子类型列表之一，而不仅仅是单个事物。

Ontologies are only true ontologies if concepts are related to other concepts (the concepts do have attributes). If that is not the case, then you would have either a taxonomy (if hyponym relationships exist between concepts) or a controlled vocabulary. These are useful, but are not considered true ontologies.
只有当概念与其他概念相关时（概念确实具有属性），本体才是真正的本体。如果不是这种情况，那么您将拥有分类法（如果概念之间存在下位词关系）或受控词汇表。这些是有用的，但不是真正的本体。
