create database if not exists cov;
use cov;

create table if not exists `history`
(
    `ds`          datetime not null comment '����',
    `confirm`     int(11) default null comment '�ۼ�ȷ��',
    `confirm_add` int(11) default null comment '��������ȷ��',
    `suspect`     int(11) default null comment 'ʣ������',
    `suspect_add` int(11) default null comment '������������',
    `heal`        int(11) default null comment '�ۼ�����',
    `heal_add`    int(11) default null comment '������������',
    `dead`        int(11) default null comment '�ۼ�����',
    `dead_add`    int(11) default null comment '������������',
    primary key (`ds`) using btree
) engine = InnoDB
  default charset = utf8mb4;

create table if not exists `details`
(
    `id`          int(11) not null auto_increment,
    `update_time` datetime    default null comment '����������ʱ��',
    `province`    varchar(50) default null comment 'ʡ',
    `city`        varchar(50) default null comment '��',
    `confirm`     int(11)     default null comment '�ۼ�ȷ��',
    `confirm_add` int(11)     default null comment '����ȷ��',
    `heal`        int(11)     default null comment '�ۼ�����',
    `dead`        int(11)     default null comment '�ۼ�����',
    primary key (`id`)
) engine = InnoDB
  default charset = utf8mb4;

create table if not exists `hotsearch`
(
    `id`      int(11) not null auto_increment,
    `dt`      datetime     default null on update current_timestamp,
    `content` varchar(255) default null,
    `hot`     int(11)      default null comment '�ȶ�',
    primary key (`id`)
) engine = InnoDB
  default charset = utf8mb4;

-- delete from history;
-- delete from details;
-- delete from hotsearch;

# drop table details;
# drop table history;
# drop table hotsearch;