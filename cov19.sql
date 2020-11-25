create database if not exists cov;
use cov;

create table if not exists `history`
(
    `ds`          datetime not null comment '日期',
    `confirm`     int(11) default null comment '累计确诊',
    `confirm_add` int(11) default null comment '当日新增确诊',
    `suspect`     int(11) default null comment '剩余疑似',
    `suspect_add` int(11) default null comment '当日新增疑似',
    `heal`        int(11) default null comment '累计治愈',
    `heal_add`    int(11) default null comment '当日新增治愈',
    `dead`        int(11) default null comment '累计死亡',
    `dead_add`    int(11) default null comment '当日新增死亡',
    primary key (`ds`) using btree
) engine = InnoDB
  default charset = utf8mb4;

create table if not exists `details`
(
    `id`          int(11) not null auto_increment,
    `update_time` datetime    default null comment '数据最后更新时间',
    `province`    varchar(50) default null comment '省',
    `city`        varchar(50) default null comment '市',
    `confirm`     int(11)     default null comment '累计确诊',
    `confirm_add` int(11)     default null comment '新增确诊',
    `heal`        int(11)     default null comment '累计治愈',
    `dead`        int(11)     default null comment '累计死亡',
    primary key (`id`)
) engine = InnoDB
  default charset = utf8mb4;

create table if not exists `hotsearch`
(
    `id`      int(11) not null auto_increment,
    `dt`      datetime     default null on update current_timestamp,
    `content` varchar(255) default null,
    `hot`     int(11)      default null comment '热度',
    primary key (`id`)
) engine = InnoDB
  default charset = utf8mb4;

-- delete from history;
-- delete from details;
-- delete from hotsearch;

# drop table details;
# drop table history;
# drop table hotsearch;