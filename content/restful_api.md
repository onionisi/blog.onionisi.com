Title: restful api
Date: 2016-08-14
Category: Blog
Tags: api, work
Slug: restful_api

#### API设计理念

    1. 将涉及的实体抽象成资源, 即按id访问资源, 在url上做文章, 以后再也不用为url起名字而苦恼.
    2. 使用HTTP动词对资源进行CRUD(增删改查); get->查, post->增, put->改, delete->删.
    3. URL命名规则, 对于资源无法使用一个单数名词表示的情况, 使用中横线(-)连接.
        * 资源采用名词命名, e.g: 产品 -> product
        * 新增资源, e.g: 新增产品, url -> /product , verb -> POST
        * 修改资源, e.g: 修改产品, url -> /products/{id} , verb -> PUT
        * 资源详情, e.g: 指定产品详情, url -> /products/{id} , verb -> GET
        * 删除资源, e.g: 删除产品, url -> /products/{id} , verb -> DELETE
        * 资源列表, e.g: 产品列表, url -> /products , verb -> GET
        * 资源关联关系, e.g: 收藏产品, url -> /products/{id}/star , verb -> PUT
        * 资源关联关系, e.g: 删除收藏产品, url -> /products/{id}/star , verb -> DELETE
