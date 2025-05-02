-- 符号学本体数据库结构设计
-- 事物表（所指）
CREATE TABLE signifieds (
  id INTEGER PRIMARY KEY,
  description TEXT NOT NULL,
  -- 事物的描述
  category TEXT,
  -- 分类（如实体、属性、关系）
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 能指表
CREATE TABLE signifiers (
  id INTEGER PRIMARY KEY,
  type TEXT CHECK (type IN ('text', 'image', 'audio')) NOT NULL,
  content BLOB,
  -- 文字内容（TEXT存储）或文件路径（BLOB存储）
  path TEXT,
  -- 图片/音频的存储路径
  media_type TEXT,
  -- 当type为image/audio时的MIME类型
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 能指与所指的关联表（多对多关系）
CREATE TABLE signifier_signified (
  signifier_id INTEGER REFERENCES signifiers (id),
  signified_id INTEGER REFERENCES signifieds (id),
  PRIMARY KEY (signifier_id, signified_id),
  context TEXT -- 关联上下文（如特定使用场景）
);

-- 示例数据插入
INSERT INTO
  signifieds (description, category)
VALUES
  ('一棵具有光合作用能力的植物', '生物实体'),
  ('婚姻契约的法律约束关系', '法律关系');

INSERT INTO
  signifiers (type, content, path, media_type)
VALUES
  ('text', '树', NULL, NULL),
  ('image', X 'FFD8FFDB', 'trees.jpg', 'image/jpeg'),
  (
    'audio',
    X '52494646',
    'tree_sound.wav',
    'audio/wav'
  );

INSERT INTO
  signifier_signified (signifier_id, signified_id, context)
VALUES
  (1, 1, '中文术语'),
  (2, 1, '视觉表征'),
  (3, 1, '自然声音'),
  (1, 2, '比喻使用（如家庭结构比作树）');