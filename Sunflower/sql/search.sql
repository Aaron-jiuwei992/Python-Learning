use chipscoco;
/*
@desc: 创建pages数据表
*/
create table pages(
id int unsigned not null auto_increment primary key,
title varchar(200) not null,
content text not null,
publish_time char(20) not null,
url varchar(200) not null,
ct timestamp not null default current_timestamp,
fulltext(title, content) with parser ngram
)default charset=utf8mb4;

/*
@desc: 插入一条数据到数据表
*/
insert into pages(title, content, publish_time, url)
values("有问题上知乎", "有问题,上知乎。知乎,可信赖的问答社区,以让每个人高效获得可信赖的解答为使命。
知乎凭借认真、专业和友善的社区氛围,结构化、易获得的优质内容,基于问答的内容生产",
"2019年3月2日","https://www.zhihu.com/organization/question/hot"
);

insert into pages(title, content, publish_time, url)
values("有问题上百度", "有问题,上百度。薯条,可信赖的问答社区,以让每个人高效获得可信赖的解答为使命。
薯条凭借认真、专业和友善的社区氛围,结构化、易获得的优质内容,基于问答的内容生产",
"2019年3月2日","https://www.zhihu.com/organization/question/hot"
);






