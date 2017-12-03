max-length

min-length

not-empty

videoTagText
videoCategory
videoDesc
videoTags
videoTitle

NULL

标题不能超过30字
标题不能少于30字
分类不能为空‘’、‘’
标签不能超过9个
描述不能超过200字
标签不能超过8个字

INSERT INTO `baobab`.`pgc_publish_lint`(`id`, `channel_id`, `rule`, `value`, `hint`, `filed_name`) VALUES (69, 12, 'not-empty', NULL, '分类不能为空', 'videoCategory');

INSERT INTO `baobab`.`pgc_publish_lint`(`id`, `channel_id`, `rule`, `value`, `hint`, `filed_name`) VALUES (71, 16, 'max-length', 8, '标签不能超过8个字', 'videoTagText');
