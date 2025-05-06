interface Thing {
    // thing是最基本的概念，它可能有多个adic，adic为0的Thing是我们普遍意义上的事物，如桌子，椅子。acid！=0时，可以称为属性或关系，如{}是红色的，{}是{}的父亲。
    // fn是描述thing的adic的
    fn: fn;
    description: Des[];
    getSuper: () => Thing[];
    getSub: () => Thing[];
}

// 描述Thing
interface Des {
    type: string;
    content: string;
}

interface fn {
    adic: number;
    limit: Limit[];
}
// Limit是对adic不为零的thing上某个元的限制，如{0}是{1}的母亲，limit即为A是人，B是人
interface Limit extends Thing {
    place: number;
}

//subset是子集，如A是B的子集，super是B，sub是A
interface Subset {
    super: Thing;
    sub: Thing;
}
//这是对adic不为0的relation或者说函数的实现过程，如A比B高的实现过程是，{0}比{1}高->0是A->A比{1}高->0是B->A比B高
//((λx. (λy. x比y高)) A) B
// => (λy. A比y高) B
// => A比B高
// 基于集合论的关系实现模型
interface Realize extends Subset {
    // super 表示抽象关系（如 "_比_高"）
    // sub 表示具体实例（如 "A比B高"）
    input: Input;
}

interface Input extends Thing {
    content: Thing;
    place: number;
}

// 索绪尔符号学的双元结构：
// 1. 能指（Signifier）：符号的物理形式（如声音/文字）
// 2. 所指（Signified）：符号引发的心理概念
// 二者共同构成语言符号（Sign）    // 符号的能指层（Signifier）
interface Signifier extends Thing {
    // 显式声明符号的任意性关联
    convention: Convention; // 记录符号约定（如语言社群共识）
    // 示例："tree" 这个词的声音/文字形式
    // 物理形式（表达平面）
    form: PhysicalForm; // 支持多种符号类型（语音/文字/图像）

    // 能指与所指的关联（索绪尔的"符号结合"）
    // 示例："tree" -> 树的概念
    target: Signified[];
}
interface PhysicalForm {
  
}
interface Signified extends Thing {
    // 符号的所指层（Signified）
    // 示例：树的具体概念（木质植物的抽象表征）

    // 所指回溯到能指的双向性
    sources: Signifier[]; // 多个能指可指向同一所指（如同义词）
}
// 定义符号网络（体现语言系统的差异性特征）
interface SignSystem {
    signs: Map<Signifier, Signified>;
    oppositions: Array<{ left: Signifier; right: Signifier }>; // 二元对立关系
}
interface Convention {
    community: string; // 共识社群（如"英语母语者"）或领域
}
interface Intersection {
    // 体现交集
    //source一定是target的父集，如何体现
    source: Thing[];
    // target 是所有 source 的交集（即 target = ⋂source）
    target: Thing;
}

interface Union {
    // 体现并集，source组成了 target，但可能还有其他thing参与组成
    // 主要是为了表现不同的划分方式，如人有男人和女人，也可以为成年人和未成年人
    source: Thing[]; //source一定是target的子集，如何体现
    target: Thing;
    has_other: boolean;
    other: Thing | null;
}
